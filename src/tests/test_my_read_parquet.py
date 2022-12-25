import mock
from fixtures import mock_response

from main import my_read_parquet


def test_my_read_parquet(mock_response):

    expected = [{"Trip_distance": 1}, {"Trip_distance": 2}, {"Trip_distance": 3}, {"Trip_distance": 4}]
    with mock.patch('requests.get', return_value=mock_response):
        data = my_read_parquet('http://example.com/data.parquet')
        assert data == expected