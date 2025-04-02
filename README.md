# Air Quality by Mareike and Wiebke

Dieses Projekt entstand im Rahmen des Kurses 'PortfolioProjekte' bei stackfuel.
Unser Ziel war es, die in den vorangegangenen Monaten erlernten Fähigkeiten zu festigen und zu erweitern.
Wir haben uns ganz bewusst entschieden, mit sehr rohen Daten zu arbeiten und keinen 'fertigen' Datensatz zu nutzen. Wohl wissend, dass dabei der DataScience-Bereich etwas kürzer kommen könnte.

## Inhaltsverzeichnis

- [Projektüberblick](#projektüberblick)
- [Projektstruktur](#projektstruktur)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Daten herunterladen](#daten-herunterladen)
- [Explorative Datenanalyse (EDA)](#EDA)
- [Testen](#testen)
- [Verwendete Technologien und Bibliotheken](#Glossar)
- [Kontakt](#kontakt)

---

## Projektüberblick

Lernziel: erlerntes Wissen festigen, Umgang mit API-Daten, Deskriptive Analyse und Vorhersagen
Analyseziel: 
Einfluss von Wetterdaten auf die Schadstoffbelastung der Luft
in Städten (weltweit)
im Zeitraum 2015 bis 2024.

<i> 
ggf Unterziel:
Prognose an welchen Tagen in 2025 ist eine erhöhter Feinstaubwert zu erwarten?
Welches 'dreckigste' Stadt Deutschlands (nach Ortsgrößenklasse)?
Haben sich die Werte in den letzten Jahren deutlich verändert? Bspw seit 2019?
Hat HomeOffice/ Pandemie einen Einfluss auf die Feinstaubbelastung?
</i>


## Projektstruktur

Die Projektstruktur ist wie folgt organisiert:

```
AIR_QUALITY/
├── .venv/
├── data/
├── Images
├── Präsentationen
├── .gitignore
├── .python-version
├── Clusteranalyse_big.ipynb 
├── data_preparation.py
├── data_HowTo.ipynb
├── EDA.ipynb 
├── Glossar.md
├── main.py
├── pyproject.toml
├── README.md
├── test_data_preparations.py
└── uv.lock
```

- **`.venv/`**: Virtuelle Python-Umgebung für das Projekt.
- **`data/`**: Ordner für die heruntergeladenen Datensätze.
- **`Images/`**: Ordner für Bilder
- **`.gitignore`**: Definiert, welche Dateien von der Versionskontrolle ausgeschlossen werden.
- **`.python-version`**: Spezifiziert die Python-Version (>=3.11).
- **`Clusteranalyse_big.ipynb`**: Notebook für die Clusteranalysen.
- **`data_preparation.py`**: Skript zum Herunterladen, Importieren und Cleanen der Datensätze.
- **`data_HowTo.ipynb`**: Jupyter Notebook mit ANleitung für manuellen Datandownload und Angaben über Datenquellen.
- **`EDA.ipynb`**: Notebook für die Explorative DatenAnalyse.
- **`Glossar.md`**: Enthält das Datenwörterbuch und Quellen.
- **`Main.py`**: Relevant um Projekt außerhalb von VSCode zu starten.
- **`pyproject.toml`**: Projektkonfigurationsdatei mit Abhängigkeiten.
- **`README.md`**: Diese Dokumentation.
- **`test_data_preparation.py`**: Testskript für die data_preparation-Funktionen unter Verwendung von pytest.
- **`uv.lock`**: Lock-Datei für den Paketmanager uv.

## Voraussetzungen

Für dieses Projekt wird Python und der Paketmanager uv benötigt. 
Alle weiteren Abhängigkeiten sind in der `pyproject.toml` Datei bzw. in der `uv.lock` dokumentiert.


## Datenquellen

- [Air Quality Historical Data Platform: Institution & University Registration](https://aqicn.org/data-platform/covid19/)
- https://aqicn.org/api/de/ 
- Offene Datenplattform für Luftqualität: Weltweiter COVID-19-Datensatz
- https://datahub.io/core/population-city#unsd-citypopulation-year-both
- Python Library | Meteostat Developers

## SSL-Zertifikate für Wetterdaten (Mac)
Wenn SSL-Zertifikate nicht verifiziert werden können, müssen u.U. die Zertifikate erneuert werden. Wenn übliche Methoden nicht funktionieren:
Versteckte Dateien anzeigen lassen.
Projektordner > .venv > bin > Suche: "Install Certificates.command" > Doppelklick
(s. StackOverflow: https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org)

## Analysen
## Explorative Datenanalyse (EDA)
1_eda_exploration.ipynb: Überblick über den Datensatz und die Variablen; deskriptive Statistik und Ausreißerentfernung
## Korrelationsanalysen
2_eda_correlations.ipynb: Pearson-Matrix, Pairplots; Visuelle Analyse ausgewählter Variablenpaare
## Feature Engineering
Muss noch gemacht werden, wenn gewollt
## Clusteranalyse
4_clusteranalysis.ipynb: 
## Klassifikationsmodelle
5_classification.ipynb: Vorhersage gute vs schlechte Luft auf Grundlage von PM2.5-Wert; logistische Regression, Random Forest, Gradient Boosting
## Zeitreihenanalyse
6_time_series.ipynb: Entwicklung der Feinstaubwerte in Hamburg und München 2015-2024


## Testen

- **`test_data_preparation.py`**: Enthält Tests für Daten-Download, -Import und -Cleaning unter Verwendung von pytest. Ergebnis: finaler Datensatz für die umgesetzten und zukünftige Analysen.
- **Tests ausführen**: im Terminal */air_quality/ pytest

  ```bash
  uv run -m pytest
  ```


''' im Terminal */air_quality/ pytest'''

  Dies führt die Tests aus und stellt sicher, dass die Pipeline-Komponenten korrekt funktionieren.

## Verwendete Technologien und Bibliotheken

- **Python 3.11**: Programmiersprache.
- **uv**: Paketmanager für Python.
- **Jupyter Notebook**: Interaktive Entwicklungsumgebung.
- **Pandas**: Datenanalyse und -manipulation.
- **NumPy**: Numerische Berechnungen.
- **Matplotlib & Seaborn**: Datenvisualisierung.
- **Scikit-Learn**: Maschinelles Lernen.
- **Statsmodels**: Statistische Modellierung.
- **meteostats**: Klimadaten für Städte
- **geopandas**: Koordinaten zum plotten von Karten.
- **Plotly**: Interaktive Visualisierungen.
- **pytest**: Framework zum Testen von Python-Code.

## Kontakt

Mareike Keller https://github.com/Mareike-K

Wiebke Sir https://github.com/whypkey