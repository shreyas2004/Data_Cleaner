import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

# Optional: Set page config
st.set_page_config(page_title="Data Cleaner", page_icon="🧹", layout="centered")

# Title Section
st.markdown("<h1 style='text-align: center;'>🧹 Welcome to Data Cleaner App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Clean your datasets instantly — without code!</h4>", unsafe_allow_html=True)
st.markdown("---")

# App Features
st.markdown("### ✨ What This App Can Do")
st.markdown("""
- 📁 Upload CSV or Excel datasets  
- 🧯 Automatically detect and remove duplicate rows  
- ❓ Fill missing values smartly (mean for numbers, drop for others)  
- 🧼 Download fully cleaned data  
- 🔐 Secure login & account management  
""")

# Navigation Buttons
st.markdown("### 🚀 Get Started")
col1, col2 = st.columns(2)

with col1:
    if st.button("🔐 Go to Account"):
        switch_page("account")

