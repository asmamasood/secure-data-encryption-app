import streamlit as st
from crypto_util import generate_key, load_key, encrypt_note, decrypt_note

st.set_page_config(page_title="🔐 Secure Notes Vault")

st.title("🔐 Secure Notes Vault")

menu = st.sidebar.selectbox("Choose Action", ["Generate Key", "Encrypt Note", "Decrypt Note"])

# Step 1: Generate Key
if menu == "Generate Key":
    if st.button("Generate Secret Key"):
        generate_key()
        st.success("✅ secret.key generated and saved!")

# Step 2: Encrypt Note
elif menu == "Encrypt Note":
    note = st.text_area("Write your secret note below:")
    if st.button("Encrypt"):
        key = load_key()
        if key:
            encrypted = encrypt_note(note, key)
            st.text_area("🔒 Encrypted Note", encrypted)
            st.download_button("💾 Download Encrypted Note", encrypted, file_name="encrypted_note.txt")
        else:
            st.error("❌ secret.key not found. Please generate the key first.")

# Step 3: Decrypt Note
elif menu == "Decrypt Note":
    encrypted_note = st.text_area("Paste your encrypted note:")
    if st.button("Decrypt"):
        key = load_key()
        if key:
            try:
                decrypted = decrypt_note(encrypted_note, key)
                st.text_area("🔓 Decrypted Note", decrypted)
            except:
                st.error("❌ Invalid encrypted text or key.")
        else:
            st.error("❌ secret.key not found. Please generate the key first.")
