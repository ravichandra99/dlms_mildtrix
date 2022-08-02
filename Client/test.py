import os
import sys
import traceback
from serial_mt import MILDSerial
from net_mt import MILDNet
from dlms_mt.enums import ObjectType
from dlms_mt.objects.MILDDLMSObjectCollection import MILDDLMSObjectCollection
from MILDSettings import MILDSettings
from MILDDLMSReader import MILDDLMSReader
from dlms_mt.MILDDLMSClient import MILDDLMSClient
from common_mt.MILDCommon import MILDCommon
from dlms_mt.enums.DataType import DataType
import locale
from dlms_mt.MILDDateTime import MILDDateTime
from dlms_mt.internal._MILDCommon import _MILDCommon
from dlms_mt import MILDDLMSException, MILDDLMSExceptionResponse, MILDDLMSConfirmedServiceError, MILDDLMSTranslator
from dlms_mt import MILDByteBuffer, MILDDLMSTranslatorMessage, MILDReplyData
from dlms_mt.enums import RequestTypes, Security, InterfaceType
from dlms_mt.secure.MILDDLMSSecureClient import MILDDLMSSecureClient


try:
    import pkg_resources
    #pylint: disable=broad-except
except Exception:
    #It's OK if this fails.
    print("pkg_resources not found")

#pylint: disable=too-few-public-methods,broad-except
class sampleclient():
    @classmethod
    def main(cls, args):

        reader = None
        settings = MILDSettings()
        # try:
        #     # //////////////////////////////////////
        #     #  Handle command line parameters.
        print(settings,'_______________setting')
        ret = settings.getParameters(args)
        print(self.client.outputFile,'__________________________tttttttttttttt')
        if ret != 0:
            print('____return')
            return

        if not isinstance(settings.media, (MILDSerial, MILDNet)):
            raise Exception("Unknown media type.")
        # //////////////////////////////////////
        reader = MILDDLMSReader(settings.client, settings.media, settings.trace, settings.invocationCounter)
        print('____________________________llllllllllllllll')

        settings.media.open()
#if __name__ == '__main__':
   
sampleclient.main(sys.argv)