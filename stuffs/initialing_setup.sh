#! /bin/bash


DIR=/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1


echo "Temperature, Humidity, Presure" > $DIR/stuffs/weatherLog/Lag_weather.log
echo "Temperature, Humidity, Presure" > $DIR/stuffs/weatherLog/Abj_weather.log
echo "Temperature, Humidity, Presure" > $DIR/stuffs/weatherLog/Port_weather.log


# * * * * * /bin/bash  /Users/nombauser/Desktop/GIT/my_git_repos/ETLWithBashScript/temperature_ETL.sh


echo "Temperature, Humidity, Presure" > $DIR/stuffs/buffered_log/Lag_weather.csv
echo "Temperature, Humidity, Presure" > $DIR/stuffs/buffered_log/Abj_weather.csv
echo "Temperature, Humidity, Presure" > $DIR/stuffs/buffered_log/Port_weather.csv



echo "firstname, lastname, gender, email, phone, address, country" > $DIR/stuffs/customer_log/customers.csv