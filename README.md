# Air Quality Data for Showcasing Data Science Tools

## 📌 Project Goal

This project was developed as part of a Data Science portfolio course and serves as a demonstration of our data analysis and data science skills. Our goal was to show that we can work with any kind of data – especially with messy, real-world datasets. This means we deliberately chose semi-structured data sources to practice the entire data science workflow: from data acquisition and cleaning to modeling and visualization.

---

## 🌍 Data Sources

- [AQICN COVID-19 Global Air Quality Dataset](https://aqicn.org/data-platform/covid19/)
- [AQICN API](https://aqicn.org/api/de/)
- [UN City Population Dataset](https://datahub.io/core/population-city#unsd-citypopulation-year-both)
- [Meteostat Python Library](https://dev.meteostat.net/)

➡️ All source data can be downloaded automatically using the `download_files()` function in `data_preparation.py`. Downloaded files will be stored in the `data/` directory.

---

## 📚 Background Resources

For more detailed information on the data context and interpretation:

- [AQI Documentation (AirNow.gov)](https://document.airnow.gov/technical-assistance-document-for-the-reporting-of-daily-air-quailty.pdf)  
  → Technical details on how the Air Quality Index (AQI) is calculated and used.

- [UN City Population Dataset](https://datahub.io/core/population-city#unsd-citypopulation-year-both)  
  → Source of urban population data used in this project.

---

## 🧱 Project Structure

```bash
AIR_QUALITY/
├── data/                           # Downloaded data (air quality, population, weather)
├── Images/                         # Visualizations and presentation graphics
├── presentations/                 # Presentation files
├── 0_data_cleaning.ipynb           # Data cleaning
├── 1_EDA_exploration.ipynb         # First visual inspection, outlier removal
├── 2_EDA_correlations.ipynb        # Relationships between variables
├── 3_feature_engineering.ipynb     # Feature transformations for linear regression
├── 4_cluster_analysis.ipynb        # K-Means clustering
├── 5_classification_models.ipynb   # Classification models
├── 6_time_series_analysis.ipynb    # Times series analysis
├── 7_dashboard.ipynb               # dashboard vor key visuals
├── app.py                          # script for running dashboard app 
├── data_dictionary.md              # Data dictionary and metadata
├── data_preparation.py             # script for data import, cleaning and transformation
├── main.py                         # Main entry point (for app execution)
├── pyproject.toml                  # Project configuration (Python 3.11, dependencies)
├── README.md                       # This document
├── test_data_preparation.py        # Unit tests (pytest)
└── uv.lock                         # Lockfile for uv dependency manager
```

---

## 🧪 Notebooks & Analyses

| Notebook | Content |
|-------------------|---------|
| `0_data_cleaning` | Data acquisition, cleaning, merging from multiple sources |
| `1_eda_exploration` | Descriptive statistics, outlier removal, visual inspection |
| `2_eda_correlations` | Pearson correlation, pairplots, variable relationship insights |
| `3_feature_engineering` | Linear regression on Hamburg air quality with R² improvement from 0.07 to 0.31 through feature transformations |
| `4_cluster_analysis` | K-Means clustering of cities based on pollutant data |
| `5_classification_models` | Predicting “good” vs. “bad” air quality using logistic regression, random forest, and gradient boosting |
| `6_time_series_analysis` | Seasonal decomposition of PM2.5 trends for Hamburg and Atlanta |
| `7_dashboard` | First version of an interactive Streamlit dashboard (work in progress) |

---

## 🧪 Testing

We used `pytest` to test the data preparation pipeline.

To run tests:

```bash
uv run -m pytest
```

This ensures that the core pipeline (download → clean → merge) functions correctly and is reproducible.

---

## 🛠️ Tools & Technologies

- **Language**: Python 3.11
- **Environment**: VS Code, virtual environment managed via `uv`
- **Development**: Jupyter Notebooks + Python Scripts
- **Packages**:
  - `pandas`, `numpy` – data manipulation
  - `matplotlib`, `seaborn`, `plotly` – visualization
  - `scikit-learn` – machine learning (classification, clustering)
  - `statsmodels` – time series decomposition
  - `geopandas` – geospatial data
  - `pytest` – testing
  - `streamlit` – interactive dashboard

---

## 🚧 Planned Extensions

- Interactive dashboard with filters for city, season, and pollutant
- Additional ML approaches (e.g., Neural Networks)
- Translation of the entire repository into English (currently mixed)

---

## 📖 Reusability & Documentation

All steps are clearly documented and include:
- Explanations of the reasoning behind transformations and model decisions
- Reusable code structured in functions and modular notebooks
- A data dictionary in `data_dictionary.md` for reference

---

## 🤝 Authors

- [Mareike Keller](https://github.com/Mareike-K)  
- [Wiebke Sir](https://github.com/whypkey)