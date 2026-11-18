import streamlit as st

# Set your password securely (in production, use environment variables)
CORRECT_PASSWORD = "secret123"

# Initialize session state variables
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

st.title("Password Protected Button Example")

# Password input field
password_input = st.text_input("Enter password:", type="password")

# Check password and update authentication state
if st.button("Login"):
    if password_input == CORRECT_PASSWORD:
        st.session_state.authenticated = True
        st.success("Password correct! You are now logged in.")
    else:
        st.session_state.authenticated = False
        st.error("Incorrect password. Try again.")

st.write("---")

# Protected button
if st.session_state.authenticated:
    if st.button("Run Protected Action"):
        st.info("Protected action executed successfully!")
else:
    st.warning("Please log in with the correct password to access the protected action.")
