import streamlit as st

st.set_page_config(page_title="CosmicMirror.ai", page_icon="🌌", layout="centered")

st.title("🌌 CosmicMirror.ai")
st.subheader("The Universal Digital Twin & File Conversion Marketplace")

st.write("Unlock Pro for $2 and access unlimited features! (NFTs, File Chat, Voice AI, and more)")

stripe_checkout_url = "https://buy.stripe.com/test_1234567890abcdefg"  # Replace with your LIVE Stripe link

if "pro" not in st.session_state:
    st.session_state.pro = False

if not st.session_state.pro:
    if st.button("🔓 Upgrade to Cosmic Pro ($2 Lifetime!)"):
        st.markdown(f"[**Pay $2 and Unlock Pro**]({stripe_checkout_url})", unsafe_allow_html=True)
        st.info("After payment, return here and click below to unlock Pro features!")
    if st.button("✅ I have paid - Unlock Pro!"):
        st.session_state.pro = True
        st.success("Pro unlocked! Enjoy all features.")
else:
    st.success("🌟 You are a Cosmic Pro! All features are now enabled.")
    st.write("🎉 Start using NFT, File Conversion, Voice AI, and more. (Add your features here!)")
