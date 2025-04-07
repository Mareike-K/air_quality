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

# Daten für beide Städte filtern
df_a = df[df["City"] == stadt_a].copy()
df_b = df[df["City"] == stadt_b].copy()

# Plot erstellen
fig, ax = plt.subplots()

# Stadt A plotten
ax.plot(df_a["Datum"], df_a[auswahl], label=stadt_a, marker='o')

# Stadt B plotten
ax.plot(df_b["Datum"], df_b[auswahl], label=stadt_b, marker='x')

# Styling
ax.set_title(f"{anzeige_namen[auswahl]}-Werte in {stadt_a} vs. {stadt_b}")
ax.set_xlabel("Datum")
ax.set_ylabel(anzeige_namen[auswahl])
ax.legend()
ax.grid(True)

# Plot anzeigen
st.pyplot(fig)
