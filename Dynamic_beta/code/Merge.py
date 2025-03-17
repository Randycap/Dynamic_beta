import pandas as pd
import numpy as np
from arch import arch_model

# 读取 Excel 文件
sp500_data = pd.read_excel('/Users/randy/Downloads/Dynamic_beta/data/adjust_sp500_data.xlsx', index_col=0)
btc_data = pd.read_excel('/Users/randy/Downloads/Dynamic_beta/data/adjusted_bit_price_date.xlsx', index_col=0)

# 重命名列以便合并
sp500_data.columns = ['SP500']
btc_data.columns = ['BTC']

# 合并数据
data = pd.merge(sp500_data, btc_data, left_index=True, right_index=True, how='inner')

# 数据清洗和预处理
# 计算对数收益率
data['SP500_return'] = np.log(data['SP500'] / data['SP500'].shift(1))
data['BTC_return'] = np.log(data['BTC'] / data['BTC'].shift(1))
data = data.dropna()

data.to_excel('/Users/randy/Downloads/Dynamic_beta/data/merged_data.xlsx')
