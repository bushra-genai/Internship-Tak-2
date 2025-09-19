import streamlit as st
import spacy
from spacy import displacy

# Page Config
# ---------------------------
st.set_page_config(
    page_title="Customer Query Entity Extractor",
    page_icon="🔍",
    layout="centered"
)

# Custom CSS for Styling
# ---------------------------
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: #fafafa;
        }
        .stTextArea textarea {
            background-color: #1e2130 !important;
            color: #ffffff !important;
            border-radius: 10px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            font-weight: bold;
            padding: 0.5em 1em;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #357ABD;
            transform: scale(1.05);
        }
        .entity {
            display: inline-block;
            padding: 0.25em 0.35em;
            margin: 0 0.25em;
            border-radius: 0.25em;
            background: #357ABD;
            color: white;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)


# Load SpaCy Model (cache for speed)
# ---------------------------
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()


# App Title
# ---------------------------
st.markdown("<h1 style='text-align:center; color:#FF5733;'>🔍 Named Entity Recognition (NER)</h1>", unsafe_allow_html=True)
st.write("This app extracts **key information** (like product names, dates, organizations) from customer queries using SpaCy.")


# User Input
# ---------------------------
st.subheader("Enter your customer query 👇")
user_input = st.text_area("Example: Do you have the iPhone 15 in stock?", height=120)

if st.button("⚡ Extract Entities"):
    if user_input.strip():
        doc = nlp(user_input)

        if doc.ents:
            st.success("✅ Entities Extracted Successfully!")
            for ent in doc.ents:
                st.markdown(f"<span class='entity'>{ent.text} → {ent.label_}</span>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ No entities found. Try another text.")
    else:
        st.error("Please enter a query first!")
# Footer
# ---------------------------
st.markdown("""
    <hr style="border:1px solid #ddd;">
    <div style="text-align: center; color: white; font-size: 14px;">
        🚀 Developed by <b>Bushra Mubeen</b>
    </div>
""", unsafe_allow_html=True)
