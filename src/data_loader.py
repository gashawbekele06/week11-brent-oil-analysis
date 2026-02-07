# src/data_loader.py

import pandas as pd
from pathlib import Path


class BrentDataLoader:
    """
    OOP class for loading Brent oil price data.
    Handles path resolution, date parsing, and basic validation.
    """

    def __init__(self, data_path: str = r"C:\Users\Administrator\Desktop\10Academy\Week 11\week11-brent-oil-analysis\data\BrentOilPrices.csv"):
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
        Handles mixed formats robustly:
        - Older: '20-May-87' → %d-%b-%y
        - Newer: '"Jul 15, 2021"' → %b %d, %Y (after stripping quotes)
        """
        df = self.load_raw()

        # Keep cleaned original date strings for multiple parsing attempts
        cleaned_dates = df['Date'].astype(str).str.strip('"').str.strip()

        # First attempt: Older format (dd-mmm-yy)
        df['Date'] = pd.to_datetime(
            cleaned_dates, format='%d-%b-%y', errors='coerce')

        # Mask for failed parses (mostly newer dates)
        mask = df['Date'].isna()

        if mask.any():
            # Second attempt on failed ones: Newer format (Month dd, yyyy)
            df.loc[mask, 'Date'] = pd.to_datetime(
                cleaned_dates[mask],
                format='%b %d, %Y',
                errors='coerce'
            )

        # Final diagnostic + check
        remaining_mask = df['Date'].isna()
        if remaining_mask.any():
            # Will show original bad values
            bad_dates = df.loc[remaining_mask, 'Date'].unique()
            print("WARNING: These date strings could not be parsed:")
            print(df[remaining_mask]['Date'].unique())
            raise ValueError(
                f"Some dates could not be parsed. Examples: {bad_dates[:10]}")

        # Sort, index, and finalize
        df = df.sort_values('Date').reset_index(drop=True)
        df = df.set_index('Date')

        print(
            f"Data loaded successfully: {df.index.min().date()} to {df.index.max().date()}")
        print(f"Total observations: {len(df)}")

        return df
