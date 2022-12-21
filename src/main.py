
from typing import List, Dict
import pandas as pd
import numpy as np
import requests
import io

def main(url: str):
    rows = read_parquet(url)
    filtered_rows = filter_percentile(rows)
    return 0

if __name__ == "__main__": 
    main()

def filter_percentile(rows: List[Dict]: percentile: float):

  rows = sorted(rows, key=lambda a: a['journey_length'])
  percentile_value = rows[int(len(rows) * percentile)]['journey_length']

  return filter(lambda row: row['journey_length'] >= percentile_value, rows)

def read_parquet(url : str):

    response = requests.get(url)
    print(type(response))
    df = pd.read_parquet(io.BytesIO(response))

    return df.to_dict('records')

def test_read_parquet(mock_response):

    expected = [{"journey_length": 1, "id": 1}, {"journey_length": 2, "id": 2}, {"journey_length": 3, "id": 3}, {"journey_length": 4, "id": 4}]
    with mock.patch('requests.get', return_value=mock_response):
        data = read_parquet('http://example.com/data.parquet')
        assert data == expected
def test_filter_percentile():

    data = [
        {"journey_length": 1, "id": 1}, 
        {"journey_length": 2, "id": 2}, 
        {"journey_length": 3, "id": 3}, 
        {"journey_length": 4, "id": 4}
    ]

    response = [{"journey_length": 4, "id": 4}]
    filtered_data = filter_percentile(data)
    assert list(filtered_data) == response

def test_main():
    assert main() == 0
