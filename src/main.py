
import pandas as pd
import mock
import requests
import io

from typing import List, Dict

def main(url: str, percentile: float):
    rows = read_parquet(url)
    filtered_rows = filter_percentile(rows)
    return 0

if __name__ == "__main__": 
    main()

def filter_percentile(rows: List[Dict], percentile: float):

  rows = sorted(rows, key=lambda a: a['journey_length'])
  percentile_value = rows[int(len(rows) * percentile)]['journey_length']

  return filter(lambda row: row['journey_length'] >= percentile_value, rows)

def read_parquet(url : str):

    response = requests.get(url)
    print(type(response))
    df = pd.read_parquet(response.content)

    return df.to_dict('records')

