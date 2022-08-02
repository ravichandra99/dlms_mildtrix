#
#  --------------------------------------------------------------------------
#   Mildtrix Ltd
#
#
#
#  Filename: $HeadURL$
#
#  Version: $Revision$,
#                   $Date$
#                   $Author$
#
#  Copyright (c) Mildtrix Ltd
#
# ---------------------------------------------------------------------------
#
#   DESCRIPTION
#
#  This file is a part of Mildtrix Device Framework.
#
#  Mildtrix Device Framework is Open Source software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 2 of the License.
#  Mildtrix Device Framework is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#  See the GNU General Public License for more details.
#
#  More information of Mildtrix products: http://www.mildtrix.org
#
#  This code is licensed under the GNU General Public License v2.
#  Full text may be retrieved at http://www.gnu.org/licenses/gpl-2.0.txt
# ---------------------------------------------------------------------------
import xml.etree.cElementTree as ET
#pylint: disable=broad-except,no-name-in-module
from ..MILDByteBuffer import MILDByteBuffer
from ..MILDDateTime import MILDDateTime
from ..MILDDLMSConverter import MILDDLMSConverter
from ..internal._MILDCommon import _MILDCommon
from ..enums import DataType
from ..MILDArray import MILDArray
from ..MILDStructure import MILDStructure
from ..MILDIntEnum import MILDIntEnum
from ..MILDIntFlag import MILDIntFlag


###Python 2 requires this
#pylint: disable=bad-option-value,old-style-class
class MILDXmlWriter:
    """
    Save COSEM object to the file.
    """

    def __init__(self):
        """
        Constructor.
        """
        self.objects = list()
        self.skipDefaults = False

    def getTarget(self):
        return self.objects[len(self.objects) - 1]

    # pylint: disable=unused-argument
    def writeStartElement(self, elementName, attributeName=None, value=None, newLine=True):
        target = None
        if value:
            target = ET.SubElement(self.getTarget(), elementName)
        else:
            target = ET.SubElement(self.getTarget(), elementName)

        if attributeName:
            target.set(attributeName, value)
        self.objects.append(target)
        return target

    def writeEndElement(self):
        self.objects.pop()


    def writeElementString(self, name, value, defaultValue=None):
        if isinstance(value, (MILDIntEnum, MILDIntFlag)):
            value = int(value)

        if not(value and self.skipDefaults) or value != defaultValue:
            if value is None:
                ET.SubElement(self.getTarget(), name)
            elif isinstance(value, str):
                ET.SubElement(self.getTarget(), name).text = value
            elif isinstance(value, MILDDateTime):
                ET.SubElement(self.getTarget(), name).text = value.toFormatMeterString("%m/%d/%Y %H:%M:%S")
            elif isinstance(value, bool):
                if value:
                    ET.SubElement(self.getTarget(), name).text = "1"
                else:
                    ET.SubElement(self.getTarget(), name).text = "0"
            elif isinstance(value, int):
                ET.SubElement(self.getTarget(), name).text = str(value)
            elif isinstance(value, (bytearray, bytes)):
                ET.SubElement(self.getTarget(), name).text = MILDByteBuffer.hex(value)
            elif isinstance(value, (float)):
                ET.SubElement(self.getTarget(), name).text = str(value).replace(",", ".")

    def writeArray(self, data):
        if isinstance(data, (list)):
            arr = data
            for tmp in arr:
                if isinstance(tmp, bytearray):
                    self.writeElementObject("Item", tmp)
                elif isinstance(tmp, (MILDArray,)):
                    self.writeStartElement("Item", "Type", str(int(DataType.ARRAY)), True)
                    self.writeArray(tmp)
                    self.writeEndElement()
                elif isinstance(tmp, (MILDStructure,)):
                    self.writeStartElement("Item", "Type", str(int(DataType.STRUCTURE)), True)
                    self.writeArray(tmp)
                    self.writeEndElement()
                else:
                    self.writeElementObject("Item", tmp)

    #
    # Write object value to file.
    #
    # @param name
    # Object name.
    # @param value
    # Object value.
    #
    # pylint: disable=too-many-arguments
    def writeElementObject(self, name, value, dt=DataType.NONE, uiType=DataType.NONE):
        if isinstance(value, (MILDIntEnum, MILDIntFlag)):
            value = int(value)

        if value or not self.skipDefaults:
            if value is None:
                target = self.writeStartElement(name)
                self.writeEndElement()
                return
            if dt == DataType.OCTET_STRING:
                if uiType == DataType.STRING:
                    value = str(value)
                elif uiType == DataType.OCTET_STRING:
                    value = MILDByteBuffer.hex(value)
            elif dt != DataType.NONE and not isinstance(value, (float, MILDDateTime)):
                value = MILDDLMSConverter.changeType(value, dt)

            if dt == DataType.NONE:
                dt = _MILDCommon.getDLMSDataType(value)

            target = self.writeStartElement(name, "Type", str(int(dt)), False)
            if uiType != DataType.NONE and uiType != dt and (uiType != DataType.STRING or dt == DataType.OCTET_STRING):
                target.set("UIType", str(int(uiType)))
            if dt in (DataType.ARRAY, DataType.STRUCTURE):
                self.writeArray(value)
            else:
                if isinstance(value, (float)):
                    target.set("UIType", str(int(DataType.FLOAT64)))
                if isinstance(value, MILDDateTime):
                    target.text = value.toFormatMeterString("%m/%d/%Y %H:%M:%S")
                elif isinstance(value, (bytearray, bytes)):
                    target.text = MILDByteBuffer.hex(value)
                elif isinstance(value, bool):
                    if value:
                        target.text = "1"
                    else:
                        target.text = "0"
                else:
                    target.text = str(value)
            self.writeEndElement()
