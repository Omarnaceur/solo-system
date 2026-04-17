import streamlit as st
import google.generativeai as genai
import time
from datetime import datetime

# 1. إعدادات البروتوكول العالي
st.set_page_config(page_title="SYSTEM: MONARCH INITIALIZATION", page_icon="⚡", layout="wide")

# 2. ربط النواة (API Key) بأقصى سرعة
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("🚨 CRITICAL ERROR: API KEY NOT FOUND IN SECRETS.")
    st.stop()

# 3. محرك التصوير (Ultimate UI System)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Recursive:wght@300;800&display=swap');
    
    .stApp { background: #000000; color: #00d4ff; font-family: 'Orbitron', sans-serif; }
    
    /* شاشة الحالة (Status Plate) */
    .status-card {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(0, 0, 0, 0.9));
        border: 1px solid #00d4ff; padding: 20px; border-radius: 2px;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
        position: relative; overflow: hidden;
    }
    .status-card::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 2px;
        background: linear-gradient(90deg, transparent, #00d4ff, transparent);
        animation: scan 3s linear infinite;
    }
    @keyframes scan { 0% { left: -100%; } 100% { left: 100%; } }

    /* أزرار الطاقة */
    .stButton>button {
        width: 100%; background: #000; color: #00d4ff; border: 1px solid #00d4ff;
        font-weight: 900; letter-spacing: 3px; height: 55px; transition: 0.4s;
    }
    .stButton>button:hover { background: #00d4ff; color: #000; box-shadow: 0 0 40px #00d4ff; }
    
    /* الردود البرمجية */
    .system-response {
        background: #001a33; border-left: 5px solid #00d4ff; padding: 15px;
        margin-top: 20px; font-family: 'Recursive', sans-serif; font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. محرك البيانات (System State)
if 'lvl' not in st.session_state: st.session_state.lvl = 1
if 'exp' not in st.session_state: st.session_state.exp = 0
if 'stats' not in st.session_state:
    st.session_state.stats = {"STR": 10, "AGI": 10, "INT": 12, "VIT": 10}

def gain_exp(amount):
    st.session_state.exp += amount
    if st.session_state.exp >= 100:
        st.session_state.lvl += 1
        st.session_state.exp = 0
        for key in st.session_state.stats:
            st.session_state.stats[key] += 3
        st.balloons()
        st.sidebar.success(f"LEVEL UP: {st.session_state.lvl}!")

# --- واجهة المستخدم ---

# القائمة الجانبية (Status Window)
with st.sidebar:
    st.markdown(f"""
    <div class='status-card'>
        <h3 style='color:#fff; margin:0;'>NAME: PLAYER</h3>
        <p style='color:#00d4ff; font-size:12px;'>RANK: E-RANK (EVOLVING)</p>
        <hr style='border: 0.2px solid #00d4ff;'>
        <p style='font-size: 25px;'>LVL. {st.session_state.lvl}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### [ STATISTICS ]")
    for stat, val in st.session_state.stats.items():
        col_s1, col_s2 = st.columns([1, 1])
        col_s1.write(stat)
        col_s2.write(f"**{val}**")
    
    st.markdown("---")
    st.write(f"EXP: {st.session_state.exp} / 100")
    st.progress(st.session_state.exp / 100)

# المحتوى الرئيسي
st.markdown("<h1 style='text-align: center; color: #fff; text-shadow: 0 0 10px #00d4ff;'>SYSTEM INTERFACE</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("### ⚡ ITEM SCANNER")
    user_input = st.text_input("INPUT TARGET DATA...", placeholder="Enter food or activity...")
    
    if st.button("RUN SCAN ⚔️"):
        if user_input:
            with st.spinner("COMMUNICATING WITH THE VOID..."):
                prompt = f"Act as the Solo Leveling System. Scan: {user_input}. Output Rank (S to E), Calories, and a cold advice. Arabic language. Concise."
                try:
                    res = model.generate_content(prompt)
                    gain_exp(20)
                    st.markdown(f"<div class='system-response'>{res.text}</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"CONNECTION INTERRUPTED: {e}")

with col2:
    st.markdown("### 📜 DAILY QUESTS")
    quest_list = ["100 Push-ups", "100 Sit-ups", "10km Run"]
    for q in quest_list:
        st.markdown(f"<div style='padding:5px; border-bottom: 0.5px solid #333;'>🔳 {q}</div>", unsafe_allow_html=True)
    
    if st.button("CLAIM DAILY REWARD"):
        gain_exp(50)
        st.toast("XP RECEIVED. GET STRONGER.")

# التذييل
st.markdown("---")
st.caption(f"LAST SYNC: {datetime.now().strftime('%H:%M:%S')} | GATE STATUS: OPEN")
