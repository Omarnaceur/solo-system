import streamlit as st
import google.generativeai as genai
import datetime

# 1. تهيئة بروتوكول النظام (إعدادات الصفحة)
st.set_page_config(
    page_title="SYSTEM: MONARCH INITIALIZATION",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ربط النواة (API Key) - السرعة القصوى
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # استخدام Flash للسرعة البرقية
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("🚨 Critical Error: System Core (API) missing.")
    st.stop()

# 3. التصميم البصري (Advanced Shadow UI)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Orbitron:wght@400;900&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #001a33 0%, #000000 100%);
        color: #00d4ff;
        font-family: 'Orbitron', sans-serif;
    }
    
    /* شاشة الحالة الراقية */
    .status-panel {
        border: 1px solid #00d4ff;
        background: rgba(0, 212, 255, 0.05);
        padding: 20px;
        border-radius: 2px;
        box-shadow: inset 0 0 20px rgba(0, 212, 255, 0.2), 0 0 15px rgba(0, 212, 255, 0.1);
        clip-path: polygon(0 0, 100% 0, 100% 90%, 95% 100%, 0 100%);
    }

    /* أزرار النظام */
    .stButton>button {
        background: transparent;
        color: #00d4ff;
        border: 1px solid #00d4ff;
        font-family: 'Syncopate', sans-serif;
        font-size: 12px;
        letter-spacing: 2px;
        transition: 0.4s all;
        text-transform: uppercase;
    }
    
    .stButton>button:hover {
        background: #00d4ff;
        color: black;
        box-shadow: 0 0 40px #00d4ff;
        border: 1px solid #00d4ff;
    }

    /* الرسائل */
    .system-msg {
        background: rgba(0, 0, 0, 0.8);
        border-left: 5px solid #00d4ff;
        padding: 15px;
        font-size: 14px;
        line-height: 1.6;
    }

    /* شريط المستوى */
    .stProgress > div > div > div > div {
        background-color: #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. محرك البيانات (System State)
if 'lvl' not in st.session_state: st.session_state.lvl = 1
if 'exp' not in st.session_state: st.session_state.exp = 0
if 'str' not in st.session_state: st.session_state.str = 10
if 'agi' not in st.session_state: st.session_state.agi = 10

def level_up_logic(points):
    st.session_state.exp += points
    if st.session_state.exp >= 100:
        st.session_state.lvl += 1
        st.session_state.exp = 0
        st.session_state.str += 2
        st.session_state.agi += 2
        st.balloons()
        return True
    return False

# --- الهيكل الرئيسي ---

# القائمة الجانبية: نافذة اللاعب
with st.sidebar:
    st.markdown(f"""
    <div class='status-panel'>
        <h2 style='color: #fff; margin:0;'>PLAYER STATUS</h2>
        <hr style='border: 0.5px solid #00d4ff;'>
        <p style='font-size: 12px;'>TITLE: <b>SHADOW MONARCH</b></p>
        <p style='font-size: 24px; color:#00d4
