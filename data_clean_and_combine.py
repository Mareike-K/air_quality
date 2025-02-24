def data_import():
    """Import der Daten"""
    df = pd.read_csv('/Users/whypk/01Projekte/air_quality/data/waqi-covid19-airqualitydata-2025.csv', comment='#')
    return df



def data_cleaning():
    """Bereinigung der Daten
    - nicht benötigte Spalten löschen
    - Eine Stadt pro Land mit den meisten Messwerten
    - Spatle Species aufteilen
    - count-Spalten löschen
    - median-Spalten umbenennen"""
    df = df.drop(columns=['variance', 'min', 'max'])
    
    city_counts = df.groupby(["Country", "City"]).size().reset_index(name="count")
    cities = city_counts.loc[city_counts.groupby("Country")["count"].idxmax()]
    cities.to_csv('/Users/whypk/01Projekte/air_quality/data/city_per_country.csv', index=False)
    cities=cities['City'].tolist()
    df = df[df['City'].isin(cities)]

    df = df.pivot(index=["Date", "Country", "City"], columns="Specie", values=["median", 'count']).reset_index()
    df.columns = ['_'.join(col).strip('_') for col in df.columns]

    df = df.drop(columns=[col for col in df.columns if col.startswith('count_')])

    df.rename(columns={col: col[len('median_'):] for col in df.columns if col.startswith('median')}, inplace=True)

    return df


data_import()
data_cleaning()

