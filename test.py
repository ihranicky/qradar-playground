#!/usr/bin/env python3

import sys
import os
import requests
import json


# Hack no.1: FORCE IPV4
import socket
import requests.packages.urllib3.util.connection as urllib3_cn

def allowed_gai_family():
    family = socket.AF_INET # force IPv4
    return family

urllib3_cn.allowed_gai_family = allowed_gai_family

# Hack no.2: Disable warning about insecure HTTPS context
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ====================================================================

def main():
    h = {#'Range': 'items=0-49',
         'SEC': '<ENTER-SECURE-TOKEN-HERE>',
         'Version': '12.0',
         'Accept': 'application/json'
        }

    response = requests.get(url='https://feta1.fit.vutbr.cz/api/siem/source_addresses', headers=h, verify=False)
    resp_json = response.json()

    # Load IP addresses
    ips = set()

    for addr in resp_json:
        ips.add(addr['source_ip'])

    print(ips) # Return the list of offense source IPs


if __name__ == "__main__":
    main()
