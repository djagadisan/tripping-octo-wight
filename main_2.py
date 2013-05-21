from config_data import GetVar
from options import Options
from runTest1 import RunTest1
from runTest2 import RunTest2



__init__ = 'main'
get_options = Options()
data=get_options.arg_parse()
config = GetVar(getattr(data,"tenant"))
if getattr(data,"cell")!=None:
    config.cell = getattr(data,"cell")



if getattr(data,'all')==True and getattr(data,'instances')==False:
    RunTest1().runTest1(config)


elif getattr(data,'all')==False and getattr(data,'instances')==True:
    RunTest2().runTest2(config)
    
else:
    print "Invalid Selection,exit test"
    raise SystemExit








