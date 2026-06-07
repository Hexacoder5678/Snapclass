import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png",
        layout="wide"  
    )

    
    st.markdown(
        """
        <style>
        /* 1. Input boxes ka background clean white aur typed text ko pure black karo */
        .stTextInput input {
            color: #111111 !important; /* Jo text type hoga woh ekdam saaf black dikhega */
            background-color: #ffffff !important; /* Input box ka background pure white rahega */
            border: 1px solid #cccccc !important; /* Professional light grey border */
            font-size: 1rem !important;
            border-radius: 6px !important;
        }
        
        /* Input box par click karne par red highlight (Optional/Clean active state) */
        .stTextInput input:focus {
            border-color: #ff4b4b !important;
            box-shadow: 0 0 0 1px #ff4b4b !important;
        }

        /* 2. Form widget ke labels ko bold aur high contrast black karo (Enter username, Enter password) */
        label[data-testid="stWidgetLabel"] p, 
        .stWidgetLabel p,
        div[data-testid="stWidgetLabel"] span {
            color: #111111 !important;
            font-weight: 600 !important;
        }

        /* 3. Badi headings aur baaki ke normal texts ko pure black karo (Login using password etc.) */
        div[data-testid="stMarkdownContainer"] h1,
        div[data-testid="stMarkdownContainer"] h2,
        div[data-testid="stMarkdownContainer"] h3,
        div[data-testid="stMarkdownContainer"] p,
        span[data-font="sans serif"],
        div[data-testid="stVerticalBlock"] p {
            color: #111111 !important;
        }

        /* 4. Buttons ka text clean white lock rahe taaki unke colorful background par sahi baithe */
        .stButton>button, 
        .stButton>button p, 
        .stButton>button span {
            color: #ffffff !important;
            font-weight: 600 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)

if __name__ == "__main__":
    main()