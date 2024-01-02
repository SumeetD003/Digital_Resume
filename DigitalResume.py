from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "My Resume.pdf"
profile_pic = "assets\profile-pic.png"



# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sumeet Deshpande"
PAGE_ICON = ":wave:"
NAME = "Sumeet Deshpande"
DESCRIPTION = """
Student at Vellore Institute of Technology, Bhopal. AI and ML Enthusiast!
"""
EMAIL = "sumeetdeshpande003@gmail.com"
SOCIAL_MEDIA = {
    
    "LinkedIn": "https://www.linkedin.com/in/sumeet-deshpande-b33840227/",
    "GitHub": "https://github.com/SumeetD003",
     "LeetCode": "https://leetcode.com/SumeetDeshpande03/"
}
PROJECTS = {
    "🏆 GYM_ML:- A Digital Trainer which will help the user during the workout sessions and guide them": "https://github.com/SumeetD003/GYM.git",
    "🏆 Gesture Detection:- Detects Gestures and can form words using gestures in live feed": "https://github.com/SumeetD003/ProjectGD.git",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in Python and worked with various libraries like Scikit Learn, Pandas, Numpy
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Matplotlib, OpenCV), MySQL, Java, C
- 📚 Modeling: Logistic regression, linear regression, decision trees, Deep Learning
- 🗄️ Databases: MySQL, SQL, Oracle
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Machine Learning Engineer | Feynn Labs Ai**")
st.write("05/2023 - 08/2023")
st.write(
    """
- ► Designed an AI prototype for Restaurants and manage their billing system.
- ► Led a team of 5 Engineers to brainstorm potential marketing and sales improvements, and implemented Market Segmentation Analysis on various domains using PCA and K-Means.
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)
# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    




# ---  Accomplishments ---
st.write('\n')
st.subheader("Accomplishments")
st.write("---")
st.write(
    """
- ► First Runner-up in CodeHack2023 Hackathon.
- ► First Runner-up in National Debate Championship
- ► Acquired First Runner up in Survive Hunt Treasure, VIT Bhopal University 
"""

    )


