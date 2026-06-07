import streamlit as st
import socket

st.title("🔍 Port Scanner")

host = st.text_input("Target Host", "scanme.nmap.org")

start_port = st.number_input(
    "Start Port",
    min_value=1,
    max_value=65535,
    value=1
)

end_port = st.number_input(
    "End Port",
    min_value=1,
    max_value=65535,
    value=100
)

if st.button("Scan"):

    results = []

    with st.spinner("Scanning..."):

        for port in range(start_port, end_port + 1):

            try:
                s = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                )

                s.settimeout(0.5)

                result = s.connect_ex((host, port))

                if result == 0:
                    results.append(
                        f"❌ Port {port} OPEN"
                    )

                s.close()

            except:
                pass

    if results:
        st.success(
            f"{len(results)} open ports found"
        )

        st.text("\n".join(results))

    else:
        st.success(
            "No open ports found"
        )
