import streamlit as st
import socket
import platform

st.title("🛡️ Firewall Status")

st.write(f"Platform: {platform.system()}")
st.write(f"Hostname: {socket.gethostname()}")

st.success(
    "Application is running behind the hosting provider's network controls."
)
