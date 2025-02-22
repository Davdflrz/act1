import streamlit as st
import plotly.express as px
import pandas as pd 
import seaborn as sns 

# Load Sample Data
df = sns.load_dataset("mpg")

# Streamlit App Title
st.title("📊 Interactive Dashboard")

# Create a sidebar filter for selecting a year
selected_name = st.sidebar.slider("Select Name:", int(df["name"].min()), int(df["name"].max()), int(df["name"].min()))

# Filter data based on the selected year
filtered_df = df[df.name == selected_name]

# Create three different plots
fig1 = px.scatter(filtered_df, x="cylinders", y="mpg", size="acceleration", color="origin",
                  hover_name="model_year", log_x=True, size_max=60, title="Cylinders vs mpg")

fig2 = px.bar(filtered_df, x="origin", y="acceleration", color="origin", log_x=True, size_max=60, title="acceleration per origin")

fig3 = px.line(filtered_df, x="model_year", y="cylinders", color="origin", title="model")

# Layout - Using Tabs to Display Multiple Plots
tab1, tab2, tab3 = st.tabs(["📌 Scatter Plot", "📊 Bar Chart", "📈 Line Chart"])

with tab1:
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.plotly_chart(fig3, use_container_width=True)

