import streamlit as st
import pandas as pd
import io
from streamlit_extras.switch_page_button import switch_page

# Allow only logged-in users
if 'login_status' not in st.session_state or not st.session_state.login_status:
    st.warning("🚫 Please log in to access this page.")
    switch_page("account")

st.title("📤 Upload and Clean Your Dataset")

uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Load data
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    st.write("### 🔍 Raw Data Preview")
    st.dataframe(data)

    # 🔎 Detect and handle duplicates
    duplicates = data[data.duplicated()]
    data = data.drop_duplicates()

    if not duplicates.empty:
        st.write(f"### ⚠️ Found {len(duplicates)} Duplicate Records")
        st.dataframe(duplicates)
        dup_csv = duplicates.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Duplicate Records", data=dup_csv, file_name="duplicate_records.csv", mime="text/csv")

    # 🧼 Handle missing values
    for col in data.columns:
        if data[col].dtype in (float, int):
            data[col] = data[col].fillna(data[col].mean())
        else:
            data.dropna(subset=[col], inplace=True)

    st.write("### ✅ Final Cleaned Data")
    st.dataframe(data)

    cleaned_csv = data.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Cleaned Data", data=cleaned_csv, file_name="cleaned_data.csv", mime="text/csv")

# 🚪 Logout at the end of the page
st.markdown("---")
if st.button("🔓 Logout"):
    st.session_state.login_status = False
    switch_page("account")
