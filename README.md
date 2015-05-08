# SNMPRouter
This tool is gethering router information using SNMP

# Support router's OSs
- JUNOS
- IOS-XR
- IOS
- IOS-XE

## How to use this tool

```
python get_snmp.py [json file]
```

You can describe multipul routers using json format.
The router's OS is select from the below list.
- JUNOS
- IOS-XR

This is sample json file.

```my_router.json
[
    {
        "hostname"       : "router1",
        "ipv4"           : "192.168.0.1",
        "os"             : "JUNOS",
        "snmp_community" : "aaabbbccc"
    },
    {
        "hostname"       : "router2",
        "ipv4"           : "192.168.0.2",
        "os"             : "IOS-XR",
        "snmp_community" : "aaabbbccc"
    },
    {
        "hostname"       : "router3",
        "ipv4"           : "192.168.0.3",
        "os"             : "JUNOS",
        "snmp_community" : "aaabbbccc"
    }
]
```
