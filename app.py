import streamlit as st
from crypto_util import generate_key, encrypt_text, decrypt_text, load_key

st.set_page_config(page_title="🔐 Secure Data Encryption", layout="centered")

st.title("🔐 Secure Data Encryption App")
menu = st.selectbox("Select Option", ["Generate Key", "Encrypt", "Decrypt"])

if menu == "Generate Key":
    if st.button("Generate & Save Key"):
        key = generate_key()
        st.success("Key generated and saved as secret.key")

elif menu == "Encrypt":
    uploaded_key = st.file_uploader("Upload your secret.key", type=["key"])
    text = st.text_area("Enter the text to encrypt")
    
    if uploaded_key and text:
        key = uploaded_key.read()
        encrypted = encrypt_text(text, key)
        st.text_area("Encrypted Text", encrypted)

elif menu == "Decrypt":
    uploaded_key = st.file_uploader("Upload your secret.key", type=["key"])
    encrypted_text = st.text_area("Paste the encrypted text")
    
    if uploaded_key and encrypted_text:
        key = uploaded_key.read()
        try:
            decrypted = decrypt_text(encrypted_text, key)
            st.text_area("Decrypted Text", decrypted)
        except:
            st.error("Decryption failed! Check your key or input.")
