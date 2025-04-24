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
├── presentations/                  # Presentation files
├── 0_data_cleaning.ipynb           # Data cleaning
├── 1_EDA_exploration.ipynb         # Initial visual inspection, outlier removal
├── 2_EDA_correlations.ipynb        # Relationships between variables
├── 3_feature_engineering.ipynb     # Feature transformations for linear regression
├── 4_cluster_analysis.ipynb        # K-Means clustering
├── 5_classification_models.ipynb   # Classification models
├── 6_time_series_analysis.ipynb    # Times series analysis
├── 7_dashboard.ipynb               # First ideas for dashboard with key visuals
├── app.py                          # Script for running dashboard app 
├── data_dictionary.md              # Data dictionary and metadata
├── data_preparation.py             # Script for data import, cleaning and transformation
├── main.py                         # Main entry point (for app execution)
├── pyproject.toml                  # Project configuration (Python 3.11, dependencies)
├── README.md                       # This document
├── test_data_preparation.py        # Unit tests (pytest)
└── uv.lock                         # Lockfile for uv dependency manager
```

---

## 🧪 Testing

We used `pytest` to ensure that the core pipeline (download → clean → merge) functions correctly and is reproducible.

To run tests:

```bash
uv run -m pytest
```

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

## 📊 Results & Key Findings

The analysis of global air quality data (2015–2024) revealed several key insights across multiple analytical steps. Below are the most important findings from each stage of the project:

- **Correlation analysis** revealed strong and interpretable relationships:
  - PM10 and PM2.5 are highly correlated (r = 0.84), as expected due to compositional overlap.
  - NO₂ is moderately correlated with both PM values (r ≈ 0.42–0.49), likely due to shared emission sources such as traffic and industry.
  - Temperature variables (Tavg, Tmin, Tmax) show strong intercorrelations (r ≥ 0.90), suggesting redundancy.
  - Dew point correlates strongly with temperature (especially Tmin), highlighting their meteorological connection.
  - Air pressure correlates moderately negatively with dew point and temperature.
  → These findings supported informed feature selection and confirmed the data's consistency.

- **Feature engineering on the Hamburg dataset** significantly improved the predictive power of a linear regression model for PM2.5:
  - Through transformations, nonlinear terms (e.g. quadratic ozone), and temporal features (e.g. month, season), the model's R² increased from **0.072 to 0.313**.
  - This represents an improvement of over **330%**, demonstrating the strong impact of thoughtful feature design.

- **K-Means clustering (k=6)** grouped cities into distinct air pollution profiles based on key pollutants:
  - **Cluster 0**: Very clean air – mainly cities in Australia, New Zealand, and Canada; associated with low emissions and good ventilation.
  - **Cluster 1**: Urban but clean – cities in Europe, Japan, and the US, characterized by moderate ozone and PM2.5 levels.
  - **Cluster 2**: High ozone and NO₂ – e.g., South Korea and Southern Europe; likely driven by traffic and photochemical smog.
  - **Cluster 3**: Mixed particle pollution – Southeast Asia, South Africa, and parts of Latin America; possibly linked to residential heating and industry.
  - **Cluster 4**: Gas-dominated pollution (CO, SO₂, NO₂) – especially in Iran, Turkey, and Israel.
  - **Cluster 5**: Extreme particulate pollution – cities in China, India, and the UAE; driven by industrial activity, urbanization, and inversion weather conditions.

- **Classification of air quality (PM2.5: good vs. bad)** was performed using three models:
  - Logistic regression, random forest, and gradient boosting were compared.
  - Feature engineering improved performance across all models.
  - While overall performance was similar, non-linear models (RF, GBM) were better suited for the underlying variable structure.
  - Highly correlated features such as PM10 added little new information and were critically assessed to avoid redundancy.

- **Time series decomposition** of PM2.5 values was conducted for Hamburg and Atlanta:
  - Hamburg provided a mostly complete dataset, while other cities (e.g. Munich) contained too many gaps for meaningful analysis.
  - The decomposition (using STL and seasonal_decompose) helped uncover long-term trends and seasonal patterns despite high day-to-day variability.
  - The analysis confirmed that high-quality, continuous data is essential for reliable time series modeling.

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