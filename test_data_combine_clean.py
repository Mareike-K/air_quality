import os
import pandas as pd
from data_combine_clean import data_import, data_cleaning  
import pytest
from unittest.mock import patch, MagicMock

@patch('os.listdir')
@patch('pandas.read_csv')
def test_data_import(mock_read_csv, mock_listdir):
    # Mock-Dateien erstellen
    mock_listdir.return_value = ['waqi-covid-2020.csv', 'waqi-covid-2021.csv']

    # Mock-DataFrames erstellen
    df1 = pd.DataFrame({'Specie': ['wind gust', 'pm25'], 'Value': [10, 20]})
    df2 = pd.DataFrame({'Specie': ['wind speed', 'pm10'], 'Value': [5, 15]})

    mock_read_csv.side_effect = [df1, df2]

    result_df = data_import()

    # Erwartungen prüfen
    assert result_df is not None
    assert len(result_df) == 4
    assert 'wind-gust' in result_df['Specie'].values
    assert 'wind-speed' in result_df['Specie'].values

@patch('os.listdir')
def test_no_files(mock_listdir):
    mock_listdir.return_value = []
    result_df = data_import()
    assert result_df is None

@patch('pandas.DataFrame.to_csv')
def test_data_cleaning(mock_to_csv):
    test_df = pd.DataFrame({
        'Country': ['DE', 'DE', 'FR', 'FR'],
        'City': ['Berlin', 'Hamburg', 'Paris', 'Lyon'],
        'Specie': ['pm25', 'pm10', 'pm25', 'pm10'],
        'median': [10, 20, 15, 25],
        'variance': [1, 2, 1.5, 2.5],
        'min': [5, 10, 7, 12],
        'max': [15, 30, 22, 35]
    })

    # Übergabe des DataFrames an die Funktion
    cleaned_df = data_cleaning(test_df)

    # Erwartungen prüfen
    assert cleaned_df is not None
    assert 'variance' not in cleaned_df.columns
    assert 'min' not in cleaned_df.columns
    assert 'max' not in cleaned_df.columns
    assert len(cleaned_df) > 0

    # Prüfen, ob die Datei gespeichert wurde
    assert mock_to_csv.call_count == 2

if __name__ == '__main__':
    pytest.main()
