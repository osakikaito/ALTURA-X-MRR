import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ファイルパスが正しいことを確認
url = "ALTURA X python.csv"

# CSVファイルを読み込む
df = pd.read_csv(url, delimiter=',')

# データを新しいCSVファイルに保存
df.to_csv('formatted_data.csv', index=False)

# 'slack'列の平均値を計算
negotiations_mean = df['slack'].mean()
negotiations_mean_truncated = int(negotiations_mean)

# 全体の平均値を表示
print()
print(f"平均商談工数（全体）： {negotiations_mean_truncated}回")
print()

# 都市ごとに'slack'列の平均値を計算
city_negotiations_mean = df.groupby('city')['slack'].mean().astype(int)

# 各都市の平均値を表示
print("各都市の平均商談工数（回）：")
print(city_negotiations_mean)

# 'Negotiation lead time' 列の平均値を計算し、小数点以下を切り捨て
negotiation_lead_time_mean = df['Negotiation lead time'].mean()
negotiation_lead_time_mean_truncated = int(negotiation_lead_time_mean)

# 平均値(商談リードタイム)を表示
print()
print(f"平均商談リードタイム（全体）： {negotiation_lead_time_mean_truncated}回")
print()

# 'Negotiation lead time' 列の平均値を city ごとに計算し、小数点以下を切り捨て
city_negotiation_lead_time = df.groupby('city')['Negotiation lead time'].mean().fillna(0).astype(int)

# 各都市の平均値（商談リードタイム）を表示
print("各都市の平均商談リードタイム（回）：")
print(city_negotiation_lead_time)


# 'Contract lead time' 列の平均値を計算し、小数点以下を切り捨て
contract_lead_time_mean = df['Contract lead time'].mean()
contract_lead_time_mean_truncated = int(contract_lead_time_mean)

# 平均値(契約リードタイム)を表示
print()
print(f"平均契約リードタイム（全体）： {contract_lead_time_mean_truncated}回")
print()

# 'Contract lead time' 列の平均値を city ごとに計算し、小数点以下を切り捨て
city_contract_lead_time = df.groupby('city')['Contract lead time'].mean().fillna(0).astype(int)

# 各都市の平均値（商談リードタイム）を表示
print("各都市の平均契約リードタイム（回）：")
print(city_contract_lead_time)

# 'high Initial cost' 列の値を数値に変換（カンマを削除してから）
df['high Initial cost'] = df['high Initial cost'].str.replace(',', '').astype(float)

# 'high Initial cost' 列の平均値を計算し、小数点以下を切り捨て
high_mean = df['high Initial cost'].mean()
high_mean_truncated = int(high_mean)

#初期費用の平均値を３桁ごとにカンマ区切りで表示
high_mean_formatted = f"{high_mean_truncated:,}"

# 平均値(初期費用（高め）)を表示
print()
print(f"平均初期費用（高め）： {high_mean_formatted}円")
print()

#'high Initial cost'列の平均値をcityごとに計算し、小数点以下切り捨て
high_initial_cost = df.groupby('city')['high Initial cost'].mean().fillna(0).astype(int)

# 各都市の平均値(高めの初期費用）を3桁ごとにカンマ区切りで表示
high_initial_cost_formatted = high_initial_cost.apply(lambda x: f"{x:,}")

# 各都市の平均値(高めの初期費用）を表示
print("各都市の平均初期費用（高め）（円）：")
print(high_initial_cost_formatted)

# 'low Initial cost' 列の値を数値に変換（カンマを削除してから）
df['low Initial cost'] = df['low Initial cost'].str.replace(',', '').astype(float)

# 'low Initial cost' 列の平均値を計算し、小数点以下を切り捨て
low_mean = df['low Initial cost'].mean()
low_mean_truncated = int(low_mean)

#初期費用の平均値を３桁ごとにカンマで区切りで表示する
low_mean_formatted =f"{low_mean_truncated:,}"

# 平均値(初期費用（低め）)を表示
print()
print(f"初期費用（割引あり）： {low_mean_formatted}円")
print()

#'low initial cost'列の平均値をcityごとに計算し、小数点以下切り捨て
low_city_mean =df.groupby('city')['low Initial cost'].mean().fillna(0).astype(int)

#cityごとの平均初期費用の３桁ごとにカンマ区切りで表示
low_city_mean_formatted =low_city_mean.apply(lambda x: f"{x:,}")

#各都市の平均初期費用（割引あり）を表示
print("平均の初期費用（割引あり）(円)")
print(low_city_mean_formatted)

# 'high data storage' 列の値を数値に変換（カンマを削除してから）
df['high data storage'] = df['high data storage'].str.replace(',', '').astype(float)

# 'low Initial cost' 列の平均値を計算し、小数点以下を切り捨て
high_storage_mean = df['high data storage'].mean()
high_data_mean_truncated = int(high_storage_mean)

#データストレージの平均値を３桁ごとにカンマで区切りで表示する
high_data_mean_formatted =f"{high_data_mean_truncated:,}"

# 平均値(データストレージ)を表示
print()
print(f"データストレージの平均： {high_data_mean_formatted}円")
print()

#'high data storage'列の平均値をcityごとに計算し、小数点以下切り捨て
high_data_city_mean =df.groupby('city')['high data storage'].mean().fillna(0).astype(int)

#cityごとの平均データストレージの３桁ごとにカンマ区切りで表示
high_data_city_mean_formatted =high_data_city_mean.apply(lambda x: f"{x:,}")

#各都市の平均データストレージを表示
print("平均のデータストレージ(円)")
print(high_data_city_mean_formatted)

# 'low data storage' 列の値を数値に変換（カンマを削除してから）
df['low data storage'] = df['low data storage'].str.replace(',', '').astype(float)

# 'low datastoragecost' 列の平均値を計算し、小数点以下を切り捨て
low_storage_mean = df['low data storage'].mean()
low_data_mean_truncated = int(low_storage_mean)

#データストレージの平均値を３桁ごとにカンマで区切りで表示する
low_data_mean_formatted =f"{low_data_mean_truncated:,}"

# 平均値(データストレージ)を表示
print()
print(f"データストレージの平均（割引あり）： {low_data_mean_formatted}円")
print()

#'low data storage'列の平均値をcityごとに計算し、小数点以下切り捨て
low_data_city_mean =df.groupby('city')['low data storage'].mean().fillna(0).astype(int)

#cityごとの平均データストレージの３桁ごとにカンマ区切りで表示
low_data_city_mean_formatted =low_data_city_mean.apply(lambda x: f"{x:,}")

#各都市の平均データストレージを表示
print("平均のデータストレージ(円)（割引あり）")
print(low_data_city_mean_formatted)



# 'high Medical interview sales potential' 列の値を数値に変換（カンマを削除してから）
df['high medical'] = df['high Medical interview sales potential'].str.replace(',', '').astype(float)

# 'high medical' 列の平均値を計算し、小数点以下を切り捨て
high_medical_mean = df['high medical'].mean()
high_medical_mean_truncated = int(high_medical_mean)

# 問診売上ポテンシャルの平均値を３桁ごとにカンマで区切りで表示する
high_medical_mean_formatted = f"{high_medical_mean_truncated:,}"

# 平均値(問診売上ポテンシャル)を表示
print()
print(f"問診売上ポテンシャルの平均： {high_medical_mean_formatted}円")
print()

# 'high medical' 列の平均値をcityごとに計算し、小数点以下切り捨て
high_medical_mean_by_city = df.groupby('city')['high medical'].mean().fillna(0).astype(int)

# cityごとの平均データストレージを３桁ごとにカンマ区切りで表示
high_medical_mean_by_city_formatted = high_medical_mean_by_city.apply(lambda x: f"{x:,}")

# 各都市の平均問診売上ポテンシャルを表示
print("平均の問診売上ポテンシャル(円)")
print(high_medical_mean_by_city_formatted)


# 'low Medical interview sales potential' 列の値を数値に変換（カンマを削除してから）
df['low medical'] = df['low Medical interview sales potential'].str.replace(',', '').astype(float)

# 'low medical' 列の平均値を計算し、小数点以下を切り捨て
low_medical_mean = df['low medical'].mean()
low_medical_mean_truncated = int(low_medical_mean)

# 問診売上ポテンシャルの平均値を３桁ごとにカンマで区切りで表示する
low_medical_mean_formatted = f"{low_medical_mean_truncated:,}"

# 平均値(問診売上ポテンシャル)を表示
print()
print(f"問診売上ポテンシャルの平均（割引あり）： {low_medical_mean_formatted}円")
print()

# 'low medical' 列の平均値をcityごとに計算し、小数点以下切り捨て
low_medical_mean_by_city = df.groupby('city')['low medical'].mean().fillna(0).astype(int)

# cityごとの平均データストレージを３桁ごとにカンマ区切りで表示
low_medical_mean_by_city_formatted = low_medical_mean_by_city.apply(lambda x: f"{x:,}")

# 各都市の平均問診売上ポテンシャル（割引あり）を表示
print("平均の問診売上ポテンシャル(円)（割引あり）")
print(low_medical_mean_by_city_formatted)


# 'high Booking Sales Potential' 列の値を数値に変換（カンマを削除してから）
df['high book'] = df['high Booking Sales Potential'].str.replace(',', '').astype(float)

# 'low medical' 列の平均値を計算し、小数点以下を切り捨て
high_book_mean = df['high book'].mean()
high_book_mean_truncated = int(high_book_mean)

# 予約売上ポテンシャルの平均値を３桁ごとにカンマで区切りで表示する
high_book_mean_formatted = f"{high_book_mean_truncated:,}"

# 平均値(予約売上ポテンシャル)を表示
print()
print(f"予約売上ポテンシャルの平均： {high_book_mean_formatted}円")
print()

# 'high Booking Sales Potential' 列の平均値をcityごとに計算し、小数点以下切り捨て
high_book_mean_by_city = df.groupby('city')['high book'].mean().fillna(0).astype(int)

# cityごとの平均予約売上ポテンシャルを３桁ごとにカンマ区切りで表示
high_book_mean_by_city_formatted = high_book_mean_by_city.apply(lambda x: f"{x:,}")

# 各都市の平均予約売上ポテンシャルを表示
print("平均の予約売上ポテンシャル(円)")
print(high_book_mean_by_city_formatted)


# 'low Booking Sales Potential' 列の値を数値に変換（カンマを削除してから）
df['low book'] = df['low Booking Sales Potential'].str.replace(',', '').astype(float)

# 'low medical' 列の平均値を計算し、小数点以下を切り捨て
low_book_mean = df['low book'].mean()
low_book_mean_truncated = int(low_book_mean)

# 予約売上ポテンシャルの平均値を３桁ごとにカンマで区切りで表示する
low_book_mean_formatted = f"{low_book_mean_truncated:,}"

# 平均値(予約売上ポテンシャル)を表示
print()
print(f"予約売上ポテンシャルの平均（割引あり）： {low_book_mean_formatted}円")
print()

# 'low Booking Sales Potential' 列の平均値をcityごとに計算し、小数点以下切り捨て
low_book_mean_by_city = df.groupby('city')['low book'].mean().fillna(0).astype(int)

# cityごとの平均予約売上ポテンシャルを３桁ごとにカンマ区切りで表示
low_book_mean_by_city_formatted = low_book_mean_by_city.apply(lambda x: f"{x:,}")

# 各都市の平均予約売上ポテンシャル（割引あり）を表示
print("平均の予約売上ポテンシャル(円)（割引あり）")
print(low_book_mean_by_city_formatted)


# 'high MRR' 列の値を数値に変換（カンマを削除してから）
df['high MRR'] = df['high MRR'].str.replace(',', '').astype(float)

# 'high MRR' 列の平均値を計算し、小数点以下を切り捨て
high_MRR_mean = df['high MRR'].mean()
high_MRR_mean_truncated = int(high_MRR_mean)

# MRRの平均値を３桁ごとにカンマで区切りで表示する
high_MRR_mean_formatted = f"{high_MRR_mean_truncated:,}"

# 平均値(MRR)を表示
print()
print(f"MRRの平均： {high_MRR_mean_formatted}円")
print()

# 'high MRR' 列の平均値をcityごとに計算し、小数点以下切り捨て
high_MRR_mean_by_city = df.groupby('city')['high MRR'].mean().fillna(0).astype(int)

# cityごとの平均MRRを３桁ごとにカンマ区切りで表示
high_MRR_mean_by_city_formatted = high_MRR_mean_by_city.apply(lambda x: f"{x:,}")

# 各都市の平均MRRを表示
print("平均のMRR(円)")
print(high_MRR_mean_by_city_formatted)



# 'low MRR' 列の値を数値に変換（カンマを削除してから）
df['low MRR'] = df['low MRR'].str.replace(',', '').astype(float)

# 'low MRR' 列の平均値を計算し、小数点以下を切り捨て
low_MRR_mean = df['low MRR'].mean()
low_MRR_mean_truncated = int(low_MRR_mean)

# MRRの平均値を３桁ごとにカンマで区切りで表示する
low_MRR_mean_formatted = f"{low_MRR_mean_truncated:,}"

# 平均値(MRR,割引あり)を表示
print()
print(f"MRRの平均（割引あり）： {low_MRR_mean_formatted}円")
print()

# 'low MRR' 列の平均値をcityごとに計算し、小数点以下切り捨て
low_MRR_mean_by_city = df.groupby('city')['low MRR'].mean().fillna(0).astype(int)

# cityごとの平均MRRを３桁ごとにカンマ区切りで表示
low_MRR_mean_by_city_formatted = low_MRR_mean_by_city.apply(lambda x: f"{x:,}")

# 各都市の平均MRRを表示
print("平均のMRR（割引あり）(円)")
print(low_MRR_mean_by_city_formatted)


# エクセルファイルにデータを書き込む
with pd.ExcelWriter('output.xlsx') as writer:
    city_negotiations_mean.to_excel(writer, sheet_name='平均商談工数')
    city_negotiation_lead_time.to_excel(writer, sheet_name='平均商談リードタイム')
    city_contract_lead_time.to_excel(writer, sheet_name='平均契約リードタイム')
    high_initial_cost.to_excel(writer, sheet_name='平均初期費用')
    low_city_mean.to_excel(writer, sheet_name='平均初期費用（割引あり）')
    high_data_city_mean.to_excel(writer, sheet_name='平均データストレージ')
    low_data_city_mean.to_excel(writer, sheet_name='平均データストレージ（割引あり）')
    high_medical_mean_by_city.to_excel(writer, sheet_name='平均問診売上ポテンシャル')
    low_medical_mean_by_city.to_excel(writer, sheet_name='平均問診売上ポテンシャル（割引あり）')
    high_book_mean_by_city.to_excel(writer, sheet_name='平均予約売上ポテンシャル')
    low_book_mean_by_city.to_excel(writer, sheet_name='平均予約売上ポテンシャル（割引あり）')
    high_MRR_mean_by_city.to_excel(writer, sheet_name='MRR')
    low_MRR_mean_by_city.to_excel(writer, sheet_name='MRR（割引あり）')



print("データがエクセルファイルに保存されました。")


# グラフ1を作成
fig1, axes1 = plt.subplots(nrows=3, ncols=3, figsize=(24, 16))

# 平均商談工数の棒グラフを作成
city_negotiations_mean.plot(kind='bar', ax=axes1[0, 0])
axes1[0, 0].set_title('Average Number of Negotiations per City')
axes1[0, 0].set_xlabel('City')
axes1[0, 0].set_ylabel('Average Number of Negotiations')
axes1[0, 0].tick_params(axis='x', rotation=45)

# 平均商談リードタイムの棒グラフを作成
city_negotiation_lead_time.plot(kind='bar', ax=axes1[0, 1])
axes1[0, 1].set_title('Average Negotiation Lead Time per City')
axes1[0, 1].set_xlabel('City')
axes1[0, 1].set_ylabel('Average Negotiation Lead Time')
axes1[0, 1].tick_params(axis='x', rotation=45)

# 平均契約リードタイムの棒グラフを作成
city_contract_lead_time.plot(kind='bar', ax=axes1[0, 2])
axes1[0, 2].set_title('Average Contract Lead Time per City')
axes1[0, 2].set_xlabel('City')
axes1[0, 2].set_ylabel('Average Contract Lead Time')
axes1[0, 2].tick_params(axis='x', rotation=45)

# 初期費用（高め）の棒グラフを作成
high_initial_cost.plot(kind='bar', ax=axes1[1, 0])
axes1[1, 0].set_title('Average High Initial Cost per City')
axes1[1, 0].set_xlabel('City')
axes1[1, 0].set_ylabel('Average High Initial Cost')
axes1[1, 0].tick_params(axis='x', rotation=45)

# 初期費用（割引あり）の棒グラフを作成
low_city_mean.plot(kind='bar', ax=axes1[1, 1])
axes1[1, 1].set_title('Average Low Initial Cost per City')
axes1[1, 1].set_xlabel('City')
axes1[1, 1].set_ylabel('Average Low Initial Cost')
axes1[1, 1].tick_params(axis='x', rotation=45)

# データストレージの棒グラフを作成
high_data_city_mean.plot(kind='bar', ax=axes1[1, 2])
axes1[1, 2].set_title('Average Data Storage Cost per City')
axes1[1, 2].set_xlabel('City')
axes1[1, 2].set_ylabel('Average Data Storage Cost')
axes1[1, 2].tick_params(axis='x', rotation=45)

# データストレージ（割引あり）の棒グラフを追加
low_data_city_mean.plot(kind='bar', ax=axes1[2, 0])
axes1[2, 0].set_title('Average low Data Storage Cost per City')
axes1[2, 0].set_xlabel('City')
axes1[2, 0].set_ylabel('Average low Data Storage Cost')
axes1[2, 0].tick_params(axis='x', rotation=45)

plt.tight_layout(pad=7.0)
plt.show()

# グラフ2を作成
fig2, axes2 = plt.subplots(nrows=2, ncols=3, figsize=(24, 16))

# 問診売上ポテンシャルの棒グラフを追加
high_medical_mean_by_city.plot(kind='bar', ax=axes2[0, 0])
axes2[0, 0].set_title('Average high Medical interview sales potential ')
axes2[0, 0].set_xlabel('City')
axes2[0, 0].set_ylabel('Average high Medical sales potential')
axes2[0, 0].tick_params(axis='x', rotation=45)

# 問診売上ポテンシャル（割引あり）の棒グラフを追加
low_medical_mean_by_city.plot(kind='bar', ax=axes2[0, 1])
axes2[0, 1].set_title('Average low Medical interview sales potential ')
axes2[0, 1].set_xlabel('City')
axes2[0, 1].set_ylabel('Average high Medical sales potential')
axes2[0, 1].tick_params(axis='x', rotation=45)

# 予約売上ポテンシャルの棒グラフを追加
high_book_mean_by_city.plot(kind='bar', ax=axes2[0, 2])
axes2[0, 2].set_title('Average high Booking Sales Potential')
axes2[0, 2].set_xlabel('City')
axes2[0, 2].set_ylabel('Average high Booking Sales Potential')
axes2[0, 2].tick_params(axis='x', rotation=45)

# 予約売上ポテンシャル（割引あり）の棒グラフを追加
low_book_mean_by_city.plot(kind='bar', ax=axes2[1, 0])
axes2[1, 0].set_title('Average low Booking Sales Potential')
axes2[1, 0].set_xlabel('City')
axes2[1, 0].set_ylabel('Average low Booking Sales Potential')
axes2[1, 0].tick_params(axis='x', rotation=45)

# MRRの棒グラフを追加
high_MRR_mean_by_city.plot(kind='bar', ax=axes2[1, 1])
axes2[1, 1].set_title('Average high MRR')
axes2[1, 1].set_xlabel('City')
axes2[1, 1].set_ylabel('Average high MRR')
axes2[1, 1].tick_params(axis='x', rotation=45)

# MRR(割引あり）の棒グラフを追加
low_MRR_mean_by_city.plot(kind='bar', ax=axes2[1, 2])
axes2[1, 2].set_title('Average low MRR')
axes2[1, 2].set_xlabel('City')
axes2[1, 2].set_ylabel('Average low MRR')
axes2[1, 2].tick_params(axis='x', rotation=45)

plt.tight_layout(pad=10.0)
plt.show()

# グラフを保存
fig1.savefig('average_negotiations_and_lead_time_per_city_part_1.png')
fig2.savefig('average_negotiations_and_lead_time_per_city_part_2.png')

# グラフを表示
plt.show()

