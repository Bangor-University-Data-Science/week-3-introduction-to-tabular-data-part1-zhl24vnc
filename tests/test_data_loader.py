import os
import pandas as pd
from titanic_analysis.data_loader import load_titanic_data

def test_load_titanic_data():
 
    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, '..', 'data', 'titanic.csv')
    print("Data file path:", os.path.abspath(data_path))
    
    df = load_titanic_data(data_path)
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert not df.empty, "The DataFrame should not be empty"
