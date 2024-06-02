import numpy as np
import scipy.stats as stats
import pandas as pd
from sklearn.preprocessing import StandardScaler

# データの読み込み
df = pd.read_csv('result.csv')

new_df = pd.DataFrame()

# 標準化のためのscalerを作成
scaler = StandardScaler()

# ユーザごとに標準化した値を計算した後、新しいDataFrameに追加
new_df['normalized_index'] = df.groupby('user')['deep_sleep_duration'].transform(lambda x: scaler.fit_transform(x.values.reshape(-1, 1)).flatten())
new_df['day_group'] = df['day_group']

# 各グループのデータを取得
group_a = new_df[new_df['day_group'] == 'A']['normalized_index']
group_b = new_df[new_df['day_group'] == 'B']['normalized_index']
group_c = new_df[new_df['day_group'] == 'C']['normalized_index']

# 各グループの平均値を表示
mean_group_a = group_a.mean()
mean_group_b = group_b.mean()
mean_group_c = group_c.mean()

print("Group A mean:", mean_group_a)
print("Group B mean:", mean_group_b)
print("Group C mean:", mean_group_c)

# ANOVAを実行
t_statistic, p_value = stats.f_oneway(group_a, group_b, group_c)

# 結果の表示
print("t-statistic:", t_statistic)
print("p-value:", p_value)