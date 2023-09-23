import streamlit as st
import pandas as pd
import numpy as np


"""
### How to Creata Chart and Maps
"""

st.subheader("Charts and maps:")


st.write("Line chart")
chart_data = pd.DataFrame(
     np.random.randn(20, 2),
     columns=['a', 'b'])

st.line_chart(chart_data)

st.write("Plot a map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)