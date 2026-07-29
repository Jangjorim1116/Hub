import streamlit as st

st.set_page_config(page_title="스마트팜 도우미", page_icon="🌱", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "login"


def go_to(page: str):
    st.session_state.page = page


def login_screen():
    st.markdown("<h1 style='text-align:center;'>🌱 스마트팜 도우미</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:gray;'>텃밭·화분 초보자를 위한 AI 재배 가이드</p>", unsafe_allow_html=True)
    st.write("")

    with st.form("login_form"):
        st.subheader("로그인")
        username = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")
        submitted = st.form_submit_button("로그인", use_container_width=True)

        if submitted:
            if not username or not password:
                st.warning("아이디와 비밀번호를 입력해주세요.")
            else:
                st.info("로그인 기능은 아직 준비 중입니다.")

    st.write("")
    st.markdown("<p style='text-align:center; color:gray;'>계정이 없으신가요?</p>", unsafe_allow_html=True)
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        if st.button("회원가입", use_container_width=True):
            go_to("signup")


def signup_screen():
    st.markdown("<h1 style='text-align:center;'>🌱 회원가입</h1>", unsafe_allow_html=True)
    st.write("")

    with st.form("signup_form"):
        name = st.text_input("이름")
        email = st.text_input("이메일")
        password = st.text_input("비밀번호", type="password")
        password_confirm = st.text_input("비밀번호 확인", type="password")
        submitted = st.form_submit_button("가입하기", use_container_width=True)

        if submitted:
            if not name or not email or not password:
                st.warning("모든 항목을 입력해주세요.")
            elif password != password_confirm:
                st.error("비밀번호가 일치하지 않습니다.")
            else:
                st.success(f"{name}님, 가입 신청이 접수되었습니다. (실제 저장 기능은 아직 준비 중입니다)")

    st.write("")
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        if st.button("로그인 화면으로 돌아가기", use_container_width=True):
            go_to("login")


if st.session_state.page == "login":
    login_screen()
else:
    signup_screen()
