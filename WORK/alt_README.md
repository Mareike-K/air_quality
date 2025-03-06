# Air Quality by Mareike and Wiebke

vorbemerkungstext

## Inhaltsverzeichnis

- [Projektüberblick](#projektüberblick)
- [Projektstruktur](#projektstruktur)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Daten herunterladen](#daten-herunterladen)
- [Explorative Datenanalyse (EDA)](#explorative-datenanalyse-eda)
- [Modellierung und Pipeline](#modellierung-und-pipeline)
- [Hyperparameter-Optimierung](#hyperparameter-optimierung)
- [Testen](#testen)
- [Verwendete Technologien und Bibliotheken](#verwendete-technologien-und-bibliotheken)
- [Anleitung für Teilnehmende](#anleitung-für-teilnehmende)
- [Kontakt](#kontakt)

---

## Projektüberblick

Lernziel: erlerntes Wissen festigen, Umgang mit API-Daten, Deskriptive Analyse und Vorhersagen
Analyseziel: 
Einfluss von Wetterdaten auf die Schadstoffbelastung der Luft
in fünf ausgewählten Städten (eine pro Kontinent)
im Zeitraum 2019 bis 2024.

<i> 
ggf Unterziel:
Prognose an welchen Tagen in 2025 ist eine erhöhter Feinstaubwert zu erwarten?
Welches 'dreckigste' Stadt Deutschlands (nach Ortsgrößenklasse)?
Haben sich die Werte in den letzten Jahren deutlich verändert? Bspw seit 2019?
Hat HomeOffice/ Pandemie einen Einfluss auf die Feinstaubbelastung?
</i>


## Projektstruktur (UPDATEN)

Die Projektstruktur ist wie folgt organisiert:

```
StackFuel_Referenzprojekt/
├── .venv/
├── .vscode/
├── data/
├── .gitignore
├── .python-version
├── BaseModel.ipynb
├── Download_kagglehub.py
├── EDA_flight_prices.ipynb
├── PCA_pretest.ipynb
├── pipelines.py
├── pyproject.toml
├── README.md
├── Test_HyperparameterOptimization.ipynb
├── test_pipelines.py
└── uv.lock
```

- **`.venv/`**: Virtuelle Python-Umgebung für das Projekt.
- **`.vscode/`**: Einstellungen von Visual Studio Code für das Projekt.
- **`data/`**: Ordner für die heruntergeladenen Datensätze.
- **`.gitignore`**: Definiert, welche Dateien von der Versionskontrolle ausgeschlossen werden.
- **`.python-version`**: Spezifiziert die Python-Version (>=3.13).
- **`BaseModel.ipynb`**: Notebook zur Implementierung eines Basis-Modells mit Verwendung der Pipeline.
- **`Download_kagglehub.py`**: Skript zum Herunterladen der Datensätze von Kaggle.
- **`EDA_flight_prices.ipynb`**: Jupyter Notebook für die explorative Datenanalyse.
- **`PCA_pretest.ipynb`**: Notebook zur Voruntersuchung mittels Hauptkomponentenanalyse.
- **`pipelines.py`**: Enthält eine Beispiel-Pipeline für die Datenvorverarbeitung inklusive Column Transformer.
- **`pyproject.toml`**: Projektkonfigurationsdatei mit Abhängigkeiten.
- **`README.md`**: Diese Dokumentation.
- **`Test_HyperparameterOptimization.ipynb`**: Notebook zur Demonstration der Hyperparameter-Optimierung mit Optuna.
- **`test_pipelines.py`**: Testskript für die Pipeline-Funktionen unter Verwendung von pytest.
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


## Explorative Datenanalyse (EDA)

- 

## Modellierung und Pipeline

- **`pipelines.py`**: Enthält eine beispielhafte Preprocessing-Pipeline inklusive Column Transformer.
- **`BaseModel.ipynb`**: Demonstriert die Verwendung der Pipeline zur Erstellung eines Basis-Modells.
- **`PCA_pretest.ipynb`**: Führt eine Hauptkomponentenanalyse durch, um die Dimensionalität der Daten zu reduzieren.

## Hyperparameter-Optimierung

- **`Test_HyperparameterOptimization.ipynb`**: Zeigt, wie man mit Optuna eine Hyperparameter-Optimierung durchführt, um die Modellleistung zu verbessern.

## Testen

- **`test_data_preparation.py`**: Enthält Tests für Daten-Download, -Import und -Cleaning unter Verwendung von pytest. Ergebnis: finaler Datensatz für die umgesetzten und zukünftige Analysen.
- **Tests ausführen**: im Terminal */air_quality/ pytest

  ```bash
  uv run -m pytest
  ```


''' im Terminal */air_quality/ pytest'''

  Dies führt die Tests aus und stellt sicher, dass die Pipeline-Komponenten korrekt funktionieren.

## Verwendete Technologien und Bibliotheken

- **Python 3.13**: Programmiersprache.
- **uv**: Paketmanager für Python.
- **Jupyter Notebook**: Interaktive Entwicklungsumgebung.
- **Pandas**: Datenanalyse und -manipulation.
- **NumPy**: Numerische Berechnungen.
- **Matplotlib & Seaborn**: Datenvisualisierung.
- **Scikit-Learn**: Maschinelles Lernen.
- **Statsmodels**: Statistische Modellierung.
- **kagglehub**: Vereinfachtes Herunterladen von Kaggle-Datensätzen.
- **tqdm**: Fortschrittsbalken für Schleifen.
- **Optuna**: Hyperparameter-Optimierung.
- **Plotly**: Interaktive Visualisierungen.
- **pytest**: Framework zum Testen von Python-Code.

## Anleitung für Teilnehmende

- **Anpassung des Projekts**: Nutzen Sie dieses Projekt als Vorlage und passen Sie es an Ihre eigenen Anforderungen an.
- **Erweiterung der Analyse**: Fügen Sie weitere Analyseschritte oder Visualisierungen hinzu.
- **Modellierung**: Entwickeln Sie eigene Modelle und experimentieren Sie mit verschiedenen Algorithmen.
- **Hyperparameter-Optimierung**: Nutzen Sie Optuna, um die Hyperparameter Ihrer Modelle zu optimieren.
- **Modularisierung**: Lagern Sie wiederverwendbaren Code in Module wie `pipelines.py` aus.
- **Testen**: Schreiben Sie Tests für Ihre Funktionen, um die Zuverlässigkeit Ihres Codes sicherzustellen.
- **Dokumentation**: Kommentieren Sie Ihren Code und dokumentieren Sie Ihre Ergebnisse ausführlich.

Wir wünschen Ihnen viel Erfolg und Freude bei Ihrem Projekt!