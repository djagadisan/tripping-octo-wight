import os
import sys
import csv

class WriteCSV():
    
    def createCSVFile(self,filename):
        
        if os.path.exists(filename) is False:
            try:
                _log = open(filename, 'w+')
                return _log
            except IOError,e:
                print "File Error" %e
                raise SystemExit
        else:
            return False
        
    def WriteCSVFile(self,filename,data): 
        
        '''
        print filename
        print data[0]
        record_ = open(filename, 'wb')
        writer = csv.writer(record_,delimiter=',',quoting=csv.QUOTE_ALL)
        writer.writerow([data[0],data[1],data[2],data[3],data[4],data[5]])
        '''
        

        
        
