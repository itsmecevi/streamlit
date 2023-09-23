import streamlit as st
import pandas as pd
import numpy as np


"""
### Data Frame
"""

st.subheader("Write a data frame:")


st.write("Manual dataframe")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


st.write("Random dataframe")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

 
st.write("Using Panda Styler")
dataframe = pd.DataFrame(
    np.random.randn(7, 7),
    columns=('col %d' % i for i in range(7)))

st.dataframe(dataframe.style.highlight_max(axis=0))


st.write("Static table generation")
dataframe = pd.DataFrame(
    np.random.randn(5, 5),
    columns=('col %d' % i for i in range(5)))
st.table(dataframe)
