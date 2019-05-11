############################################
# 
# MySQL db backup script 
# using the mysqldump and subprocess 
#
# Made with python 3.7
# Based on the script of Rahul Kumar
# Author : Gurvan S.
# Script version : 0.1
#
###########################################


# Import required python libraries

import os
import subprocess
import time
import datetime
import pipes
 
# MySQL database details to which backup to be done. Make sure below user having enough privileges to take databases backup.
 
DB_HOST = 'localhost' 
DB_USER = 'root'
DB_USER_PASSWORD = ''
DB_NAME = 'dbname'
BACKUP_PATH = 'C:\DBBACKUP'
DUMP_FOLDER = "C:\Program Files/MySQL/MySQL Server 5.7/bin"
 
# Getting current DateTime to create the separate backup folder like "20180817-123433".

DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME
 
# Checking if backup folder already exists or not. If not exists will create it.

try:
    os.stat(TODAYBACKUPPATH)
except:
    os.mkdir(TODAYBACKUPPATH)
 
print ("Starting backup of database " + DB_NAME)

# Execute the mysqldump command to make a save of the db, /!\ The command have to been executed in the mysqldump folder /!\

cmd = "mysqldump -u " + DB_USER + " -p"+DB_USER_PASSWORD + " -h "+ DB_HOST + " " + DB_NAME + " > " + TODAYBACKUPPATH + "/"+ DB_NAME +".sql"
p = subprocess.run(cmd, stdin=None, input=None, stdout=None, stderr=None, shell=True, cwd=DUMP_FOLDER, timeout=None, check=False, encoding=None, errors=None, env=None)

print ("")
print ("Backup script completed")
print ("Your backups have bee created in '" + TODAYBACKUPPATH + "' directory")