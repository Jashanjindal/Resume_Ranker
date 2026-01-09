from fastapi import FastAPI, UploadFile, File, Form
from parser import extract_text_from_pdf
from model import compute_similarity, extract_skills, recommend_learning, semantic_skill_match

app = FastAPI(title="AI Resume Ranker")

@app.post("/analyze")
async def analyze(resume: UploadFile = File(...), jd: str = Form(...)):
    
    resume_text = extract_text_from_pdf(resume.file)

    
    score = compute_similarity(resume_text, jd)

    
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd)

    
    if not jd_skills:
        jd_skills = semantic_skill_match(jd)

    
    matched = [s for s in jd_skills if s in resume_skills]
    missing = [s for s in jd_skills if s not in resume_skills]

    
    recs = recommend_learning(missing)

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "recommendations": recs
    }
