#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import traceback
from pysnmp.entity.rfc3413.oneliner import cmdgen

# Open json file and convert format to dictionary_type
def load_json_file(filename):
    try:
        file = open(filename, 'r')
    except IOError:
        print 'Cannot open json file : ' + filename
        file.close()
    else:
        info_json = file.read()
        file.close()

    try:
        info_dict = json.loads(info_json)
    except ValueError as error:
        print 'JSON format error :'
        print info_json
        print error
        result = ''
    else:
        result = info_dict

    return result


class Router:
    def __init__(self, router_info):
        self.hostname   = router_info['hostname']
        self.ipv4       = router_info['ipv4']
        self.os         = router_info['os']
        self.snmp_community = router_info['snmp_community']

        # read oid list and pick out using router OS
        self.oid_info   = self.load_oid()

    def load_oid(self):
        oid_info_OSs = load_json_file('oid.json')
        if self.os == 'IOS-XR' or self.os == 'JUNOS':
            pass
        else:
            raise AttributeError( 'Plase select OS from JUNOS/IOS-XR . Your OS is ' + self.os + ' .')
        
        try:
            oid_info = oid_info_OSs[self.os]
        except:
            raise AttributeError( 'JSON format Error.')

        return oid_info

    def get_snmp(self, oid_item, port=161):
        generator      = cmdgen.CommandGenerator()
        # 1 = snmp version v2c
        community_data = cmdgen.CommunityData('server','mesh', 1)
        transport      = cmdgen.UdpTransportTarget( ('202.247.123.108', 161) )
        function = getattr(generator, 'nextCmd')
        #oid = (1,3,6,1,4,1,2636,3,1,13,1,8,9,1,0,0)
        oid = '.1.3.6.1.4.1.2636.3.1.13.1.8.9.1.0.0'
        try :
            (error, error_text, error_no, result) = function( community_data, transport, oid )
            
            #(error, error_text, error_no, result) = command.getCmd( commuminity_data, transport, self.oid_info[oid_item] )
        except:
            traceback.print_exc()
            sys.exit()
        return result
