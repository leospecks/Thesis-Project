# run with: 
# streamlit run "6_frontend/streamlit_app.py"
# CTRL S in VS code to save and then R in the browser to rerun

import streamlit as st
from pathlib import Path
from datetime import datetime


st.set_page_config(page_title="Thesis Dashboard", layout="wide")

st.title("Thesis Dashboard")
st.text("Can Machine Learning Variable Selection and Individual Commodity Fundamentals Improve Futures Return Forecasting?")
st.link_button("🔗 Github repository", "https://github.com/leospecks/Thesis-Project")

st.header("Current Draft")

pdf_path = Path("1_latex/build/main.pdf")

if pdf_path.exists():
    today = datetime.now().strftime("%Y-%m-%d")  # e.g. 2026-04-18
    filename = f"thesis_leospecks_{today}.pdf"
    with open(pdf_path, "rb") as f:
        st.download_button(
            label="⬇️ Download PDF",
            data=f,
            file_name= filename,
            mime="application/pdf"
        )
    #st.pdf(str(pdf_path), height=500)
else:
    st.error(f"PDF not found: {pdf_path.resolve()}")


st.header("Presentation")
pdf_path2 = Path("7_docs/defence_presentation.pdf")

if pdf_path2.exists():
    today = datetime.now().strftime("%Y-%m-%d")  # e.g. 2026-04-18
    filename = f"presentation_leospecks_{today}.pdf"
    with open(pdf_path2, "rb") as f:
        st.download_button(
            label="⬇️ Download PDF",
            data=f,
            file_name= filename,
            mime="application/pdf"
        )
    #st.pdf(str(pdf_path2), height=500)
else:
    st.error(f"PDF not found: {pdf_path2.resolve()}")