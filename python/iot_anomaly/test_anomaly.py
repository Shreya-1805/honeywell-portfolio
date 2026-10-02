import pandas as pd
from anomaly import detect_anomalies


def test_spike_is_flagged():
    vals = [20.0 + (i % 3) * 0.1 for i in range(40)] + [90.0]
    res = detect_anomalies(pd.DataFrame({"temperature": vals}))
    assert res["is_anomaly"].iloc[-1]
    assert not res["is_anomaly"].iloc[:30].any()
