import os
import sys
from config_data import GetVar
from util import GetConfig
from runtestinstances import RunInstancesTest
from runsnapshot import RunSnapshot
from logger import Logger



__init__ = 'main'

config = GetVar("deven")
var_ = GetConfig()
log = Logger()
test = RunInstancesTest()




def runTest1():
    if test.preTestCheck(config)!=None:
        msg = "Pre Check passed, running instances test"
        log.log_data(config.log_file,"INFO")
        if test.runTest(config)!=None:
            msg = "Instances test completed, proceed with snapshot"
            log.log_data(config.log_file,msg,"INFO")
            snap = RunSnapshot()
            if snap.runSnapshot(config)!=None:
                msg = "Snapshot Test passed, Test completed sucessfully"
                log.log_debug(config.log_name,"INFO")
                raise SystemExit
            
            else:
                msg = "Run instances test failed, exiting test"
                log.log_debug(config.log_name,msg,"ERROR")
                raise SystemExit
        else:
            msg = "Pre Check failed, test halted"
            raise SystemExit

   

def runTest2():
    if test.preTestCheck(config)!=None:
        msg = "Pre Check passed, running instances test"
        log.log_data(config.log_file,"INFO")
        if test.runTest(config)!=None:
            msg = "Instances test ok, exiting the test"
            log.log_data(config.log_file,msg,"INFO")
            raise SystemExit
        else:
            msg = "Run instances test failed, exiting test"
            log.log_debug(config.log_name,msg,"ERROR")
            raise SystemExit
        
    else:
        msg = "Pre Check failed,test halted"
        raise SystemExit
    
        
    
    

def runTest3():
    raise SystemExit
 


    
    
select = {0 : runTest1,
           1 : runTest2,
           2 : runTest3,           
}



select[0]()

''''
msg = "Test %s started" % (var_._randomName())
log.log_data(config.log_file,msg,"INFO")


# print test.preTestCheck(config)



if test.preTestCheck(config)!=None:
     msg = "Pre Check passed, running instances test"
     log.log_data(config.log_file,"INFO")


     
    




if test.preTestCheck(config)!=None:
    msg = "Pre Check passed, running instances test"
    log.log_debug(config.log_name,"INFO")
    if test.runTest(config)!=None:
        msg = "Instances test completed, proceed with snapshot"
        log.log_debug(config.log_name,msg,"INFO")
        snap = RunSnapshot()
        if snap.runSnapshot(config)!=None:
            msg = "Snapshot Test passed, Test completed sucessfully"
            log.log_debug(config.log_name,"INFO")
            
    else:
        msg = "Run instances test failed, exiting test"
        log.log_debug(config.log_name,msg,"ERROR")
        raise SystemExit
else:
    msg = "Pre Check failed, not continuning the test"
    raise SystemExit
'''           
        


 





