import os
import pandas as pd
import json
import requests
from datetime import datetime


def data_import():
    """
    Import der Daten aus allen Dateien, die mit 'waqi-covid-' anfangen.
    Entfernen von Kommentaren, Duplikaten und Umbenennung bestimmter Spaltenwerte.
    Zusammenführung der DataFrames.
    """
    data_folder = '../data/'
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

    df = geo_data(df)

    output_path = '../data/cleaned_data.csv'
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
    df["City"] = df["City"].str.lower().str.strip()

    # Zusammenführen der beiden DataFrames über "City"
    df = df.merge(df_places, on="City", how="left")

    # Überprüfung auf fehlende Geodaten
    fehlende_staedte = df[df["Latitude"].isna()]["City"].unique()
    if fehlende_staedte.size > 0:
        print(f"Keine Geodaten gefunden für: {', '.join(fehlende_staedte)}")

    return df