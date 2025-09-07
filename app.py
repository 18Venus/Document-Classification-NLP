from flask import Flask, request, render_template
import os
import joblib
from werkzeug.utils import secure_filename
import PyPDF2
import docx
import re

try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    nlp = None
    print("⚠️ spaCy model not loaded, preprocessing disabled:", e)

model = joblib.load("svm_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def preprocess_text(text: str) -> str:
    """
    Preprocess text:
    - Lowercase
    - Remove punctuation/numbers
    - Lemmatize
    - Remove stopwords
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)

    if nlp:  
        doc = nlp(text)
        tokens = [
            token.lemma_
            for token in doc
            if not token.is_stop and token.lemma_.strip() != ''
        ]
        return " ".join(tokens)
    else:
        return text  

def extract_text_from_file(filepath):
    text = ""
    if filepath.endswith(".txt"):
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    elif filepath.endswith(".pdf"):
        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
    elif filepath.endswith(".docx"):
        doc = docx.Document(filepath)
        text = " ".join([p.text for p in doc.paragraphs])
    return text.strip()

@app.route("/")
def home():
    return render_template("index.html", prediction=None, input_text=None)

@app.route("/predict", methods=["POST"])
def predict_text():
    input_text = request.form.get("news_text")
    prediction = None
    if input_text and input_text.strip():
        cleaned_text = preprocess_text(input_text)
        text_vector = vectorizer.transform([cleaned_text])
        pred_num = model.predict(text_vector)[0]
        prediction = label_encoder.inverse_transform([pred_num])[0].title()
    return render_template("index.html", prediction=prediction, input_text=input_text)

@app.route("/predict_file", methods=["POST"])
def predict_file():
    file = request.files["file"]
    if not file:
        return render_template("index.html", prediction="⚠️ No file uploaded")

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    # Extract text
    input_text = extract_text_from_file(filepath)
    if not input_text:
        return render_template("index.html", prediction="⚠️ Could not extract text")

    # Preprocess + predict
    cleaned_text = preprocess_text(input_text)
    text_vector = vectorizer.transform([cleaned_text])
    pred_num = model.predict(text_vector)[0]
    prediction = label_encoder.inverse_transform([pred_num])[0].title()

    return render_template("index.html", prediction=prediction, input_text=input_text[:500] + "...")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True)
