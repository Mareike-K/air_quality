import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Seite konfigurieren
st.set_page_config(page_title="Luftqualitätsvergleich", layout="centered")

# Daten laden
df = pd.read_csv("data/test_dashboard_air_quality.csv")
df["Datum"] = pd.to_datetime(df[["Year", "Month", "Day"]])

# Stadt A und Stadt B auswählen
alle_staedte = sorted(df["City"].unique())
stadt_a = st.selectbox("Stadt A auswählen", alle_staedte, index=0)
stadt_b = st.selectbox("Stadt B auswählen", alle_staedte, index=1)

# Schadstoff-Auswahl
schadstoffe = ["Pm25", "Co", "No2", "So2", "O3"]
anzeige_namen = {
    "Pm25": "PM2.5",
    "Co": "CO",
    "No2": "NO₂",
    "So2": "SO₂",
    "O3": "O₃"
}
auswahl = st.selectbox("Wähle einen Schadstoff", schadstoffe)

# Grenzwert-Modus auswählen
modus = st.radio(
    "Wie sollen hohe Schadstoffwerte erkannt werden?",
    ("Offizieller Grenzwert", "Statistisch (oberes Quartil)")
)

# Grenzwert festlegen
if modus == "Offizieller Grenzwert":
    if auswahl == "Pm25":
        grenzwert = 25
    elif auswahl == "No2":
        grenzwert = 40
    elif auswahl == "So2":
        grenzwert = 20
    elif auswahl == "O3":
        grenzwert = 100
    elif auswahl == "Co":
        grenzwert = 5  # Beispielwert in mg/m³
    else:
        grenzwert = None
else:
    grenzwert = df[auswahl].quantile(0.75)

st.caption(f"Verwendeter Grenzwert für {anzeige_namen[auswahl]}: {grenzwert:.2f}")

# Farben definieren
farbe_a = "#4c7195"     # Stadt A
farbe_b = "#6ec9e0"     # Stadt B
farbe_hoch_a = "#c62828"  # Hoher Wert A (Dunkelrot)
farbe_hoch_b = "#ff4069"  # Hoher Wert B (Leuchtrot)

# Monatliche Mittelwerte vorbereiten
df["Jahr_Monat"] = df["Datum"].dt.to_period("M")
df_grouped = df.groupby(["City", "Jahr_Monat"])[auswahl].mean().reset_index()
df_grouped["Jahr_Monat"] = df_grouped["Jahr_Monat"].astype(str)
df_grouped["Jahr_Monat"] = pd.to_datetime(df_grouped["Jahr_Monat"])

# Daten filtern
df_a = df_grouped[df_grouped["City"] == stadt_a]
df_b = df_grouped[df_grouped["City"] == stadt_b]

# Abschnittstrennung im Dashboard: Balkendiagramm
st.markdown("## 🌍 Vergleich der Jahresmittelwerte")

# Jahresmittelwerte berechnen
df["Jahr"] = df["Datum"].dt.year
jahresmittel = df.groupby(["City", "Jahr"])[auswahl].mean().reset_index()

# Neuestes Jahr wählen (z. B. 2023, 2022 ...)
letztes_jahr = jahresmittel["Jahr"].max()
df_letztes_jahr = jahresmittel[jahresmittel["Jahr"] == letztes_jahr]

# Balkendiagramm mit matplotlib
fig_bar, ax_bar = plt.subplots()
farben = {
    "Delhi": "#ff4069",
    "Tokyo": "#4c7195",
    "Osaka": "#6ec9e0"
}
ax_bar.bar(
    df_letztes_jahr["City"],
    df_letztes_jahr[auswahl],
    color=[farben[stadt] for stadt in df_letztes_jahr["City"]]
)

# Styling
ax_bar.set_title(f"{anzeige_namen[auswahl]}-Jahresmittel {letztes_jahr}")
ax_bar.set_ylabel(f"{anzeige_namen[auswahl]} (µg/m³)")
ax_bar.set_xlabel("Stadt")
ax_bar.grid(axis="y")

# Balkendiagramm anzeigen
st.pyplot(fig_bar)

# Abschnittstrennung im Dashboard: Liniendiagramm

# Plot erstellen
fig, ax = plt.subplots()

# Linien plotten
# Linien plotten
ax.plot(df_a["Jahr_Monat"], df_a[auswahl], label=stadt_a, marker='o', color=farbe_a)
ax.plot(df_b["Jahr_Monat"], df_b[auswahl], label=stadt_b, marker='x', color=farbe_b)

# Hohe Werte hervorheben
hoch_a = df_a[df_a[auswahl] > grenzwert]
hoch_b = df_b[df_b[auswahl] > grenzwert]

ax.scatter(hoch_a["Jahr_Monat"], hoch_a[auswahl], color=farbe_hoch_a, s=50, label=f"hoch in {stadt_a}", zorder=5)
ax.scatter(hoch_b["Jahr_Monat"], hoch_b[auswahl], color=farbe_hoch_b, s=50, label=f"hoch in {stadt_b}", zorder=5)

# Styling
ax.set_title(f"{anzeige_namen[auswahl]}-Monatsmittel in {stadt_a} vs. {stadt_b}")
ax.set_xlabel("Monat")
ax.set_ylabel(f"{anzeige_namen[auswahl]} (Monatsmittel)")
ax.legend()
ax.grid(True)

# Plot anzeigen
st.pyplot(fig)

# Kennzahlen berechnen
mean_a = df_a[auswahl].mean()
min_a = df_a[auswahl].min()
max_a = df_a[auswahl].max()
count_a = df_a[auswahl].count()

mean_b = df_b[auswahl].mean()
min_b = df_b[auswahl].min()
max_b = df_b[auswahl].max()
count_b = df_b[auswahl].count()

# In zwei Spalten anzeigen
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{stadt_a}")
    st.metric("Mittelwert", f"{mean_a:.2f}")
    st.metric("Minimum", f"{min_a:.2f}")
    st.metric("Maximum", f"{max_a:.2f}")
    st.caption(f"{count_a} Monatswerte")

with col2:
    st.subheader(f"{stadt_b}")
    st.metric("Mittelwert", f"{mean_b:.2f}")
    st.metric("Minimum", f"{min_b:.2f}")
    st.metric("Maximum", f"{max_b:.2f}")
    st.caption(f"{count_b} Monatswerte")

st.markdown("## 🔍 Langfristige Entwicklung (Trend aus Zeitreihenzerlegung)")
st.caption("Visualisierung der PM2.5-Trendlinie auf Basis monatlicher Mittelwerte")

# Abschnittstrennung im Dashboard: Trendlinien

# Trenddaten laden
df_trend = pd.read_csv("data/trendlinien_pm25.csv")
df_trend["Datum"] = pd.to_datetime(df_trend["Datum"])

# Daten für Stadt A und B
trend_a = df_trend[df_trend["City"] == stadt_a]
trend_b = df_trend[df_trend["City"] == stadt_b]

# Plot erstellen
fig_trend, ax_trend = plt.subplots()

# Linien plotten
ax_trend.plot(trend_a["Datum"], trend_a["Trend"], label=f"{stadt_a}", color=farbe_a, linewidth=2)
ax_trend.plot(trend_b["Datum"], trend_b["Trend"], label=f"{stadt_b}", color=farbe_b, linewidth=2)

# Styling
ax_trend.set_title(f"PM2.5-Trend in {stadt_a} vs. {stadt_b}")
ax_trend.set_xlabel("Jahr")
ax_trend.set_ylabel("Trend (PM2.5)")
ax_trend.legend()
ax_trend.grid(True)

# Anzeigen
st.pyplot(fig_trend)
