import os
import sys
import argparse

class Options ():

    def arg_parse(self):
        parse = argparse.ArgumentParser(description="Run VM Test on NeCTAR")
        parse.add_argument('tenant',help='Tenant name listed in config file')
        group = parse.add_mutually_exclusive_group(required=True)
        group.add_argument("--all",action='store_true',help="Run VM and Snapshot Test")
        group.add_argument("--instances",action='store_true',help="Run VM Test only")
        args = parse.parse_args()
    
        return args