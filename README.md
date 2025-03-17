# 标普500与比特币数据分析项目

## 项目概述
本项目旨在分析标普500指数和比特币的历史数据，计算动态贝塔值，并可视化两者的收益率和百分比增长情况。项目包含多个Python脚本，用于数据获取、处理、合并以及GARCH模型分析。

## 项目结构
项目主要由以下几个Python脚本组成：
1. **sp500_data.py**：获取标普500指数的历史数据，并保存为Excel文件。
2. **bit_price.py**：获取比特币的历史价格数据，并进行处理后保存为Excel文件。
3. **Merge.py**：合并标普500指数和比特币的数据，并进行数据清洗和预处理，保存为合并后的Excel文件。
4. **GARCH_analysis.py**：读取合并后的数据，使用GARCH模型计算动态贝塔值，并可视化最后一年的收益率和动态贝塔值，以及2014年以来的百分比增长情况。

## 环境要求
- Python 3.x
- 所需Python库：
  - `pandas`：用于数据处理和分析。
  - `numpy`：用于数值计算。
  - `yfinance`：用于获取金融数据。
  - `arch`：用于构建和拟合GARCH模型。
  - `requests`：用于从CoinGecko获取比特币数据（当前未使用）。
  - `matplotlib`：用于数据可视化。
  - `scipy`：用于计算Z分数以去除异常值。

你可以使用以下命令安装所需的库：
```bash
pip install pandas numpy yfinance arch requests matplotlib scipy
```

## 使用方法
### 1. 数据获取
运行`sp500_data.py`脚本，获取标普500指数的历史数据，并保存为`adjust_sp500_data.xlsx`文件：
```bash
python sp500_data.py
```

运行`bit_price.py`脚本，获取比特币的历史价格数据，并保存为`adjusted_bit_price_date.xlsx`文件：
```bash
python bit_price.py
```

### 2. 数据合并
运行`Merge.py`脚本，合并标普500指数和比特币的数据，并保存为`merged_data.xlsx`文件：
```bash
python Merge.py
```

### 3. 数据分析和可视化
运行`GARCH_analysis.py`脚本，使用GARCH模型计算动态贝塔值，并可视化最后一年的收益率和动态贝塔值，以及2014年以来的百分比增长情况：
```bash
python GARCH_analysis.py
```

## 注意事项
- 请确保你有足够的权限在指定的路径下创建和保存Excel文件。
- 脚本中的日期范围可以根据需要进行调整，修改`sp500_data.py`和`bit_price.py`中的`start_date`和`end_date`变量。
- GARCH模型的参数`p`和`q`可以在`GARCH_analysis.py`中的`calculate_dynamic_beta`函数中进行调整。

