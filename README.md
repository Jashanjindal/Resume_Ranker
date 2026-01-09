# AI Resume Ranker

AI Resume Ranker is a full-stack machine learning application that analyzes how well a resume matches a given job description. It uses natural language processing and semantic similarity to compute a match score, extract relevant skills, identify skill gaps, and suggest what the candidate should learn to better fit the role.

The goal of this project is to demonstrate how AI can be used to support hiring decisions and help candidates understand where they stand and how to improve.

---

## 🚀 Features

- Upload resume as PDF
- Paste job description text
- Compute semantic match score (0–100)
- Extract technical skills from both resume and job description
- Identify matched and missing skills
- Provide personalized learning recommendations
- Clean and interactive web UI

---

## 🧠 How It Works

1. Resume PDF is parsed into raw text.
2. A pretrained sentence embedding model converts resume and job description into vectors.
3. Cosine similarity is used to compute a semantic match score.
4. A hybrid skill extractor (keyword + semantic fallback) detects technical skills.
5. Missing skills are mapped to learning recommendations.

---

## 🛠 Tech Stack

- **Language:** Python
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **ML/NLP:** Sentence Transformers (MiniLM), scikit-learn
- **PDF Parsing:** pdfplumber
- **Similarity:** Cosine similarity
- **Deployment:** Local / Streamlit Cloud / Render (optional)

---

## 📸 Demo

<img width="1627" height="983" alt="image" src="https://github.com/user-attachments/assets/f12af72a-fc4f-4bd9-9d07-47456f4df1bc" />
<img width="1627" height="983" alt="image" src="https://github.com/user-attachments/assets/f12af72a-fc4f-4bd9-9d07-47456f4df1bc" />

<img width="1627" height="983" alt="Screenshot 2026-01-10 012849" src="https://github.com/user-attachments/assets/ee4b31bd-0971-41fa-9766-5bee54f64a6b" />
<img width="1627" height="983" alt="Screenshot 2026-01-10 012849" src="https://github.com/user-attachments/assets/ee4b31bd-0971-41fa-9766-5bee54f64a6b" />

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/ai-resume-ranker.git
cd ai-resume-ranker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
