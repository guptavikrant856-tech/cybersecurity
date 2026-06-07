import streamlit as st
import platform
import subprocess

st.title("🛡️ Firewall Status")

try:
    system = platform.system()

    if system == "Windows":
        result = subprocess.run(
            ["netsh", "advfirewall", "show", "allprofiles"],
            capture_output=True,
            text=True
        )
        st.code(result.stdout)

    elif system == "Linux":
        try:
            result = subprocess.run(
                ["ufw", "status"],
                capture_output=True,
                text=True
            )
            st.code(result.stdout)
        except:
            st.warning("UFW not installed on this server.")

    else:
        st.info(f"Firewall check not implemented for {system}")

except Exception as e:
    st.error(str(e))
