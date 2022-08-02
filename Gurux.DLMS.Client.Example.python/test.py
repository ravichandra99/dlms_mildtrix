import os
import sys
import traceback
from gurux_serial import GXSerial
from gurux_net import GXNet
from gurux_dlms.enums import ObjectType
from gurux_dlms.objects.GXDLMSObjectCollection import GXDLMSObjectCollection
from GXSettings import GXSettings
from GXDLMSReader import GXDLMSReader
from gurux_dlms.GXDLMSClient import GXDLMSClient
from gurux_common.GXCommon import GXCommon
from gurux_dlms.enums.DataType import DataType
import locale
from gurux_dlms.GXDateTime import GXDateTime
from gurux_dlms.internal._GXCommon import _GXCommon
from gurux_dlms import GXDLMSException, GXDLMSExceptionResponse, GXDLMSConfirmedServiceError, GXDLMSTranslator
from gurux_dlms import GXByteBuffer, GXDLMSTranslatorMessage, GXReplyData
from gurux_dlms.enums import RequestTypes, Security, InterfaceType
from gurux_dlms.secure.GXDLMSSecureClient import GXDLMSSecureClient


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
        settings = GXSettings()
        # try:
        #     # //////////////////////////////////////
        #     #  Handle command line parameters.
        print(settings,'_______________setting')
        ret = settings.getParameters(args)
        print(self.client.outputFile,'__________________________tttttttttttttt')
        if ret != 0:
            print('____return')
            return

        if not isinstance(settings.media, (GXSerial, GXNet)):
            raise Exception("Unknown media type.")
        # //////////////////////////////////////
        reader = GXDLMSReader(settings.client, settings.media, settings.trace, settings.invocationCounter)
        print('____________________________llllllllllllllll')

        settings.media.open()
#if __name__ == '__main__':
   
sampleclient.main(sys.argv)