import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    """Load the Titanic dataset from a CSV file."""
return pd.titanic_csv(filepath)
