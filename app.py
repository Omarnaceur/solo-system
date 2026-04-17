import streamlit as st
import google.generativeai as genai

# 1. إعدادات واجهة النظام (Solo Leveling UI)
st.set_page_config(page_title="SYSTEM: MONARCH ASCENSION", page_icon="⚡")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00d4ff; font-family: 'Courier New', monospace; }
    .status-box { border: 1px solid #00d4ff; padding: 15px; background: rgba(0,212,255,0.05); border-left: 5px solid #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

# 2. محرك الربط الذكي (تجاوز خطأ 404)
def initialize_monarch_system():
    if "GOOGLE_API_KEY" not in st.secrets:
        return None, "❌ مفتاح الـ API مفقود في إعدادات Secrets."
    
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        
        # استخدام الاسم الأكثر استقراراً وتوافقاً لعام 2026
        # هذا الاسم يتجنب مشاكل v1beta و 404
        model_name = 'gemini-1.5-flash-latest' 
        model = genai.GenerativeModel(model_name)
        
        # اختبار الاتصال فوراً
        model.generate_content("test", generation_config={"max_output_tokens": 1})
        return model, f"✅ تم الاتصال بالموديل: {model_name}"
    
    except Exception as e:
        # إذا فشل الفلاش، ننتقل فوراً لموديل برو كخطة بديلة
        try:
            model = genai.GenerativeModel('gemini-pro')
            return model, "✅ تم الاتصال بموديل Gemini-Pro (Plan B)"
        except:
            return None, f"🚨 فشل كلي في النظام: {str(e)}"

system_model, status_msg = initialize_monarch_system()

# 3. عرض حالة النظام
st.sidebar.title("👤 STATUS WINDOW")
if system_model:
    st.sidebar.success(status_msg)
else:
    st.sidebar.error(status_msg)

# 4. الواجهة الرئيسية
st.title("⚡ THE SYSTEM : VOID INTERFACE")

if system_model:
    target = st.text_input("أدخل مادة للمسح (أكلة أو تمرين):", placeholder="مثال: 200g صدور دجاج")
    
    if st.button("بدء المسح (EXECUTE SCAN)"):
        if target:
            with st.spinner("⏳ جاري استدعاء البيانات من الفراغ..."):
                try:
                    prompt = f"Act as the Solo Leveling System. Analyze '{target}' in Arabic. Give: Rank (S-E), Calories, and a cold advice."
                    response = system_model.generate_content(prompt)
                    st.markdown(f"<div class='status-box'>{response.text}</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"❌ حدث خطأ أثناء المسح: {str(e)}")
        else:
            st.warning("⚠️ أدخل هدفاً للمسح.")
else:
    st.warning("🚨 البوابة مغلقة. تحقق من مفتاح الـ API في الإعدادات.")
