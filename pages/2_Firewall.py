import streamlit as st
import subprocess
import platform

st.title("🛡️ Firewall Status")

if platform.system() != "Windows":
    st.warning("Firewall check only works on Windows.")
else:

    if st.button("Check Firewall"):

        try:

            result = subprocess.run(
                ["netsh", "advfirewall", "show", "allprofiles"],
                capture_output=True,
                text=True
            )

            output = result.stdout

            st.code(output)

        except Exception as e:
            st.error(str(e))