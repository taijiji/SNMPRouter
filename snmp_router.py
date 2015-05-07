#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json

from pysnmp import role, v2c

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
        oid_info_OSs = load_json_file('oid.json', 'r')
        try: 
            oid_info = oid_info_OSs[self.os]
        except:
            raise AttributeError( self.os + ' is not support. Please use JUNOS/IOS-XR')

        return oid_info
    
    def get_snmp(self, ip, port=161):
	   	session = role.namager((self.ip, port))

