# Data Dictionary

This file contains an overview of all variables used in the project. It includes:
- Column names and descriptions
- Available pollutant and weather types
- Meteostat weather variable definitions
- ISO-3166-2 country codes
- Data source references


# Spaltennamen

| Spalte    |           | Beschreibung                                                      |
|-----------|-----------|-------------------------------------------------------------------|
| Date      |   Datum   | Tag der Messung                                                   |
| Country   |   Land    | Land in dem die Messstation steht                                 |
| City      |   Stadt   | Stadt in der die Messstation steht                                |
| Species   |   Arten   | Art des Messwerts                                                 |
| count     |   Anzahl  | Anzahl Messungen um Median und Standardabweichungen zu berechnen  |
| min       |   Minimum | Median der Tiefstwerte aller Messungen aller Stationen an dem Tag |
| max       |   Maximum | Median der Höchstwerte aller Messungen aller Stationen an dem Tag |
| median    |   Median  | Median aller Messungen aller Stationen an dem Tag                 |
| variance  |   Varianz | Quadrierte Abweichung vom Median                                  |

# Messwerte (Arten)

| Name           | Bedeutung                                 | Beschreibung                                           |
|-----------     |-------------------------------------------|--------------------------------------------------------|
| aqi            | Air Quality Index                         |      
| co             | Kohlenmonoxid                             |
| dew            | Tau                                       |
| humidity       | Luftfeuchtigkeit                          |
| mepaqi         | Ministry of Environment Protection AQI    |
| neph           | Nephelometer-Messungen                    | Lichtstreuung an Aerosolpartikeln
| no2            | Stickstoffdioxid                          |
| o3             | Ozon                                      |
| pm1            | particulate matter 1                      | Partikel die kleiner als 1 Mikrometer sind
| pm10           | particulate matter 10                     | Partikel, die kleiner als 10 Mikrometer sind
| pm25           | particulate matter 2,5                    | Partikel, die kleiner als 2,5 Mikrometer sind
| precipitation* | Niederschlag                              |
| pressure*      | Luftdruck                                 |
| so2            | Schwefeldioxid                            |
| temperature*   | Temperatur                                |
| uvi*           | UV-Index                                  |
| wd*            | Wind Direction                            | Windrichtung
| wind-gust*     |                                           | Windböen
| wind-speed*    |                                           | Windstärke
|* Werden durch Meteostat ersetzt.

# Meteostat-Daten 
(https://dev.meteostat.net/python/daily.html#data-structure):
| Name           | Bedeutung                                 | Beschreibung                                           |
|-----------     |-------------------------------------------|--------------------------------------------------------|
| Tavg           | Average Temperature                       | Durchschnittstemperatur in °C
| Tmin           | Minimum Temperature                       | Tiefsttemperatur in °C
| Tmax           | Maximum Temperature                       | Höchsttemperatur in °C
| Prcp           | Precipitation                             | Niederschlag mm
| Wdir           | Wind Direction                            | Windrichtung in °
| Wsp            | Wind Speed                                | Windstärke in km/h
| Pres           | Pressure                                  | Luftdruck in hPa






# Länderkürzel (nach ISO-3166-2)

|    |  Land                            |  |    |   Land                           |--|    |    Land                          |
|----|----------------------------------|--|----|----------------------------------|--|----|----------------------------------|
| AE |  Vereinigte Arabische Emirate    |  | AR |  Argentinien                     |  | AT |  Österreich                      |
| AU |  Australien                      |  | BA |  Bosnien und Herzegowina         |  | BD |  Bangladesch                     |
| BE |  Belgien                         |  | BG |  Bulgarien                       |  | BH |  Bahrain                         |
| BR |  Brasilien                       |  | CA |  Kanada                          |  | CH |  Schweiz                         |
| CI |  Elfenbeinküste                  |  | CL |  Chile                           |  | CN |  Volksrepublik China             |
| CO |  Kolumbien                       |  | CW |  Curaçao                         |  | CY |  Zypern                          |
| CZ |  Tschechien                      |  | DE |  Deutschland                     |  | DK |  Dänemark                        |
| DZ |  Algerien                        |  | EC |  Ecuador                         |  | EE |  Estland                         |
| ES |  Spanien                         |  | ET |  Äthiopien                       |  | FI |  Finnland                        |
| FR |  Frankreich                      |  | GB |  Vereinigtes Königreich          |  | GE |  Georgien                        |
| GH |  Ghana                           |  | GN |  Guinea                          |  | GR |  Griechenland                    |
| GT |  Guatemala                       |  | HK |  Hongkong                        |  | HR |  Kroatien                        |
| HU |  Ungarn                          |  | ID |  Indonesien                      |  | IE |  Irland                          |
| IL |  Israel                          |  | IN |  Indien                          |  | IQ |  Irak                            |
| IR |  Iran                            |  | IS |  Island                          |  | IT |  Italien                         |
| JO |  Jordanien                       |  | JP |  Japan                           |  | KG |  Kirgisistan                     |
| KR |  Südkorea                        |  | KW |  Kuwait                          |  | KZ |  Kasachstan                      |
| LA |  Laos                            |  | LK |  Sri Lanka                       |  | LT |  Litauen                         |
| MK |  Nordmazedonien                  |  | MM |  Myanmar                         |  | MN |  Mongolei                        |
| MO |  Macau                           |  | MX |  Mexiko                          |  | MY |  Malaysia                        |       
| NL |  Niederlande                     |  | NO |  Norwegen                        |  | NP |  Nepal                           |
| NZ |  Neuseeland                      |  | PE |  Peru                            |  | PH |  Philippinen                     |
| PK |  Pakistan                        |  | PL |  Polen                           |  | PR |  Puerto Rico                     |
| PT |  Portugal                        |  | RE |  Réunion                         |  | RO |  Rumänien                        |
| RS |  Serbien                         |  | RU |  Russland                        |  | SA |  Saudi-Arabien                   |
| SE |  Schweden                        |  | SG |  Singapur                        |  | SK |  Slowakei                        |
| SV |  El Salvador                     |  | TH |  Thailand                        |  | TJ |  Tadschikistan                   |
| TM |  Turkmenistan                    |  | TR |  Türkei                          |  | TW |  Taiwan                          |
| UG |  Uganda                          |  | US |  Vereinigte Staaten              |  | UZ |  Usbekistan                      |
| VN |  Vietnam                         |  | XK |  Kosovo                          |  | ZA |  Südafrika                       |

# Detaillierte Infos zum AQI:
https://document.airnow.gov/technical-assistance-document-for-the-reporting-of-daily-air-quailty.pdf


# Bevölkerungsdaten: 
https://datahub.io/core/population-city#unsd-citypopulation-year-both