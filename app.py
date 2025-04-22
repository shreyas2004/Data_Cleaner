import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Data Cleaner App", layout="centered")
st.title("🚀 Data Cleaner Launcher")

st.markdown("Click below to start from the homepage.")

if st.button("👉 Launch App"):
    switch_page("home")
