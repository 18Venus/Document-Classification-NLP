# 📑 Document Classification with NLP

This project is an **NLP-based Document Classifier** that predicts categories of text documents such as **Business, Politics, Tech, Sports, and Entertainment**.  
It uses the **BBC News Dataset** for training and is deployed as a **Flask web app** (with options to paste text or upload a file: `.txt`, `.pdf`, `.docx`).  

🚀 Live Demo: [Render App Link](https://document-classification-bbc-news.onrender.com)

---

## 📂 Dataset

- **Source**: [BBC News Classification Dataset](https://www.kaggle.com/datasets/alfathterry/bbc-full-text-document-classification)  
- **Size**: ~2225 documents  
- **Categories**:  
  - Business  
  - Politics  
  - Tech  
  - Sports  
  - Entertainment  

---

## ⚙️ Features

✅ Text preprocessing (lowercasing, punctuation removal, stopword removal, lemmatization using **spaCy**)  
✅ Machine Learning models tested: Naive Bayes, Logistic Regression, Random Forest, SVM  
✅ Best performing model: **Linear SVM (~98% accuracy)**  
✅ Supports classification of **raw text or uploaded documents (TXT, PDF, DOCX)**  
✅ Flask-based web application with **user-friendly interface**  
✅ Deployed on **Render**  

---

## 📊 Model Performance

| Model               | Accuracy |
|----------------------|----------|
| Naive Bayes         | ~92%     |
| Logistic Regression | ~95%     |
| Random Forest       | ~96%     |
| **Linear SVM**      | **98%**  |

---

## 🖼️ Screenshots

### 🔹 Prediction Example

#### Example Video Link : [DemoLink]([https://your-app.onrender.com](https://drive.google.com/file/d/1sot7VUcI73UHdt5hpfAXIbhPeT4aVOKk/view?usp=sharing)) 

<img width="905" height="558" alt="Doc1" src="https://github.com/user-attachments/assets/0588e0e5-fc70-47d6-86fb-70a7b15e8e9e" />
<img width="935" height="560" alt="Doc2" src="https://github.com/user-attachments/assets/f78803fc-ede8-496a-b51e-a6eae45db85a" />
<img width="946" height="548" alt="Doc3" src="https://github.com/user-attachments/assets/72108dea-ace8-41b5-b904-419a08def7f3" />
<img width="973" height="563" alt="Doc4" src="https://github.com/user-attachments/assets/dc74f1b0-0bb3-4c17-95c0-ae48a82517b1" />
<img width="916" height="549" alt="Doc5" src="https://github.com/user-attachments/assets/fedb3dee-2c1f-46b4-aede-77136071ad2d" />

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Flask**
- **scikit-learn**
- **spaCy**
- **joblib**
- **PyPDF2 / python-docx**
- **HTML + CSS (custom styling)**

---

## 🚀 How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/18Venus/Document-Classification-NLP.git
   cd Document-Classification-NLP
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Run the Flask app:
    ```bash
    python app.py
4. Open in browser: http://127.0.0.1:5000

