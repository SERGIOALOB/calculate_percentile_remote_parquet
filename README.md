# Parquet File Stored Remotely Percentile Parameter Filter
This program is used to filter rows of data based on a given percentile value. The data is read from a Parquet file located at a given URL and the rows are filtered based on the value of a given field.

## How to Install Dependencies
 To install by pipenv these dependencies, you can use the command:
### Copy code
```
pip install pipenv
```
```
pipenv install
```
## How to Run the Program
 To run the this program, you can use the command:

### Copy code
```
pipenv shell
```
```
python3 main.py https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-07.parquet 0.9 trip_distance
```
The main function will retrieve the data from the given URL, filter the rows based on the 90th percentile value of the given parameter.

## Running the Unit Tests
 To run the unit tests for this program, you can use the pytest command:
### Copy code
```
pytest tests
```
This will run all the test files in the tests directory using pytest.