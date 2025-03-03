import os
import pandas as pd
import json
import requests

def download_files(file_info, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename, url in file_info.items():
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
file_info = {
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
    "airquality-covid19-cities.json": "https://aqicn.org/data-platform/covid19/airquality-covid19-cities.json"
}
output_folder = "data"

download_files(file_info, output_folder)




def data_import():
    """
    Import der Daten aus allen Dateien, die mit 'waqi-covid-' anfangen.
    Ohne die vier ersten Kommentarzeilen,
    Umbenennung von 'wind gust' und 'wind speed' in 'wind-gust' und 'wind-speed',
    Entfernen von Duplikaten
    Rückgabe einer Liste von DataFrames
    Check, ob Dataframes vorhanden sind, wenn nicht, Rückgabe von None
    Duplikate entfernen
    Zusammenführen der DataFrames zu einem großen DataFrame
    """
    data_folder = './data/'
    all_files = [f for f in os.listdir(data_folder) if f.startswith('waqi-covid-') and f.endswith('.csv') or f == 'airquality-covid19-cities.json']
    dataframes = []
    for file in all_files:
        file_path = os.path.join(data_folder, file)
        df = pd.read_csv(file_path, comment='#')
        df["Specie"] = df["Specie"].replace("wind gust", "wind-gust")
        df["Specie"] = df["Specie"].replace("wind speed", "wind-speed")
        df = df.drop_duplicates()
        dataframes.append(df)

    if not dataframes:
        print("Keine Daten gefunden.")
        return None
        
        #else:
        #    df = pd.concat(dataframes, ignore_index=True)
            
    #df = df.drop_duplicates()

    
    return pd.concat(dataframes, ignore_index=True)
    



def data_cleaning(df):
    """Bereinigung der Daten
    - nicht benötigte Spalten löschen
    - Eine Stadt pro Land mit den meisten Messwerten 
    - und die Liste als csv ins Datenverzeichnis speichern
    - Zusammenfassung der Daten nach Datum, Land, Stadt und Spezies, so dass nur ein Messwert je Species (Median) pro Tag/ Stadt verbleibt
    - filtern des df nach den ausgewählten Städten
    - Spalte Species aufteilen
    - df als csv speichern im Datenverzeichnis
    """
    df = df.copy()

    df = df.drop(columns=['variance', 'min', 'max'], errors='ignore')

    city_counts = df.groupby(["Country", "City"]).size().reset_index(name="count")
    cities = city_counts.loc[city_counts.groupby("Country")["count"].idxmax()]
  
    output_path = './data/city_per_country.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cities.to_csv(output_path, index=False)
    print(f"✅ Datei wurde gespeichert: {output_path}")
    
    cities=cities['City'].tolist()
    df = df[df['City'].isin(cities)]

    df = df.groupby(["Date", "Country", "City", "Specie"], as_index=False).agg({"median": "mean"})  

    df = df.pivot(index=["Date", "Country", "City"], columns="Specie", values='median').reset_index()

    output_path = './data/cleaned_data.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Datei wurde gespeichert: {output_path}")

    return df

def add_geodata(df):
    """
    Fügt die Geodaten zu den Städten hinzu
    """
    df = df.copy()

    # JSON-Datei laden
    with open('./data/airquality-covid19-cities.json', 'r', encoding='utf-8') as file:
        geodata = json.load(file)
    
    geodata = geodata["data"] 

    # Erstellen eines DataFrames mit Städten und Geokoordinaten
    df_places = pd.DataFrame([
        {
            "City": entry["Place"]["name"],  # Stadtname
            "Latitude": entry["Place"]["geo"][0],  
            "Longitude": entry["Place"]["geo"][1]
        }
        for entry in geodata if "Place" in entry])  # Nur Einträge mit "Place" verwenden
    

    # Standardisiere den Stadtnamen für eine bessere Übereinstimmung
    df["City"] = df["City"].str.lower().str.strip()
    df_places["City"] = df_places["City"].str.lower().str.strip()

    # Zusammenführen der beiden DataFrames über "City"
    df = df.merge(df_places, on="City", how="left")

    return df

#data_import()
#data_cleaning()

