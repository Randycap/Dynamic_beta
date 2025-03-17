import yfinance as yf
import pandas as pd

# 定义比特币的 ticker 符号
btc_ticker = "BTC-USD"

# 获取比特币历史价格数据，这里获取 2012 年 1 月 1 日到 2024 年 12 月 31 日的数据
btc_data = yf.download(btc_ticker, start="2012-01-01", end="2024-12-31")

# 提取收盘价和时间
btc_close_data = btc_data[['Close']]

# 重置索引
btc_close_data = btc_close_data.reset_index()

# 删除前两行
btc_close_data = btc_close_data.drop([0, 1]).reset_index(drop=True)

# 在新的 Excel 文件的第一行的第一列填充 Date，第二列填充 BTC-USD
btc_close_data.columns = ['Date', 'BTC-USD']

# 将 Date 列转换为日期格式，并格式化为短日期格式
btc_close_data['Date'] = pd.to_datetime(btc_close_data['Date']).dt.strftime('%Y-%m-%d')

# 保存修改后的 Excel 文件
btc_close_data.to_excel('/Users/randy/Downloads/Dynamic_beta/data/adjusted_bit_price_date.xlsx', index=False)