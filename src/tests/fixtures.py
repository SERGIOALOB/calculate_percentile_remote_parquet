import mock
import pytest
import io
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

@pytest.fixture
def mock_response():
    mock_response = mock.Mock()

    data = [{"journey_length": 1, "id": 1},{"journey_length": 2, "id": 2},{"journey_length": 3, "id": 3},{"journey_length": 4, "id": 4}]
    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df)

    buf = io.BytesIO()
    pq.write_table(table, buf)
    mock_response.content = buf

    return mock_response