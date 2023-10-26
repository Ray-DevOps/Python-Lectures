
#                   DESCRIPTION
#                ------------------

# Assuming we're presented with a CSV file with days of the week, temperature and conditions,
# (see weather_data.csv) and we need to print the temperature as a list, we can achieve that
# either by using csv reader or by using pandas as follows


################################### USING CSV READER ###########################################

import csv

temperatures = [ ]
with open("weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[1].isdigit() == True:
            temperatures.append(int(row[1]))
          
print(temperatures)          -------------------- >       [12, 14, 15, 14, 21, 22, 24]


################################### USING PANDAS ###############################################

import pandas                                      

data = pandas.read_csv("weather_data.csv")      # Not only does using pandas reduce the code to only
print(data["temp"])                             # 3 lines, it also produces a better formatted result

# ------------------  (output below)
    ↓
0    12
1    14
2    15
3    14
4    21
5    22
6    24
Name: temp, dtype: int64
