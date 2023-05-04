import os
import time
import requests
import sys


def CollectData():
    global url
    for year in range(2012, 2022):
        for month in range(1, 13):
            if month < 10:
                url = ('https://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month, year))

            else:
                url = ('https://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month, year))

            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8')

            if not os.path.exists("C:\\Users\\Vinayak S N\\PycharmProjects\\AirQuality_Project\\Data\\Html_Data\\{}".
                                          format(year)):
                os.makedirs("C:\\Users\\Vinayak S N\\PycharmProjects\\AirQuality_Project\\Data\\Html_Data\\{}".format(year))
            with open(
                    "C:\\Users\\Vinayak S N\\PycharmProjects\\AirQuality_Project\\Data\\Html_Data\\{}\\{}.html".format(year, month),
                    "wb") as output:
                output.write(text_utf)

        sys.stdout.flush()


if __name__ == "__main__":
    start_time = time.time()
    CollectData()
    stop_time = time.time()
    print(" Time Taken {}".format(stop_time - start_time))
