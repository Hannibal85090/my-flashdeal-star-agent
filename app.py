import streamlit as st
from core.security import SovereignSecurity
from services.live_market import LiveMarketService

st.set_page_config(page_title="My FlashDeal Star Portal", page_icon="⭐", layout="centered")

st.markdown("""
    <style>
    .reportview-container { background: linear-gradient(135deg, #0d0d1a 0%, #05050a 100%); }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.07);
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    .neon-text { color: #00f3ff; text-shadow: 0 0 10px #00f3ff; text-align: center; font-weight: bold; }
    .slogan { color: #ff007f; text-shadow: 0 0 8px #ff007f; font-size: 1.2rem; text-align: center; letter-spacing: 2px; }
    </style>
""", unsafe_allowed_html=True)

st.markdown("<h1 class='neon-text'>MY FLASHDEAL STAR</h1>", unsafe_allowed_html=True)
st.markdown("<p class='slogan'>TALK. PAY. DONE.</p>", unsafe_allowed_html=True)

st.markdown("<div class='glass-card'>", unsafe_allowed_html=True)
st.subheader("🔒 Sovereign Authentication Layer")
col1, col2 = st.columns(2)
with col1:
    user_token = st.text_input("Mutual Token Seed", type="password", value="STAR_TOKEN_2026")
with col2:
    secure_code = st.text_input("Security PIN", type="password", max_chars=4, value="1234")

biometric_sync = st.checkbox("Enable Biometric Hand Gesture Sync / Face ID")
if biometric_sync:
    st.info(SovereignSecurity.simulate_biometrics(True))
st.markdown("</div>", unsafe_allowed_html=True)

st.markdown("<div class='glass-card'>", unsafe_allowed_html=True)
st.subheader("🌐 Real-Time Market Intelligence Context")
base_curr = st.selectbox("Anchor Base Currency", ["USD", "EUR", "TND", "SAR"])

if st.button("Fetch Market Rates via Bright Data API"):
    with st.spinner("Scraping and structures global web contexts live..."):
        market_service = LiveMarketService()
        market_data = market_service.fetch_exchange_context(base_curr)
        st.success(f"Successfully integrated live alternative market pipeline for {base_curr}!")
        st.json(market_data)
st.markdown("</div>", unsafe_allowed_html=True)

if st.button("EXECUTE SECURE TRANSACTION"):
    if SovereignSecurity.verify_credentials(user_token, secure_code):
        st.markdown("<div style='border: 2px solid #00f3ff; padding: 15px; border-radius: 10px; text-align: center; background: rgba(0,243,255,0.05);'>", unsafe_allowed_html=True)
        st.balloons()
        st.subheader("🚀 Sovereign Agent Transaction Dispatched")
        st.write("Ecosystem Status: **Transaction completed flawlessly. Talk. Pay. Done.**")
        st.markdown("</div>", unsafe_allowed_html=True)
    else:
        st.error("❌ Authentication Layer Blocked: Credentials Refused.")

