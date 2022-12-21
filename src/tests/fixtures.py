import mock
import pytest

@pytest.fixture
def mock_response():
    mock_response = mock.Mock()

    mock_response.content = [   {"journey_length": 1, "id": 1},
                                {"journey_length": 2, "id": 2},
                                {"journey_length": 3, "id": 3},
                                {"journey_length": 4, "id": 4}
                            ]

    return mock_response