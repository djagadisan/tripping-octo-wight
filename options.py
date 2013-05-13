import os
import sys
import argparse



def _arg_parse():
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('run_test',help='Run Test')
    parser.add_argument('--all',action='store',required=True,help='Run VM and Snapshot Test')
    parser.add_argument('--instances',action='store',required=True,help='Run VM Test only')
    
    
    return parser.parse_args()



__init__ = 'main'

results=_arg_parse()