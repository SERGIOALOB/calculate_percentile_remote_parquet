import mock
import pytest
import io
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

@pytest.fixture
def mock_response():
    mock_response = mock.Mock()

    data = [{"trip_distance": 1},{"trip_distance": 2},{"trip_distance": 3},{"trip_distance": 4}]
    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df)

    buf = io.BytesIO()
    pq.write_table(table, buf)
    mock_response.content = buf.getvalue()


    return mock_response
