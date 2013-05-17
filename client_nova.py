import os
import sys
from novaclient.v1_1 import client 


class Connection():
    
    def createConnection(self,obj):
        try:
            conn = client.Client(username=obj.username,api_key=obj.passwd,project_id=obj.name,auth_url=obj.url)
            conn2 = client.Client()
        except Exception,e:
            return "Error %s" % e
        return conn