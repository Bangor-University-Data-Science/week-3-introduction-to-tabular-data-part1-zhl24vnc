     import os
     import pandas as pd
     import pytest
     from titanic_analysis.data_loader import load_titanic_data

     def test_load_titanic_data():
         print("Current working directory:", os.getcwd())
         data_path = os.path.abspath("../../data/titanic.csv")
         print("Data file path:", data_path)
         
         df = load_titanic_data(data_path)
         assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
         assert not df.empty, "The DataFrame should not be empty"
