
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



import json
from pymongo import MongoClient

import json
import xmltodict

import pymysql
import random

client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.5.3")
db = client['countries_db']
collection_currency = db['currency']

def mysqlconnect(sql,res):
	# To connect MySQL database
	conn = pymysql.connect(
		host='localhost',
		user='root',
		password = "Mildtrix#432317",
		db='smartmeter1',
		)
	
	cur = conn.cursor()
	cur.execute(sql,res)
	conn.commit()
	# To close the connection
	conn.close()



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
        try:
            print("gurux_dlms version: " + pkg_resources.get_distribution("gurux_dlms").version)
            print("gurux_net version: " + pkg_resources.get_distribution("gurux_net").version)
            print("gurux_serial version: " + pkg_resources.get_distribution("gurux_serial").version)
        except Exception:
            #It's OK if this fails.
            print("pkg_resources not found")

        # args: the command line arguments
        reader = None
        settings = GXSettings()
        try:
            # //////////////////////////////////////
            #  Handle command line parameters.
            ret = settings.getParameters(args)
            if ret != 0:
                return
            # //////////////////////////////////////
            #  Initialize connection settings.
            if not isinstance(settings.media, (GXSerial, GXNet)):
                raise Exception("Unknown media type.")
            # //////////////////////////////////////
            reader = GXDLMSReader(settings.client, settings.media, settings.trace, settings.invocationCounter)
            settings.media.open()
            print(settings.readObjects)
            if settings.readObjects:
                
                read = False
                reader.initializeConnection()
                print('________main_sucess6')
                if settings.outputFile and os.path.exists(settings.outputFile):
                    try:
                        c = GXDLMSObjectCollection.load(settings.outputFile)
                        settings.client.objects.extend(c)
                        if settings.client.objects:
                            read = True
                            print('________main_sucess')

                    except Exception:
                        print('________main_sucess2')
                        read = False
                if not read:
                    print('________main_sucess3')
                    reader.getAssociationView()
                for k, v in settings.readObjects:
                    print('________main_sucess5')
                    obj = settings.client.objects.findByLN(ObjectType.NONE, k)
                    if obj is None:
                        raise Exception("Unknown logical name:" + k)
                    val = reader.read(obj, v)
                    reader.showValue(v, val)
                if settings.outputFile:
                    settings.client.objects.save(settings.outputFile)
            else:
                print('________main_sucess4')
                reader.readAll(settings.outputFile)
                with open('/var/www/gurux_yash/Gurux.DLMS.Client.Example.python/device.xml') as xml_file:
                        data_dict = xmltodict.parse(xml_file.read())
                        xml_file.close()

                        collection_currency.insert_one(data_dict)
                        # if pymongo >= 3.0 use insert_many() for inserting many documents
                        #collection_currency.insert_many(file_data)
                        print('sent data to mongodb sucessfully')
                        client.close()

                        mylist = data_dict['Objects']['GXDLMSData']

                        columns = ['COSEM_Logical_Device_Name', 'Meter_Serial_Number', 'Device_ID', 'Manufacturer_Name', 'Firmware_Version_For_Meter', 'Meter_Type', 'Meter_Category', 'Current_Rating', 'Year_Of_Manufacture', 'Demand_Integration_Period', 'Profile_Capture_Period', 'Recording_interval_2', 'Cumulative_Tamper_Count', 'Cum_Billing_Count', 'Cum_Programming_Count', 'Event_Voltage_Related', 'Event_Current_Related', 'Event_Power_Related', 'Event_Transaction_Related', 'Event_Others', 'Event_Non_Roll_Over', 'Event_Control', 'Available_Billing_Periods', 'Event_Status_Word_1_ESW1', 'ESWF', 'Metering_Mode', 'Payment_Mode', 'Last_Token_Recharge_Amount', 'Last_Token_Recharge_Time', 'Total_Amount_At_Last_Recharge', 'Current_Balance_Amount', 'Current_Balance_Time', 'Manufacturer_specific_1', 'Manufacturer_specific_2', 'Manufacturer_specific_3', 'Manufacturer_specific_4', 'Entry_Date_Time', 'Update_Date_Time', 'Entry_By', 'Update_BY']

                        obis_codes = ['1.0.0.8.4.255', '0.0.96.11.0.255', '0.0.96.11.1.255', '0.0.96.11.2.255', '0.0.96.11.3.255', '0.0.96.11.4.255', '0.0.96.11.5.255', '0.0.96.11.6.255', '0.0.94.91.18.255', '0.0.94.91.26.255', '0.0.94.96.19.255', '0.0.94.96.20.255', '0.0.94.96.24.255', '0.0.94.96.25.255', '0.0.128.128.6.255', '0.0.128.128.7.255', '0.0.128.128.8.255', '0.0.19.128.0.255']

                        obis_names = ['Profile_Capture_Period','Event_Voltage_Related','Event_Current_Related','Event_Power_Related','Event_Transaction_Related','Event_Others','Event_Non_Roll_Over','Event_control','Event_Status_Word_1_ESW1','ESWF','Metering_Mode','Payment_Mode','Current_Balance_Amount','Current_Balance_Time','Manufacturer_specific_1','Manufacturer_specific_2','Manufacturer_specific_3','Manufacturer_specific_4']

                        obis = dict(zip(obis_names,obis_codes))

                        a = random.randint(0,100000000)

                        res = []
                        for i in columns:
                            if i in obis_names:
                                j = obis[i]
                                r = list(filter(lambda ln: ln['LN'] == j, mylist))
                                res.append(r[0]['Value']['#text'])
                            else:
                                res.append(None)

                        res = [a] + res

                        params = ['%s' for item in res]
                        sql    = 'INSERT INTO obis_15min VALUES (%s);' % ','.join(params)
                        mysqlconnect(sql,res)


        except (ValueError, GXDLMSException, GXDLMSExceptionResponse, GXDLMSConfirmedServiceError) as ex:
            print(ex)
        except (KeyboardInterrupt, SystemExit, Exception) as ex:
            traceback.print_exc()
            if settings.media:
                settings.media.close()
            reader = None
        finally:
            if reader:
                try:
                    reader.close()
                except Exception:
                    traceback.print_exc()
            print("Ended. Press any key to continue.")

if __name__ == '__main__':
   
    sampleclient.main(sys.argv)



#python3 main.py -h 2402:3A80:1702:116::1 -p 4059  -d DLMS  -i WRAPPER -c 48 -a High -P TriHLS1234567890 -C AuthenticationEncryption -T 5452493030303030 -A 5472695F5F5F556E6963617374417363 -B 5472695F5F5F556E6963617374417363 -L TIS -s 1 -W 1 -l 0 -t Verbose -o device.xml
