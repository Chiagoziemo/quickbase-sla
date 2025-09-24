import os
import requests
import pandas as pd


BASE_URL = os.getenv("REALM", "https://example.quickbase.com")
TABLE_ID = os.getenv("TABLE_ID", "dummy_table")
USER_TOKEN = os.getenv("QB_USER_TOKEN", "dummy_token")

HEADERS = {
    "Authorization": f"QB-USER-TOKEN {USER_TOKEN}",
    "Content-Type": "application/json",
}


def query_overdue_records():
    """
    Query records from Quickbase where DueDate < today.
    Returns list of records in Quickbase API format.
    """
    import datetime

    query_url = f"{BASE_URL}/v1/records/query"
    payload = {
        "from": TABLE_ID,
        "select": [3, 6, 7],  # RecordID, Status, DueDate
        "where": "{'7'.LT.'" + datetime.date.today().isoformat() + "'}",
    }

    resp = requests.post(query_url, headers=HEADERS, json=payload)
    resp.raise_for_status()
    return resp.json().get("data", [])


def transform_to_dataframe(records):
    """
    Convert Quickbase API records to pandas DataFrame.
    Expected keys: 3 (RecordID), 6 (Status), 7 (DueDate).
    """
    rows = [
        {
            "RecordID": r["3"]["value"],
            "Status": r["6"]["value"],
            "DueDate": r["7"]["value"],
        }
        for r in records
    ]
    return pd.DataFrame(rows)
