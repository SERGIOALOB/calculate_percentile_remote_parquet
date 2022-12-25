from main import filter_percentile
import requests

def test_filter_percentile():

    data = [
        {"trip_distance": 1}, 
        {"trip_distance": 2}, 
        {"trip_distance": 3}, 
        {"trip_distance": 4}
    ]
    parameter = 'trip_distance'
    response = [{"trip_distance": 4}]
    filtered_data = filter_percentile(data, 0.9,'trip_distance')
    assert list(filtered_data) == response
