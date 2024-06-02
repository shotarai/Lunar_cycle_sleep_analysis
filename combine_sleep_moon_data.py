import pandas as pd

dataframe1 = pd.read_csv('sleep_data.csv')
dataframe2 = pd.read_csv('moon_group.csv')
dataframe1['day'] = pd.to_datetime(dataframe1['day'], format='%Y/%m/%d')
dataframe2['day'] = pd.to_datetime(dataframe2['day'], format='%Y/%m/%d')

# day列をキーにして結合
dataframe1 = pd.merge(dataframe1, dataframe2, on='day', how='left')

# 結果の表示
dataframe1.to_csv('sleep_and_moon.csv', index=False)