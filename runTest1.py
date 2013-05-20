import time
from util import GetConfig
from runtestinstances import RunInstancesTest
from runsnapshot import RunSnapshot
from logger import Logger
from cleanup import CleanUp


class RunTest1():
    
   
    
    var_ = GetConfig()
    log = Logger()
    test = RunInstancesTest()
    clear = CleanUp()
    startTime = time.time()
    
    def runTest1(self,config):
        
        test_name = self.var_._randomName()
        print "Running Instances and Snapshot Test:%s" % test_name
        
        if self.test.preTestCheck(config)!=None:
            
            msg = "Pre Check passed, running instances test"
            self.log.log_data(config.log_file,msg,"INFO")
            run_result = self.test.runTest(config,test_name)
            if run_result!=None:
                msg = "Instances test completed, proceed with snapshot"
                self.log.log_data(config.log_file,msg,"INFO")
                print msg
                snap = RunSnapshot().runSnapshot(config,run_result,test_name)
                if snap[1]!=False:
                    msg = "Snapshot Test passed"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                
                    msg = "Test Successful, took %.2f seconds to complete " % (time.time()-self.startTime)
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                
                    msg = "Running Cleaning up"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                
                    msg = "Terminating Instances"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                    self.clear.removeInstances(config, run_result)
                
                    msg = "Removing Snapshot"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                    self.clear.removeSnapshot(config, snap[0])
                
                
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
                    msg = "Snapshot test failed"
                    self.log.log_data(config.log_file,msg,"ERROR")
                    print msg
                    
                    msg = "Running Cleaning up"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                    
                    msg = "Removing Failed Snapshot"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                    self.clear.removeSnapshot(config, snap[0])
                    
                    msg = "Terminating Instances"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                    self.clear.removeInstances(config, run_result)
                    
                    msg = "Removing Security Groups and Keypair in next 10 seconds"
                    self.log.log_data(config.log_file,msg,"INFO")
                    misc = {'sg':test_name,'kp':test_name}
                    time.sleep(int(config.timeout))
                    self.clear.removeMisc(config,misc)
                    print msg
                
                    msg = "Clean Up complete, exiting test"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                    
                    
                    raise SystemExit
            
            else:
                msg = "Run instances test failed"
                self.log.log_data(config.log_file,msg,"ERROR")
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
                
                raise SystemExit
        else:
            msg = "Pre Check failed, test halted"
            self.log.log_data(config.log_file,msg,"ERROR")
            print msg
            raise SystemExit
            