from fastapi import FastAPI, UploadFile, File, Form
from parser import extract_text_from_pdf
from model import compute_similarity, extract_skills, recommend_learning, semantic_skill_match

app = FastAPI(title="AI Resume Ranker")

@app.post("/analyze")
async def analyze(resume: UploadFile = File(...), jd: str = Form(...)):
    # Extract resume text
    resume_text = extract_text_from_pdf(resume.file)

    # Compute similarity score
    score = compute_similarity(resume_text, jd)

    # Extract skills
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd)

    # Fallback to semantic matching if JD skills empty
    if not jd_skills:
        jd_skills = semantic_skill_match(jd)

    # Compute matched and missing
    matched = [s for s in jd_skills if s in resume_skills]
    missing = [s for s in jd_skills if s not in resume_skills]

    # Learning recommendations
    recs = recommend_learning(missing)

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "recommendations": recs
    }
