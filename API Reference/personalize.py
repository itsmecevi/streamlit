
import streamlit as st

if st.experimental_user.email=="itsmecevi@gmail.com":
 st.write("Welcome Back Cevi", st.experimental_user.email)

else:
 
    st.write("You Are Forbidden")

