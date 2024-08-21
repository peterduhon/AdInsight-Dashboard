import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from datetime import datetime

# Set page config and custom CSS
st.set_page_config(page_title="AdInsight: Reddit Ad Performance Dashboard", layout="wide")

# Custom CSS to reduce spacing and improve layout
st.markdown("""
    <style>
    .reportview-container .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 95%;
    }
    .stDateInput > label {
        display: inline-block;
        margin-right: 1rem;
    }
    .stDateInput > div {
        display: inline-block;
    }
    h1 {
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("AdInsight: Reddit Ad Performance Dashboard")

# Date range selector in a single row
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", value=datetime(2024, 8, 1))
with col2:
    end_date = st.date_input("End Date", value=datetime(2024, 8, 3))

# Fetch data
@st.cache_data
def get_data():
    conn = sqlite3.connect('data/ad_performance.db')
    df = pd.read_sql_query("SELECT * FROM ad_performance", conn)
    conn.close()
    df.columns = ['id', 'date', 'impressions', 'clicks', 'ctr', 'conversions']
    df['date'] = pd.to_datetime(df['date']).dt.date
    return df

df = get_data()

# Filter data based on date range
mask = (df['date'] >= start_date) & (df['date'] <= end_date)
filtered_df = df.loc[mask].drop_duplicates(subset=['date'])

# Display metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Impressions", f"{filtered_df['impressions'].sum():,}")
col2.metric("Total Clicks", f"{filtered_df['clicks'].sum():,}")
col3.metric("Average CTR", f"{(filtered_df['ctr'].mean() * 100):.2f}%")
col4.metric("Total Conversions", f"{filtered_df['conversions'].sum():,}")

# Create and display chart
fig = px.line(filtered_df, x='date', y=['clicks', 'conversions'], title='Clicks and Conversions Over Time')
fig.update_layout(height=400)  # Reduce the height of the chart
st.plotly_chart(fig, use_container_width=True)

# Display raw data in an expandable section
with st.expander("View Raw Data", expanded=False):
    st.dataframe(filtered_df)
    
    # Add a download button for the data
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="ad_performance_data.csv",
        mime="text/csv",
    )