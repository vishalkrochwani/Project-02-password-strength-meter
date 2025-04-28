import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔑")

# Custom CSS
st.markdown("""
    <style>
    .stTitle {
        text-align: center;
        color: #2c3e50;
        font-family: 'Arial', sans-serif;
    }
    div[data-testid="stTextInput"] input {
        border: 2px solid #3498db;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        background-color: #f7f9fc;
    }
    .stMarkdown p {
        font-size: 16px;
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
    }
    .stSuccess {
        background-color: #e8f5e9;
        border: 1px solid #4caf50;
        border-radius: 5px;
        padding: 10px;
        color: #2e7d32;
    }
    .stWarning {
        background-color: #fff3e0;
        border: 1px solid #fb8c00;
        border-radius: 5px;
        padding: 10px;
        color: #e65100;
    }
    .stError {
        background-color: #ffebee;
        border: 1px solid #e57373;
        border-radius: 5px;
        padding: 10px;
        color: #c62828;
    }
    .container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 600px;
        margin: auto;
    }
    .feedback {
        background-color: #f1f8ff;
        padding: 15px;
        border-radius: 8px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Main content
with st.container():
    
    st.title("🔐 Password Strength Checker")
    st.markdown(""" 
    ## Welcome!
    This is a simple password strength checker that evaluates the strength of your password based on various criteria and also provides tips to improve it.
    """)  

    password = st.text_input("Enter your password", type="password")

    feedback = []
    score = 0

    if password:
        # Check length
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Password should be at least 8 characters long.")
        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("❌ Password should contain both uppercase and lowercase letters.")
        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("❌ Password should contain at least one digit.")
        if re.search(r'[@$!%*?&]', password):
            score += 1
        else:
            feedback.append("❌ Password should contain at least one special character (@, $, !, %, *, ?, &).")
        if re.search(r'\s', password):
            feedback.append("❌ Password should not contain any spaces.")
        else:
            score += 1

        # Strength meter
        strength_label = "Weak"
        strength_color = "#e57373"
        if score == 5:
            strength_label = "Strong"
            strength_color = "#4caf50"
        elif score >= 3:
            strength_label = "Moderate"
            strength_color = "#fb8c00"

        st.markdown(f"""
            <div style='text-align: center; margin: 20px 0;'>
                <h4>Password Strength: <span style='color: {strength_color};'>{strength_label}</span></h4>
                <div style='background-color: #e0e0e0; border-radius: 5px; height: 10px; width: 100%;'>
                    <div style='background-color: {strength_color}; width: {score * 20}%; height: 100%; border-radius: 5px;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Display feedback
        if score == 5:
            st.success("✅ Your password is strong!")
        elif score >= 3:
            st.warning("⚠️ Your password is moderate. Consider adding more complexity.")
        else:
            st.error("❌ Your password is weak. Follow the feedback below to improve it.")

        if feedback:
            st.markdown('<div class="feedback">', unsafe_allow_html=True)
            st.markdown("### Feedback:")
            for tip in feedback:
                st.write(tip)
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a password to check its strength.")

    st.markdown('</div>', unsafe_allow_html=True)