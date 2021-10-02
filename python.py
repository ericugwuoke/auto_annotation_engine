import os
#get current system date for date metadata
from datetime import date
today = date.today()
date_metadata = today.strftime("%d-%m-%Y")
#sql_ontolgy="INSERT INTO ontology (SENSORS, SENSOR_VALUE, UNIT, DATE, TIME, OBSERVATION_DOMAIN, METADATA, PLATFORM, LATITUDE, LONGITUDE) VALUES ('_sensorid_',_sensorvalue_,'_unit_', '_date_', _time_, '_domain_', '_metadata_', '_platform_', _lat_, _long_);"
database_update_command="java -cp /path/to/h2/h2/bin/h2-1.4.200.jar org.h2.tools.Shell -url jdbc:h2:tcp://localhost/~/test -user sa -sql \"INSERT INTO ontology (SENSORS, SENSOR_VALUE, UNIT, ACCURACY, DATE, TIME, OBSERVATION_DOMAIN, METADATA, PLATFORM, LATITUDE, LONGITUDE) VALUES ('_sensorid_', _sensorvalue_, '_unit_', _accuracy_, '_date_', _time_, '_domain_', '_metadata_', '_platform_', _lat_, _long_);\""
tagX_output=""

while tagX_output !="done":
    tagX_output=input('enter sensor output from tagx app:  ')
    if tagX_output =="done":
        break;
    else:
        try:
            sensor_output=tagX_output.split(' ')[0]
            sensor_metadata=tagX_output.split(' ')[1].split('_')
            #create sql file
            if len(sensor_metadata) == 9:
                #update_script= open("update_script.sql", "w")
                #update_script.write(sql_ontolgy.replace("_sensorid_",sensor_metadata[0]).replace("_sensorvalue_",sensor_output).replace("_long_",sensor_metadata[2]).replace("_lat_",sensor_metadata[1]).replace("_domain_",sensor_metadata[5]).replace("_unit_",sensor_metadata[6]).replace("_accuracy_",sensor_metadata[4]).replace("_date_",date_metadata).replace("_platform_",sensor_metadata[8]).replace("_metadata_",sensor_metadata[7]).replace("_time_",sensor_metadata[3]))
                #update_script.close()
                sqlupdate=database_update_command.replace("_sensorid_",sensor_metadata[0]).replace("_sensorvalue_",sensor_output).replace("_long_",sensor_metadata[2]).replace("_lat_",sensor_metadata[1]).replace("_domain_",sensor_metadata[5]).replace("_unit_",sensor_metadata[6]).replace("_accuracy_",sensor_metadata[4]).replace("_date_",date_metadata).replace("_platform_",sensor_metadata[8]).replace("_metadata_",sensor_metadata[7]).replace("_time_",sensor_metadata[3])

                print('updating the H2 dtabase with the following scrip \n \n')
                
                #update_script= open("update_script.sql", "r")
                #print(update_script.read())
                #update h2 database
                print(sqlupdate)
                os.system(sqlupdate)
            else:
                print ("please try again with correct metatdata format \n")
        except:
            print("you probably didn't enter a valid data, please try again")
