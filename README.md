# 🔎 Named Entity Recognition (NER) App

This project is part of my internship tasks, where I built a **Named Entity Recognition (NER) application** using **SpaCy** and **Streamlit**.  
The app extracts key information (like product names, dates, locations, and organizations) from customer queries in real-time.  

---

## 🚀 Features
- 📝 **Customer Query Input** – Type any sentence or query.  
- 🧠 **NER Extraction** – Automatically identifies and highlights entities like:
  - Dates (e.g., "December 2025")  
  - Locations (e.g., "Dubai")  
  - Organizations  
  - Numbers and Ordinals  
- 🎨 **User-Friendly Interface** – Clean and interactive frontend built with **Streamlit**.  
- ✅ **Instant Results** – Extracted entities displayed with clear labels.  
- ✨ Footer credit: *Developed by Bushra Mubeen*  

---

## 🛠️ Tech Stack
- **Python**  
- **SpaCy** – for NLP & Named Entity Recognition  
- **Streamlit** – for building the frontend interface  

---

## 📂 Project Structure


NER-App/
│── app.py # Main Streamlit app
│── requirements.txt # Dependencies
│── README.md # Documentation


---

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ner-app.git
cd ner-app

2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

3. Install dependencies
pip install -r requirements.txt

4. Download SpaCy model
python -m spacy download en_core_web_sm

5. Run the app
streamlit run app.py

🎯 Example

Input Query:

I will visit Dubai in December 2025. The meeting is scheduled on 15th September 2025


Output Entities:

Dubai → GPE

December 2025 → DATE

15th → ORDINAL

September 2025 → DATE
Future Enhancements

Add support for multiple languages

Extend entity types with custom NER models

Export results as CSV/JSON

✍️ Author

💡 Developed by Bushra Mubeen
