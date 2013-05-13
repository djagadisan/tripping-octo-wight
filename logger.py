import logging
import sys



class Logger():
    
    def log_data(self,log_file,info,type):
        
        logging.basicConfig(filename=log_file,format='%(asctime)s - %(levelname)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
            
        if type=="INFO":
            logging.info(info)
            
        elif type=="DEBUG":
            logging.error(info)
        
        elif type=="ERROR":
            logging.error(info)
            
        else:
            logging.warning(info)
        
        
        