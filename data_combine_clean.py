import os
import pandas as pd

def data_import():
    """
    Import der Daten aus allen Dateien, die mit 'waqi-covid-' anfangen.
    Ohne die vier ersten Kommetarzeilen,
    Umbenennung von 'wind gust' und 'wind speed' in 'wind-gust' und 'wind-speed',
    Entfernen von Duplikaten
    Rückgabe einer Liste von DataFrames
    Check, ob Dataframes vorhanden sind, wenn nicht, Rückgabe von None
    Duplikate entfernen
    Zusammenführen der DataFrames zu einem großen DataFrame
    """
    data_folder = './data/'
    all_files = [f for f in os.listdir(data_folder) if f.startswith('waqi-covid-') and f.endswith('.csv')]
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
    - filtern des df nach den ausgewählten Städten
    - Spalte Species aufteilen
    - df als csv speichern im Datenverzeichnis
    """
    df = df.drop(columns=['variance', 'min', 'max'], errors='ignore')

    city_counts = df.groupby(["Country", "City"]).size().reset_index(name="count")
    cities = city_counts.loc[city_counts.groupby("Country")["count"].idxmax()]
  
    output_path = './data/city_per_country.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cities.to_csv(output_path, index=False)
    print(f"✅ Datei wurde gespeichert: {output_path}")
    
    cities=cities['City'].tolist()
    df = df[df['City'].isin(cities)]

    df = df.pivot(index=["Date", "Country", "City"], columns="Specie", values='median').reset_index()

    output_path = './data/cleaned_data.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Datei wurde gespeichert: {output_path}")

    return df



#data_import()
#data_cleaning()

