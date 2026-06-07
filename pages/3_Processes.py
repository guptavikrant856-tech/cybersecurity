import streamlit as st
import subprocess
import platform

st.title("⚙️ Running Processes")

if platform.system() != "Windows":
    st.warning("Process listing only works on Windows.")
else:

    if st.button("Show Processes"):

        try:

            result = subprocess.check_output(
                "tasklist",
                shell=True
            ).decode(errors="ignore")

            st.text(result)

        except Exception as e:
            st.error(str(e))