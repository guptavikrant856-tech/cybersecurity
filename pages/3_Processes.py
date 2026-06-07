import streamlit as st
import psutil

st.title("⚙️ Running Processes")

try:
    processes = []

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            processes.append(
                f"PID: {proc.info['pid']} | {proc.info['name']}"
            )
        except:
            pass

    st.text("\n".join(processes[:500]))

except Exception as e:
    st.error(str(e))
