#script to auto create folders on windows startup
#e.g:
    #Documents
        #year
            #month
                #day

from subprocess import call
import os
import datetime

USER = 'user'

now = datetime.datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

path_year = 'C:\Users\\'+USER+'\Documents\\'+str(year)
path_month = path_year + '\\' + str(month)
path_day = path_month+'\\'+str(day)

if not (os.path.isdir(path_year)):
    call('mkdir ' + path_year, shell=True)
 
if not(os.path.isdir(path_month)):
    call('mkdir ' + path_month, shell=True)

if not (os.path.isdir(path_day)):
    call('mkdir ' + path_day, shell=True)
