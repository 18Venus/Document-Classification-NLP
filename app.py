from flask import Flask, request, render_template
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
        pred_num = model.predict(text_vector)[0]   # numeric (0–4)
        prediction = label_encoder.inverse_transform([pred_num])[0].title()  # category string
        print("DEBUG: Prediction =", prediction)  # log to terminal

    return render_template("index.html",
                           prediction=prediction,
                           input_text=input_text)

if __name__ == "__main__":
    app.run(debug=True)
