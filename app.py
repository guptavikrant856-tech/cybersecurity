import streamlit as st

st.set_page_config(
    page_title="Cyber Security Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Cyber Security Dashboard")

st.markdown("""
Welcome to the Cyber Security Dashboard.

Use the sidebar to access:

- Port Scanner
- Firewall Status
- Running Processes
""")

st.success("Dashboard Loaded Successfully")