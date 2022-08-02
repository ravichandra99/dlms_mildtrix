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
from .MILDDLMSObject import MILDDLMSObject
from .IMILDDLMSBase import IMILDDLMSBase
from ..enums import ErrorCode
from ..internal._MILDCommon import _MILDCommon
from ..MILDByteBuffer import MILDByteBuffer
from ..enums import ObjectType, DataType

# pylint: disable=too-many-instance-attributes
class MILDDLMSSapAssignment(MILDDLMSObject, IMILDDLMSBase):
    """
    Online help:
    http://www.mildtrix.fi/Mildtrix.DLMS.Objects.MILDDLMSSapAssignment
    """
    def __init__(self, ln=None, sn=0):
        """
        Constructor.

        ln : Logical Name of the object.
        sn : Short Name of the object.
        """
        super(MILDDLMSSapAssignment, self).__init__(ObjectType.SAP_ASSIGNMENT, ln, sn)
        self.sapAssignmentList = list()

    def getValues(self):
        return [self.logicalName,
                self.sapAssignmentList]

    def addSap(self, client, id_, name):
        """Add new SAP item."""
        data = MILDByteBuffer()
        data.setUInt8(DataType.STRUCTURE)
        #Add structure size.
        data.setUInt8(2)
        _MILDCommon.setData(client.settings, data, DataType.UINT16, id_)
        _MILDCommon.setData(client.settings, data, DataType.OCTET_STRING, name.encode())
        return client.method(self, 1, data.array(), DataType.STRUCTURE)

    def removeSap(self, client, name):
        """Remove SAP item."""
        data = MILDByteBuffer()
        data.setUInt8(DataType.STRUCTURE)
        #Add structure size.
        data.setUInt8(2)
        _MILDCommon.setData(client.settings, data, DataType.UINT16, 0)
        _MILDCommon.setData(client.settings, data, DataType.OCTET_STRING, name.encode())
        return client.method(self, 1, data.array(), DataType.STRUCTURE)

    #
    # Returns collection of attributes to read.  If attribute is static and
    # already read or device is returned HW error it is not returned.
    #
    def getAttributeIndexToRead(self, all_):
        attributes = list()
        #  LN is static and read only once.
        if all_ or not self.logicalName:
            attributes.append(1)
        #  SapAssignmentList
        if all_ or not self.isRead(2):
            attributes.append(2)
        return attributes

    #
    # Returns amount of attributes.
    #
    def getAttributeCount(self):
        return 2

    #
    # Returns amount of methods.
    #
    def getMethodCount(self):
        return 1

    def getDataType(self, index):
        if index == 1:
            return DataType.OCTET_STRING
        if index == 2:
            return DataType.ARRAY
        raise ValueError("getDataType failed. Invalid attribute index.")

    #
    # Returns value of given attribute.
    #
    def getValue(self, settings, e):
        if e.index == 1:
            return _MILDCommon.logicalNameToBytes(self.logicalName)
        if e.index == 2:
            cnt = len(self.sapAssignmentList)
            data = MILDByteBuffer()
            data.setUInt8(DataType.ARRAY)
            #  Add count
            _MILDCommon.setObjectCount(cnt, data)
            if cnt != 0:
                for k, v in self.sapAssignmentList:
                    data.setUInt8(DataType.STRUCTURE)
                    data.setUInt8(2)
                    #  Count
                    _MILDCommon.setData(settings, data, DataType.UINT16, k)
                    _MILDCommon.setData(settings, data, DataType.OCTET_STRING, _MILDCommon.getBytes(v))
            return data
        e.error = ErrorCode.READ_WRITE_DENIED
        return None

    #
    # Set value of given attribute.
    #
    def setValue(self, settings, e):
        if e.index == 1:
            self.logicalName = _MILDCommon.toLogicalName(e.value)
        elif e.index == 2:
            self.sapAssignmentList = []
            if e.value:
                for item in e.value:
                    str_ = None
                    if isinstance(item[1], bytearray):
                        str_ = _MILDCommon.changeType(settings, item[1], DataType.STRING)
                    else:
                        str_ = str(item[1])
                    self.sapAssignmentList.append((item[0], str_))
        else:
            e.error = ErrorCode.READ_WRITE_DENIED

    def load(self, reader):
        self.sapAssignmentList = []
        if reader.isStartElement("SapAssignmentList", True):
            while reader.isStartElement("Item", True):
                sap = reader.readElementContentAsInt("SAP")
                ldn = reader.readElementContentAsString("LDN")
                self.sapAssignmentList.append((sap, ldn))
            reader.readEndElement("SapAssignmentList")

    def save(self, writer):
        if self.sapAssignmentList:
            writer.writeStartElement("SapAssignmentList")
            for k, v in self.sapAssignmentList:
                writer.writeStartElement("Item")
                writer.writeElementString("SAP", k)
                writer.writeElementString("LDN", v)
                writer.writeEndElement()
            writer.writeEndElement()
