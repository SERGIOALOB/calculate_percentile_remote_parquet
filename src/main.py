import requests
import io
import argparse
import pyarrow as pa
import pyarrow.parquet as pq

from typing import List, Dict


def filter_percentile(rows: List[Dict], percentile: float, parameter: str):

  rows = sorted(rows, key=lambda a: a[parameter])
  percentile_value = rows[int(len(rows) * percentile)][parameter]

  return filter(lambda row: row[parameter] >= percentile_value, rows)

def my_read_parquet(url : str, parameter : str):
    response = requests.get(url)
    my_file = io.BytesIO(response.content)
    parquet_reader = pq.ParquetFile(my_file)
    schema = pa.schema([(parameter, pa.float32())])

    for batch in parquet_reader.iter_batches(columns=[parameter]):
        df = batch.to_pandas()
    
    return df.to_dict('records')


def main(url: str, percentile: float, parameter: str):
    rows = my_read_parquet(url, parameter)
    filtered_rows = list(filter_percentile(rows, percentile, parameter))
    print(filtered_rows)
    return 0

if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The URL of the parquet file to read")
    parser.add_argument("percentile", type=float, help="The percentile value to use for filtering")
    parser.add_argument("parameter", help="The column parameter to use for filtering")
    args = parser.parse_args()
    main(args.url, args.percentile, args.parameter)
