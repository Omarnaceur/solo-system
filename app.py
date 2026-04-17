import streamlit as st
import google.generativeai as genai

# 1. إعدادات واجهة النظام
st.set_page_config(page_title="SYSTEM RECOVERY", page_icon="⚡")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00d4ff; font-family: 'Courier New', monospace; }
    .status-box { border: 1px solid #00d4ff; padding: 10px; background: rgba(0,212,255,0.1); }
    </style>
    """, unsafe_allow_html=True)

# 2. وظيفة الربط الذكي - محاولات متعددة لإصلاح الاتصال
def connect_to_system():
    # التحقق من وجود المفتاح في السيكرتس
    if "GOOGLE_API_KEY" not in st.secrets:
        return None, "❌ لم يتم العثور على GOOGLE_API_KEY في إعدادات Secrets."
    
    api_key = st.secrets["GOOGLE_API_KEY"]
    
    try:
        genai.configure(api_key=api_key)
        # محاولة الوصول لموديل فلاش الأحدث
        model = genai.GenerativeModel('gemini-1.5-flash')
        # اختبار اتصال بسيط
        model.generate_content("test", generation_config={"max_output_tokens": 1})
        return model, "✅ النظام متصل بنجاح! البوابة مفتوحة."
    except Exception as e:
        error_msg = str(e)
        if "API_KEY_INVALID" in error_msg:
            return None, "❌ مفتاح الـ API غير صالح. يرجى التأكد من نسخه كاملاً من AI Studio."
        elif "location not supported" in error_msg:
            return None, "❌ منطقتك غير مدعومة حالياً أو الـ VPN يمنع الاتصال."
        else:
            return None, f"❌ فشل الاتصال: {error_msg}"

# تشغيل الفحص
system_model, status_message = connect_to_system()

# 3. عرض الحالة في القائمة الجانبية
st.sidebar.title("🛡️ SYSTEM CHECK")
if "✅" in status_message:
    st.sidebar.success(status_message)
else:
    st.sidebar.error(status_message)

# 4. واجهة المستخدم
st.title("⚡ THE SYSTEM : INTERFACE")

if system_model:
    target = st.text_input("أدخل هدف المسح (أكلة أو تمرين):", placeholder="مثال: صدر دجاج مشوي")
    
    if st.button("بدء المسح (EXECUTE SCAN)"):
        if target:
            with st.spinner("جاري تحليل البيانات من الفراغ..."):
                try:
                    # توجيه أمر صارم للذكاء الاصطناعي
                    prompt = f"حلل المادة التالية بأسلوب نظام Solo Leveling: {target}. اعطني السعرات، الرتبة (S-E)، ونصيحة باردة."
                    response = system_model.generate_content(prompt)
                    st.markdown(f"<div class='status-box'>{response.text}</div>", unsafe_allow_html=True)
                except:
                    st.error("فشل المسح. حاول مرة أخرى.")
        else:
            st.warning("أدخل هدفاً للمسح أولاً.")
else:
    st.warning("⚠️ النظام في وضع الخمول. يرجى إصلاح مفتاح الـ API لفتح البوابة.")
