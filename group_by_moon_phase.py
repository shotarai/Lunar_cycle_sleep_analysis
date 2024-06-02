import pandas as pd

# サンプルデータフレームを作成
df = pd.read_csv('moon_info.csv')

# 新しい列 'day_group' を作成し、'C'で埋める
df['day_group'] = 'C'

# 'full' 列が 1 の行のインデックスを取得
full_index = df.index[df['full_moon'] == 1]

# day_group を更新
for index in full_index:
    start_index = max(0, index - 4)
    end_index = min(index + 4, len(df) - 1)
    
    if index - 9 >= 0:
        df.loc[index - 9:start_index, 'day_group'] = 'B'
    if index + 9 < len(df):
        df.loc[end_index:index + 9, 'day_group'] = 'B'
    
    df.loc[start_index:end_index, 'day_group'] = 'A'

df.to_csv('moon_group.csv', index=False)
