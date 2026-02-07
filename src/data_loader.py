import pandas as pd
from pathlib import Path


class BrentDataLoader:
    """
    OOP class for loading Brent oil price data.
    Handles path resolution, date parsing, and basic validation.
    """

    def __init__(self, data_path: str = "data/BrentOilPrices.csv"):
        self.data_path = Path(data_path)
        if not self.data_path.exists():
            raise FileNotFoundError(f"Data file not found at {self.data_path}")

    def load_raw(self) -> pd.DataFrame:
        """
        Load raw CSV with flexible date parsing.
        Returns: pd.DataFrame with 'Date' as index (not yet parsed).
        """
        df = pd.read_csv(self.data_path)
        print(f"Raw data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
        return df

    def load(self) -> pd.DataFrame:
        """
        Load and parse dates properly.
        Handles mixed formats (dd-mmm-yy and "Month dd, yyyy").
        Returns: pd.DataFrame sorted by Date, indexed by datetime.
        """
        df = self.load_raw()

        # Flexible date parsing
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)

        if df['Date'].isna().any():
            # Fallback for quoted formats like "Jul 15, 2021"
            mask = df['Date'].isna()
            df.loc[mask, 'Date'] = pd.to_datetime(
                df.loc[mask, 'Date'].str.strip('"'), format='%b %d, %Y', errors='coerce')

        if df['Date'].isna().any():
            raise ValueError("Some dates could not be parsed. Check the CSV.")

        df = df.sort_values('Date').reset_index(drop=True)
        df = df.set_index('Date')

        print(
            f"Data loaded successfully: {df.index.min().date()} to {df.index.max().date()}")
        print(f"Total observations: {len(df)}")

        return df
