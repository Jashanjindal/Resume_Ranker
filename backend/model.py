from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from recommendations import RECOMMENDATIONS

def recommend_learning(missing_skills):
    recs = {}
    for skill in missing_skills:
        if skill in RECOMMENDATIONS:
            recs[skill] = RECOMMENDATIONS[skill]
    return recs

_model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(text1: str, text2: str) -> float:
    emb1 = _model.encode([text1])
    emb2 = _model.encode([text2])
    score = cosine_similarity(emb1, emb2)[0][0]
    return round(float(score) * 100, 1)
from skills import SKILLS

def extract_skills(text):
    found = []
    for skill in SKILLS:
        if skill.lower() in text.lower():
            found.append(skill)
    return found
from skills import SKILLS

def extract_skills(text):
    text = text.lower()
    found = []

    for skill, keywords in SKILLS.items():
        for kw in keywords:
            if kw in text:
                found.append(skill)
                break

    return found
def semantic_skill_match(jd_text):
    skills = list(SKILLS.keys())
    emb_skills = _model.encode(skills)
    emb_jd = _model.encode([jd_text])

    sims = cosine_similarity(emb_jd, emb_skills)[0]
    return [skills[i] for i, s in enumerate(sims) if s > 0.4]

