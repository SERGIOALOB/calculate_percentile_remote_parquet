import mock
from fixtures import mock_response

from main import read_parquet


def test_read_parquet(mock_response):

    expected = [{"journey_length": 1, "id": 1}, {"journey_length": 2, "id": 2}, {"journey_length": 3, "id": 3}, {"journey_length": 4, "id": 4}]
    with mock.patch('requests.get', return_value=mock_response):
        data = read_parquet('http://example.com/data.parquet')
        assert data == expected