# Parquet File Stored Remotely Percentile Parameter Filter
### This program is used to filter rows of data based on a given percentile value and a parameter contained. The data is read from a Parquet file located at a given URL and the rows are filtered based on the value of the journey_length field. Only rows with a journey_length value greater than or equal to the 90th percentile value are retained.

### How to Run the Program

## Copy code
```
python3 main.py https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-07.parquet 0.9 trip_distance
```
### The main function will retrieve the data from the given URL, filter the rows based on the 90th percentile value of the given parameter.

## Running the Unit Tests
### To run the unit tests for this program, you can use the pytest command:

```
pytest tests
```
### This will run all the test files in the tests directory using pytest.