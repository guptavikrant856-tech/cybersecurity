import streamlit as st
import socket

st.title("🔍 Port Scanner")

host = st.text_input("Target Host", "127.0.0.1")

if st.button("Scan Ports"):

    results = []

    with st.spinner("Scanning..."):

        for port in range(1, 101):

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)

            result = s.connect_ex((host, port))

            if result == 0:
                results.append(f"❌ Port {port} OPEN")
            else:
                results.append(f"✅ Port {port} CLOSED")

            s.close()

    st.text("\n".join(results))
