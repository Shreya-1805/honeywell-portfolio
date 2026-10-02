"""Create a Salesforce Case when an anomaly is detected (triggers the Apex escalation).
pip install simple-salesforce ; set SF_USER, SF_PASS, SF_TOKEN env vars."""
import os
from simple_salesforce import Salesforce


def raise_case(asset_name: str, index: int, value: float) -> str:
    sf = Salesforce(username=os.environ["SF_USER"], password=os.environ["SF_PASS"],
                    security_token=os.environ["SF_TOKEN"])
    res = sf.Case.create({
        "Subject": f"Anomaly on {asset_name}",
        "Description": f"Reading #{index} = {value} outside expected range.",
        "Priority": "High",
        "Origin": "IoT Alert",
    })
    return res["id"]
