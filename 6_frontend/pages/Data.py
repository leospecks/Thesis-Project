import streamlit as st
import pandas as pd
from pathlib import Path
from numpy.random import default_rng as rng

st.set_page_config(page_title="Data", layout="wide")

st.title("Data")

st.header("Raw Data")

df = pd.DataFrame(
    {
        "series": ["Roadmap", "Extras", "Issues"],
        "source": ["na", "na", "na"],
        "status": ["✅ Downloaded", "❌ Missing", "⚠️ Not Final"],
        "stars": rng(0).integers(0, 1000, size=3),
        "url": [
            "https://roadmap.streamlit.app",
            "https://extras.streamlit.app",
            "https://issues.streamlit.app",
        ],
        "views_history": rng(0).integers(0, 5000, size=(3, 30)).tolist(),
    }
)

st.dataframe(
    df,
    column_config={
        "series": "Series",
        "source": "Data Provider",
        "status": "Status",
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

st.header("Combined Dataframe")
df_path = Path("1_latex/build/main.pdf")
if df_path.exists():
    with open(df_path, "rb") as f:
        st.download_button(
            label="⬇️ Download dataset",
            data=f,
            file_name="thesis.pdf",
            mime="application/pdf"
        )
else:
    st.error(f"PDF not found: {df_path.resolve()}")

st.header("Summary Statistics")