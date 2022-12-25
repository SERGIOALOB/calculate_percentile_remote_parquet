from main import filter_percentile
import requests

def test_filter_percentile():

    data = [
        {"Trip_distance": 1}, 
        {"Trip_distance": 2}, 
        {"Trip_distance": 3}, 
        {"Trip_distance": 4}
    ]
    parameter = 'Trip_distance'
    response = [{"Trip_distance": 4}]
    filtered_data = filter_percentile(data, 0.9,'Trip_distance')
    assert list(filtered_data) == response