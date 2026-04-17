import streamlit as st
import google.generativeai as genai
import time

# 1. إعدادات النظام الأساسية
st.set_page_config(page_title="SOLO LEVELING: THE SYSTEM", layout="wide")

# 2. تفعيل القوة (API Key)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash') # الموديل الأسرع عالمياً
else:
    st.error("⚠️ خطأ في مفتاح API. يرجى ضبطه في Secrets.")
    st.stop()

# 3. تصميم الواجهة (Neon UI Design)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .main { background-color: #050a12; color: #00d4ff; font-family: 'Orbitron', sans-serif; }
    .stButton>button {
        background: linear-gradient(90deg, #001f3f, #00d4ff);
        color: white; border: 1px solid #00d4ff;
        font-weight: bold; border-radius: 5px; box-shadow: 0 0 15px #00d4ff;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 30px #00d4ff; }
    .status-card {
        background: rgba(0, 212, 255, 0.05);
        border: 2px solid #00d4ff; border-radius: 15px;
        padding: 20px; margin-bottom: 20px;
    }
    .exp-bar { height: 10px; background: #111; border-radius: 5px; overflow: hidden; }
    .exp-progress { height: 100%; background: #00d4ff; box-shadow: 0 0 10px #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

# 4. إدارة بيانات اللاعب (Player Data)
if 'lvl' not in st.session_state: st.session_state.lvl = 1
if 'exp' not in st.session_state: st.session_state.exp = 0
if 'history' not in st.session_state: st.session_state.history = []

# 5. دوال النظام
def add_exp(amount):
    st.session_state.exp += amount
    if st.session_state.exp >= 100:
        st.session_state.lvl += 1
        st.session_state.exp = 0
        st.balloons()
        st.sidebar.success(f"LEVEL UP! أنت الآن في المستوى {st.session_state.lvl}")

# --- القائمة الجانبية (STATUS WINDOW) ---
with st.sidebar:
    st.image("https://i.imgur.com/8Qp2C7H.png", width=100) # صورة تعبيرية للنظام
    st.title("👤 PLAYER STATUS")
    st.subheader(f"Level: {st.session_state.lvl}")
    st.write("EXP Progress")
    st.markdown(f"""<div class='exp-bar'><div class='exp-progress' style='width: {st.session_state.exp}%'></div></div>""", unsafe_allow_html=True)
    st.write(f"{st.session_state.exp} / 100")
    st.markdown("---")
    st.write("🏆 الرتبة: Shadow Monarch")

# --- الواجهة الرئيسية ---
st.title("⚡ THE SYSTEM : INTERFACE")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<div class='status-card'>", unsafe_allow_html=True)
    item_name = st.text_input("📝 أدخل الوجبة أو التمرين (Daily Quest):", placeholder="مثال: بيتزا، 50 ضغط...")
    
    if st.button("تأكيد المهمة (CONFIRM)"):
        if item_name:
            with st.spinner("⚡ جاري استدعاء البيانات من الفراغ..."):
                start_time = time.time()
                # طلب التحليل من الذكاء الاصطناعي
                prompt = f"حلل {item_name} بأسلوب نظام Solo Leveling. اعطني السعرات، البروتين، وتقييم رتبة (S, A, B, C). اجعل الرد قصيراً جداً وصارماً."
                try:
                    response = model.generate_content(prompt)
                    end_time = time.time()
                    
                    st.session_state.history.insert(0, f"{item_name} (Level Up!)")
                    add_exp(20) # مكافأة الإكمال
                    
                    st.markdown(f"**النتيجة التحليلية:** \n\n {response.text}")
                    st.caption(f"تم التحليل في {round(end_time - start_time, 2)} ثانية")
                except Exception as e:
                    st.error("⚠️ البوابة مغلقة حالياً. تأكد من اتصال الإنترنت أو مفتاح API.")
        else:
            st.warning("الرجاء كتابة اسم المهمة!")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.subheader("📜 سجل المهام")
    for log in st.session_state.history[:5]:
        st.write(f"✅ {log}")
