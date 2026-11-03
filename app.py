from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ART VISION — Custom Applied AI Diploma",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome and make the page fill the whole window
st.markdown(
    """
    <style>
      #MainMenu, header, footer, [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display: none !important;}
      .block-container, [data-testid="stMainBlockContainer"] {padding: 0 !important; max-width: 100% !important;}
      .stMain, [data-testid="stMain"], [data-testid="stVerticalBlock"] {padding-top: 0 !important; gap: 0 !important;}
      [data-testid="stElementContainer"]:has(style) {display: none !important;}
      [data-testid="stAppViewContainer"], .stApp {background: #2a0f14;}
      iframe {height: 100vh !important; width: 100% !important; border: 0; display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=1000, scrolling=True)
