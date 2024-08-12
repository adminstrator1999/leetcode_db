import pandas as pd


# def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
#     # Sort the DataFrame by 'recordDate' to ensure correct order
#     weather = weather.sort_values(by='recordDate')
#
#     # Shift the temperature and date columns by 1 to compare with the previous day
#     weather['previousTemperature'] = weather['temperature'].shift(1)
#     weather['previousDate'] = weather['recordDate'].shift(1)
#
#     # Filter rows where the current temperature is higher than the previous day
#     result = weather[(weather['temperature'] > weather['previousTemperature']) &
#                      (weather['previousDate'] + pd.Timedelta(days=1) == weather['recordDate'])]
#
#     # Return the 'id' column of the filtered result
#     return result[['id']]

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')
    return weather[
        (weather.temperature.diff() > 0)
        & (weather.recordDate.diff().dt.days == 1)
        ][['id']]


data = [[1, '2015-01-01', 10], [2, '2015-01-03', 25], [3, '2015-01-04', 20], [4, '2015-01-05', 30]]
weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype(
    {'id': 'Int64', 'recordDate': 'datetime64[ns]', 'temperature': 'Int64'})

print(rising_temperature(weather))
