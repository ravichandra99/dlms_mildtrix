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
from .MILDDLMSSettings import MILDDLMSSettings
from .ValueEventArgs import ValueEventArgs
from .MILDDateTime import MILDDateTime
from .internal._MILDCommon import _MILDCommon
from .enums.Command import Command
from .MILDDLMS import MILDDLMS
from .MILDDLMSLNParameters import MILDDLMSLNParameters
from .MILDByteBuffer import MILDByteBuffer
from .MILDDLMSSNParameters import MILDDLMSSNParameters
from .VariableAccessSpecification import VariableAccessSpecification
from .enums.DataType import DataType
from .enums.Conformance import Conformance

#pylint: disable=bad-option-value,useless-object-inheritance,too-many-public-methods
class MILDDLMSNotify(object):
    """This class is used to send data notify and push messages to the clients."""

    #
    # Constructor.
    #
    # @param useLogicalNameReferencing
    #            Is Logical Name referencing used.
    # @param clientAddress
    #            Server address.
    # @param serverAddress
    #            Client address.
    # @param interfaceType
    #            Object type.
    #
    def __init__(self, useLogicalNameReferencing, clientAddress, serverAddress, interfaceType):
        # DLMS settings.
        self.settings = MILDDLMSSettings(True)
        self.useLogicalNameReferencing = useLogicalNameReferencing
        self.settings.clientAddress = clientAddress
        self.settings.serverAddress = serverAddress
        self.settings.interfaceType = interfaceType

    def getConformance(self):
        """What kind of services are used."""
        return self.settings.negotiatedConformance

    def setConformance(self, value):
        """What kind of services are used."""
        self.settings.negotiatedConformance = value

    # What kind of services are used.
    conformance = property(getConformance, setConformance)

    #
    # @param value
    #            Cipher interface that is used to cipher PDU.
    #
    def setCipher(self, value):
        self.settings.ipher = value

    def getObjects(self):
        return self.settings.objects

    # Get list of meter's objects.
    objects = property(getObjects)

    #
    # Information from the connection size that server can
    #      handle.
    #
    @property
    def limits(self):
        """Obsolete. Use hdlcSettings instead."""
        return self.settings.hdlc

    #
    # HDLC framing settings.
    #
    @property
    def hdlcSettings(self):
        return self.settings.hdlc

    def getMaxReceivePDUSize(self):
        return self.settings.maxPduSize

    def setMaxReceivePDUSize(self, value):
        self.settings.maxPduSize = value

    #
    # Retrieves the maximum size of received PDU.  PDU size tells maximum size
    # of PDU packet.  Value can be from 0 to 0xFFFF.  By default the value is
    # 0xFFFF.
    #
    # @see MILDDLMSClient#clientAddress
    # @see MILDDLMSClient#serverAddress
    # @see MILDDLMSClient#useLogicalNameReferencing
    # Maximum size of received PDU.
    #
    maxReceivePDUSize = property(getMaxReceivePDUSize, setMaxReceivePDUSize)

    def getUseLogicalNameReferencing(self):
        return self.settings.getUseLogicalNameReferencing()

    def setUseLogicalNameReferencing(self, value):
        self.settings.setUseLogicalNameReferencing(value)

    #
    # Determines, whether Logical, or Short name, referencing is used.
    # Referencing depends on the device to communicate with.  Normally, a
    # device
    # supports only either Logical or Short name referencing.  The referencing
    # is defined by the device manufacturer.  If the referencing is wrong, the
    # SNMR message will fail.
    #
    # Is Logical Name referencing used.
    #
    useLogicalNameReferencing = property(getUseLogicalNameReferencing, setUseLogicalNameReferencing)

    def getPriority(self):
        return self.settings.priority

    def setPriority(self, value):
        self.settings.priority = value

    #
    # Used Priority.
    #
    priority = property(getPriority, setPriority)

    def getServiceClass(self):
        return self.settings.serviceClass

    def setServiceClass(self, value):
        self.settings.serviceClass = value

    #
    # Used service class.
    #
    serviceClass = property(getServiceClass, setServiceClass)

    def getInvokeID(self):
        return self.settings.invokeId

    def setInvokeID(self, value):
        self.settings.invokeID = value

    #
    # Invoke ID.
    #
    invokeID = property(getInvokeID, setInvokeID)

    #
    # Removes the HDLC frame from the packet, and returns COSEM data only.
    #
    # @param reply
    #            The received data from the device.
    # @param data
    #            Information from the received data.
    # Is frame complete.
    #
    def getData(self, reply, data):
        return MILDDLMS.getData(self.settings, reply, data, None)

    #
    # Add value of COSEM object to byte buffer.  AddData method can be used
    # with
    # GetDataNotificationMessage -method.  DLMS specification do not specify
    # the
    # structure of Data-Notification body.  So each manufacture can sent
    # different data.
    #
    # @param obj
    #            COSEM object.
    # @param index
    #            Attribute index.
    # @param buff
    #            Byte buffer.
    #
    def addData(self, obj, index, buff):
        dt = None
        e = ValueEventArgs(self.settings, obj, index, 0, None)
        value = obj.getValue(self.settings, e)
        dt = obj.getDataType(index)
        if dt == DataType.NONE and value:
            dt = _MILDCommon.getDLMSDataType(value)
        _MILDCommon.setData(self.settings, buff, dt, value)

    #
    # Generates data notification message.
    #
    # @param time
    #            Date time.  Set Date(0) if not added.
    # @param data
    #            Notification body.
    # Generated data notification message(s).
    #
    def generateDataNotificationMessages(self, time, data):
        reply = None
        if self.useLogicalNameReferencing:
            p = MILDDLMSLNParameters(self.settings, 0, Command.DATA_NOTIFICATION, 0, None, data, 0xff)
            if time is None:
                p.time = None
            else:
                p.time = MILDDateTime(time)
            reply = MILDDLMS.getLnMessages(p)
        else:
            p2 = MILDDLMSSNParameters(self.settings, Command.DATA_NOTIFICATION, 1, 0, data, None)
            reply = MILDDLMS.getSnMessages(p2)
        if self.settings.negotiatedConformance & Conformance.GENERAL_BLOCK_TRANSFER == 0 and len(reply) != 1:
            raise ValueError("Data is not fit to one PDU. Use general block transfer.")
        return reply

    #
    # Generates push setup message.
    #
    # @param date
    #            Date time.  Set to null or Date(0) if not used.
    # @param push
    #            Target Push object.
    # Generated data notification message(s).
    #
    def generatePushSetupMessages(self, date, push):
        if push is None:
            raise ValueError("push")
        buff = MILDByteBuffer()
        buff.setUInt8(DataType.STRUCTURE)
        _MILDCommon.setObjectCount(len(push.pushObjectList), buff)
        for k, v in push.pushObjectList:
            self.addData(k, v.attributeIndex, buff)
        return self.generateDataNotificationMessages(date, buff)

    def generateReport(self, time, list_):
        #pylint: disable=bad-option-value,redefined-variable-type
        if not list_:
            raise ValueError("list")
        if self.useLogicalNameReferencing and len(list_) != 1:
            raise ValueError("Only one object can send with Event Notification request.")
        buff = MILDByteBuffer()
        reply = None
        if self.useLogicalNameReferencing:
            for k, v in list_:
                buff.setUInt16(k.objectType)
                buff.set(_MILDCommon.logicalNameToBytes(k.logicalName))
                buff.setUInt8(v)
                self.addData(k, v, buff)
            p = MILDDLMSLNParameters(self.settings, 0, Command.EVENT_NOTIFICATION, 0, None, buff, 0xff)
            p.time = time
            reply = MILDDLMS.getLnMessages(p)
        else:
            p = MILDDLMSSNParameters(self.settings, Command.INFORMATION_REPORT, len(list_), 0xFF, None, buff)
            for k, v in list_:
                buff.setUInt8(VariableAccessSpecification.VARIABLE_NAME)
                sn = k.shortName
                sn += (v - 1) * 8
                buff.setUInt16(sn)
            _MILDCommon.setObjectCount(len(list_), buff)
            for k, v in list_:
                self.addData(k, v, buff)
            reply = MILDDLMS.getSnMessages(p)
        return reply
