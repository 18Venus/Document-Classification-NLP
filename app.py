from flask import Flask, request, render_template
import os
import joblib

# Load model, vectorizer, and label encoder
model = joblib.load("svm_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", prediction=None, input_text="")

@app.route("/predict", methods=["POST"])
def predict():
    input_text = request.form.get("news_text")
    prediction = None

    if input_text and input_text.strip() != "":
        text_vector = vectorizer.transform([input_text])
        pred_num = model.predict(text_vector)[0]   
        prediction = label_encoder.inverse_transform([pred_num])[0].title()  
        print("DEBUG: Prediction =", prediction)  

    return render_template("index.html",
                           prediction=prediction,
                           input_text=input_text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port)
