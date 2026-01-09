# Resume Ranker

AI-powered Resume Ranker is a full-stack machine learning application that evaluates how well a resume matches a job description. It calculates a match score, extracts technical skills, identifies missing skills, and provides personalized learning recommendations — all in an interactive web interface.

Built by **Jashan Jindal** as a practical demonstration of NLP, embeddings, and full-stack AI engineering.

---

## 🎯 Features

- Upload resume in PDF format  
- Paste a job description  
- Compute semantic match score (0–100)  
- Extract matched skills  
- Identify missing skills  
- Provide learning recommendations  

---

## 🧠 How It Works

1. Resume PDF is parsed into text.  
2. A pretrained sentence embedding model converts resume and job description into vectors.  
3. Cosine similarity is used to compute a semantic match score.  
4. A hybrid keyword + semantic approach extracts technical skills.  
5. Missing skills are mapped to personalized learning recommendations.

---

## 🛠 Tech Stack

| Layer | Technology |
|------|------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| NLP | Sentence Transformers (MiniLM) |
| Similarity | Cosine Similarity |
| PDF Parsing | pdfplumber |

---

## 📁 Project Structure
Resume_Ranker/
├── backend/
│ ├── main.py
│ ├── model.py
│ ├── parser.py
│ ├── skills.py
│ └── recommendations.py
├── frontend/
│ └── app.py
├── requirements.txt
└── README.md


---


## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Jashanjindal/Resume_Ranker.git
cd Resume_Ranker
```

### (Optional but recommended) Create virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run Locally

### Start Backend (FastAPI)

```bash
cd backend
uvicorn main:app --reload
```

Backend runs at:
http://127.0.0.1:8000/docs

---

### Start Frontend (Streamlit)

Open a **new terminal**:

```bash
cd frontend
streamlit run app.py
```

---

## 🧪 Example

**Input:**
```
Machine Learning Engineer with Python, SQL, and NLP
```

**Output:**
```
Match Score: 74 / 100
Matched Skills: Python, ML
Missing Skills: SQL, NLP
```
<img width="1160" height="928" alt="image" src="https://github.com/user-attachments/assets/c986ee12-4bd1-47bd-aae7-0ff6e998f549" />

---

## 💡 Why This Project?

This project demonstrates:

- Practical NLP using embeddings
- End-to-end ML product development
- API + frontend integration
## 📌 Future Improvements

- User accounts and history tracking  
- Visual analytics dashboard  
- Cloud deployment  
- Model fine-tuning with user feedback  

---

## 👤 Author

**Jashan Jindal**  
AIML Student  

- GitHub: https://github.com/Jashanjindal
  
