from util import GetConfig
from novaaction import NovaAction

from logger import Logger

class CleanUp():
    nova_ = NovaAction()
    log = Logger()
    helper = GetConfig()
    
    def removeInstances(self,obj,instances):
        
            client = self.nova_.createNovaConnection(obj)            
            self.nova_.terminateInstances(instances.id, client)
            msg="Instances %s terminated" %instances.name
            self.log.log_data(obj.log_file,msg,"INFO")
            
            return True
            
    def removeMisc(self,obj,misc):
            
            client = self.nova_.createNovaConnection(obj)
            
            self.nova_.removeSecurityGroupRules(misc.get('sg'), client)
            msg="Security group %s removed" % misc.get('security_group')
            self.log.log_data(obj.log_file,msg,"INFO")
            
            self.nova_.deleteKeypair(misc.get('kp'),client)
            msg="Key pair %s removed" % misc.get('kp')
            self.log.log_data(obj.log_file,msg,"INFO")
            
            self.helper.removeFiles(obj.ssh_key)
            msg="SSH Key removed"
            self.log.log_data(obj.log_file,msg,"INFO")
            
            
    def removeSnapshot(self,obj,snapshot_id):
            
            client = self.nova_.createNovaConnection(obj)
            self.nova_.deleteSnapshot(snapshot_id, client)
            msg="Snapshot Removed"
            self.log.log_data(obj.log_file,msg,"INFO")
            

            
            
            
            
            
            
            
            
        
        
        
        