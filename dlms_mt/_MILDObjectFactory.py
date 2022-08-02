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
from .enums import ObjectType
#pylint: disable=bad-option-value,too-many-locals,
#cyclic-import,old-style-class,too-few-public-methods
from .objects.MILDDLMSAssociationLogicalName import MILDDLMSAssociationLogicalName
from .objects.MILDDLMSObject import MILDDLMSObject
from .objects.MILDDLMSActionSchedule import MILDDLMSActionSchedule
from .objects.MILDDLMSActivityCalendar import MILDDLMSActivityCalendar
from .objects.MILDDLMSAssociationShortName import MILDDLMSAssociationShortName
from .objects.MILDDLMSAutoAnswer import MILDDLMSAutoAnswer
from .objects.MILDDLMSAutoConnect import MILDDLMSAutoConnect
from .objects.MILDDLMSClock import MILDDLMSClock
from .objects.MILDDLMSData import MILDDLMSData
from .objects.MILDDLMSDemandRegister import MILDDLMSDemandRegister
from .objects.MILDDLMSMacAddressSetup import MILDDLMSMacAddressSetup
from .objects.MILDDLMSRegister import MILDDLMSRegister
from .objects.MILDDLMSExtendedRegister import MILDDLMSExtendedRegister
from .objects.MILDDLMSGprsSetup import MILDDLMSGprsSetup
from .objects.MILDDLMSHdlcSetup import MILDDLMSHdlcSetup
from .objects.MILDDLMSIECLocalPortSetup import MILDDLMSIECLocalPortSetup
from .objects.MILDDLMSIecTwistedPairSetup import MILDDLMSIecTwistedPairSetup
from .objects.MILDDLMSIp4Setup import MILDDLMSIp4Setup
from .objects.MILDDLMSIp6Setup import MILDDLMSIp6Setup
from .objects.MILDDLMSMBusSlavePortSetup import MILDDLMSMBusSlavePortSetup
from .objects.MILDDLMSImageTransfer import MILDDLMSImageTransfer
from .objects.MILDDLMSSecuritySetup import MILDDLMSSecuritySetup
from .objects.MILDDLMSDisconnectControl import MILDDLMSDisconnectControl
from .objects.MILDDLMSLimiter import MILDDLMSLimiter

from .objects.MILDDLMSMBusClient import MILDDLMSMBusClient
from .objects.MILDDLMSModemConfiguration import MILDDLMSModemConfiguration
from .objects.MILDDLMSPppSetup import MILDDLMSPppSetup
from .objects.MILDDLMSProfileGeneric import MILDDLMSProfileGeneric
from .objects.MILDDLMSRegisterMonitor import MILDDLMSRegisterMonitor
from .objects.MILDDLMSRegisterActivation import MILDDLMSRegisterActivation
from .objects.MILDDLMSSapAssignment import MILDDLMSSapAssignment
from .objects.MILDDLMSSchedule import MILDDLMSSchedule
from .objects.MILDDLMSScriptTable import MILDDLMSScriptTable
from .objects.MILDDLMSSpecialDaysTable import MILDDLMSSpecialDaysTable
from .objects.MILDDLMSTcpUdpSetup  import MILDDLMSTcpUdpSetup
from .objects.MILDDLMSPushSetup import MILDDLMSPushSetup
from .objects.MILDDLMSMBusMasterPortSetup import MILDDLMSMBusMasterPortSetup
from .objects.MILDDLMSGSMDiagnostic import MILDDLMSGSMDiagnostic
from .objects.MILDDLMSAccount import MILDDLMSAccount
from .objects.MILDDLMSCredit import MILDDLMSCredit
from .objects.MILDDLMSCharge import MILDDLMSCharge
from .objects.MILDDLMSTokenGateway import MILDDLMSTokenGateway
from .objects.MILDDLMSParameterMonitor import MILDDLMSParameterMonitor
from .objects.MILDDLMSUtilityTables import MILDDLMSUtilityTables
from .objects.MILDDLMSLlcSscsSetup import MILDDLMSLlcSscsSetup
from .objects.MILDDLMSPrimeNbOfdmPlcPhysicalLayerCounters import MILDDLMSPrimeNbOfdmPlcPhysicalLayerCounters
from .objects.MILDDLMSPrimeNbOfdmPlcMacSetup import MILDDLMSPrimeNbOfdmPlcMacSetup
from .objects.MILDDLMSPrimeNbOfdmPlcMacFunctionalParameters import MILDDLMSPrimeNbOfdmPlcMacFunctionalParameters
from .objects.MILDDLMSPrimeNbOfdmPlcMacCounters import MILDDLMSPrimeNbOfdmPlcMacCounters
from .objects.MILDDLMSPrimeNbOfdmPlcMacNetworkAdministrationData import MILDDLMSPrimeNbOfdmPlcMacNetworkAdministrationData
from .objects.MILDDLMSPrimeNbOfdmPlcApplicationsIdentification import MILDDLMSPrimeNbOfdmPlcApplicationsIdentification
from .objects.MILDDLMSNtpSetup import MILDDLMSNtpSetup

class _MILDObjectFactory:
    #Reserved for internal use.

    #
    # Constructor.
    def __init__(self):
        pass

    @classmethod
    def createObject(cls, ot):
        #pylint: disable=bad-option-value,redefined-variable-type
        #  If IC is manufacturer specific or unknown.
        if ot is None:
            raise ValueError("Invalid object type.")

        if ot == ObjectType.ACTION_SCHEDULE:
            ret = MILDDLMSActionSchedule()
        elif ot == ObjectType.ACTIVITY_CALENDAR:
            ret = MILDDLMSActivityCalendar()
        elif ot == ObjectType.ASSOCIATION_LOGICAL_NAME:
            ret = MILDDLMSAssociationLogicalName()
        elif ot == ObjectType.ASSOCIATION_SHORT_NAME:
            ret = MILDDLMSAssociationShortName()
        elif ot == ObjectType.AUTO_ANSWER:
            ret = MILDDLMSAutoAnswer()
        elif ot == ObjectType.AUTO_CONNECT:
            ret = MILDDLMSAutoConnect()
        elif ot == ObjectType.CLOCK:
            ret = MILDDLMSClock()
        elif ot == ObjectType.DATA:
            ret = MILDDLMSData()
        elif ot == ObjectType.DEMAND_REGISTER:
            ret = MILDDLMSDemandRegister()
        elif ot == ObjectType.MAC_ADDRESS_SETUP:
            ret = MILDDLMSMacAddressSetup()
        elif ot == ObjectType.REGISTER:
            ret = MILDDLMSRegister()
        elif ot == ObjectType.EXTENDED_REGISTER:
            ret = MILDDLMSExtendedRegister()
        elif ot == ObjectType.GPRS_SETUP:
            ret = MILDDLMSGprsSetup()
        elif ot == ObjectType.IEC_HDLC_SETUP:
            ret = MILDDLMSHdlcSetup()
        elif ot == ObjectType.IEC_LOCAL_PORT_SETUP:
            ret = MILDDLMSIECLocalPortSetup()
        elif ot == ObjectType.IEC_TWISTED_PAIR_SETUP:
            ret = MILDDLMSIecTwistedPairSetup()
        elif ot == ObjectType.IP4_SETUP:
            ret = MILDDLMSIp4Setup()
        elif ot == ObjectType.IP6_SETUP:
            ret = MILDDLMSIp6Setup()
        elif ot == ObjectType.MBUS_SLAVE_PORT_SETUP:
            ret = MILDDLMSMBusSlavePortSetup()
        elif ot == ObjectType.IMAGE_TRANSFER:
            ret = MILDDLMSImageTransfer()
        elif ot == ObjectType.SECURITY_SETUP:
            ret = MILDDLMSSecuritySetup()
        elif ot == ObjectType.DISCONNECT_CONTROL:
            ret = MILDDLMSDisconnectControl()
        elif ot == ObjectType.LIMITER:
            ret = MILDDLMSLimiter()
        elif ot == ObjectType.MBUS_CLIENT:
            ret = MILDDLMSMBusClient()
        elif ot == ObjectType.MODEM_CONFIGURATION:
            ret = MILDDLMSModemConfiguration()
        elif ot == ObjectType.PPP_SETUP:
            ret = MILDDLMSPppSetup()
        elif ot == ObjectType.PROFILE_GENERIC:
            ret = MILDDLMSProfileGeneric()
        elif ot == ObjectType.REGISTER_MONITOR:
            ret = MILDDLMSRegisterMonitor()
        elif ot == ObjectType.REGISTER_ACTIVATION:
            ret = MILDDLMSRegisterActivation()
        elif ot == ObjectType.REGISTER_TABLE:
            ret = MILDDLMSObject(ot)
        elif ot == ObjectType.ZIG_BEE_SAS_STARTUP:
            ret = MILDDLMSObject(ot)
        elif ot == ObjectType.ZIG_BEE_SAS_JOIN:
            ret = MILDDLMSObject(ot)
        elif ot == ObjectType.SAP_ASSIGNMENT:
            ret = MILDDLMSSapAssignment()
        elif ot == ObjectType.SCHEDULE:
            ret = MILDDLMSSchedule()
        elif ot == ObjectType.SCRIPT_TABLE:
            ret = MILDDLMSScriptTable()
        elif ot == ObjectType.SPECIAL_DAYS_TABLE:
            ret = MILDDLMSSpecialDaysTable()
        elif ot == ObjectType.STATUS_MAPPING:
            ret = MILDDLMSObject(ot)
        elif ot == ObjectType.TCP_UDP_SETUP:
            ret = MILDDLMSTcpUdpSetup()
        elif ot == ObjectType.ZIG_BEE_SAS_APS_FRAGMENTATION:
            ret = MILDDLMSObject(ot)
        elif ot == ObjectType.UTILITY_TABLES:
            ret = MILDDLMSUtilityTables()
        elif ot == ObjectType.PUSH_SETUP:
            ret = MILDDLMSPushSetup()
        elif ot == ObjectType.MBUS_MASTER_PORT_SETUP:
            ret = MILDDLMSMBusMasterPortSetup()
        elif ot == ObjectType.GSM_DIAGNOSTIC:
            ret = MILDDLMSGSMDiagnostic()
        elif ot == ObjectType.ACCOUNT:
            ret = MILDDLMSAccount()
        elif ot == ObjectType.CREDIT:
            ret = MILDDLMSCredit()
        elif ot == ObjectType.CHARGE:
            ret = MILDDLMSCharge()
        elif ot == ObjectType.TOKEN_GATEWAY:
            ret = MILDDLMSTokenGateway()
        elif ot == ObjectType.PARAMETER_MONITOR:
            ret = MILDDLMSParameterMonitor()
        elif ot == ObjectType.LLC_SSCS_SETUP:
            ret = MILDDLMSLlcSscsSetup()
        elif ot == ObjectType.PRIME_NB_OFDM_PLC_PHYSICAL_LAYER_COUNTERS:
            ret = MILDDLMSPrimeNbOfdmPlcPhysicalLayerCounters()
        elif ot == ObjectType.PRIME_NB_OFDM_PLC_MAC_SETUP:
            ret = MILDDLMSPrimeNbOfdmPlcMacSetup()
        elif ot == ObjectType.PRIME_NB_OFDM_PLC_MAC_FUNCTIONAL_PARAMETERS:
            ret = MILDDLMSPrimeNbOfdmPlcMacFunctionalParameters()
        elif ot == ObjectType.PRIME_NB_OFDM_PLC_MAC_COUNTERS:
            ret = MILDDLMSPrimeNbOfdmPlcMacCounters()
        elif ot == ObjectType.PRIME_NB_OFDM_PLC_MAC_NETWORK_ADMINISTRATION_DATA:
            ret = MILDDLMSPrimeNbOfdmPlcMacNetworkAdministrationData()
        elif ot == ObjectType.PRIME_NB_OFDM_PLC_APPLICATIONS_IDENTIFICATION:
            ret = MILDDLMSPrimeNbOfdmPlcApplicationsIdentification()
        elif ot == ObjectType.NTP_SETUP:
            ret = MILDDLMSNtpSetup()
        else:
            ret = MILDDLMSObject(ot)
        return ret
