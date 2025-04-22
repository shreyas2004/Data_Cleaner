import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
from streamlit_extras.switch_page_button import switch_page
import requests

# ---------- Firebase Initialization ----------
if not firebase_admin._apps:
    cred = credentials.Certificate("data-cleaner-47f72-96c5a3c00bce.json")  
    firebase_admin.initialize_app(cred)

API_KEY = "AIzaSyAUgnmKpVyKmjPfK_lhyrQr11BT-ko9L1w"   

# ---------- Firebase Auth Functions ----------
def verify_user_with_firebase(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    payload = {"email": email, "password": password, "returnSecureToken": True}
    response = requests.post(url, json=payload)
    return response.status_code == 200, response.json()

# ---------- Login / Sign Up Page ----------
st.title("🔐 Login / Sign Up to Data Cleaner")

if 'login_status' not in st.session_state:
    st.session_state.login_status = False

option = st.selectbox("Choose Action", ["Login", "Sign Up"])

# ------------------ LOGIN ------------------
if option == "Login":
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        if email and password:
            success, data = verify_user_with_firebase(email, password)
            if success:
                st.session_state.login_status = True
                st.success("✅ Login successful! Redirecting...")
                switch_page("uploadfiles")
            else:
                st.error("❌ Login failed: " + data.get("error", {}).get("message", "Unknown error"))
        else:
            st.warning("⚠️ Please enter both email and password.")



# ------------------ SIGN UP ------------------
else:
    email = st.text_input("Email", key="signup_email")
    password = st.text_input("Password", type="password", key="signup_password")
    username = st.text_input("Enter your unique username", key="signup_username")

    if st.button("Create Account"):
        if email and password and username:
            try:
                auth.create_user(email=email, password=password, uid=username)
                st.success("✅ Account created successfully! Please log in.")
            except Exception as e:
                st.error(f"❌ Error: {e}")
        else:
            st.warning("⚠️ Please fill all the fields.")
