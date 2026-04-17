import streamlit as st
import google.generativeai as genai

# 1. إعدادات النظام السرية
st.set_page_config(page_title="SYSTEM: SOLO LEVELING", layout="wide", initial_sidebar_state="expanded")

# 2. تفعيل الاتصال بالبوابة (API)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ فشل الربط: مفتاح API غير موجود في Secrets.")
    st.stop()

# 3. واجهة النظام (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .main { background-color: #000000; color: #00d4ff; font-family: 'Orbitron', sans-serif; }
    .stApp { background: radial-gradient(circle, #001529 0%, #000000 100%); }
    .status-window { border: 2px solid #00d4ff; padding: 15px; border-radius: 5px; background: rgba(0, 212, 255, 0.1); box-shadow: 0 0 20px #00d4ff; }
    .quest-item { border-left: 4px solid #00d4ff; padding-left: 10px; margin: 10px 0; background: rgba(255, 255, 255, 0.05); }
    .stButton>button { width: 100%; background: transparent; color: #00d4ff; border: 1px solid #00d4ff; text-shadow: 0 0 5px #00d4ff; height: 50px; }
    .stButton>button:hover { background: #00d4ff; color: black; box-shadow: 0 0 30px #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

# 4. إدارة حالة اللاعب
if 'lvl' not in st.session_state: st.session_state.lvl = 1
if 'exp' not in st.session_state: st.session_state.exp = 0

# --- الجانب الأيسر: نافذة الحالة (Status) ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #00d4ff;'>STATUS</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='status-window'>
        <p><b>NAME:</b> PLAYER</p>
        <p><b>JOB:</b> SHADOW MONARCH</p>
        <p><b>LEVEL:</b> {st.session_state.lvl}</p>
        <p><b>HP:</b> 100 / 100</p>
        <p><b>MP:</b> 50 / 50</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("📊 STATS")
    st.write(f"STR (القوة): {10 + st.session_state.lvl}")
    st.write(f"AGI (الرشاقة): {10 + st.session_state.lvl}")
    st.write(f"INT (الذكاء): {10 + (st.session_state.lvl * 2)}")

# --- القسم الرئيسي ---
st.markdown("<h2 style='text-align: center;'>⚠️ DAILY QUEST: GETTING STRONGER</h2>", unsafe_allow_html=True)

# نظام المهام اليومية (Quests)
with st.expander("📜 عرض المهام المطلوبة اليوم"):
    st.markdown("""
    <div class='quest-item'>1. تمارين الضعط (Push-ups): 0/100</div>
    <div class='quest-item'>2. تمارين البطن (Sit-ups): 0/100</div>
    <div class='quest-item'>3. الجري (Running): 0/10km</div>
    """, unsafe_allow_html=True)
    if st.button("إكمال المهام اليومية ✅"):
        st.session_state.exp += 50
        st.toast("تم الحصول على مكافأة المهمة! +50 EXP")

st.markdown("---")

# تحليل الأكل والتمرين بالذكاء الاصطناعي
st.subheader("🔍 استهلاك العناصر (Item Analysis)")
input_data = st.text_input("أدخل ما أكلت أو تمرين قمت به..", placeholder="مثال: وجبة كفتة مشوية / تمرين رفع أثقال 20kg")

if st.button("بدء المسح (SCAN) ⚡"):
    if input_data:
        with st.spinner("جاري الاتصال بالنظام..."):
            # برومبت فائق السرعة
            prompt = f"Act as the System from Solo Leveling. Analyze '{input_data}'. Provide Calories, Protein, and a Rank (S-E) in a very short, robotic, cool style in Arabic."
            try:
                response = model.generate_content(prompt)
                
                # زيادة الخبرة عند الاستخدام
                st.session_state.exp += 15
                if st.session_state.exp >= 100:
                    st.session_state.lvl += 1
                    st.session_state.exp = 0
                    st.balloons()
                
                st.markdown(f"<div class='status-window'>{response.text}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error("فشل النظام في الوصول للبوابة.")
    else:
        st.warning("أدخل بيانات ليقوم النظام بمسحها.")

# شريط الخبرة في الأسفل
st.markdown(f"**EXP:** {st.session_state.exp} / 100")
st.progress(st.session_state.exp / 100)
