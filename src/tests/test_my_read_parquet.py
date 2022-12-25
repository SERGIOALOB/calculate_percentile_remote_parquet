import mock
from fixtures import mock_response

from main import my_read_parquet


def test_my_read_parquet(mock_response):

    expected = [{"trip_distance": 1}, {"trip_distance": 2}, {"trip_distance": 3}, {"trip_distance": 4}]
    with mock.patch('requests.get', return_value=mock_response):
        data = my_read_parquet('http://example.com/data.parquet', 'trip_distance')
        assert data == expected
