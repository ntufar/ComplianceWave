# 🌍 Global E-Invoice Compliance Map (The "Compliance Wave")

**Live Demo:** [https://compliance-wave.streamlit.app/](https://compliance-wave.streamlit.app/)

## Overview
The **Compliance Wave** is an interactive dashboard designed to visualize the rapidly shifting landscape of global e-invoicing mandates. As governments worldwide transition from paper to digital reporting, tax managers and strategists need a clear way to track *where* and *when* these laws take effect.

This tool provides a time-based geospatial visualization, allowing users to explore the evolution of mandates from 2015 to 2030.

## Key Features
- **Interactive Choropleth Map**: Visualizes the status of e-invoicing mandates globally (Mandatory, Optional, Upcoming, No Mandate).
- **Time Travel**: A timeline slider lets you view the state of compliance in the past, present, and future.
- **Scope Filtering**: Toggle between **B2G** (Business-to-Government) and **B2B** (Business-to-Business) mandates.
- **Country Details**: View specific details like platform names (e.g., Chorus Pro, KSeF) and model types (Clearance vs. Post-Audit).

## Tech Stack
- **Python 3.9+**
- **Streamlit**: For the web application framework.
- **Plotly Express**: For interactive map visualizations.
- **Pandas**: For data manipulation.

## Local Development

To run this application locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/compliance-wave.git
    cd compliance-wave
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

## Deployment
This application is designed to be deployed on **Streamlit Community Cloud**.
Simply connect your GitHub repository to Streamlit Cloud to deploy.

---
Created by Nicolai Tufar.
