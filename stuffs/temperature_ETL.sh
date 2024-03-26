#!/bin/bash

# Extract reading with get_temp_API
# Append reading to temperature.log
# python3 fetching_data.py | grep "Lagos" | cut -d "," -f2-4 | tr ")" " "  >> logs/Lag_weather.log
# python3 fetching_data.py | grep "Abuja" | cut -d "," -f2-4 | tr ")" " "  >> logs/Abj_weather.log
# python3 fetching_data.py | grep "Port Harcourt" | cut -d "," -f2-4 | tr ")" " "  >> logs/Port_weather.log


# # Buffer the last hour of readings
# head -n1 < logs/Abj_weather.log > buffered_log/Abj_weather.csv && tail -n10 <  logs/Abj_weather.log >> buffered_log/Abj_weather.csv
# head -n1 < logs/Lag_weather.log > buffered_log/Lag_weather.csv && tail -n10 <  logs/Lag_weather.log >> buffered_log/Lag_weather.csv
# head -n1 < logs/Port_weather.log > buffered_log/Port_weather.csv && tail -n10 <  logs/Port_weather.log >> buffered_log/Port_weather.csv

# sleep 1

# cat <  buffered_log/Abj_weather.csv > logs/Abj_weather.log
# cat <  buffered_log/Lag_weather.csv > logs/Lag_weather.log
# cat <  buffered_log/Port_weather.csv > logs/Port_weather.log





# Call get_stats.py to  aggregate the readings.

# Load the stats using load_stats_api

# Schedule the script to run every minutes.



PWD='/Users/nombauser/Desktop/GIT/my_git_repos/ETLAirflowDbtProject1/stuffs/'


python3 $(PWD)fetching_data.py | grep "Lagos" | cut -d "," -f2-4 | tr ")" " "  >> $(PWD)weatherLog/Lag_weather.log
python3 $(PWD)fetching_data.py | grep "Abuja" | cut -d "," -f2-4 | tr ")" " "  >> $(PWD)weatherLog/Abj_weather.log
python3 $(PWD)fetching_data.py | grep "Port Harcourt" | cut -d "," -f2-4 | tr ")" " "  >> $(PWD)weatherLog/Port_weather.log



head -n2 < $(PWD)weatherLog/Abj_weather.log > $(PWD)buffered_log/Abj_weather.csv && tail -n30 <  $(PWD)weatherLog/Abj_weather.log >> $(PWD)buffered_log/Abj_weather.csv
head -n2 < $(PWD)weatherLog/Lag_weather.log > $(PWD)buffered_log/Lag_weather.csv && tail -n30 <  $(PWD)weatherLog/Lag_weather.log >> $(PWD)buffered_log/Lag_weather.csv
head -n2 < $(PWD)weatherLog/Port_weather.log > $(PWD)buffered_log/Port_weather.csv && tail -n30 <  $(PWD)weatherLog/Port_weather.log >> $(PWD)buffered_log/Port_weather.csv


sleep 1

cat <  $(PWD)buffered_log/Abj_weather.csv > $(PWD)weatherLog/Abj_weather.log
cat <  $(PWD)buffered_log/Lag_weather.csv > $(PWD)weatherLog/Lag_weather.log
cat <  $(PWD)buffered_log/Port_weather.csv > $(PWD)weatherLog/Port_weather.log



