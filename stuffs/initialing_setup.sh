#! /bin/bash


DIR=/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1


echo "Temperature, Humidity, Presure" > $DIR/stuffs/weatherLog/Lag_weather.log
echo "Temperature, Humidity, Presure" > $DIR/stuffs/weatherLog/Abj_weather.log
echo "Temperature, Humidity, Presure" > $DIR/stuffs/weatherLog/Port_weather.log


# * * * * * /bin/bash  /Users/nombauser/Desktop/GIT/my_git_repos/ETLWithBashScript/temperature_ETL.sh


echo "Temperature, Humidity, Presure" > $DIR/stuffs/buffered_log/Lag_weather.csv
echo "Temperature, Humidity, Presure" > $DIR/stuffs/buffered_log/Abj_weather.csv
echo "Temperature, Humidity, Presure" > $DIR/stuffs/buffered_log/Port_weather.csv


DIR=/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1
echo "customer_id, firstname, lastname, gender, email, phone, address, country, date_added" > $DIR/stuffs/customer_log/customers.csv

DIR=/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1
echo "product_id, name, description, price" > $DIR/stuffs/customer_log/products.csv

DIR=/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1
echo "sale_id, customer_id, product_id, quantity, sale_date" > $DIR/stuffs/customer_log/sales.csv


psql
COPY salesperson FROM '/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/stuffs/customer_log/salesperson.csv' DELIMITER ',' CSV HEADER;
COPY products FROM '/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/stuffs/customer_log/products.csv' DELIMITER ',' CSV HEADER;
