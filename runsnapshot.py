import os
import sys
import time
import datetime
from util import GetConfig
from novaaction import NovaAction

from logger import Logger


class RunSnapshot():
    
    snap = NovaAction()
    log = Logger()
    helper = GetConfig()
    
    def runSnapshot(self, obj,vm_obj):
        
        now = datetime.datetime.now()
        startTime = time.time()
        
        msg = "Snapshot Test started"
        self.log.log_debug(obj.log_file,msg,"INFO")
        client = self.nova_.createNovaConnection(obj)
        vm_snap = snap.createSnapshot("snap-"+obj.test_name,vm_obj[0].id,client)
        
        msg = "Snapshot requested on VM:" % vm_obj[0].id
        self.log.log_debug(obj.log_file,msg,"INFO")
        
        while snap.getImageInfo(vm_snap,client)!='ACTIVE':
            if count!=30:
                if snap.getImageInfo(vm_snap,client)!='ERROR':
                    time.sleep(10)
                    count=count+1
                elif nova_action.getImageInfo(snapshot_,client)==None:
                    msg = "Snapshot Failed, most likely snapshot is killed by glance"
                    self.log.log_debug(obj.log_file,msg,"ERROR")
                    raise SystemExit
                else:
                    msg = "Snaphot failed, did not reach active state after %r seconds" % (time.time()-startTime) 
                    self.log.log_debug(obj.log_file,msg,"ERROR")
                    raise SystemExit
                        
        msg = "Snapshot %s is ok, test took %r to complete" % (vm_snap,(time.time()-startTime))
        self.log.log_debug(obj.log_file,msg,"INFO")
        return vm_snap
           
        