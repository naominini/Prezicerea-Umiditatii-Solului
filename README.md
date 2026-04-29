# Prezicerea Umidității Solului 🌱

## Despre proiect

Acest proiect analizează și prezice umiditatea solului folosind date meteorologice zilnice colectate în zona lacului Urmia din Iran, acoperind perioada 1993-2022. Lacul Urmia este unul dintre cele mai mari lacuri sărate din lume și a suferit o reducere drastică a suprafeței în ultimele decenii din cauza schimbărilor climatice și a activității umane, făcând analiza condițiilor meteorologice din zonă extrem de relevantă pentru cercetarea hidrologică și agricolă.

Umiditatea solului joacă un rol esențial în agricultură, hidrologie și gestionarea resurselor de apă. Prezicerea acesteia pe baza parametrilor meteorologici poate contribui la o mai bună planificare în aceste domenii, în special în regiuni aride și semi-aride.

## Dataset

Datasetul conține **10957 înregistrări zilnice** pe o perioadă de **30 de ani (1993-2022)** cu următoarele variabile:

| Coloană | Descriere |
|--------|-----------|
| Tmax | Temperatura maximă zilnică (°C) |
| Tmin | Temperatura minimă zilnică (°C) |
| Tmean | Temperatura medie zilnică (°C) |
| RHmax | Umiditatea relativă maximă (%) |
| RHmin | Umiditatea relativă minimă (%) |
| SSHtime | Durata strălucirii solare (ore) |
| U | Viteza vântului (m/s) |
| P24 | Precipitații zilnice (mm) |

## Metodologie

**Curățarea datelor** — valorile anomale au fost eliminate prin metoda Z-score, păstrând 10573 înregistrări.

**Analiza datelor** — au fost calculați indicatori statistici precum Gini Index și Entropia pentru fiecare variabilă, iar corelațiile dintre variabile au fost vizualizate printr-un heatmap.

**Modele ML** — variabila țintă este **RHmin** (umiditatea minimă), iar variabilele de intrare sunt restul coloanelor meteorologice. Datele au fost împărțite 70% antrenare și 30% testare.

## Rezultate

Au fost antrenați și optimizați 3 algoritmi prin RandomizedSearchCV cu validare încrucișată:

| Model | R2 | RMSE |
|-------|----|------|
| Linear Regression | 0.7970 | 7.1103 |
| Random Forest | 0.8265 | 6.5740 |
| **XGBoost** | **0.8319** | **6.4705** |

**XGBoost** a fost ales ca model final datorită celui mai bun R2 și celui mai mic RMSE după optimizarea hiperparametrilor.

## Valoare practică

Prezicerea umidității solului pe baza parametrilor meteorologici poate contribui la o mai bună gestionare a resurselor de apă în regiuni aride, la optimizarea irigațiilor în agricultură și la înțelegerea impactului schimbărilor climatice asupra ecosistemelor locale.

## Cod

Codul complet se găsește în [cod.ipynb](https://github.com/naominini/Prezicerea-Umiditatii-Solului/blob/main/cod.ipynb).

## Tehnologii

- Python 3.13
- pandas, numpy, matplotlib, seaborn
- scikit-learn, xgboost, scipy