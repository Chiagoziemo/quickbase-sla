# tests/test_quickbase_pipeline.py
import json
import responses
import quickbase_pipeline as qp
from quickbase_pipeline import transform_to_dataframe

BASE_URL = qp.BASE_URL

@responses.activate
def test_query_overdue_records_and_transform(tmp_path):
    # mock query endpoint
    query_url = f"{BASE_URL}/v1/records/query"
    sample_data = {
        "data": [
            {"3": {"value": "1001"}, "6": {"value": "Open"}, "7": {"value": "2025-09-01"}},
            {"3": {"value": "1002"}, "6": {"value": "Open"}, "7": {"value": "2025-08-30"}}
        ]
    }
    responses.add(responses.POST, query_url, json=sample_data, status=200)

    # call query function
    records = qp.query_overdue_records()
    assert len(records) == 2

    df = transform_to_dataframe(records)
    assert list(df.columns) == ["RecordID", "Status", "DueDate"]
    assert df.shape[0] == 2
