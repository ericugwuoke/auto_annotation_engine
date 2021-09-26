import os
#get current system date for date metadata
from datetime import date
today = date.today()
date_metadata = today.strftime("%d-%m-%Y")
sql_sensor_ID="INSERT INTO Sensors (Sensor_ID) VALUES ('_sensorid_');"
sql_sensor_value="INSERT INTO Sensor_value (Sensor_value) VALUES (_sensorvalue_);"
sql_longitude="INSERT INTO LONGITUDE  (longitude ) VALUES (_long_);"
sql_latitude="INSERT INTO Latitude  (latitude ) VALUES (_lat_);"
sql_observation_domain="INSERT INTO obSERVATION_DOMAIN   (obserVATION_DOMAIN) VALUES ('_domain_');"
sql_unit="INSERT INTO Unit   (unit ) VALUES ('_unit_');"
sql_accuracy="INSERT INTO accuracy   (accuracy ) VALUES (_accuracy_);"
sql_date="INSERT INTO Date   (Date) VALUES ('_date_');"
sql_platform="INSERT INTO platform    (platform) VALUES ('_platform_');"
sql_metadata="INSERT INTO metadata    (metadata) VALUES ('_metadata_');"
sql_time="INSERT INTO time    (time) VALUES ('_time_');"
database_update_command="java -cp ./h2/bin/h2-1.4.200.jar org.h2.tools.RunScript -url jdbc:h2:~/Documents/my_project/test -script update_script.sql -user sa"
tagX_output=input('enter sensor output from tagx app:  ')

try:
    sensor_output=tagX_output.split(' ')[0]
    sensor_metadata=tagX_output.split(' ')[1].split('_')
    #create sql file
    update_script= open("update_script.sql", "w")
    update_script.write(sql_sensor_ID.replace("_sensorid_",sensor_metadata[0])+"\n")
    update_script.write(sql_sensor_value.replace("_sensorvalue_",sensor_output)+"\n")
    update_script.write(sql_longitude.replace("_long_",sensor_metadata[2])+"\n")
    update_script.write(sql_latitude.replace("_lat_",sensor_metadata[1])+"\n")
    update_script.write(sql_observation_domain.replace("_domain_",sensor_metadata[5])+"\n")
    update_script.write(sql_unit.replace("_unit_",sensor_metadata[6])+"\n")
    update_script.write(sql_accuracy.replace("_accuracy_",sensor_metadata[4])+"\n")
    update_script.write(sql_date.replace("_date_",date_metadata)+"\n")
    update_script.write(sql_platform.replace("_platform_",sensor_metadata[8])+"\n")
    update_script.write(sql_metadata.replace("_metadata_",sensor_metadata[7])+"\n")
    update_script.write(sql_time.replace("_time_",sensor_metadata[3])+"\n")
    update_script.close()

    print('updating the H2 dtabase with the following scrip \n \n')
    
    update_script= open("update_script.sql", "r")
    print(update_script.read())
except:
    print("you probably didn't enter a value, please try again")


#update h2 database
os.system(database_update_command)

