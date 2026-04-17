import streamlit as st
import google.generativeai as genai
import time
from datetime import datetime

# --- 1. إعدادات النواة العليا ---
st.set_page_config(page_title="SYSTEM: FINAL ASCENSION", page_icon="⚡", layout="wide")

# --- 2. محرك الربط وتصحيح الأخطاء (Auto-Fix Engine) ---
@st.cache_resource
def load_system_core():
    if "GOOGLE_API_KEY" not in st.secrets:
        return None, "MISSING_KEY"
    
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # محاولة الاتصال بأحدث الموديلات المتاحة لعام 2026
    model_names = ['gemini-1.5-flash-latest', 'gemini-1.5-flash', 'gemini-pro']
    
    for name in model_names:
        try:
            model = genai.GenerativeModel(name)
            # فحص سريع للاتصال
            model.generate_content("test", generation_config={"max_output_tokens": 1})
            return model, name
        except:
            continue
    return None, "CONNECTION_FAILED"

system_model, active_model_name = load_system_core()

# --- 3. محرك الجرافيك (Extreme Shadow UI) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');
    
    .stApp {{ background: #000; color: #00d4ff; font-family: 'Share Tech Mono', monospace; }}
    
    /* لوحة الحالة الملكية */
    .status-panel {{
        border: 2px solid #00d4ff; background: rgba(0, 212, 255, 0.05);
        padding: 20px; border-radius: 5px; box-shadow: 0 0 25px rgba(0, 212, 255, 0.2);
        margin-bottom: 20px; border-left: 8px solid #00d4ff;
    }}
    
    .stat-row {{ display: flex; justify-content: space-between; margin: 10px 0; border-bottom: 1px solid rgba(0,212,255,0.1); }}
    
    /* أزرار النظام */
    .stButton>button {{
        width: 100%; background: transparent; color: #00d4ff; border: 1px solid #00d4ff;
        font-family: 'Orbitron', sans-serif; height: 50px; font-weight: 900; transition: 0.3s;
    }}
    .stButton>button:hover {{ background: #00d4ff; color: #000; box-shadow: 0 0 30px #00d4ff; }}
    
    /* صندوق الردود */
    .system-response {{
        background: rgba(0, 20, 40, 0.8); border: 1px solid #00d4ff; padding: 15px;
        color: #fff; font-size: 16px; line-height: 1.5; border-radius: 4px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. إدارة بيانات اللاعب ---
if 'lvl' not in st.session_state: st.session_state.lvl = 1
if 'exp' not in st.session_state: st.session_state.exp = 0
if 'power' not in st.session_state: st.session_state.power = 150

def add_experience(amount):
    st.session_state.exp += amount
    if st.session_state.exp >= 100:
        st.session_state.lvl += 1
        st.session_state.exp = 0
        st.session_state.power += 50
        st.balloons()

# --- 5. واجهة المستخدم الرسومية ---
st.markdown("<h1 style='text-align:center; text-shadow: 0 0 15px #00d4ff;'>● SYSTEM INTERFACE ●</h1>", unsafe_allow_html=True)

if active_model_name == "MISSING_KEY":
    st.error("🚨 خطأ: لم يتم العثور على مفتاح API في Secrets. يرجى إضافته.")
    st.stop()
elif not system_model:
    st.error("🚨 فشل في الاتصال بالبوابة. تأكد من صحة المفتاح أو اتصال الإنترنت.")
    st.stop()

col_left, col_right = st.columns([1, 2])

with col_left:
    st.markdown(f"""
    <div class='status-panel'>
        <h3 style='margin:0; color:#fff;'>PLAYER STATUS</h3>
        <p style='color:#00d4ff; font-size:12px;'>RANK: SHADOW MONARCH</p>
        <hr style='border: 0.1px solid #00d4ff;'>
        <div class='stat-row'><span>LEVEL</span><span>{st.session_state.lvl}</span></div>
        <div class='stat-row'><span>POWER</span><span>{st.session_state.power}</span></div>
        <div class='stat-row'><span>MODEL</span><span>ONLINE</span></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(f"EXP: {st.session_state.exp}/100")
    st.progress(st.session_state.exp / 100)
    
    if st.button("DAILY QUEST: COMPLETE"):
        add_experience(40)
        st.toast("XP RECEIVED. LEVELING UP...")

with col_right:
    st.subheader("⚡ VOID SCANNER")
    target = st.text_input("INPUT TARGET (FOOD/EXERCISE):", placeholder="Scanning for soul frequency...")
    
    if st.button("EXECUTE SCAN"):
        if target:
            with st.spinner("ANALYZING..."):
                try:
                    prompt = f"System Scan for '{target}'. Provide: Rank (S-E), Calories, Protein, and a cold Monarch's verdict. Arabic language. Cool UI style."
                    response = system_model.generate_content(prompt)
                    add_experience(15)
                    st.markdown(f"<div class='system-response'>{response.text}</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"SCAN INTERRUPTED: {str(e)}")
        else:
            st.warning("⚠️ أدخل اسم الهدف للمسح.")

# --- التذييل ---
st.markdown("---")
st.caption(f"GATE STATUS: STABLE | ACTIVE CORE: {active_model_name} | TIME: {datetime.now().strftime('%H:%M')}")
