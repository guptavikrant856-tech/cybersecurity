import streamlit as st

st.set_page_config(
    page_title="Cyber Security Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Cyber Security Dashboard")

st.markdown("""
### Available Tools

- 🔍 Port Scanner
- 🛡️ Firewall Status
- ⚙️ Running Processes

Use the sidebar to navigate.
""")

st.info(
    "When deployed publicly, results reflect the server running the application."
)
