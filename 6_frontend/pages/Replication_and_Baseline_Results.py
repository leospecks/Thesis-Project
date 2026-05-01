import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Data", layout="wide")

st.title("Replication and Baseline Results")

video_path = Path("6_frontend/animations/media/videos/simple_scene/1080p60/HelloScene.mp4")
st.video(str(video_path), autoplay=False, loop=False, width=800)