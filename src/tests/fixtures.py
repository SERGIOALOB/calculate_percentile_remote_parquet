import mock
import pytest
import io
import pandas as pd

@pytest.fixture
def mock_response():
    mock_response = mock.Mock()


    data = [{"journey_length": 1, "id": 1},{"journey_length": 2, "id": 2},{"journey_length": 3, "id": 3},{"journey_length": 4, "id": 4}]
    df = pd.DataFrame(data)

    mock_file = io.BytesIO()
    mock_response.content = mock_file
    df.to_parquet(mock_file)

    return mock_response