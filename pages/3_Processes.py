import streamlit as st
import subprocess
import platform

st.title("⚙️ Running Processes")

try:
    if platform.system() == "Windows":

        result = subprocess.check_output(
            "tasklist",
            shell=True
        ).decode(errors="ignore")

    else:

        result = subprocess.check_output(
            ["ps", "aux"],
            text=True
        )

    st.text(result)

except Exception as e:
    st.error(str(e))
