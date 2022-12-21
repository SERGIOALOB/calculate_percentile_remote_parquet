from main import filter_percentile

def test_filter_percentile():

    data = [
        {"journey_length": 1, "id": 1}, 
        {"journey_length": 2, "id": 2}, 
        {"journey_length": 3, "id": 3}, 
        {"journey_length": 4, "id": 4}
    ]

    response = [{"journey_length": 4, "id": 4}]
    filtered_data = filter_percentile(data, 0.75)
    assert list(filtered_data) == response