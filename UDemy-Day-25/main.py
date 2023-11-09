# list_of_csv = []
# with open("weather_data.csv") as csv_file:
#     file = csv_file.readlines()
#     print(file)
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     # for row in data:
#     #     print(row)
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
#
# import pandas
# data = pandas.read_csv("weather_data.csv")
# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.temp * (9/5) + 32)
