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
from .MILDDLMSScript import MILDDLMSScript
from .MILDDLMSScriptAction import MILDDLMSScriptAction
from .enums import ScriptActionType

# pylint: disable=too-many-instance-attributes
class MILDDLMSScriptTable(MILDDLMSObject, IMILDDLMSBase):
    """
    Online help:
    http://www.mildtrix.fi/Mildtrix.DLMS.Objects.MILDDLMSScriptTable
    """
    def __init__(self, ln=None, sn=0):
        """
        Constructor.

        ln : Logical Name of the object.
        sn : Short Name of the object.
        """
        super(MILDDLMSScriptTable, self).__init__(ObjectType.SCRIPT_TABLE, ln, sn)
        self.scripts = list()

    def getValues(self):
        return [self.logicalName,
                self.scripts]

    #
    # Returns collection of attributes to read.  If attribute is static
    #      and
    # already read or device is returned HW error it is not returned.
    #
    def getAttributeIndexToRead(self, all_):
        attributes = list()
        #  LN is static and read only once.
        if all_ or not self.logicalName:
            attributes.append(1)
        #  Scripts
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
            cnt = len(self.scripts)
            data = MILDByteBuffer()
            data.setUInt8(DataType.ARRAY)
            #  Add count
            _MILDCommon.setObjectCount(cnt, data)
            for it in self.scripts:
                data.setUInt8(DataType.STRUCTURE)
                #  Count
                data.setUInt8(2)
                #  Script_identifier:
                _MILDCommon.setData(settings, data, DataType.UINT16, it.id)
                data.setUInt8(DataType.ARRAY)
                #  Count
                data.setUInt8(len(it.actions))
                for a in it.actions:
                    data.setUInt8(DataType.STRUCTURE)
                    data.setUInt8(5)
                    #  service_id
                    _MILDCommon.setData(settings, data, DataType.ENUM, a.type_)
                    if not a.target:
                        #  class_id
                        _MILDCommon.setData(settings, data, DataType.UINT16, a.objectType)
                        #  logical_name
                        _MILDCommon.setData(settings, data, DataType.OCTET_STRING, _MILDCommon.logicalNameToBytes(a.logicalName))
                    else:
                        #  class_id
                        _MILDCommon.setData(settings, data, DataType.UINT16, a.target.objectType)
                        _MILDCommon.setData(settings, data, DataType.OCTET_STRING, _MILDCommon.logicalNameToBytes(a.target.logicalName))
                    _MILDCommon.setData(settings, data, DataType.INT8, a.index)
                    _MILDCommon.setData(settings, data, a.parameterDataType, a.parameter)
            return data
        e.error = ErrorCode.READ_WRITE_DENIED
        return None

    def setValue(self, settings, e):
        # pylint: disable=import-outside-toplevel,bad-option-value,too-many-nested-blocks,redefined-variable-type
        from .._MILDObjectFactory import _MILDObjectFactory
        if e.index == 1:
            self.logicalName = _MILDCommon.toLogicalName(e.value)
        elif e.index == 2:
            self.scripts = []
            if isinstance(e.value, list) and e.value:
                if isinstance(e.value[0], list):
                    for item in e.value:
                        script = MILDDLMSScript()
                        script.id = item[0]
                        self.scripts.append(script)
                        for arr in item[1]:
                            it = MILDDLMSScriptAction()
                            it.type_ = arr[0]
                            ot = arr[1]
                            ln = _MILDCommon.toLogicalName(arr[2])
                            t = settings.objects.findByLN(ot, ln)
                            if t is None:
                                t = _MILDObjectFactory.createObject(ot)
                                t.logicalName = ln
                            it.target = t
                            it.index = arr[3]
                            it.parameter = arr[4]
                            it.parameterDataType = _MILDCommon.getDLMSDataType(it.parameter)
                            script.actions.append(it)
                else:
                    script = MILDDLMSScript()
                    script.id = e.value[0]
                    arr = e.value[1]
                    it = MILDDLMSScriptAction()
                    it.type_ = arr[0]
                    ot = arr[1]
                    ln = _MILDCommon.toLogicalName(arr[2])
                    t = settings.objects.findByLN(ot, ln)
                    if t is None:
                        t = _MILDObjectFactory.createObject(ot)
                        t.logicalName = ln
                    it.target = t
                    it.index = arr[3]
                    it.parameter = arr[4]
                    script.actions.append(it)
        else:
            e.error = ErrorCode.READ_WRITE_DENIED

    def execute(self, client, script):
        if isinstance(script, MILDDLMSScript):
            script = script.getId()
        return client.method(self, 1, script, DataType.UINT16)

    def load(self, reader):
        #pylint: disable=import-outside-toplevel
        from .._MILDObjectFactory import _MILDObjectFactory
        self.scripts = []
        if reader.isStartElement("Scripts", True):
            while reader.isStartElement("Script", True):
                it = MILDDLMSScript()
                self.scripts.append(it)
                it.id = reader.readElementContentAsInt("ID")
                if reader.isStartElement("Actions", True):
                    while reader.isStartElement("Action", True):
                        a = MILDDLMSScriptAction()
                        a.type_ = ScriptActionType(reader.readElementContentAsInt("Type"))
                        ot = ObjectType(reader.readElementContentAsInt("ObjectType"))
                        ln = reader.readElementContentAsString("LN")
                        t = reader.objects.findByLN(ot, ln)
                        if t is None:
                            t = _MILDObjectFactory.createObject(ot)
                            t.logicalName = ln
                        a.target = t
                        a.index = reader.readElementContentAsInt("Index")
                        a.parameterDataType = reader.readElementContentAsInt("ParameterDataType")
                        a.parameter = reader.readElementContentAsObject("Parameter", None)
                        it.actions.append(a)
                    reader.readEndElement("Actions")
            reader.readEndElement("Scripts")

    def save(self, writer):
        if self.scripts:
            writer.writeStartElement("Scripts")
            for it in self.scripts:
                writer.writeStartElement("Script")
                writer.writeElementString("ID", it.id)
                writer.writeStartElement("Actions")
                for a in it.actions:
                    writer.writeStartElement("Action")
                    writer.writeElementString("Type", int(a.type_))
                    if a.target is None:
                        writer.writeElementString("ObjectType", int(ObjectType.NONE))
                        writer.writeElementString("LN", "0.0.0.0.0.0")
                        writer.writeElementString("Index", "0")
                        writer.writeElementString("ParameterDataType", int(DataType.NONE))
                        writer.writeElementObject("Parameter", "")
                    else:
                        writer.writeElementString("ObjectType", int(a.target.objectType))
                        writer.writeElementString("LN", a.target.logicalName)
                        writer.writeElementString("Index", a.index)
                        writer.writeElementString("ParameterDataType", int(a.parameterDataType))
                        writer.writeElementObject("Parameter", a.parameter)
                    writer.writeEndElement()
                writer.writeEndElement()
                writer.writeEndElement()
            writer.writeEndElement()