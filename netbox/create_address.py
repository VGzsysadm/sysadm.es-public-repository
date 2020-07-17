#!/usr/bin/env python
#######
# Author: VGzsysadm - sysadm.es - 
# repository: https://github.com/VGzsysadm/sysadm.es-public-repository
#######
#Pytohn version - Python3.8
#Dependencies
#pip install pynetbox

import pynetbox
import argparse



def init_conn():
    try:
        nb = pynetbox.api(
        'http://192.168.1.100:8000',
        token='0123456789abcdef0123456789abcdef01234567'
        )
    except Exception as e:
        print(e)
    return nb

def serialization(data_string):
    try: 
        data = data_string.isdigit()
        return data
    except ValueError:
        return data

def create_available_ip(nb, identity, dns=None):
    try: 
        prefix = nb.ipam.prefixes.get(identity)
        if dns is not None:
            return prefix.available_ips.create(
                {'dns_name': dns}
            )
        else:
            return prefix.available_ips.create()
    except Exception as e:
        return print(e)

def main():
    """
    Params expected
    Params:
        *Required -p --prefix: Prefix id from netblox
        Optional -d --dns: DNS name for object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--prefix', action="store", dest="prefix")
    parser.add_argument('-d','--dns', action="store", dest="dns")
    args = parser.parse_args()
    if args.prefix:
        res = serialization(args.prefix)
        if res == True:
            nb = init_conn()
            res = create_available_ip(nb, args.prefix, args.dns)
            print(res)
        else:
            print("-p or --prefix must be an id, example /ipam/prefixes/1/ -> -p 1 or --prefix 1")
    else:
        print("-p or --prefix argument are required, example --prefix 1")

if __name__ == "__main__":
    main()
