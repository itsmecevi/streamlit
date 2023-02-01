import streamlit as st
import pandas as pd
import numpy as np

"""
# My first app
Here's our first attempt at using data to create a table:
"""
st.subheader("1-Magic:")
import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


st.subheader("2-Write a data frame:")


st.write("2A: Manual dataframe")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


st.write("2B: Random dataframe")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

 
st.write("2C: Using Panda Styler")
dataframe = pd.DataFrame(
    np.random.randn(7, 7),
    columns=('col %d' % i for i in range(7)))

st.dataframe(dataframe.style.highlight_max(axis=0))


st.write("2D: Static table generation")
dataframe = pd.DataFrame(
    np.random.randn(5, 5),
    columns=('col %d' % i for i in range(5)))
st.table(dataframe)


st.subheader("3-Charts and maps:")


st.write("3A: Line chart")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("3B: Plot a map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)



st.subheader("4-Widgets:")

st.write("4A: Slider")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


st.write("4B: Text input")
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name


st.write("4C: Checkbox")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(5, 2),
       columns=['a', 'b'])

    chart_data



st.write("4D: Selectbox")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option


st.subheader("5-Layout:")
st.write("5A: Sidebar")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


st.write("5B: Expander")
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")



st.write("5C: Show progress")
import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'


st.subheader("6-Caching:")

"""
The Streamlit cache allows your app to execute 
quickly even when loading data from the web, manipulating large datasets, or performing expensive computations.
"""

import streamlit as st

@st.cache  # 👈 This function will be cached
def my_slow_function(arg1, arg2):
    # Do something really slow in here!
    return the_output