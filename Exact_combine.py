import os
import csv
from bs4 import  BeautifulSoup
import  pandas as pd

def met_data(month, year):
    file_html = open('C:\\Users\\Vinayak S N\\PycharmProjects\\AirQuality_Project\\Data\\Html_Data\\{}\\{}.html'.format(year, month), 'rb')
    plain_text = file_html.read()

    tempD = []
    finalD = []

    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)

    rows = len(tempD) / 15

    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)

    length = len(finalD)

    finalD.pop(length - 1)
    finalD.pop(0)

    for a in range(len(finalD)):
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)

    return finalD

if __name__ == "__main__":
    if not os.path.exists("Data/Real-Data"):
        os.makedirs("Data/Real-Data")

    for year in range(2013, 2016):
        final_data = []
        with open('Data/Real-Data/{}.csv'.format(year), 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])

        for month in range(1, 13):
            temp = met_data(month, year)
            final_data = final_data + temp

        with open('Data/Real-Data/{}.csv'.format(year), 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                wr.writerow(row)
