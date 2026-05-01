import streamlit as st
from pathlib import Path
import subprocess
import time

st.set_page_config(page_title="Animation", layout="wide")

st.title("Animation Generator")

commodity = st.selectbox("Commodity", ["Gold", "Oil", "Wheat"])
model = st.selectbox("Model", ["LASSO", "Elastic Net"])
period = st.selectbox("Period", ["2004-2012", "2013-2024"])

if st.button("Generate animation"):
    cmd = [
        "manim",
        "-pql",
        "frontend/animations/dynamic_scene.py",
        "DynamicScene",
        "--media_dir",
        "media",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        video_path = Path("media/videos/dynamic_scene/480p15/DynamicScene.mp4")
        if video_path.exists():
            st.video(str(video_path))
        else:
            st.error("Video rendered, but file not found.")
    else:
        st.error("Rendering failed.")
        st.code(result.stderr)