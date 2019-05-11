# mysqlbackupscript
> Make a backup of a mysql database

Change the param to match w/ your need 
 - `DB_HOST` : The host of your database, if it's a local one use : `localhost or 127.0.0.1`, but if it's not use the ip of the computer : `192.168.x.x for example`
 - `DB-USER` : The username of the account that you use to make the save, it must have at least the next privrileges : `EVENT / LOCK TABLES / SELECT / SHOW DATABASES`
 - `DB_PASSWORD` : ~~Should i really explain that one ?~~ The password of the account 
 - `DB_NAME` : Name of the database 
 - `BACKUP_PATH` : this is where the backup file will be stored
 
 # Requirement 
 
 I've tested it with python 3.7 , i'm not really sure that this would work on a version lower than 3.x
