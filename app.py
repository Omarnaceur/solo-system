if st.button("EXECUTE SCAN ⚡"):
    if user_input:
        placeholder = st.empty()
        placeholder.warning("⚠️ جاري اختراق البوابة... انتظر")
        
        try:
            # التأكد من استدعاء الموديل داخل الزر لضمان التحديث
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # أمر صريح ومختصر جداً لضمان السرعة
            full_prompt = f"Analyze briefly: {user_input}. Language: Arabic. Style: Solo Leveling."
            
            response = model.generate_content(full_prompt)
            
            if response.text:
                placeholder.empty()
                st.markdown(f"<div class='status-panel'>{response.text}</div>", unsafe_allow_html=True)
                # زيادة المستوى
                st.session_state.exp += 20
                if st.session_state.exp >= 100:
                    st.session_state.lvl += 1
                    st.session_state.exp = 0
                    st.balloons()
            else:
                st.error("❌ النظام لم يجد بيانات. حاول صياغة الطلب بشكل أوضح.")
                
        except Exception as e:
            placeholder.empty()
            st.error(f"🚨 خطأ في الاتصال: {str(e)}")
            st.info("تأكد أنك وضعت GOOGLE_API_KEY في صفحة Secrets بشكل صحيح.")
    else:
        st.warning("⚠️ أدخل اسم الهدف (الأكلة) أولاً!")
