import time
from util import GetConfig
from novaaction import NovaAction

from logger import Logger


class RunSnapshot():
    
    snap = NovaAction()
    log = Logger()
    helper = GetConfig()
    
    def runSnapshot(self, obj,vm_obj,test_name):
        
        startTime = time.time()
        
        msg = "Snapshot Test started"
        self.log.log_data(obj.log_file,msg,"INFO")
        client = self.snap.createNovaConnection(obj)
        vm_snap = self.snap.createSnapshot(test_name,vm_obj.id,client)
        
        msg = "Snapshot requested on VM-:%s" % vm_obj.id
        self.log.log_data(obj.log_file,msg,"INFO")
        count = 0
        while self.snap.getImageInfo(vm_snap,True,client)!='ACTIVE':
            if count!=30:
                msg = "Count: %s" % count
                self.log.log_data(obj.log_file,msg,"INFO")
                if self.snap.getImageInfo(vm_snap,True,client)!='ERROR':
                    time.sleep(10)
                    count=count+1
                elif self.snap.getImageInfo(vm_snap,True,client)==None:
                    msg = "Snapshot Failed, most likely snapshot is killed by glance"
                    self.log.log_data(obj.log_file,msg,"ERROR")
                    return vm_snap,False
            else:
                msg = "Snapshot failed, did not reach active state after %.2f seconds" % (time.time()-startTime) 
                self.log.log_data(obj.log_file,msg,"ERROR")
                print msg
                return vm_snap,False
                        
        msg = "Snapshot %s is ok, test took %.2f to complete" % (vm_snap,(time.time()-startTime))
        self.log.log_data(obj.log_file,msg,"INFO")
        print msg
        return vm_snap,True
           
        