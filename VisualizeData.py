import pandas as pd
import matplotlib.pyplot as plt


def read_weather_data(year=2020, month=11, day=None):
    data = pd.read_csv('../Data/Weather '+str(year)+'/en_climate_hourly_ON_6158359_'+str(month)+'-'+str(year)+'_P1H.csv', usecols=[5, 6, 7, 8, 9, 11, 13, 15, 17, 19, 21])
    if day:
        data = data.truncate((day-1)*24, day*24-1)
    return data


if __name__ == '__main__':
    weather_data = read_weather_data(day=12)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(weather_data)
    weather_data.plot.line(3, 4)
    plt.show()

