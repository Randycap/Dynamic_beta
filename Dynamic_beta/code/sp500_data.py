import pandas as pd
import numpy as np
import yfinance as yf  # 用于获取标普500指数数据，这里为了方便获取数据使用该库
from arch import arch_model
import requests  # 用于从 CoinGecko 获取比特币数据

# （一）数据选取与处理
# 定义数据时间段
start_date = '2012-01-01'
end_date = '2024-12-31'

# 获取标普500指数数据
sp500 = yf.download('^GSPC', start=start_date, end=end_date)['Close']

# 打印标普500指数数据以检查是否成功获取
print(sp500.head())
print(sp500.tail())

# 重置索引，将日期从索引变为列
sp500 = sp500.reset_index()


# 将 Date 列转换为日期格式，并格式化为短日期格式
sp500['Date'] = pd.to_datetime(sp500['Date']).dt.strftime('%Y-%m-%d')
# 将标普500指数数据保存为 Excel 文件
sp500.to_excel('/Users/randy/Downloads/Dynamic_beta/data/adjust_sp500_data.xlsx', index=False)
# 打印保存成功的信息# 打印保存成功的信息
print("标普500指数数据已成功保存为 adjust_sp500_data.xlsx")





