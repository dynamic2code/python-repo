from itertools import count
from re import X
import matplotlib.pyplot as plt
import numpy as np
import csv


class Graphploter:

    def getdata(self):
        file = "Untitled spreadsheet - IMDb_movies.csv"
        global length, countries

        countries =[]
        length = []
        with open(file, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile)

            all = []
            for row in reader:
                all.append(row[7])
        # print(all)
        countries_b4 = []
        length_b4 = []
        for i in all:
            data =[i,all.count(i)]
            
            countries_b4.append(data[0])
            length_b4.append(data[1])

            print('running...')

        # print(countries_b4)
        # print(length_b4)

        countries = countries_b4[1:9]
        length = length_b4[1:9]
        
        # print(countries)
        # print(length)
            # print (data)

    def showgraph(self,countries, length):
        country_position = np.arange(len(countries))

        plt.barh(country_position, length)
        
        # Create names on the x-axis
        plt.yticks(country_position, countries)
        
        plt.show()

obj = Graphploter()
obj.getdata()
obj.showgraph(countries, length)

