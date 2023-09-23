import streamlit as st
import time


st.header("st.progress:")
my_bar = st.progress(0)

for percent_complete in range(10):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)


st.header("st.spinner:")
import time
import streamlit as st

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')


st.header("st.balloons:")
import streamlit as st
st.balloons()


st.header("st.snow:")
import streamlit as st
st.snow()


st.header("st.error:")
import streamlit as st
st.error('This is an error', icon="🚨")


st.header("st.error:")
import streamlit as st
st.warning('This is a warning', icon="⚠️")


st.header("st.info:")
import streamlit as st
st.info('This is a purely informational message', icon="ℹ️")


st.header("st.success:")
import streamlit as st
st.success('This is a success message!', icon="✅")


st.header("st.exception:")
import streamlit as st
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)


