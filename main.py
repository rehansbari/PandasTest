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

#converting the dataframe into a dictionary
data_dict = data.to_dict()
print(data_dict)

#converting series into python data
temp_list = data["temp"].to_list()

#calculating average temperature from csv file
average_temp = sum(temp_list) / len(temp_list)
print(f"Average temperature = {average_temp} ")

#Using Pandas to do the calculation instead
print(data["temp"].mean())

#Getting max value of temparture data
#https://pandas.pydata.org/docs/reference/series.html
print(data["temp"].max())

#You can get column data this way too by passing a Key, pandas converts columns into an attribute
print(data.condition)

#Getting Data in a particular row
print(data[data.day == "Monday"])

#Getting data from a row where temp = the maximum, which row had max temp?
print(data[data.temp == data["temp"].max()])

#You can tap into a rows specific attributes the same way you can with a dataframe in pandas
monday = data[data.day == "Monday"]
print(monday.condition)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James"],
    "scores": [76, 120]
}

dict_as_df = pandas.DataFrame(data_dict)
print(dict_as_df)