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
        /* 1. White cards, markdown text, headings aur subheadings ko target karke pure black karo */
        div[data-testid="stVerticalBlock"] p,
        div[data-testid="stVerticalBlock"] h1,
        div[data-testid="stVerticalBlock"] h2,
        div[data-testid="stVerticalBlock"] h3,
        div[data-testid="stMarkdownContainer"] p,
        div[data-testid="stMarkdownContainer"] h1,
        div[data-testid="stMarkdownContainer"] h2,
        div[data-testid="stMarkdownContainer"] h3,
        span[data-font="sans serif"] {
            color: #111111 !important;
        }

        /* 2. Login/Register Form ke text inputs ke labels (Enter username, password) ko high contrast karo */
        label[data-testid="stWidgetLabel"] p, 
        .stWidgetLabel p,
        div[data-testid="stWidgetLabel"] span {
            color: #111111 !important;
            font-weight: 600 !important;
        }

        /* 3. Main buttons ke andar ka text clean white lock rahe taaki background par chamke */
        .stButton>button, 
        .stButton>button p, 
        .stButton>button span {
            color: #ffffff !important;
            font-weight: 600 !important;
        }
        
        /* 4. TextInput containers ke placeholders/input text values ko sharp black/dark rakho */
        .stTextInput input {
            color: #111111 !important;
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