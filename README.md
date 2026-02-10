# Week 11 – Brent Oil Change Point Analysis & Interactive Dashboard

**Birhan Energies** – Data-Driven Insights on Brent Crude Oil Price Regimes  
**Prepared by**: Gashaw Bekele  
**Date**: February 08–10, 2026

## Project Overview

This project performs **Bayesian change point detection** on historical Brent crude oil prices (1987–2022) to identify structural breaks (regime shifts) and associate them with major geopolitical, OPEC policy, sanctions, and economic events.

**Business Objective**  
Help stakeholders (investors, policymakers, energy companies) better understand which external shocks historically caused the largest price movements and by approximately how much — improving risk management, policy design, and strategic planning.

**Key Results**  
- Single change-point model detects a major regime shift around **2014-10-22** (index 706)  
- Average price shifted from ~$109/barrel to ~$62/barrel (–42.7% drop)  
- Strong alignment with OPEC's November 2014 no-cut decision and the 2014–2016 oil price collapse  
- Model convergence: max R-hat ≈1.004 (GOOD)

**Technologies Used**  
- Python: Pandas, NumPy, PyMC, ArviZ (Bayesian modeling)  
- Flask: Backend API  
- React + Recharts: Interactive frontend dashboard  
- Data sources: `BrentOilPrices.csv`, `events.csv`, `change_points.json`
## Folder Structure
week11-brent-oil-analysis/
├── data/
│   ├── BrentOilPrices.csv          # Raw daily prices 1987–2022
│   └── events.csv                  # Curated list of 10–15 major events
├── backend/
│   ├── app.py                      # Flask API server
│   └── requirements_backend.txt    # Flask + data dependencies
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── services/
│   │   │   └── api.js
│   │   └── components/
│   │       └── Dashboard.js
│   ├── package.json
│   └── package-lock.json
├── notebooks/
│   ├── eda.ipynb                # Exploratory analysis & visualizations
│   └── modeling.ipynb           # Bayesian change point modeling
├── outputs/                        # Saved model traces, figures (gitignored except .gitkeep)
│   └── .gitkeep
├── src/
│   ├── init.py
│   ├── data_loader.py              # OOP data loading class
│   └── data_preprocessor.py        # OOP cleaning & feature engineering
├── change_points.json              # Detected change points (static export from modeling)
├── .gitignore
├── README.md                       # ← You are here
└── requirements.txt                # Optional: combined project dependencies



## Setup & Run

### Prerequisites

- Python 3.8+ (venv recommended)
- Node.js 16+ & npm
- Git (optional)

### 1. Backend (Flask API)

```bash
cd backend
pip install -r requirements.txt   # or manually: flask flask-cors pandas numpy
python app.py

flask
flask-cors
pandas
numpy
```
### 2 Frontend (React Dashboard)

```bash
cd frontend
npm install
npm start
