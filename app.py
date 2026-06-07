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

    # 🛠️ THE MASTER SYSTEM CONFIG: Text, Inputs, and Dialog Modals
    st.markdown(
        """
        <style>
        /* 1. DIALOG / POPUP FIX: Popup modal ka background white aur uske andar ka text black */
        div[role="dialog"], 
        div[data-testid="stModal"],
        div[data-testid="stDialog"] div,
        div[role="dialog"] div[data-testid="stVerticalBlock"] {
            background-color: #ffffff !important;
        }
        
        div[role="dialog"] h1, 
        div[role="dialog"] h2, 
        div[role="dialog"] h3, 
        div[role="dialog"] p,
        div[role="dialog"] span,
        div[data-testid="stModal"] p,
        div[data-testid="stModal"] h3,
        div[data-testid="stModal"] span {
            color: #111111 !important; /* Popup ke andar ka sab kuch dark black */
        }

        /* 2. INPUT BOXES FIX: Input box background white aur typed text pure black */
        .stTextInput input {
            color: #111111 !important; 
            background-color: #ffffff !important; 
            border: 1px solid #cccccc !important; 
            font-size: 1rem !important;
            border-radius: 6px !important;
        }
        
        .stTextInput input:focus {
            border-color: #ff4b4b !important;
            box-shadow: 0 0 0 1px #ff4b4b !important;
        }

        /* 3. WIDGET LABELS FIX: Widget labels ko bold aur clear black karo (Enter username, password) */
        label[data-testid="stWidgetLabel"] p, 
        .stWidgetLabel p,
        div[data-testid="stWidgetLabel"] span {
            color: #111111 !important;
            font-weight: 600 !important;
        }

        /* 4. HEADINGS & MARKDOWN FIX: Normal pages ki headings aur text ko pure black karo */
        div[data-testid="stMarkdownContainer"] h1,
        div[data-testid="stMarkdownContainer"] h2,
        div[data-testid="stMarkdownContainer"] h3,
        div[data-testid="stMarkdownContainer"] p,
        span[data-font="sans serif"],
        div[data-testid="stVerticalBlock"] p {
            color: #111111 !important;
        }

        /* 5. BUTTONS FIX: Main buttons ke andar ka text clean white hi lock rahe */
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