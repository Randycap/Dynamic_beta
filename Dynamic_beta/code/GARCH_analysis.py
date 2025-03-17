import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from arch import arch_model
from scipy.stats import zscore

# 读取合并后的数据
data = pd.read_excel('/Users/randy/Downloads/Dynamic_beta/data/merged_data.xlsx', index_col=0)

# 将索引转换为日期类型
data.index = pd.to_datetime(data.index)

# 过滤数据，只保留2016年以后的数据
data = data[data.index >= '2016-01-01']

# 数据清洗和预处理
# 计算对数收益率
data['SP500_return'] = np.log(data['SP500'] / data['SP500'].shift(1))
data['BTC_return'] = np.log(data['BTC'] / data['BTC'].shift(1))
data = data.dropna()

# 去除异常值
data = data[(np.abs(zscore(data['SP500_return'])) < 3) & (np.abs(zscore(data['BTC_return'])) < 3)]

# 数据平滑处理
data['SP500_return'] = data['SP500_return'].rolling(window=5).mean().dropna()
data['BTC_return'] = data['BTC_return'].rolling(window=5).mean().dropna()
data = data.dropna()

# 定义 GARCH 模型函数
def calculate_dynamic_beta(data, p=1, q=1):
    dynamic_betas = []
    for i in range(len(data) - 1):
        # 提取当前时间段的数据
        current_data = data.iloc[:i + 1]
        # 构建 GARCH 模型
        model_sp500 = arch_model(current_data['SP500_return'], vol='GARCH', p=p, q=q)
        model_btc = arch_model(current_data['BTC_return'], vol='GARCH', p=p, q=q)
        # 拟合模型
        res_sp500 = model_sp500.fit(disp='off')
        res_btc = model_btc.fit(disp='off')
        # 获取条件方差
        sigma_sp500 = res_sp500.conditional_volatility
        sigma_btc = res_btc.conditional_volatility
        # 计算协方差
        cov = np.cov(current_data['SP500_return'], current_data['BTC_return'])[0, 1]
        # 计算动态贝塔
        beta = cov / sigma_sp500[-1]**2
        dynamic_betas.append(beta)
    return dynamic_betas

# 分析最后一年的数据
last_year_data = data[data.index >= (data.index.max() - pd.DateOffset(years=1))]

# 计算最后一年的动态贝塔
last_year_dynamic_betas = calculate_dynamic_beta(last_year_data)

# 将动态贝塔添加到最后一年的数据框中
last_year_data = last_year_data.iloc[1:]
last_year_data['Dynamic_Beta'] = last_year_dynamic_betas

# 打印最后一年的结果
print(last_year_data[['SP500', 'BTC', 'SP500_return', 'BTC_return', 'Dynamic_Beta']])

# 可视化最后一年的结果
plt.figure(figsize=(14, 7))

# 绘制最后一年的 SP500 和 BTC 回报
plt.subplot(2, 1, 1)
plt.plot(last_year_data.index, last_year_data['SP500_return'] * 100, label='SP500-Return')
plt.plot(last_year_data.index, last_year_data['BTC_return'] * 100, label='BTC-Return')
plt.title('Last Year SP500 and BTC Returns')
plt.ylabel('Return (%)')
plt.legend()

# 绘制最后一年的动态贝塔
plt.subplot(2, 1, 2)
plt.plot(last_year_data.index, last_year_data['Dynamic_Beta'], label='Dynamic Beta', color='red')
plt.title('Last Year Dynamic Beta')
plt.legend()

plt.tight_layout()
plt.show()

# 计算百分比增长
data['SP500_pct'] = (data['SP500'] / data['SP500'].iloc[0]) * 100
data['BTC_pct'] = (data['BTC'] / data['BTC'].iloc[0]) * 100

 #计算百分比增长
data['SP500_pct'] = (data['SP500'] / data['SP500'].iloc[0]) * 100
data['BTC_pct'] = (data['BTC'] / data['BTC'].iloc[0]) * 100


data.to_excel('/Users/randy/Downloads/Dynamic_beta/data/dynamic_data.xlsx')
# 将索引转换为日期类型
data.index = pd.to_datetime(data.index)

# 过滤数据，只保留2014年以后的数据
data = data[data.index >= '2014-01-01']

# ...existing code...

# 可视化从2014年以来的百分比增长
fig, ax1 = plt.subplots(figsize=(14, 7))

# 使用更美观的预定义颜色
ax1.plot(data.index, data['BTC_pct'], label='BTC', color='tomato')
ax1.set_ylabel('BTC Percentage Growth (%)', color='tomato')
ax1.tick_params(axis='y', labelcolor='tomato')

ax2 = ax1.twinx()
ax2.plot(data.index, data['SP500_pct'], label='SP500', color='dodgerblue')
ax2.set_ylabel('SP500 Percentage Growth (%)', color='dodgerblue')
ax2.tick_params(axis='y', labelcolor='dodgerblue')

fig.suptitle('SP500 and BTC Percentage Growth Since 2014')
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
plt.show()