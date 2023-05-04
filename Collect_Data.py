import pandas as pd

# for year in range(2013, 2016):
#     url = f"https://raw.githubusercontent.com/krishnaik06/AQI-Project/master/Data/AQI/aqi{year}.csv"
#     df = pd.read_csv(url)
#     filepath = fr"{directory}\aqi{year}.csv"
#     df.to_csv(filepath, index=False)


import matplotlib.pyplot as plt


def avg_data_2013_to_2016():
    all_averages = []
    for year in range(2013, 2016):
        filepath = f'C:\\Users\\Vinayak S N\\PycharmProjects\\AirQuality_Project\\Data\\Raw_Data\\aqi{year}.csv'
        temp_i = 0
        averages = []
        for row in pd.read_csv(filepath, chunksize=24):
            add_var = 0
            avg = 0.0
            data = []
            df = pd.DataFrame(data=row)
            for index, row in df.iterrows():
                data.append(row['PM2.5'])
            for i in data:
                if type(i) is float or type(i) is int:
                    add_var = add_var + i
                elif type(i) is str:
                    if i != "NoData" and i != 'PwrFail' and i != '---' and i != "InVld":
                        temp = float(i)
                        add_var = add_var + temp
            avg = add_var / 24
            temp_i = temp_i + 1
            averages.append(avg)
        all_averages.append(averages)
        plt.plot(averages, label=year)

    # Plotting the graph
    plt.xlabel('Days')
    plt.ylabel('PM2.5')
    plt.title('PM2.5 levels from 2013 to 2019')
    plt.legend(loc='upper left')
    plt.show()

    # Printing all the averages with year
    for i in range(len(all_averages)):
        print(f'Average PM2.5 for {2013 + i}: {all_averages[i]}')




if __name__ == '__main__':
    avg_data_2013_to_2016()
