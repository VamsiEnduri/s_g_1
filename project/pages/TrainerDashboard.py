import streamlit as st 


def login_status_check():
    if not st.session_state.get("status",False):
        st.title("login first")
        st.switch_page("app.py")


def role_check():
    if "trainer" != "trainer"  : 
        st.title("access denied")
        st.switch_page("app.py")


login_status_check() 
role_check()        


st.title("trainer dashboard")