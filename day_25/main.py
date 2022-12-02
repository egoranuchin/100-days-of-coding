# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#     print(data)
#
import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# data_dictionary = data.to_dict()
# print(data_dictionary)
# temp_list = data["temp"].to_list()
# # avg_temp = sum(temp_list)/len(temp_list)
# # print(avg_temp)
# # or
# print(data["temp"].mean())
# print(data["temp"].max())
#
#
# # Dataframe is a table and Series is a column
#
# #Get data in columns:
# print(data["condition"])
# print(data.condition)
#
# #Get data in row:
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
#
# # Get data in cell:
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# #farenhiet = c *1.8 +32
#
#
# monday_temp_far = int(monday.temp) * 1.8 + 32
# print(monday_temp_far)
#
#
# # Create a data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"]
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)
#
#


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)


data_dict = {
    "Fur color" : ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

# print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
