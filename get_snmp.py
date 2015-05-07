#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from snmp import router, load_json_file

# Read router infomation from JSON file.
if sys.argv[1]:
    pass
else:
    print 'Please use bellow: " python snmp_router.py [JSON file] " '
    sys.exit()

router_info = load_json_file( sys.argv[1] )

# Create router object and execute SNMP.
for num in range( len(router_info) ):
    router = Router( router_info[num] )
    
    cpu_usage = router.get_snmp('cpu_usage')
    memory_usage = router.get_snmp('memory_usage')
   
    print 'Router : ' + router_info[num]['hostname']
    print '  cpu_usage : ' + str(cpu_usage)
    print '  memory_usage : ' + str(memory_usage)
    
