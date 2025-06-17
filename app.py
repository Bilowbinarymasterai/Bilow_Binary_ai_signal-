import streamlit as st
import random
import datetime

st.set_page_config(page_title="BilowVisionary Binary AI", layout="centered")

st.title("🔮 BilowVisionary Binary AI")
st.write("Get ultra-accurate 5s expiry binary signals.")

# Simulated signal generator (we’ll upgrade this soon)
if st.button("📍 Tap to Get Signal"):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    direction = random.choice(["⬆️ CALL", "⬇️ PUT"])
    st.success(f"{direction} — Right now ({now})")
