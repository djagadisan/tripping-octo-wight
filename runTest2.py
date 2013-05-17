import time
from util import GetConfig
from runtestinstances import RunInstancesTest
from logger import Logger
from cleanup import CleanUp


class RunTest2():
    
   
    
    var_ = GetConfig()
    log = Logger()
    test = RunInstancesTest()
    clear = CleanUp()
    startTime = time.time()
    
    
    def runTest2(self,config):
        test_name = self.var_._randomName()
        print "Running Instances Test"
        if self.test.preTestCheck(config)!=None:
            msg = "Pre Check passed, running instances test %s" % test_name
            self.log.log_data(config.log_file,msg,"INFO")
            run_result = self.test.runTest(config,test_name)
            if run_result!=None:
                msg = "Instances test passed, test took %.2f to complete" % (time.time()-self.startTime) 
                self.log.log_data(config.log_file,msg,"INFO")
                print msg
            
                msg = "Running Cleaning up"
                self.log.log_data(config.log_file,msg,"INFO")
                print msg
            
                msg = "Terminating Instances"
                self.log.log_data(config.log_file,msg,"INFO")
                print msg
                self.clear.removeInstances(config, run_result)
            
                msg = "Removing Security Groups and Keypair in next 10 seconds"
                self.log.log_data(config.log_file,msg,"INFO")
                misc = {'sg':test_name,'kp':test_name}
                time.sleep(int(config.timeout))
                self.clear.removeMisc(config,misc)
            
                msg = "Clean Up complete, exiting test"
                self.log.log_data(config.log_file,msg,"INFO")
                print msg  
                raise SystemExit
            else:
                msg = "Run instances test failed"
                self.log.log_debug(config.log_name,msg,"ERROR")
                raise SystemExit
            
                msg = "Running Cleaning up"
                self.log.log_data(config.log_file,msg,"INFO")
                print msg
                
                msg = "Terminating Instances"
                self.log.log_data(config.log_file,msg,"INFO")
                print msg
                self.clear.removeInstances(config, run_result)
                
                msg = "Removing Security Groups and Keypair in next 10 seconds"
                self.log.log_data(config.log_file,msg,"INFO")
                misc = {'sg':test_name,'kp':test_name}
                time.sleep(int(config.timeout))
                self.clear.removeMisc(config,misc)
                
                msg = "Clean Up complete, exiting test"
                self.log.log_data(config.log_file,msg,"INFO")
        
        else:
            msg = "Pre Check failed,test halted"
            self.log.log_debug(config.log_name,msg,"ERROR")
            print msg
            raise SystemExit
            
            