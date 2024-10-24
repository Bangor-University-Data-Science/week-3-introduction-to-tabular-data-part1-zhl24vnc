import pandas as pd

def create_summary_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a summary table with feature names, data types, number of unique values, and missing value status.
    
    Args:
        df (pd.DataFrame): The dataset to summarize.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary_data = []
    for column in df.columns:
        summary_data.append({
            'Feature Name': column,
            'Data Type': df[column].dtype,
            'Unique Values': df[column].nunique(),
            'Missing Values': df[column].isnull().sum() > 0
        })
    
    return pd.DataFrame(summary_data)
