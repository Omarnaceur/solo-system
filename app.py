import streamlit as st
import google.generativeai as genai
import time

# 1. إعدادات النواة المركزية
st.set_page_config(page_title="SYSTEM : MONARCH", page_icon="🔗", layout="wide")

# 2. تفعيل القوة العظمى (Gemini Flash 1.5)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("🚨 SYSTEM CORE NOT FOUND. PLEASE INSERT API KEY IN SECRETS.")
    st.stop()

# 3. محرك الجرافيك (Extreme Shadow UI)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Krona+One&display=swap');
    
    .stApp { background: #000; color: #00d4ff; font-family: 'Orbitron', sans-serif; }
    
    /* تأثير البرق والوميض للنظام */
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }
    .system-title { font-size: 50px; text-align: center; color: #fff; text-shadow: 0 0 20px #00d4ff; animation: blink 2s infinite; font-weight: 900; }
    
    /* بطاقة الحالة المتقدمة */
    .status-panel {
        border: 2px solid #00d4ff; background: rgba(0, 212, 255, 0.05);
        padding: 25px; border-radius: 0px; box-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
        border-left: 10px solid #00d4ff; margin-bottom: 25px;
    }
    
    .stat-val { font-size: 28px; color: #fff; font-weight: bold; }
    
    /* أزرار المهمات */
    .stButton>button {
        width: 100%; height: 60px; background: transparent; color: #00d4ff;
        border: 2px solid #00d4ff; font-size: 18px; letter-spacing: 3px;
        transition: 0.5s; font-family: 'Krona One', sans-serif;
    }
    .stButton>button:hover { background: #00d4ff; color: #000; box-shadow: 0 0 50px #00d4ff; }
    
    /* شريط المستوى النيوني */
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #001a33, #00d4ff); }
    </style>
    """, unsafe_allow_html=True)

# 4. قاعدة بيانات اللاعب (Persistence Logic)
if 'lvl' not in st.session_state: st.session_state.lvl = 1
if 'exp' not in st.session_state: st.session_state.exp = 0
if 'str' not in st.session_state: st.session_state.str = 10
if 'agi' not in st.session_state: st.session_state.agi = 10
if 'int' not in st.session_state: st.session_state.int = 10

def process_level_up(xp_gain):
    st.session_state.exp += xp_gain
    if st.session_state.exp >= 100:
        st.session_state.lvl += 1
        st.session_state.exp = 0
        st.session_state.str += 5
        st.session_state.agi += 3
        st.session_state.int += 2
        return True
    return False

# --- الواجهة الرئيسية (The Interface) ---
st.markdown("<div class='system-title'>THE SYSTEM</div>", unsafe_allow_html=True)

# القائمة الجانبية (The Monarch's Stats)
with st.sidebar:
    st.markdown("<h2 style='color:#fff; text-shadow: 0 0 10px #00d4ff;'>👤 STATUS</h2>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='status-panel'>
        <p style='color:#777;'>TITLE: <b style='color:#fff;'>SHADOW SOVEREIGN</b></p>
        <p>LEVEL: <span class='stat-val'>{st.session_state.lvl}</span></p>
        <p>STR: <span class='stat-val'>{st.session_state.str}</span></p>
        <p>AGI: <span class='stat-val'>{st.session_state.agi}</span></p>
        <p>INT: <span class='stat-val'>{st.session_state.int}</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(f"EXP PROGRESS: {st.session_state.exp}%")
    st.progress(st.session_state.exp / 100)

# محتوى الصفحة
col1, col2 = st.columns([1.5, 1])

with col1:
    st.subheader("🛠️ SCANNER MODE")
    scan_target = st.text_input("ENTER OBJECTIVE (FOOD/WORKOUT):", placeholder="Target name...")
    
    if st.button("INITIATE SCAN"):
        if scan_target:
            placeholder = st.empty()
            placeholder.info("⏳ Connecting to the Void...")
            
            # برومبت عسكري فائق السرعة
            prompt = f"""
            SYSTEM COMMAND: Scan '{scan_target}'. 
            Output Format:
            - Item Rank: [S/A/B/C]
            - Nutrients/Output: [Brief Data]
            - Monarch's Advice: [One Cold Sentence]
            Style: Shadow Monarch System. Language: Arabic.
            """
            
            try:
                response = model.generate_content(prompt)
                placeholder.empty()
                if process_level_up(15):
                    st.balloons()
                    st.success("⚠️ ALERT: LEVEL UP! ALL STATS INCREASED.")
                
                st.markdown(f"<div class='status-panel'>{response.text}</div>", unsafe_allow_html=True)
            except:
                st.error("System Failure: Gateway Closed.")

with col2:
    st.subheader("📜 DAILY QUEST")
    with st.container():
        st.markdown("""
        <div style='background:rgba(255,255,255,0.05); padding:10px; border-radius:5px;'>
        <p>🔘 100 Push-ups</p>
        <p>🔘 10km Run</p>
        <p>🔘 100 Squats</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("CLAIM QUEST REWARDS"):
            if process_level_up(40):
                st.balloons()
                st.success("LEVEL UP!")
            st.toast("XP Recieved. Stay focused, Player.")

st.markdown("---")
st.caption("CONNECTION STATUS: SYNCED WITH THE SHADOW REALM")
