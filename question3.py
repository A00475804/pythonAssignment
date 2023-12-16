# -*- coding: utf-8 -*-
"""

@author: mehta
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Age Distribution Analyzer')
uploaded_file = st.file_uploader("Select a CSV file:", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if 'Age' in df.columns and 'Name' in df.columns:
        st.write("Visualizing age distribution with a histogram")
        fig, ax = plt.subplots()
        ax.hist(df['Age'], bins=100, color='cyan', edgecolor='black')
        ax.set_xlabel('Ages')
        ax.set_ylabel('Frequency')
        ax.set_title('Age Distribution')
        st.pyplot(fig)
    else:
        st.error("Invalid file format. The CSV must contain 'Age' and 'Name' columns.")
else:
    st.write("Please upload a CSV file to proceed.")

