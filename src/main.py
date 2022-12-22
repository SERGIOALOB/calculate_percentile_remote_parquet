
import pandas as pd
import mock
import requests
import io
import argparse
import json

from typing import List, Dict



def filter_percentile(rows: List[Dict], percentile: float):

  rows = sorted(rows, key=lambda a: a['journey_length'])
  percentile_value = rows[int(len(rows) * percentile)]['journey_length']

  return filter(lambda row: row['journey_length'] >= percentile_value, rows)

def my_read_parquet(url : str):

    response = requests.get(url)
    df = pd.read_parquet(response.content)

    return df.to_dict('records')


def main(url: str, percentile: float):
    rows = my_read_parquet(url)
    filtered_rows = filter_percentile(rows, percentile)
    print(filtered_rows)
    return 0

if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The URL of the parquet file to read")
    parser.add_argument("percentile", type=float, help="The percentile value to use for filtering")
    args = parser.parse_args()
    main(args.url, args.percentile)
