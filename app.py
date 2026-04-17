import streamlit as st
import google.generativeai as genai
import time
from datetime import datetime

# --- إعدادات النظام العليا ---
st.set_page_config(page_title="SYSTEM: THE GREAT MONARCH", page_icon="🔗", layout="wide")

# --- محرك الربط العصبي (API Connection) ---
def initialize_system():
    if "GOOGLE_API_KEY" in st.secrets:
        try:
            genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
            return genai.GenerativeModel('gemini-1.5-flash')
        except Exception as e:
            st.error(f"SYSTEM FAILURE: {e}")
            return None
    return None

model = initialize_system()

# --- التصميم السينمائي (Ultra Cyberpunk UI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Share+Tech+Mono&display=swap');
    
    .stApp { background: #000; color: #00d4ff; font-family: 'Share Tech Mono', monospace; }
    
    /* نافذة الحالة الملكية */
    .status-window {
        border: 2px solid #00d4ff; background: rgba(0, 212, 255, 0.03);
        padding: 25px; border-radius: 0px; position: relative;
        box-shadow: inset 0 0 15px #00d4ff, 0 0 10px #00d4ff;
    }
    
    .status-window::after {
        content: "SYSTEM ACTIVE"; position: absolute; top: -10px; right: 10;
        background: #000; padding: 0 10px; font-size: 10px; color: #00d4ff;
    }

    /* أزرار النظام */
    .stButton>button {
        width: 100%; border: 1px solid #00d4ff; background: transparent;
        color: #00d4ff; font-family: 'Syncopate', sans-serif; height: 60px;
        transition: 0.3s; text-transform: uppercase; letter-spacing: 5px;
    }
    .stButton>button:hover { background: #00d4ff; color: #000; box-shadow: 0 0 50px #00d4ff; }

    /* تحليل البيانات */
    .analysis-box {
        background: rgba(255, 255, 255, 0.05); border-left: 10px solid #00d4ff;
        padding: 20px; font-size: 18px; color: #fff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- محرك الحالة (Persistence Engine) ---
if 'player_lvl' not in st.session_state: st.session_state.player_lvl = 1
if 'player_exp' not in st.session_state: st.session_state.player_exp = 0
if 'stats' not in st.session_state:
    st.session_state.stats = {"STR": 15, "AGI": 12, "INT": 20, "VIT": 15}

def update_exp(gain):
    st.session_state.player_exp += gain
    if st.session_state.player_exp >= 100:
        st.session_state.player_lvl += 1
        st.session_state.player_exp = 0
        for s in st.session_state.stats: st.session_state.stats[s] += 5
        st.balloons()

# --- الواجهة (The Interface) ---
st.markdown("<h1 style='text-align:center; font-family:Syncopate;'>● THE SYSTEM INTERFACE ●</h1>", unsafe_allow_html=True)

left_col, right_col = st.columns([1, 2])

with left_col:
    st.markdown(f"""
    <div class='status-window'>
        <p style='margin:0; font-size:12px; color:rgba(0,212,255,0.5);'>PLAYER PROFILE</p>
        <h2 style='margin:0; color:#fff;'>MONARCH</h2>
        <p style='font-size:30px; margin:0;'>LVL. {st.session_state.player_lvl}</p>
        <hr style='border: 0.1px solid #00d4ff;'>
        <p>STR: {st.session_state.stats['STR']} | AGI: {st.session_state.stats['AGI']}</p>
        <p>INT: {st.session_state.stats['INT']} | VIT: {st.session_state.stats['VIT']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(f"EXP: {st.session_state.player_exp}/100")
    st.progress(st.session_state.player_exp / 100)
    
    if st.button("DAILY QUEST: RECOVER"):
        update_exp(50)
        st.toast("XP RECEIVED. BODY RECOVERED.")

with right_col:
    st.subheader("⚡ VOID SCANNER")
    target = st.text_input("INPUT TARGET (FOOD/EXERCISE):", placeholder="Scanning for targets...")
    
    if st.button("EXECUTE ANALYSIS"):
        if target and model:
            with st.spinner("SCANNING TARGET..."):
                try:
                    # برومبت مصمم لردود قوية جداً
                    prompt = f"System Scan for '{target}'. Output details: Calories, Rank, and a harsh Monarch's verdict. Arabic. Cyberpunk format."
                    response = model.generate_content(prompt)
                    update_exp(20)
                    st.markdown(f"<div class='analysis-box'>{response.text}</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"SCAN FAILED: {e}")
        else:
            st.warning("SYSTEM ALERT: No target detected or API Key missing.")

# --- التذييل ---
st.markdown("---")
st.markdown(f"<p style='text-align:center; font-size:10px;'>SYNC TIME: {datetime.now().strftime('%H:%M:%S')} | GATE STATUS: STABLE</p>", unsafe_allow_html=True)
