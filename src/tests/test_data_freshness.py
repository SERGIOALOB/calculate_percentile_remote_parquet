from fixtures import mock_response


def test_data_completeness(mock_response):
    assert b'trip_distance' in mock_response.content, "value1 is missing from data"