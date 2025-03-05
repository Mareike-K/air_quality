import os
import pandas as pd
import json
import requests
from meteostat import Daily, Stations
from datetime import datetime

def download_files(files, output_folder):
    """lädt die benötigten Dateien herunter und 
    speichert sie im angegebenen Verzeichnis"""
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename, url in files.items():
        output_path = os.path.join(output_folder, filename)

        try:
            response = requests.get(url, headers={"Accept-Encoding": "gzip"})
            if isinstance(response.status_code, int) and response.status_code == 200:
                with open(output_path, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download {filename}: HTTP {response.status_code}")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")
# Nutzung
files = {
    "waqi-covid-2025.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2025",
    "waqi-covid-2015H1.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2015H1",
    "waqi-covid-2016H1.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2016H1",
    "waqi-covid-2017H1.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2017H1",
    "waqi-covid-2018H1.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2018H1",
    "waqi-covid-2019Q1.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2019Q1",
    "waqi-covid-2019Q2.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2019Q2",
    "waqi-covid-2019Q3.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2019Q3",
    "waqi-covid-2019Q4.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2019Q4",
    "waqi-covid-2020Q1.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2020Q1",
    "waqi-covid-2020Q2.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2020Q2",
    "waqi-covid-2020Q3.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2020Q3",
    "waqi-covid-2020Q4.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2020Q4",
    "waqi-covid-2021Q1.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2021Q1",
    "waqi-covid-2021Q2.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2021Q2",
    "waqi-covid-2021Q3.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2021Q3",
    "waqi-covid-2021Q4.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2021Q4",
    "waqi-covid-2022Q1.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2022Q1",
    "waqi-covid-2022Q2.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2022Q2",
    "waqi-covid-2022Q3.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2022Q3",
    "waqi-covid-2022Q4.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2022Q4",
    "waqi-covid-2023Q1.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2023Q1",
    "waqi-covid-2023Q2.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2023Q2",
    "waqi-covid-2023Q3.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2023Q3",
    "waqi-covid-2023Q4.csv": "https://aqicn.org/data-platform/covid19/report/45108-d76dd600/2023Q4",
    "airquality-covid19-cities.json": "https://aqicn.org/data-platform/covid19/airquality-covid19-cities.json",
    "population.csv": "https://datahub.io/core/population-city/r/unsd-citypopulation-year-both.csv"}
output_folder = "data"





def data_import():
    """
    Import der Daten aus allen Dateien, die mit 'waqi-covid-' anfangen.
    Entfernen von Kommentaren, Duplikaten und Umbenennung bestimmter Spaltenwerte.
    Zusammenführung der DataFrames.
    """
    data_folder = './data/'
    all_files = [f for f in os.listdir(data_folder) if f.startswith('waqi-covid-') and f.endswith('.csv') or f == 'airquality-covid19-cities.json']
    dataframes = []

    if not all_files:
        print("Keine Dateien gefunden.")
        return None

    for file in all_files:
        file_path = os.path.join(data_folder, file)
        try:
            df = pd.read_csv(file_path, comment='#')

            if "Specie" not in df.columns:
                print(f"Spalte 'Specie' fehlt in {file}")
                continue

            df["Specie"] = df["Specie"].replace("wind gust", "wind-gust")
            df["Specie"] = df["Specie"].replace("wind speed", "wind-speed")
            df = df.drop_duplicates()

            if df.empty:
                print(f"{file} enthält nach Duplikat-Entfernung keine Daten mehr.")
                continue

            dataframes.append(df)
        except Exception as e:
            print(f"Fehler beim Verarbeiten von {file}: {e}")

    if not dataframes:
        print("Keine gültigen Daten vorhanden.")
        return None

    return pd.concat(dataframes, ignore_index=True)
    



def data_cleaning(df):
    """Bereinigung der Daten
    - nicht benötigte Spalten löschen
    - Zusammenfassung der Daten nach Datum, Land, Stadt und Spezies, so dass nur ein Messwert je Species (Median) pro Tag/ Stadt verbleibt
    - Spalte Species aufteilen
    - df als csv speichern im Datenverzeichnis
    """
    df = df.copy()

    df = df.drop(columns=['variance', 'min', 'max'], errors='ignore')

    df = df.groupby(["Date", "Country", "City", "Specie"], as_index=False).agg({"median": "mean"})  

    df = df.pivot(index=["Date", "Country", "City"], columns="Specie", values='median').reset_index()

    df["City"] = df["City"].str.lower().str.strip()
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
    df.columns = df.columns.str.strip().str.lower()

    df = geo_data(df)

    df = weather_data(df)


    output_path = './data/cleaned_data.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Datei wurde gespeichert: {output_path}")




    return df

def geo_data(df):
    """
    Fügt die Geodaten zu den Städten hinzu
    """
    df = df.copy()

    # JSON-Datei laden mit Fehlerbehandlung
    try:
        with open('./data/airquality-covid19-cities.json', 'r', encoding='utf-8') as file:
            geodata = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Fehler beim Laden der JSON-Datei: {e}")
        return df

    geodata = geodata.get("data", [])

    # Erstellen eines DataFrames mit Städten und Geokoordinaten
    df_places = pd.DataFrame([
        {
            "City": entry.get("Place", {}).get("name"),
            "Latitude": entry.get("Place", {}).get("geo", [None, None])[0],
            "Longitude": entry.get("Place", {}).get("geo", [None, None])[1]
        }
        for entry in geodata if "Place" in entry and "geo" in entry.get("Place", {})
    ])

    # Entferne Zeilen mit fehlenden Stadtnamen
    df_places.dropna(subset=["City"], inplace=True)

    # Standardisiere Stadtnamen
    df_places["City"] = df_places["City"].str.lower().str.strip()
    #df["City"] = df["City"].str.lower().str.strip()
    df_places.columns = df_places.columns.str.strip().str.lower()

    # Zusammenführen der beiden DataFrames über "City"
    df = df.merge(df_places, on="City", how="left")

    # Überprüfung auf fehlende Geodaten
    fehlende_staedte = df[df["Latitude"].isna()]["City"].unique()
    if fehlende_staedte.size > 0:
        print(f"Keine Geodaten gefunden für: {', '.join(fehlende_staedte)}")

    return df

def weather_data(df):
    """
    Ruft Wetterdaten für Städte im DataFrame ab und integriert sie.
    """
    df = df.copy()

    # Städte extrahieren und Duplikate entfernen
    cities = df[['City', 'Latitude', 'Longitude']].drop_duplicates()

    # Zeitspanne festlegen
    start = datetime(2015, 1, 1)
    end = datetime(2024, 12, 31)

    # DataFrame für alle Städte vorbereiten
    all_data = pd.DataFrame()

    # Wetterdaten für jede Stadt abrufen und hinzufügen
    for _, city in cities.iterrows():
        try:
            # Nächste Wetterstation suchen
            stations = Stations().nearby(city['Latitude'], city['Longitude'])
            station = stations.fetch(1)

            if not station.empty:
                station_id = station.index[0]

                # Tägliche Wetterdaten abrufen
                data = Daily(station_id, start, end).fetch()

                # NaN-Daten rausfiltern
                data.dropna(how='all', inplace=True)

                if not data.empty:
                    # Stadtname hinzufügen
                    data["City"] = city["City"]

                    # Daten in den Gesamtdaten-Frame einfügen
                    all_data = pd.concat([all_data, data])

        except Exception as e:
            print(f"⚠️ Fehler beim Abrufen der Daten für {city['City']}: {e}")

    # Index zurücksetzen
    all_data.reset_index(inplace=True)

    # Spalte 'time' umbenennen in 'Date'
    all_data.rename(columns={'time': 'Date'}, inplace=True)

    # Standardisiere den Stadtnamen
    all_data["City"] = all_data["City"].str.lower().str.strip()

    print(f"✅ Wetterdaten gesammelt für {all_data['City'].nunique()} Städte")

    # Konvertiere die 'Date'-Spalte in beiden DataFrames zu String-Format
    # df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
    all_data['Date'] = pd.to_datetime(all_data['Date']).dt.strftime('%Y-%m-%d')
    all_data.columns = all_data.columns.str.strip().str.lower()

    # Berechne den Anteil der NaN-Werte pro Spalte
    missing_percentage = all_data.isna().mean() * 100
    # Lösche Spalten mit mehr als 80% NaN-Werten
    all_data = all_data.loc[:, missing_percentage <= 80]

    # Zusammenführen der beiden DataFrames über "City" und "Date"
    df = pd.merge(df, all_data, on=["City", 'Date'], how="left")

    return df

def population_data(df):
    '''
    Fügt dem jeder Stadt Einwohner hinzu
    '''
    df = df_copy()
    
    df_population = pd.read_csv(
                    './data/population.csv',
                    sep=',', 
                    header=0,
                    engine='python',  # Hilft oft bei Parsing-Problemen
                    on_bad_lines='skip',  # Methode zum Überspringen von fehlerhaften Zeilen
                    encoding='utf-8')  # Falls Sonderzeichen vorhanden sind

    df_population = df_population[['City', 'Value', 'Year']]

    df_population.rename(columns={'Value': 'Population'}, inplace=True)

    df_population.dropna(inplace=True)
    df_population['Population'] = df_population['Population'].astype(int)
    df_population.columns = df_population.columns.str.strip().str.lower()

    output_path = './data/population_data.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_population.to_csv(output_path, index=False)
    print(f"✅ Datei wurde gespeichert: {output_path}")

    # Merge der beiden DataFrames basierend auf der "City"-Spalte
    df = pd.merge(df, df_population, on=['City', 'Year'], how='left')

    return(df)