import streamlit as st
import requests

st.set_page_config(page_title="Resume Ranker", layout="centered")

st.title("AI Resume Ranker")

resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume and jd:
        files = {"resume": resume}
        data = {"jd": jd}

        res = requests.post(
            "http://127.0.0.1:8000/analyze",
            files=files,
            data=data
        )

        result = res.json()

        st.success(f"Match Score: {result['match_score']} / 100")

        st.write("### Matched Skills")
        st.write(result.get("matched_skills", []))

        st.write("### Missing Skills")
        st.write(result.get("missing_skills", []))

        st.write("### What You Should Learn")

        recs = result.get("recommendations", {})
        jd_skills = result.get("matched_skills", []) + result.get("missing_skills", [])

        if recs:
            for skill, advice in recs.items():
                st.markdown(f"- **{skill}**: {advice}")
        elif jd_skills:
            st.write("You're well aligned with this role 🎉")
        else:
            st.write("We couldn't extract explicit skills — try using a more detailed job description.")

    else:
        st.warning("Please upload a resume and paste a job description.")
