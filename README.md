# Brent Oil Prices Dashboard & Bayesian Change Point Analysis  
**Birhan Energies – Week 11 Challenge**

Interactive dashboard and Bayesian analysis to understand how major geopolitical, OPEC policy, sanctions, and economic events have historically driven structural breaks (regime shifts) in Brent crude oil prices.

**Current date reference**: February 08, 2026 (interim submission)

## Project Overview

**Business Objective**  
Quantify and explain how significant external shocks affect Brent oil price regimes to support better decision-making for:  
- Investors (risk management, timing, hedging)  
- Policymakers (energy security, inflation control)  
- Energy companies (cost forecasting, operations, supply chain)

**Core Deliverables**  
- Bayesian change point detection (PyMC) identifying mean-level regime shifts  
- Temporal association with curated high-impact events  
- Fully interactive Flask + React dashboard showing prices, events, change points, volatility, and impact metrics

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


## Prerequisites

**Backend**
- Python 3.9+
- pip

**Frontend**
- Node.js 16+ / npm 8+
- (yarn optional)

## Installation & Setup

### 1. Backend (Flask API)

```bash
# Navigate to backend folder
cd backend

# Install dependencies
pip install -r requirements_backend.txt

flask
flask-cors
pandas
numpy
