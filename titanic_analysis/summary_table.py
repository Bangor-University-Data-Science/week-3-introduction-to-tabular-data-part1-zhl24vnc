def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary_data = []
    for column in df.columns:
        summary_data.append({
            'Feature': column,
            'Data Type': df[column].dtype,
            'Unique Values': df[column].nunique(),
            'Has Missing Values': df[column].isnull().sum() > 0
        })
    
    return pd.DataFrame(summary_data)