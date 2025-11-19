import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_loader import load_data

# Page Configuration
st.set_page_config(
    page_title="Compliance Wave",
    page_icon="🌍",
    layout="wide"
)

# Load Data
DATA_PATH = "data/mandate_data.csv"
df = load_data(DATA_PATH)

# Sidebar
st.sidebar.header("Filters")
scope_filter = st.sidebar.radio("Select Scope", ["All", "B2G Only", "B2B & B2G"], index=0)
# Region filter placeholder - to be implemented when data has region info
# region_filter = st.sidebar.selectbox("Region", ["Global", "Europe", "Asia-Pac", "LatAm"])

st.sidebar.markdown("---")
st.sidebar.info("Data last updated: Nov 2025")

# Main Content
st.title("Global E-Invoice Compliance Map")
st.markdown("Visualize the global adoption of e-invoicing mandates.")

# Timeline Slider
min_year = 2015
max_year = 2030
selected_year = st.slider("Select Year", min_value=min_year, max_value=max_year, value=2025)

# Data Processing for Visualization
def get_status_for_year(row, year):
    mandate_year = row['Year']
    if year >= mandate_year:
        return row['Status_B2B'] # Using B2B status as primary for now
    elif year >= mandate_year - 1: # 1 year prior
        return "Upcoming"
    else:
        return "No Mandate"

if not df.empty:
    # Apply logic to determine status based on selected year
    df['Current_Status'] = df.apply(lambda x: get_status_for_year(x, selected_year), axis=1)
    
    # Color mapping
    color_discrete_map = {
        "Mandatory": "darkblue",
        "Optional": "yellow",
        "Upcoming": "orange",
        "No Mandate": "lightgrey"
    }

    # Map Visualization
    fig = px.choropleth(
        df,
        locations="Country Code",
        color="Current_Status",
        hover_name="Country Name",
        hover_data=["Year", "Model_Type", "Platform_Name"],
        color_discrete_map=color_discrete_map,
        projection="mercator",
        title=f"E-Invoicing Status in {selected_year}"
    )
    
    fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

    # Country Details (Simple table for now, or filtered view)
    st.subheader("Country Details")
    st.dataframe(df[['Country Name', 'Status_B2B', 'Year', 'Model_Type', 'Platform_Name', 'Current_Status']])

else:
    st.error("No data found. Please check data/mandate_data.csv")
