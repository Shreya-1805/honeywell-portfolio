"""Rolling z-score anomaly detection for sensor time series."""
import pandas as pd


def detect_anomalies(df: pd.DataFrame, column: str = "temperature",
                     window: int = 20, threshold: float = 3.0) -> pd.DataFrame:
    s = df[column]
    mean = s.rolling(window, min_periods=window // 2).mean()
    std = s.rolling(window, min_periods=window // 2).std().replace(0, pd.NA)
    out = df.copy()
    out["zscore"] = ((s - mean) / std).astype(float)
    out["is_anomaly"] = out["zscore"].abs() > threshold
    return out
