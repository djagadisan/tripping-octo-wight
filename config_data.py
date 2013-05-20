import os
import sys
from util import GetConfig



class GetVar(object):
    
    def __init__(self,infra,cell=None):
        
        
        
        
        helper = GetConfig()
        
        self.username = helper.process_config(infra,'user')
        self.passwd = helper.process_config(infra,'passwd')
        self.name = helper.process_config(infra,'name')
        self.url = helper.process_config(infra,'url')
        self.image_id = helper.process_config('image','image_id')
        self.image_username = helper.process_config('image','user_name')
        self.work_directory = helper.process_config('config','directory')
        self.ssh_key_name = helper.process_config('config','ssh_key_name') 
        self.timeout = helper.process_config('timeout','period')
        self.flavour_name = helper.process_config('flavour','flavour_type')
        self.cp_file = helper.process_config('file_check','local_file')
        self.tmp_dir = helper.process_config('file_check','tmp_dir')
        self.cell = helper.process_config('cell','location')
        self.scheduler={'cell':self.cell}
        self.ssh_key = self.work_directory+self.ssh_key_name
        self.log_file = helper.process_config('log_file','file')
        
        
        @property
        
        @property
        def cell(self):
            if cell!=None:
                self.cell = helper.process_config('cell','location')
            else: 
                self.cell
                
            return self.cell
                
        
        
        

    
        
        