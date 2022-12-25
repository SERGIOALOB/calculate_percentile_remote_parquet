
import requests
import mock

from main import main
from fixtures import mock_response

def test_main(mock_response):
    with mock.patch('requests.get', return_value=mock_response):
        assert main('http://example.com/data.parquet', 0.9, 'trip_distance') == 0