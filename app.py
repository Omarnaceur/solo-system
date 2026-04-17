import streamlit as st
import google.generativeai as genai

# إعدادات الواجهة
st.set_page_config(page_title="Solo Leveling System", layout="centered")

# الربط مع الذكاء الاصطناعي
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("الرجاء إضافة GOOGLE_API_KEY في الإعدادات (Secrets)")

# تصميم النظام (CSS)
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #00d4ff; }
    .stTextInput>div>div>input { background-color: #161b22; color: white; border: 1px solid #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ نظام سولو ليفلينج الذكي")

# منطق التطبيق
food = st.text_input("ماذا أكلت اليوم؟")

if st.button("تحليل النظام ⚔️"):
    if food:
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(f"حلل وجبة {food} من حيث السعرات والبروتين بأسلوب Solo Leveling")
            st.info(response.text)
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
    else:
        st.warning("أدخل اسم الوجبة أولاً")
