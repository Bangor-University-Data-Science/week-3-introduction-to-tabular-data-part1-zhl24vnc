import pandas as pd

def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],  # Continuous numerical features
            'discrete': []  # Discrete numerical features
        },
        'categorical': {
            'nominal': [],  # Nominal categorical features
            'ordinal': []  # Ordinal categorical features
        }
    }
    
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            unique_values = df[column].nunique()

            # Assuming features with a large number of unique values are continuous
            if unique_values < 10:
                feature_types['numerical']['discrete'].append(column)
            else:
                feature_types['numerical']['continuous'].append(column)
        else:
            # Manually classify ordinal features if known (e.g., Pclass)
            if column == 'Pclass':
                feature_types['categorical']['ordinal'].append(column)
            else:
                feature_types['categorical']['nominal'].append(column)
    
    return feature_types
