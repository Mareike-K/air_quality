import pytest
import os
import pandas as pd
import json
import sys
import meteostat
sys.path.append('.')
from datetime import datetime
from unittest.mock import patch, mock_open
from data_preparation import download_files, data_import, data_cleaning, geo_data, weather_data, population_data, convert_date  

@patch('requests.get')
@patch('os.makedirs')
@patch('os.path.exists', return_value=False)
@patch('builtins.open', new_callable=mock_open)
def test_download_files(mock_open, mock_makedirs, mock_get):
    files = {
        'test_file.csv': 'https://example.com/test_file.csv'
    }
    output_folder = 'test_folder'

    # Mock the response
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.content = b'test content'

    # Call the function
    download_files(files, output_folder)

    # Assertions
    mock_makedirs.assert_called_once_with(output_folder)
    mock_get.assert_called_once_with('https://example.com/test_file.csv', headers={"Accept-Encoding": "gzip"})
    mock_open.assert_called_once_with(os.path.join(output_folder, 'test_file.csv'), 'wb')
    mock_open().write.assert_called_once_with(b'test content')

def test_download_files_failed_status_code(mock_get):
    files = {
        'test_file.csv': 'https://example.com/test_file.csv'
    }
    output_folder = 'test_folder'

    # Mock failed response
    mock_response = mock_get.return_value
    mock_response.status_code = 404

    with patch('requests.get', return_value=mock_response):
        download_files(files, output_folder)

    mock_get.assert_called_once_with('https://example.com/test_file.csv', headers={"Accept-Encoding": "gzip"})

@patch('requests.get', side_effect=Exception('Download error'))
def test_download_files_exception(mock_get):
    files = {
        'test_file.csv': 'https://example.com/test_file.csv'
    }
    output_folder = 'test_folder'

    download_files(files, output_folder)

    mock_get.assert_called_once_with('https://example.com/test_file.csv', headers={"Accept-Encoding": "gzip"})


@patch('os.listdir')
@patch('pandas.read_csv')
def test_data_import_success(mock_read_csv, mock_listdir):
    mock_listdir.return_value = ['waqi-covid-test.csv']

    test_data = pd.DataFrame({
        'Specie': ['wind gust', 'wind speed', 'pm25'],
        'Value': [1, 2, 3]
    })
    mock_read_csv.return_value = test_data

    result = data_import()

    assert result is not None
    assert 'Specie' in result.columns
    assert 'wind-gust' in result['Specie'].values
    assert 'wind-speed' in result['Specie'].values

@patch('os.listdir')
def test_data_import_no_files(mock_listdir):
    mock_listdir.return_value = []
    result = data_import()
    assert result is None

@patch('os.listdir')
@patch('pandas.read_csv', side_effect=Exception('Read error'))
def test_data_import_read_error(mock_read_csv, mock_listdir):
    mock_listdir.return_value = ['waqi-covid-test.csv']
    result = data_import()
    assert result is None

@patch('os.listdir')
@patch('pandas.read_csv')
def test_data_import_missing_column(mock_read_csv, mock_listdir):
    mock_listdir.return_value = ['waqi-covid-test.csv']

    test_data = pd.DataFrame({
        'Value': [1, 2, 3]
    })
    mock_read_csv.return_value = test_data

    result = data_import()
    assert result is None

@patch('os.listdir')
@patch('pandas.read_csv')
def test_data_import_empty_dataframe(mock_read_csv, mock_listdir):
    mock_listdir.return_value = ['waqi-covid-test.csv']

    test_data = pd.DataFrame({
        'Specie': [],
        'Value': []
    })
    mock_read_csv.return_value = test_data

    result = data_import()
    assert result is None

@patch('builtins.open', new_callable=mock_open, read_data='{"data": [{"Place": {"name": "Berlin", "geo": [52.52, 13.405]}}]}')
def test_geo_data_success(mock_file):
    test_data = pd.DataFrame({
        'City': ['Berlin'],
        'Country': ['Germany'],
        'Date': ['2025-01-01']
    })

    result = geo_data(test_data)

    assert 'Latitude' in result.columns
    assert 'Longitude' in result.columns
    assert result.loc[0, 'Latitude'] == 52.52
    assert result.loc[0, 'Longitude'] == 13.405

@patch('builtins.open', side_effect=FileNotFoundError)
def test_geo_data_file_not_found(mock_file):
    test_data = pd.DataFrame({'City': ['Berlin']})
    result = geo_data(test_data)
    assert 'Latitude' not in result.columns
    assert 'Longitude' not in result.columns

@patch('builtins.open', new_callable=mock_open, read_data='not a valid json')
def test_geo_data_json_decode_error(mock_file):
    test_data = pd.DataFrame({'City': ['Berlin']})
    result = geo_data(test_data)
    assert 'Latitude' not in result.columns
    assert 'Longitude' not in result.columns

@patch('builtins.open', new_callable=mock_open, read_data='{"data": []}')
def test_geo_data_no_geo_data(mock_file):
    test_data = pd.DataFrame({'City': ['Berlin']})
    result = geo_data(test_data)
    assert 'Latitude' in result.columns
    assert 'Longitude' in result.columns
    assert result['Latitude'].isna().all()
    assert result['Longitude'].isna().all()

@patch('builtins.open', new_callable=mock_open, read_data='{"data": [{"Place": {"name": "Berlin"}}]}')
def test_geo_data_missing_geo_fields(mock_file):
    test_data = pd.DataFrame({'City': ['Berlin']})
    result = geo_data(test_data)
    assert 'Latitude' in result.columns
    assert 'Longitude' in result.columns
    assert result['Latitude'].isna().all()
    assert result['Longitude'].isna().all()

@patch('meteostat.Stations')
@patch('meteostat.Daily')
def test_weather_data(mock_daily, mock_stations):
    mock_stations().nearby().fetch.return_value = pd.DataFrame({'index': ['12345']})
    mock_daily().fetch.return_value = pd.DataFrame({
        'time': ['2025-01-01'],
        'tavg': [5.5]
    })

    test_df = pd.DataFrame({
        'City': ['Berlin'],
        'Latitude': [52.52],
        'Longitude': [13.405],
        'Date': ['2025-01-01']
    })

    result = weather_data(test_df)

    assert 'tavg' in result.columns
    assert result.loc[0, 'tavg'] == 5.5

@patch('pandas.read_csv')
def test_population_data(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame({
        'City': ['Berlin'],
        'Value': [3500000],
        'Year': [2025]
    })

    test_df = pd.DataFrame({
        'City': ['Berlin'],
        'Year': [2025]
    })

    result = population_data(test_df)

    assert 'Population' in result.columns
    assert result.loc[0, 'Population'] == 3500000

def test_convert_date():
    test_df = pd.DataFrame({'Date': ['2025-03-05']})

    result = convert_date(test_df)

    assert 'year' in result.columns
    assert 'month' in result.columns
    assert 'day' in result.columns
    assert result.loc[0, 'year'] == 2025
    assert result.loc[0, 'month'] == 3
    assert result.loc[0, 'day'] == 5

@patch('data_preparation.geo_data', side_effect=lambda x: x)
@patch('data_preparation.weather_data', side_effect=lambda x: x)
@patch('data_preparation.convert_date', side_effect=lambda x: x)
@patch('data_preparation.population_data', side_effect=lambda x: x)
@patch('os.makedirs')
@patch('pandas.DataFrame.to_csv')
def test_data_cleaning(mock_to_csv, mock_makedirs, mock_population, mock_convert, mock_weather, mock_geo):
    test_data = pd.DataFrame({
        'Date': ['2025-01-01', '2025-01-01'],
        'Country': ['Germany', 'Germany'],
        'City': ['Berlin', 'Berlin'],
        'Specie': ['pm25', 'pm10'],
        'median': [12.5, 20.1],
        'variance': [1.1, 1.5],
        'min': [10, 18],
        'max': [15, 22]
    })

    result = data_cleaning(test_data)

    assert 'variance' not in result.columns
    assert 'min' not in result.columns
    assert 'max' not in result.columns
    assert 'pm25' in result.columns
    assert 'pm10' in result.columns
    assert result['City'].iloc[0] == 'Berlin'
    assert result['Date'].iloc[0] == '2025-01-01'

    mock_makedirs.assert_called_once()
    mock_to_csv.assert_called_once_with('./data/cleaned_data.csv', index=False)

@patch('data_preparation.geo_data', side_effect=lambda x: x)
@patch('data_preparation.weather_data', side_effect=lambda x: x)
@patch('data_preparation.convert_date', side_effect=lambda x: x)
@patch('data_preparation.population_data', side_effect=lambda x: x)
def test_data_cleaning_empty_df(mock_population, mock_convert, mock_weather, mock_geo):
    test_data = pd.DataFrame(columns=['Date', 'Country', 'City', 'Specie', 'median'])
    result = data_cleaning(test_data)
    assert result.empty

@patch('data_preparation.geo_data', side_effect=lambda x: x)
@patch('data_preparation.weather_data', side_effect=lambda x: x)
@patch('data_preparation.convert_date', side_effect=lambda x: x)
@patch('data_preparation.population_data', side_effect=lambda x: x)
@patch('os.makedirs')
@patch('pandas.DataFrame.to_csv')
def test_data_cleaning_missing_columns(mock_to_csv, mock_makedirs, mock_population, mock_convert, mock_weather, mock_geo):
    test_data = pd.DataFrame({
        'Date': ['2025-01-01'],
        'Country': ['Germany'],
        'City': ['Berlin']
    })
    result = data_cleaning(test_data)
    assert result.empty