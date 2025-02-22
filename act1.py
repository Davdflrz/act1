# Example 4

import streamlit as st
import plotly.express as px
import pandas as pd 
import seaborn as sns 

# Load Sample Data
df = sns.load_dataset("mpg")

# Streamlit App Title
st.title("📊 Interactive Dashboard")

# Create a sidebar filter for selecting a year
# Selecting model_year instead of name as name column was causing the error.
selected_year = st.sidebar.slider("Select Model Year:", int(df["model_year"].min()), int(df["model_year"].max()), int(df["model_year"].min()))

# Filter data based on the selected year
filtered_df = df[df.model_year == selected_year]

# Create three different plots
fig1 = px.scatter(filtered_df, x="cylinders", y="mpg", size="acceleration", color="origin",
                  hover_name="model_year", log_x=True, size_max=60, title="Cylinders vs mpg")

# Removing size_max as it is not a valid argument for px.bar
fig2 = px.bar(filtered_df, x="origin", y="acceleration", color="origin", log_x=True,  title="acceleration per origin")

fig3 = px.line(filtered_df, x="model_year", y="cylinders", color="origin", title="model")

# Layout - Using Tabs to Display Multiple Plots
tab1, tab2, tab3 = st.tabs(["📌 Scatter Plot", "📊 Bar Chart", "📈 Line Chart"])

with tab1:
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.plotly_chart(fig3, use_container_width=True)

# Layout - Using Tabs to Display Multiple Plots
tab1, tab2, tab3 = st.tabs(["📌 Scatter Plot", "📊 Bar Chart", "📈 Line Chart"])

with tab1:
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.plotly_chart(fig3, use_container_width=True)

