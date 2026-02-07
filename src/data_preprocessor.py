# src/data_preprocessor.py

import pandas as pd
import numpy as np
from src.data_loader import BrentDataLoader


class BrentDataPreprocessor:
    """
    OOP class for cleaning and feature engineering.
    Takes a loaded DataFrame (or loads it) and adds useful features.
    """

    def __init__(self, df: pd.DataFrame = None, data_path: str = None):
        if df is None:
            if data_path is None:
                # Updated absolute path for your local environment
                data_path = r"C:\Users\Administrator\Desktop\10Academy\Week 11\week11-brent-oil-analysis\data\BrentOilPrices.csv"
            loader = BrentDataLoader(data_path)
            self.df = loader.load()
        else:
            self.df = df.copy()

    def clean(self) -> pd.DataFrame:
        """Basic cleaning: ensure positive prices, no duplicates."""
        if self.df['Price'].le(0).any():
            raise ValueError("Negative or zero prices detected.")

        if self.df.index.duplicated().any():
            print("Removing duplicate dates...")
            self.df = self.df[~self.df.index.duplicated(keep='first')]

        return self.df

    def add_features(self, focus_period: str = None) -> pd.DataFrame:
        """
        Add key features:
        - log_price
        - log_return
        - rolling_vol (30-day annualized)
        Optional: subset to focus_period (e.g., '2012-01-01')
        """
        df = self.clean()

        df['log_price'] = np.log(df['Price'])
        df['log_return'] = df['log_price'].diff()
        df['rolling_vol_30d'] = (
            df['log_return'].rolling(window=30).std() * np.sqrt(252)
        )

        if focus_period:
            df = df[focus_period:]
            print(f"Subset to {focus_period}: {len(df)} observations")

        self.df = df
        return df

    def get_processed(self, focus_period: str = '2012-01-01') -> pd.DataFrame:
        """Convenience: full pipeline."""
        return self.add_features(focus_period=focus_period)
