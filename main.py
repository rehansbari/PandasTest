import csv
import pandas

#Playing around with the built in CSV library to extract data from a csv file
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#Playing with Pandas Library
data = pandas.read_csv("weather_data.csv")
print(data)
