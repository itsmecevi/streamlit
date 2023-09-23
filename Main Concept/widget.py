import streamlit as st
import pandas as pd
import numpy as np


"""
### How to Create Widget
"""

st.subheader("Widgets:")

st.write("Slider")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


st.write("Text input")
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name


st.write("Checkbox")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(5, 2),
       columns=['a', 'b'])

    chart_data



st.write("Selectbox")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
