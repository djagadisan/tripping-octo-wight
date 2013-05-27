import time
import datetime
from util import GetConfig
from runtestinstances import RunInstancesTest
from logger import Logger
from cleanup import CleanUp
from write_to_csv import WriteCSV

class RunTest2():
    
   
    
    var_ = GetConfig()
    log = Logger()
    test = RunInstancesTest()
    clear = CleanUp()
    writer_ = WriteCSV()
    startTime = time.time()
    run_time = datetime.datetime.now().strftime("%d%m%y%H%M%S")
    def runTest2(self,config):
        test_name = self.var_._randomName()
        print "Running Instances Test"
        if self.test.preTestCheck(config)!=None:
            msg = "Pre Check passed, running instances test %s" % test_name
            self.log.log_data(config.log_file,msg,"INFO")
            run_result = self.test.runTest(config,test_name)
            if run_result[0]!=False:
                msg = "Instances test passed"
                self.log.log_data(config.log_file,msg,"INFO")
                print msg
            
                msg = "Running Cleaning up"
                self.log.log_data(config.log_file,msg,"INFO")
                print msg
            
                msg = "Terminating Instances"
                self.log.log_data(config.log_file,msg,"INFO")
                print msg
                self.clear.removeInstances(config, run_result[1])
                
                msg = "Waiting for instances to be removed, before removing security group and key pair"
                self.log.log_data(config.log_file,msg,"INFO")
                misc = {'sg':test_name,'kp':test_name}
                if self.clear.removeMisc(config,misc,run_result[1])==True:
                    time_comp = time.time()-self.startTime
                    msg = "Clean Up complete, exiting test"
                    self.log.log_data(config.log_file,msg,"INFO")
                
                    print msg  
                    data_insert = [test_name,self.run_time,config.cell,run_result[2],'0','NA','NA',time_comp,'0']
                    WriteCSV().createCSVFile(config.csv_file, data_insert)
                    raise SystemExit
                else:
                    time_comp = time.time()-self.startTime
                    msg = "Error, Unable to remove security group and key pair"
                    self.log.log_data(config.log_file,msg,"ERROR")
                    print msg
                    data_insert = [test_name,self.run_time,config.cell,run_result[2],'0','NA','NA',time_comp,'1']
                    WriteCSV().createCSVFile(config.csv_file, data_insert)
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
                self.clear.removeInstances(config, run_result[1])
                
                msg = "Removing Security Groups and Keypair in next 10 seconds"
                self.log.log_data(config.log_file,msg,"INFO")
                misc = {'sg':test_name,'kp':test_name}
                time.sleep(int(config.timeout))
                if self.clear.removeMisc(config,misc,run_result[1])==True:
                    time_comp = time.time()-self.startTime
                    data_insert = [test_name,self.run_time,config.cell,run_result[2],'1','NA','NA',time_comp,'1']
                    WriteCSV().createCSVFile(config.csv_file, data_insert)
                    msg = "Clean Up complete, exiting test"
                    self.log.log_data(config.log_file,msg,"INFO")
                else:
                    time_comp = time.time()-self.startTime
                    msg = "Error, Unable to remove security group and key pair"
                    self.log.log_data(config.log_file,msg,"ERROR")
                    print msg
                    data_insert = [test_name,self.run_time,config.cell,run_result[2],'0','NA','NA',time_comp,'1']
                    WriteCSV().createCSVFile(config.csv_file, data_insert)
                    raise SystemExit
                    
        
        else:
            msg = "Pre Check failed,test halted"
            self.log.log_data(config.log_file,msg,"ERROR")
            time_comp = self.var_.getrunTime('start')-self.var_.getrunTime(type)
            data_insert = [test_name,self.run_time,config.cell,'F','1','NA','NA',time_comp,'1']
            WriteCSV().createCSVFile(config.csv_file, data_insert)
            print msg
            raise SystemExit
            
            