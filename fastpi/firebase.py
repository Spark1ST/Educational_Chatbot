import firebase_admin
from firebase_admin import credentials, firestore, auth
import streamlit as st
import json
def initialize_firebase():
    if not firebase_admin._apps:
        firebase_key_str = st.secrets["firebase"]["firebase_admin_key"]
        
        # Parse the JSON string to a dictionary
        try:
            firebase_key_dict = json.loads(firebase_key_str)
        except json.JSONDecodeError as e:
            st.error(f"Failed to parse Firebase key. Check its format: {e}")
            st.stop()
        cred = credentials.Certificate(cred_dict)
        
        # Initialize Firebase
        firebase_admin.initialize_app(cred)
    
    return {
        'auth': auth,
        'db': firestore.client()
    }

# Usage
firebase = initialize_firebase()
