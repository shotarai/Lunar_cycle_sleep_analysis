import os
import pandas as pd

# フォルダパス
folder_path = "./oura_user"  # 対象のディレクトリパス

# ファイル一覧を取得
file_list = [file.lower() for file in os.listdir(folder_path) if "sleep" in file]
file_list.sort()

# 空のデータフレームを作成
df_combined = pd.DataFrame()

# ファイルごとにデータを読み込み統合
for file in file_list:
    file_path = os.path.join(folder_path, file)

    # 必要なファイル形式に合わせて読み込み方法を変更する
    df = pd.read_csv(file_path)
    
    # 欠損値を0で置き換える
    df['deep_sleep_duration'] = df['deep_sleep_duration'].fillna(0)

    # 「day」列ごとに「deep sleep」が最大の行を抽出する
    max_deep_sleep_rows = df.loc[df.groupby('day')['deep_sleep_duration'].idxmax()]

    # 新しいDataFrameとして抽出された行を設定する
    new_df = pd.DataFrame(max_deep_sleep_rows)

    new_df.insert(0, 'user', file.split('_sleep')[0])
    
    # DataFrameの連結（新しいインデックスを割り当てる）
    df_combined = pd.concat([df_combined, new_df], ignore_index=True)

# total_sleep_durationが0の行とtypeがlong_sleepでないデータを消す
df_combined['type'] = df_combined['type'].fillna(0)
df_combined.drop(df_combined[df_combined['type'] != 'long_sleep'].index, inplace=True)
df_combined.drop(df_combined[df_combined['deep_sleep_duration'] == 0].index, inplace=True)

# インデックスを連番にする
df_combined.reset_index(drop=True, inplace=True)

# 統合したデータフレームを保存
df_combined.to_csv('combined_sleep_data.csv', index=False)







