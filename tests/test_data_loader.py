import os
import pandas as pd
from titanic_analysis.data_loader import load_titanic_data

def test_load_titanic_data():
    # 获取当前文件的目录
    current_dir = os.path.dirname(__file__)
    # 构建数据文件的绝对路径
    data_path = os.path.join(current_dir, '..', 'data', 'titanic.csv')
    
    # 打印路径以进行调试
    print("Data file path:", os.path.abspath(data_path))
    
    df = load_titanic_data(data_path)
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert not df.empty, "The DataFrame should not be empty"
