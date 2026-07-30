import base64
import datetime
import json
import re
import threading

import streamlit as st
import streamlit.components.v1 as components
from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx

import ai
import auth
import care
import chat
import fertilizer
import gardens
import i18n
import tips
import pots
import regions

st.set_page_config(page_title="허브", page_icon="🌱", layout="wide")

st.markdown(
    """
    <style>
    .block-container {
        max-width: 1120px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "page" not in st.session_state:
    st.session_state.page = "login"
if "keep_logged_in" not in st.session_state:
    st.session_state.keep_logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None
if "current_email" not in st.session_state:
    st.session_state.current_email = None
if "flash_message" not in st.session_state:
    st.session_state.flash_message = None
if "tab" not in st.session_state:
    st.session_state.tab = "home"
if "selected_pot" not in st.session_state:
    st.session_state.selected_pot = None
if "diagnosis_result" not in st.session_state:
    st.session_state.diagnosis_result = None
if "editing_pot_name" not in st.session_state:
    st.session_state.editing_pot_name = False
if "confirm_delete_pot" not in st.session_state:
    st.session_state.confirm_delete_pot = False
if "chat_subview" not in st.session_state:
    st.session_state.chat_subview = "users"
if "chat_room" not in st.session_state:
    st.session_state.chat_room = "화분"
if "selected_plot" not in st.session_state:
    st.session_state.selected_plot = None
if "diagnosis_result_garden" not in st.session_state:
    st.session_state.diagnosis_result_garden = None
if "editing_plot_name" not in st.session_state:
    st.session_state.editing_plot_name = False
if "confirm_delete_plot" not in st.session_state:
    st.session_state.confirm_delete_plot = False
if "home_tip" not in st.session_state:
    st.session_state.home_tip = None
if "_prev_tab" not in st.session_state:
    st.session_state._prev_tab = None
if "settings_return_page" not in st.session_state:
    st.session_state.settings_return_page = "home"
if "selected_task" not in st.session_state:
    st.session_state.selected_task = None
if "task_explain_cache" not in st.session_state:
    st.session_state.task_explain_cache = {}
if "task_explain_inflight" not in st.session_state:
    st.session_state.task_explain_inflight = set()
if "notified_milestones" not in st.session_state:
    st.session_state.notified_milestones = set()
if "review_analysis" not in st.session_state:
    st.session_state.review_analysis = None

def go_to(page: str):
    st.session_state.page = page


def L(key: str) -> str:
    return i18n.t(key, auth.get_language(st.session_state.current_email))


def current_language() -> str:
    return auth.get_language(st.session_state.current_email)


def login_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    st.write("")

    _, mid, _ = st.columns([1, 3, 1])
    with mid:
        st.markdown(
            f"""
            <div style='margin-bottom:26px; padding:0 4px;'>
                <div style='font-size:32px; font-weight:800; color:{ACCENT}; margin-bottom:14px;'>허브</div>
                <div style='font-size:17px; color:#1E293B; line-height:1.8; margin-bottom:18px; max-width:640px;'>
                    텃밭·화분 재배가 처음이어도 괜찮아요. 작물명만 알려주면
                    <span style='color:{ACCENT}; font-weight:700;'>AI가 심기부터 수확까지</span> 맞춤 가이드를
                    만들어드리고, 그 이후로도 계속 곁에서 챙겨드려요.
                </div>
                <div style='font-size:15px; color:#4B5563; line-height:2.0;'>
                    <div><span style='color:{ACCENT}; font-weight:700;'>✓</span> 작물명만 입력하면 심기부터 수확까지 단계별 일정을 자동 생성해요</div>
                    <div><span style='color:{ACCENT}; font-weight:700;'>✓</span> 식물 사진 한 장으로 AI가 생육 상태를 정밀검사하고 가이드를 다시 조정해요</div>
                    <div><span style='color:{ACCENT}; font-weight:700;'>✓</span> 텃밭 위치를 등록하면 폭염·한파·태풍 같은 날씨 위기를 매일 자동으로 알려드려요</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            if st.session_state.flash_message:
                st.success(st.session_state.flash_message)
                st.session_state.flash_message = None

            st.markdown("<h3 style='margin-bottom:2px;'>로그인</h3>", unsafe_allow_html=True)
            st.caption("이메일로 로그인하고 재배를 이어가요.")
            st.write("")

            with st.form("login_form"):
                email = st.text_input("이메일")
                password = st.text_input("비밀번호", type="password")
                keep_logged_in = st.checkbox("로그인 상태 유지", value=st.session_state.keep_logged_in)
                submitted = st.form_submit_button("로그인", use_container_width=True, type="primary")

                if submitted:
                    if not email or not password:
                        st.warning("이메일과 비밀번호를 입력해주세요.")
                    else:
                        user = auth.authenticate(email, password)
                        if user is None:
                            st.error("이메일 또는 비밀번호가 일치하지 않습니다. 가입되지 않은 계정이면 먼저 회원가입해주세요.")
                        else:
                            st.session_state.keep_logged_in = keep_logged_in
                            st.session_state.current_user = user["name"]
                            st.session_state.current_email = user["email"]
                            go_to("home")
                            st.session_state.tab = "home"
                            st.rerun()

            st.write("")
            st.caption("계정이 없으신가요?")
            if st.button("회원가입", use_container_width=True):
                go_to("signup")
                st.rerun()


def signup_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    st.markdown(f"<div class='sf-topnav-brand'>🌱 허브</div>", unsafe_allow_html=True)
    st.write("")

    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        with st.container(border=True):
            st.markdown("<h3 style='margin-bottom:2px;'>회원가입</h3>", unsafe_allow_html=True)
            st.caption("몇 가지 정보만 입력하면 바로 시작할 수 있어요.")

            with st.form("signup_form"):
                name = st.text_input("이름")
                email = st.text_input("이메일")
                password = st.text_input("비밀번호", type="password")
                password_confirm = st.text_input("비밀번호 확인", type="password")

                with st.expander(L("terms_title")):
                    st.markdown(L("terms_text"))
                    agree_terms = st.checkbox(L("terms_agree_checkbox"))

                submitted = st.form_submit_button("가입하기", use_container_width=True, type="primary")

                if submitted:
                    if not name or not email or not password:
                        st.warning("모든 항목을 입력해주세요.")
                    elif password != password_confirm:
                        st.error("비밀번호가 일치하지 않습니다.")
                    elif not agree_terms:
                        st.warning(L("terms_required_warning"))
                    else:
                        ok, message = auth.register_user(name, email, password)
                        if ok:
                            st.session_state.flash_message = f"{name}, 가입이 완료되었습니다. 로그인해주세요."
                            go_to("login")
                            st.rerun()
                        else:
                            st.error(message)

            st.divider()
            if st.button("로그인 화면으로 돌아가기", use_container_width=True):
                go_to("login")
                st.rerun()


ACCENT = "#2F8F5B"
ACCENT_SOFT = "#E7F2EB"

CARD_STYLE = """
<style>
.sf-card {
    background: #FFFFFF;
    border: 1px solid #ECE4D3;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
}
.sf-card-title {
    font-size: 15px;
    font-weight: 700;
    color: #1E293B;
    margin-bottom: 8px;
}
.sf-card-empty {
    color: #8B95A1;
    font-size: 15px;
}
.sf-empty-state {
    text-align: center;
    padding: 22px 8px;
}
.sf-empty-icon {
    font-size: 30px;
    opacity: 0.55;
    margin-bottom: 8px;
}
.sf-profile-name {
    font-size: 18px;
    font-weight: 700;
    color: #1E293B;
}
.sf-profile-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 8px;
}
.sf-avatar-placeholder {
    width: 40px;
    height: 40px;
    min-width: 40px;
    border-radius: 50%;
    background: #E7F2EB;
}
.sf-pot-item {
    display: flex;
    justify-content: space-between;
    padding: 6px 0;
    font-size: 14px;
}
.sf-pot-avatar {
    width: 48px;
    height: 48px;
    min-width: 48px;
    border-radius: 14px;
    background: linear-gradient(160deg, #E7F2EB 0%, #CFE8D8 100%);
    box-shadow: inset 0 0 0 1px rgba(47, 143, 91, 0.15);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
}
.sf-pot-meta {
    color: #8B95A1;
    font-size: 13px;
}
.sf-milestone-row {
    padding: 8px 0;
    font-size: 14px;
    border-bottom: 1px solid #EFE8D9;
}
.sf-milestone-row:last-child {
    border-bottom: none;
}
.sf-chat-msg {
    padding: 8px 4px;
    font-size: 14px;
    border-bottom: 1px solid #EFE8D9;
}
.sf-chat-msg-ai {
    padding: 8px;
    font-size: 14px;
    background: #E7F2EB;
    border-radius: 8px;
    margin: 4px 0;
}
.sf-chat-time {
    color: #B0B0B0;
    font-size: 11px;
    margin-left: 6px;
}
.st-key-topnav_wrap {
    border-bottom: 1px solid #ECE4D3;
    padding-bottom: 14px;
    margin-bottom: 28px;
}
.st-key-topnav_wrap [data-testid="stVerticalBlockBorderWrapper"] {
    border: none;
}
.sf-topnav-brand {
    font-size: 22px;
    font-weight: 800;
    color: #2F8F5B;
    letter-spacing: -0.5px;
    padding-top: 6px;
}
.st-key-topnav_home button,
.st-key-topnav_chat button,
.st-key-topnav_settings button {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: #1E293B !important;
    font-weight: 600 !important;
}
.st-key-topnav_home button:disabled,
.st-key-topnav_chat button:disabled,
.st-key-topnav_settings button:disabled {
    color: #2F8F5B !important;
    border-bottom: 2px solid #2F8F5B !important;
    border-radius: 0 !important;
    opacity: 1 !important;
}
</style>
"""


def _fetch_task_explanation_bg(cache_key, species, kind_label, size, title, desc, api_key, language):
    explanation = ai.explain_task(species, kind_label, size, title, desc, api_key=api_key, language=language)
    st.session_state.task_explain_cache[cache_key] = explanation
    st.session_state.task_explain_inflight.discard(cache_key)


def _send_ai_chat_message(ai_room_key, room, bot_name, text):
    chat.add_message(ai_room_key, st.session_state.current_user, text)
    api_messages = [
        {"role": "assistant" if m["is_ai"] else "user", "content": m["text"]}
        for m in chat.get_messages(ai_room_key)
    ]
    with st.spinner(L("chat_ai_thinking").format(bot=bot_name)):
        reply = ai.continue_ai_chat(room, api_messages, language=current_language())
    chat.add_message(ai_room_key, bot_name, reply or L("ai_reply_fallback_error"), is_ai=True)


def _email_change_dialog():
    @st.dialog(L("setting_email"))
    def _inner():
        st.caption(f"{L('current_email_prefix')}{st.session_state.current_email}")
        new_email = st.text_input(L("new_email_label"), key="email_change_new")
        password = st.text_input(L("password_label"), type="password", key="email_change_pw")
        password_confirm = st.text_input(L("password_confirm_label"), type="password", key="email_change_pw2")

        mismatch = password and password_confirm and password != password_confirm
        if mismatch:
            st.caption(f":red[{L('password_mismatch_msg')}]")

        can_submit = bool(new_email.strip() and password and password_confirm and not mismatch)
        if st.button(L("change_submit"), use_container_width=True, disabled=not can_submit, key="email_change_submit", type="primary"):
            ok, msg = auth.change_email(st.session_state.current_email, password, new_email.strip())
            if ok:
                old_email = st.session_state.current_email
                new_email_clean = new_email.strip()
                pots.rename_owner(old_email, new_email_clean)
                gardens.rename_owner(old_email, new_email_clean)
                chat.rename_owner(old_email, new_email_clean)
                st.session_state.current_email = new_email_clean
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)

    _inner()


def _password_change_dialog():
    @st.dialog(L("setting_password"))
    def _inner():
        current_password = st.text_input(L("current_password_label"), type="password", key="pw_change_current")
        new_password = st.text_input(L("new_password_label"), type="password", key="pw_change_new")
        new_password_confirm = st.text_input(L("new_password_confirm_label"), type="password", key="pw_change_new2")

        mismatch = new_password and new_password_confirm and new_password != new_password_confirm
        if mismatch:
            st.caption(f":red[{L('new_password_mismatch_msg')}]")

        can_submit = bool(current_password and new_password and new_password_confirm and not mismatch)
        if st.button(L("change_submit"), use_container_width=True, disabled=not can_submit, key="pw_change_submit", type="primary"):
            ok, msg = auth.change_password(st.session_state.current_email, current_password, new_password)
            if ok:
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)

    _inner()


def _language_dialog():
    @st.dialog(L("setting_language"))
    def _inner():
        lang_codes = [code for code, _ in i18n.LANGUAGES]
        lang_labels = dict(i18n.LANGUAGES)
        current_lang = current_language()
        new_lang = st.selectbox(
            L("setting_language"),
            options=lang_codes,
            index=lang_codes.index(current_lang) if current_lang in lang_codes else 0,
            format_func=lambda c: lang_labels[c],
            key="setting_language_select",
        )
        if new_lang != current_lang:
            auth.set_language(st.session_state.current_email, new_lang)
            st.rerun()

    _inner()


def _delete_account_dialog():
    @st.dialog(L("setting_delete"))
    def _inner():
        st.warning(L("delete_account_warning"))
        password = st.text_input(L("password_confirm_label"), type="password", key="delete_account_pw")

        can_submit = bool(password)
        if st.button(L("delete_account_confirm_button"), use_container_width=True, disabled=not can_submit, key="delete_account_submit"):
            email = st.session_state.current_email
            ok, msg = auth.delete_account(email, password)
            if ok:
                pots.delete_owner(email)
                gardens.delete_owner(email)
                chat.delete_owner(email)
                st.session_state.current_user = None
                st.session_state.current_email = None
                go_to("login")
                st.rerun()
            else:
                st.error(msg)

    _inner()


def _privacy_dialog():
    @st.dialog(L("setting_privacy"))
    def _inner():
        st.markdown(L("privacy_policy_text"))

    _inner()


def _due_milestone_messages(email):
    """오늘 날짜가 된, 아직 알리지 않은 가이드라인 일정을 모은다. day=0(등록일)은 제외한다."""
    today = datetime.date.today()
    messages = []
    for pot in pots.get_pots(email):
        planted = datetime.date.fromisoformat(pot["planted_date"])
        for m in pot["milestones"]:
            if m["day"] == 0:
                continue
            if planted + datetime.timedelta(days=m["day"]) == today:
                key = f"pot:{pot['name']}:{m['day']}:{today.isoformat()}"
                if key not in st.session_state.notified_milestones:
                    messages.append((key, f"[{pot['name']}] {m['title']} - {m['desc']}"))
    for plot in gardens.get_plots(email):
        planted = datetime.date.fromisoformat(plot["planted_date"])
        for m in plot["milestones"]:
            if m["day"] == 0:
                continue
            if planted + datetime.timedelta(days=m["day"]) == today:
                key = f"plot:{plot['name']}:{m['day']}:{today.isoformat()}"
                if key not in st.session_state.notified_milestones:
                    messages.append((key, f"[{plot['name']}] {m['title']} - {m['desc']}"))
    return messages


def _weather_risk_messages(email):
    """위치가 설정된 텃밭에 대해 하루 한 번 날씨 긴급 위기 여부를 확인하고, 위험하면 메시지를 반환한다."""
    today_iso = datetime.date.today().isoformat()
    language = auth.get_language(email)
    plots_to_check = [
        p for p in gardens.get_plots(email)
        if p.get("location") and p.get("weather_check_date") != today_iso
    ]
    if plots_to_check:
        with st.spinner(i18n.t("weather_risk_checking", language)):
            for plot in plots_to_check:
                result = ai.check_weather_risk(plot["species"], "텃밭", plot["location"], language=language)
                risk = bool(result and result.get("risk"))
                message = (result or {}).get("message", "") if risk else ""
                gardens.set_weather_alert(email, plot["name"], today_iso, risk, message)

    by_location = {}
    for plot in gardens.get_plots(email):
        if (
            plot.get("location")
            and plot.get("weather_check_date") == today_iso
            and plot.get("weather_risk")
            and plot.get("weather_message")
        ):
            group = by_location.setdefault(plot["location"], {"names": [], "message": plot["weather_message"]})
            group["names"].append(plot["name"])

    messages = []
    for location, group in by_location.items():
        names = ", ".join(group["names"])
        key = f"weather:{location}:{today_iso}"
        messages.append((key, f"[{names}] {group['message']}"))
    return messages


def _md_safe(text):
    """AI/사용자 생성 텍스트의 홑물결(~)이 마크다운 취소선(~~text~~)으로 잘못 해석되는 것을 막는다."""
    return text.replace("~", "\\~") if isinstance(text, str) else text


def _empty_state(icon: str, text: str):
    st.markdown(
        f"<div class='sf-empty-state'><div class='sf-empty-icon'>{icon}</div>"
        f"<div class='sf-card-empty'>{text}</div></div>",
        unsafe_allow_html=True,
    )


def _render_fertilizer_advice(species, kind):
    lang = current_language()
    advice = fertilizer.get_advice(species, kind, language=lang)
    kind_display = L("kind_pot") if kind == "화분" else L("kind_garden")
    if advice:
        st.caption(f"{advice['emoji']} {_md_safe(advice['title'])}")
        st.markdown(f"**{L('feature_label')}**: {_md_safe(advice['feature'])}")
        st.markdown(f"**{L('cultivation_tip_label').format(kind=kind_display)}**: {_md_safe(advice['tip'])}")
        st.markdown(f"- {L('base_fertilizer_label')}: {_md_safe(advice['base'])}")
        st.markdown(f"- {L('top_fertilizer_label')}: {_md_safe(advice['top'])}")
        if advice.get("extra"):
            st.markdown(f"- {L('caution_label')}: {_md_safe(advice['extra'])}")
    else:
        st.markdown(
            f"<div class='sf-card-empty'>{L('fertilizer_unavailable')}</div>", unsafe_allow_html=True,
        )
    with st.expander(L("common_fertilizer_expander")):
        for tip in fertilizer.COMMON_TIPS:
            st.markdown(f"**{_md_safe(tip['title'])}**")
            st.markdown(_md_safe(tip["desc"]))


def _fire_browser_notifications(messages):
    payload = json.dumps(messages, ensure_ascii=False)
    notif_title = L("browser_notification_title")
    components.html(
        f"""
        <script>
        (function() {{
            const msgs = {payload};
            function fire() {{
                msgs.forEach(function(m) {{ new Notification('{notif_title}', {{ body: m }}); }});
            }}
            if (typeof Notification === 'undefined') return;
            if (Notification.permission === 'granted') {{
                fire();
            }} else if (Notification.permission !== 'denied') {{
                Notification.requestPermission().then(function(p) {{ if (p === 'granted') fire(); }});
            }}
        }})();
        </script>
        """,
        height=0,
    )


def _topnav():
    on_home_page = st.session_state.page == "home"
    with st.container(key="topnav_wrap"):
        brand_col, _spacer_col, nav1, nav2, nav3 = st.columns([2, 3, 1, 1, 1])
        with brand_col:
            st.markdown("<div class='sf-topnav-brand'>🌱 허브</div>", unsafe_allow_html=True)
        with nav1:
            if st.button(L("nav_home"), use_container_width=True, key="topnav_home", disabled=(on_home_page and st.session_state.tab == "home")):
                go_to("home")
                st.session_state.tab = "home"
                st.rerun()
        with nav2:
            if st.button(L("nav_chat"), use_container_width=True, key="topnav_chat", disabled=(on_home_page and st.session_state.tab == "chat")):
                go_to("home")
                st.session_state.tab = "chat"
                st.rerun()
        with nav3:
            if st.button(L("nav_settings"), use_container_width=True, key="topnav_settings", disabled=(on_home_page and st.session_state.tab == "settings")):
                go_to("home")
                st.session_state.tab = "settings"
                st.rerun()


def home_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    _topnav()

    if auth.get_alarm_enabled(st.session_state.current_email):
        due = _due_milestone_messages(st.session_state.current_email)
        if due:
            for key, _ in due:
                st.session_state.notified_milestones.add(key)
            _fire_browser_notifications([text for _, text in due])

    weather_due = _weather_risk_messages(st.session_state.current_email)
    if weather_due:
        new_keys = [key for key, _ in weather_due if key not in st.session_state.notified_milestones]
        if new_keys:
            st.session_state.notified_milestones.update(new_keys)
            _fire_browser_notifications([text for key, text in weather_due if key in new_keys])
        for _, text in weather_due:
            st.warning(f"🚨 {_md_safe(text)}")

    user_icon = auth.get_icon(st.session_state.current_email)
    if user_icon.get("type") == "photo":
        pos = user_icon.get("position", {"x": 50, "y": 50})
        avatar_html = (
            f"<div class='sf-avatar-placeholder' style='overflow:hidden;background:transparent;'>"
            f"<img src='{user_icon['value']}' style='width:100%;height:100%;object-fit:cover;"
            f"object-position:{pos['x']}% {pos['y']}%;' /></div>"
        )
    elif user_icon.get("type") == "color":
        avatar_html = f"<div class='sf-avatar-placeholder' style='background:{user_icon['value']};'></div>"
    else:
        avatar_html = (
            f"<div class='sf-avatar-placeholder' style='display:flex;align-items:center;"
            f"justify-content:center;font-size:20px;'>{user_icon.get('value', '🙂')}</div>"
        )
    st.markdown(
        f"<div class='sf-profile-row'>"
        f"{avatar_html}"
        f"<div class='sf-profile-name'>{st.session_state.current_user}</div>"
        f"</div>",
        unsafe_allow_html=True,
    )

    st.write("")

    if st.session_state.flash_message:
        st.success(st.session_state.flash_message)
        st.session_state.flash_message = None

    if st.session_state.tab == "home":
        user_pots = pots.get_pots(st.session_state.current_email)
        user_plots = gardens.get_plots(st.session_state.current_email)

        pot_tasks = pots.todays_tasks(st.session_state.current_email)
        plot_tasks = gardens.this_month_tasks(st.session_state.current_email)
        review_pending_pots = [p for p in user_pots if pots.is_harvested(p) and not p.get("review")]
        review_pending_plots = [p for p in user_plots if gardens.is_harvested(p) and not p.get("review")]
        lang = current_language()

        main_col, side_col = st.columns([2, 1], gap="large")

        with main_col:
            with st.container(border=True):
                st.markdown(f"<div class='sf-card-title'>{L('today_tasks_pot')}</div>", unsafe_allow_html=True)
                if pot_tasks or review_pending_pots:
                    for t in pot_tasks:
                        mark = "✅" if t["done"] else "☐"
                        st.markdown(f"{mark} [{t['pot_name']}] {t['title']} — {t['desc']}")
                        if st.button(L("view_details"), key=f"task_detail_pot_{t['pot_name']}_{t['day']}"):
                            st.session_state.selected_task = {
                                "kind": "pot", "item_name": t["pot_name"], "day": t["day"],
                                "title": t["title"], "desc": t["desc"],
                            }
                            go_to("task_detail")
                            st.rerun()
                        st.write("")
                    for p in review_pending_pots:
                        if st.button(
                            f"[{p['name']}] {L('write_review')}",
                            key=f"review_task_pot_{p['name']}",
                            use_container_width=True,
                        ):
                            st.session_state.selected_pot = p["name"]
                            go_to("pot_review")
                            st.rerun()
                else:
                    _empty_state("✅", L("no_tasks_today"))

            st.write("")

            with st.container(border=True):
                st.markdown(f"<div class='sf-card-title'>{L('month_tasks_plot')}</div>", unsafe_allow_html=True)
                if plot_tasks or review_pending_plots:
                    for t in plot_tasks:
                        mark = "✅" if t["done"] else "☐"
                        st.markdown(f"{mark} {t['date'].strftime('%m/%d')} · [{t['pot_name']}] {t['title']} — {t['desc']}")
                        if st.button(L("view_details"), key=f"task_detail_plot_{t['pot_name']}_{t['day']}"):
                            st.session_state.selected_task = {
                                "kind": "plot", "item_name": t["pot_name"], "day": t["day"],
                                "title": t["title"], "desc": t["desc"],
                            }
                            go_to("task_detail")
                            st.rerun()
                        st.write("")
                    for p in review_pending_plots:
                        if st.button(
                            f"[{p['name']}] {L('write_review')}",
                            key=f"review_task_plot_{p['name']}",
                            use_container_width=True,
                        ):
                            st.session_state.selected_plot = p["name"]
                            go_to("plot_review")
                            st.rerun()
                else:
                    _empty_state("✅", L("no_tasks_month"))

            st.write("")

            if (
                st.session_state.home_tip is None
                or st.session_state._prev_tab != "home"
                or st.session_state.get("home_tip_lang") != lang
            ):
                all_species = [p["species"] for p in user_pots] + [p["species"] for p in user_plots]
                st.session_state.home_tip = tips.get_tip(all_species, language=lang)
                st.session_state.home_tip_lang = lang
            tip_species, tip_text = st.session_state.home_tip
            tip_title = f"💡 TIP · {i18n.species_name(tip_species, lang)}" if tip_species else f"💡 {L('today_tip')}"
            st.markdown(
                f"<div class='sf-card'><div class='sf-card-title'>{tip_title}</div>"
                f"<div class='sf-card-empty'>{tip_text}</div></div>",
                unsafe_allow_html=True,
            )

        with side_col:
            with st.container(border=True):
                st.markdown(f"<div class='sf-card-title'>{L('my_pots')}</div>", unsafe_allow_html=True)
                if user_pots:
                    for pot in user_pots:
                        if st.button(
                            f"{pot['emoji']} {pot['name']} · {i18n.species_name(pot['species'], lang)} · {i18n.size_name(pot['size'], lang)}",
                            key=f"pot_tile_{pot['name']}",
                            use_container_width=True,
                        ):
                            st.session_state.selected_pot = pot["name"]
                            st.session_state.diagnosis_result = None
                            st.session_state.confirm_delete_pot = False
                            go_to("pot_detail")
                            st.rerun()
                else:
                    _empty_state("🪴", L("no_pots"))

                if st.button(L("add_pot"), use_container_width=True, type="primary"):
                    go_to("register_pot")
                    st.rerun()

            st.write("")

            with st.container(border=True):
                st.markdown(f"<div class='sf-card-title'>{L('my_plots')}</div>", unsafe_allow_html=True)
                if user_plots:
                    for plot in user_plots:
                        if st.button(
                            f"{plot['emoji']} {plot['name']} · {i18n.species_name(plot['species'], lang)} · {i18n.size_name(plot['size'], lang)}",
                            key=f"plot_tile_{plot['name']}",
                            use_container_width=True,
                        ):
                            st.session_state.selected_plot = plot["name"]
                            st.session_state.diagnosis_result_garden = None
                            st.session_state.confirm_delete_plot = False
                            go_to("plot_detail")
                            st.rerun()
                else:
                    _empty_state("🌾", L("no_plots"))

                if st.button(L("add_plot"), use_container_width=True, type="primary"):
                    go_to("register_plot")
                    st.rerun()

    elif st.session_state.tab == "chat":
        room = st.session_state.chat_room
        kind_display = L("kind_pot") if room == "화분" else L("kind_garden")
        bot_name = L("bot_name_pot") if room == "화분" else L("bot_name_garden")

        sub1, sub2 = st.columns(2)
        with sub1:
            if st.button(L("chat_users"), use_container_width=True, key="chat_sub_users", disabled=(st.session_state.chat_subview == "users")):
                st.session_state.chat_subview = "users"
                st.rerun()
        with sub2:
            if st.button(f"{bot_name} {L('chat_ai_1on1')}", use_container_width=True, key="chat_sub_ai", disabled=(st.session_state.chat_subview == "ai")):
                st.session_state.chat_subview = "ai"
                st.rerun()

        st.write("")

        if st.session_state.chat_subview == "users":
            chat.maybe_reset_daily(room)

            with st.container(border=True):
                st.markdown(f"<div class='sf-card-title'>{L('chat_room_title').format(kind=kind_display)}</div>", unsafe_allow_html=True)
                st.caption(L("chat_room_desc").format(kind=kind_display))

                messages = chat.get_messages(room)
                with st.container(height=320):
                    if messages:
                        for m in messages:
                            st.markdown(
                                f"<div class='sf-chat-msg'><b>{m['sender']}</b>"
                                f"<span class='sf-chat-time'>{m['timestamp']}</span><br>{m['text']}</div>",
                                unsafe_allow_html=True,
                            )
                    else:
                        _empty_state("💬", L("chat_no_messages"))

                with st.form(f"user_chat_form_{room}", clear_on_submit=True):
                    message_text = st.text_input(
                        L("message_input_label"), label_visibility="collapsed", placeholder=L("chat_message_placeholder")
                    )
                    sent = st.form_submit_button(L("chat_send"), use_container_width=True, type="primary")

                if sent and message_text.strip():
                    chat.add_message(room, st.session_state.current_user, message_text.strip())
                    st.rerun()

        else:
            ai_room_key = f"ai::{room}::{st.session_state.current_email}"
            chat.maybe_reset_daily(ai_room_key)
            with st.container(border=True):
                title_col, toggle_col = st.columns([4, 1])
                with title_col:
                    st.markdown(f"<div class='sf-card-title'>{L('chat_ai_title').format(bot=bot_name)}</div>", unsafe_allow_html=True)
                with toggle_col:
                    if st.button(bot_name, key="chat_room_toggle_ai", use_container_width=True, help=L("chat_bot_toggle_help")):
                        st.session_state.chat_room = "텃밭" if room == "화분" else "화분"
                        st.rerun()
                st.caption(L("chat_ai_desc").format(kind=kind_display))

                ai_messages = chat.get_messages(ai_room_key)
                with st.container(height=320):
                    if ai_messages:
                        for m in ai_messages:
                            if m["is_ai"]:
                                st.markdown(
                                    f"<div class='sf-chat-msg-ai'><b>{bot_name}</b>"
                                    f"<span class='sf-chat-time'>{m['timestamp']}</span><br>{m['text']}</div>",
                                    unsafe_allow_html=True,
                                )
                            else:
                                st.markdown(
                                    f"<div class='sf-chat-msg'><b>{L('chat_me_label')}</b>"
                                    f"<span class='sf-chat-time'>{m['timestamp']}</span><br>{m['text']}</div>",
                                    unsafe_allow_html=True,
                                )
                    else:
                        st.markdown(
                            f"<div class='sf-card-empty'>{bot_name} · {L('chat_ai_placeholder')}</div>",
                            unsafe_allow_html=True,
                        )

                if not ai_messages:
                    st.caption(L("chat_suggested_label"))
                    suggested_questions = [L("chat_suggested_q1"), L("chat_suggested_q2"), L("chat_suggested_q3")]
                    q_cols = st.columns(len(suggested_questions))
                    for i, (col, question) in enumerate(zip(q_cols, suggested_questions)):
                        with col:
                            if st.button(question, key=f"chat_suggested_{room}_{i}", use_container_width=True):
                                _send_ai_chat_message(ai_room_key, room, bot_name, question)
                                st.rerun()

                with st.form(f"ai_chat_form_{room}", clear_on_submit=True):
                    ai_message_text = st.text_input(
                        L("ai_message_input_label"), label_visibility="collapsed", placeholder=f"{bot_name} · {L('chat_ai_placeholder')}"
                    )
                    ai_sent = st.form_submit_button(f"{bot_name} · {L('chat_send')}", use_container_width=True, type="primary")

                if ai_sent and ai_message_text.strip():
                    _send_ai_chat_message(ai_room_key, room, bot_name, ai_message_text.strip())
                    st.rerun()

    elif st.session_state.tab == "settings":
        with st.container(border=True):
            st.markdown(f"<div class='sf-card-title'>{L('settings_title')}</div>", unsafe_allow_html=True)
            if st.button(L("setting_icon"), use_container_width=True, key="setting_icon"):
                st.session_state.settings_return_page = "home"
                go_to("icon_screen")
                st.rerun()
            if st.button(L("setting_alarm"), use_container_width=True, key="setting_alarm"):
                st.session_state.settings_return_page = "home"
                go_to("alarm_screen")
                st.rerun()
            if st.button(L("setting_language"), use_container_width=True, key="setting_language_btn"):
                _language_dialog()

            if st.button(L("setting_email"), use_container_width=True, key="setting_email"):
                _email_change_dialog()
            if st.button(L("setting_password"), use_container_width=True, key="setting_password"):
                _password_change_dialog()
            if st.button(L("setting_logout"), use_container_width=True, key="logout"):
                st.session_state.current_user = None
                st.session_state.current_email = None
                go_to("login")
                st.rerun()
            if st.button(L("setting_delete"), use_container_width=True, key="setting_delete"):
                _delete_account_dialog()
            if st.button(L("setting_privacy"), use_container_width=True, key="setting_privacy"):
                _privacy_dialog()

    st.session_state._prev_tab = st.session_state.tab


@st.fragment(run_every="1s")
def _task_explanation_fragment(cache_key, species, kind_label, size, title, desc):
    # 이 조각(fragment)만 1초마다 자체적으로 새로고침된다. 전체 페이지(task_detail_screen)는
    # 매번 정상적으로 끝까지 실행되므로, 이전 화면의 잔여 요소가 남는 문제가 생기지 않는다.
    if cache_key not in st.session_state.task_explain_cache:
        if cache_key not in st.session_state.task_explain_inflight:
            st.session_state.task_explain_inflight.add(cache_key)
            resolved_api_key = ai._get_api_key()
            resolved_language = current_language()
            bg_thread = threading.Thread(
                target=_fetch_task_explanation_bg,
                args=(cache_key, species, kind_label, size, title, desc, resolved_api_key, resolved_language),
                daemon=True,
            )
            add_script_run_ctx(bg_thread, get_script_run_ctx())
            bg_thread.start()
        with st.container(border=True):
            st.info(L("generating_explanation_spinner"))
        return

    explanation = st.session_state.task_explain_cache.get(cache_key)
    with st.container(border=True):
        if explanation:
            st.markdown(_md_safe(explanation))
        else:
            st.markdown(
                f"<div class='sf-card-empty'>{L('explanation_failed_fallback').format(desc=desc)}</div>",
                unsafe_allow_html=True,
            )


def task_detail_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    _topnav()

    task = st.session_state.selected_task
    if not task:
        st.error(L("task_not_found"))
        if st.button(L("back_to_home"), key="task_detail_not_found_home"):
            go_to("home")
            st.rerun()
        return

    if task["kind"] == "pot":
        item = pots.get_pot(st.session_state.current_email, task["item_name"])
        kind_label = "화분"
    else:
        item = gardens.get_plot(st.session_state.current_email, task["item_name"])
        kind_label = "텃밭"

    if item is None:
        st.error(L("info_not_found"))
        if st.button(L("back_to_home"), key="task_detail_missing_home"):
            go_to("home")
            st.rerun()
        return

    if st.button(L("back"), key="task_detail_back"):
        go_to("home")
        st.rerun()

    kind_label_display = L("kind_pot") if task["kind"] == "pot" else L("kind_garden")
    st.markdown(
        f"<div style='text-align:center; font-size:18px; font-weight:700;'>{item['emoji']} {task['title']}</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='text-align:center; font-size:13px; color:gray;'>{item['name']} · {i18n.species_name(item['species'], current_language())} ({kind_label_display})</p>",
        unsafe_allow_html=True,
    )
    st.write("")

    current_done = next((m.get("done", False) for m in item["milestones"] if m["day"] == task["day"]), False)
    checked = st.checkbox(L("task_done_checkbox"), value=current_done, key=f"task_detail_done_{task['kind']}_{task['item_name']}_{task['day']}")
    if checked != current_done:
        if task["kind"] == "pot":
            pots.set_task_done(st.session_state.current_email, task["item_name"], task["day"], checked)
        else:
            gardens.set_task_done(st.session_state.current_email, task["item_name"], task["day"], checked)
        st.rerun()

    st.write("")

    with st.container(border=True):
        st.markdown(f"<div class='sf-card-title'>{L('one_line_summary')}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='sf-card-empty'>{task['desc']}</div>", unsafe_allow_html=True)

    st.write("")

    cache_key = f"{task['kind']}:{task['item_name']}:{task['day']}"
    _task_explanation_fragment(cache_key, item["species"], kind_label, item["size"], task["title"], task["desc"])


def register_pot_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    _topnav()
    lang = current_language()
    st.markdown(f"<h1 style='text-align:center;'>{L('new_pot_title')}</h1>", unsafe_allow_html=True)
    st.write("")

    species_options = list(pots.CROP_GUIDES.keys()) + ["기타"]
    species_choice = st.selectbox(
        L("species_to_plant"), species_options,
        format_func=lambda s: L("other_species") if s == "기타" else i18n.species_name(s, lang),
    )
    species_final = species_choice
    if species_choice == "기타":
        species_final = st.text_input(L("custom_species_prompt"))

    size = st.selectbox(L("pot_size_label"), pots.SIZE_OPTIONS, format_func=lambda s: i18n.size_name(s, lang))
    name = st.text_input(L("pot_name_label"))

    st.write("")
    if st.button(L("register_button"), use_container_width=True, type="primary"):
        if not name or not species_final:
            st.warning(L("register_warning_pot"))
        elif pots.get_pot(st.session_state.current_email, name.strip()):
            st.warning(L("duplicate_pot_name"))
        else:
            with st.spinner(L("generating_guide_spinner")):
                pots.add_pot(st.session_state.current_email, name, species_final, size)
            st.session_state.flash_message = L("pot_registered_flash").format(name=name)
            go_to("home")
            st.session_state.tab = "home"
            st.rerun()

    if st.button(L("cancel_and_back")):
        go_to("home")
        st.rerun()


def pot_detail_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    _topnav()

    pot = pots.get_pot(st.session_state.current_email, st.session_state.selected_pot)
    lang = current_language()

    if pot is None:
        st.error(L("pot_not_found"))
        if st.button(L("back_to_home")):
            go_to("home")
            st.rerun()
        return

    if st.button(L("back")):
        st.session_state.selected_pot = None
        st.session_state.diagnosis_result = None
        st.session_state.editing_pot_name = False
        st.session_state.confirm_delete_pot = False
        go_to("home")
        st.rerun()

    if st.session_state.flash_message:
        st.success(st.session_state.flash_message)
        st.session_state.flash_message = None

    planted = datetime.date.fromisoformat(pot["planted_date"])
    today = datetime.date.today()

    # 프로필 행과 같은 스타일의 좌측 정렬 헤더
    avatar_col, name_col, edit_col = st.columns([1, 4, 2])
    with avatar_col:
        st.markdown(f"<div class='sf-pot-avatar'>{pot['emoji']}</div>", unsafe_allow_html=True)
    with name_col:
        if st.session_state.editing_pot_name:
            pass
        else:
            st.markdown(f"<div class='sf-profile-name'>{pot['name']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='sf-pot-meta'>{i18n.species_name(pot['species'], lang)} · {i18n.size_name(pot['size'], lang)}</div>", unsafe_allow_html=True)
    with edit_col:
        if not st.session_state.editing_pot_name:
            if st.button(L("edit_name"), use_container_width=True):
                st.session_state.editing_pot_name = True
                st.rerun()

    if st.session_state.editing_pot_name:
        new_name = st.text_input(L("new_pot_name_label"), value=pot["name"], key="rename_input")
        save_col, cancel_col = st.columns(2)
        with save_col:
            if st.button(L("save"), use_container_width=True):
                new_name_clean = new_name.strip()
                if new_name_clean and new_name_clean != pot["name"]:
                    if pots.get_pot(st.session_state.current_email, new_name_clean):
                        st.warning(L("duplicate_pot_name"))
                    else:
                        pots.rename_pot(st.session_state.current_email, pot["name"], new_name_clean)
                        st.session_state.selected_pot = new_name_clean
                        st.session_state.editing_pot_name = False
                        st.rerun()
                else:
                    st.session_state.editing_pot_name = False
                    st.rerun()
        with cancel_col:
            if st.button(L("cancel"), use_container_width=True):
                st.session_state.editing_pot_name = False
                st.rerun()

    if pot.get("guide_source") == "ai":
        st.caption(L("guide_ai_caption"))
    else:
        st.caption(L("guide_default_caption"))

    st.write("")

    pot_care = care.get_care(pot["species"])
    main_col, side_col = st.columns([2, 1], gap="large")

    with main_col:
        with st.container(border=True):
            st.markdown(f"<div class='sf-card-title'>{L('current_status_memo')}</div>", unsafe_allow_html=True)
            memo = st.text_input(
                L("memo_label"), value=pot.get("memo", ""), label_visibility="collapsed",
                placeholder=L("memo_placeholder"), key="pot_memo_input",
            )
            if memo != pot.get("memo", ""):
                pots.set_memo(st.session_state.current_email, pot["name"], memo)

        st.write("")

        with st.container(border=True):
            st.markdown(f"<div class='sf-card-title'>{L('guideline_title')}</div>", unsafe_allow_html=True)
            total_steps = len(pot["milestones"])
            done_steps = sum(
                1 for m in pot["milestones"]
                if m.get("done", False) or (planted + datetime.timedelta(days=m["day"])) <= today
            )
            if total_steps:
                st.progress(done_steps / total_steps, text=L("guideline_progress").format(done=done_steps, total=total_steps))
            for m in pot["milestones"]:
                target = planted + datetime.timedelta(days=m["day"])
                mark = "✅" if m.get("done", False) or target <= today else "⏳"
                st.markdown(
                    f"<div class='sf-milestone-row'>{mark} <b>{target.strftime('%m/%d')}</b> — {m['title']}: {m['desc']}</div>",
                    unsafe_allow_html=True,
                )

        st.write("")

        with st.container(border=True):
            st.markdown(f"<div class='sf-card-title'>{L('photo_diagnosis_title')}</div>", unsafe_allow_html=True)
            st.caption(L("photo_diagnosis_caption"))
            uploaded = st.file_uploader(L("upload_photo"), type=["png", "jpg", "jpeg"], key="photo_uploader")

            if uploaded is not None:
                st.image(uploaded, width=300)
                if st.button(L("start_ai_diagnosis"), use_container_width=True, type="primary"):
                    elapsed_days = (today - planted).days
                    with st.spinner(L("analyzing_photo_spinner")):
                        result = ai.diagnose_photo(
                            pot["species"], pot["size"], elapsed_days, pot["milestones"],
                            uploaded.getvalue(), uploaded.type,
                            history=pot.get("diagnosis_history", []),
                            language=lang,
                        )
                    if result:
                        st.session_state.diagnosis_result = result
                        pots.add_diagnosis_record(
                            st.session_state.current_email, pot["name"],
                            today.isoformat(), elapsed_days, result["diagnosis"],
                        )
                    else:
                        st.error(L("diagnosis_failed"))
                    st.rerun()

            if st.session_state.diagnosis_result:
                result = st.session_state.diagnosis_result
                st.success(_md_safe(result["diagnosis"]))
                st.caption(L("adjusted_guide_preview"))
                for m in result["milestones"]:
                    target = planted + datetime.timedelta(days=m["day"])
                    st.markdown(f"• **{target.strftime('%m/%d')}** — {_md_safe(m['title'])}: {_md_safe(m['desc'])}")

                if st.button(L("update_guide_button"), use_container_width=True, type="primary"):
                    pots.update_pot_milestones(st.session_state.current_email, pot["name"], result["milestones"])
                    st.session_state.diagnosis_result = None
                    st.toast(L("guide_updated_flash"))
                    go_to("home")
                    st.session_state.tab = "home"
                    st.rerun()

            history = pot.get("diagnosis_history", [])
            if history:
                with st.expander(L("growth_history_title").format(n=len(history))):
                    for h in reversed(history):
                        st.markdown(f"**{h['date']}** ({L('days_since_planted').format(n=h['elapsed_days'])}) — {_md_safe(h['diagnosis'])}")

    with side_col:
        with st.container(border=True):
            st.markdown(f"<div class='sf-card-title'>{L('soil_title')}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='sf-card-empty'>{pot_care['soil']}</div>", unsafe_allow_html=True)

        st.write("")

        with st.container(border=True):
            st.markdown(f"<div class='sf-card-title'>{L('fertilizer_title')}</div>", unsafe_allow_html=True)
            _render_fertilizer_advice(pot["species"], "화분")
            st.markdown(f"<div class='sf-card-title' style='margin-top:12px;'>{L('homemade_fertilizer_title')}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='sf-card-empty'>{pot_care['homemade']}</div>", unsafe_allow_html=True)

    if pot["milestones"]:
        last_milestone = pot["milestones"][-1]
        harvest_date = planted + datetime.timedelta(days=last_milestone["day"])
        harvest_reached = last_milestone.get("done", False) or harvest_date <= today
    else:
        harvest_reached = False

    if harvest_reached:
        st.write("")
        with st.container(border=True):
            st.markdown(f"<div class='sf-card-title'>{L('harvest_review_title')}</div>", unsafe_allow_html=True)
            if pot.get("review"):
                difficulty_display = L("difficulty_easy") if pot.get("difficulty") == "쉬웠어요" else L("difficulty_hard") if pot.get("difficulty") == "어려웠어요" else pot.get("difficulty", "-")
                st.markdown(f"<div class='sf-card-empty'>{L('difficulty_label').format(value=difficulty_display)}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='sf-card-empty'>{pot['review']}</div>", unsafe_allow_html=True)
                st.success(_md_safe(pot.get("recommendation")) or L("no_recommendation"))
            else:
                st.caption(L("harvest_reached_caption"))
                if st.button(L("go_write_review"), use_container_width=True, key=f"go_review_pot_{pot['name']}", type="primary"):
                    st.session_state.selected_pot = pot["name"]
                    go_to("pot_review")
                    st.rerun()

    st.write("")
    with st.container(key="delete_pot_container"):
        if st.button(L("delete_button"), use_container_width=True, key="delete_pot_btn"):
            st.session_state.confirm_delete_pot = True
            st.rerun()
    st.markdown(
        "<style>.st-key-delete_pot_container button { color: #E53935 !important; "
        "border-color: #E53935 !important; }</style>",
        unsafe_allow_html=True,
    )

    if st.session_state.confirm_delete_pot:
        st.warning(L("confirm_delete_pot").format(name=pot['name']))
        confirm_col, cancel_col = st.columns(2)
        with confirm_col:
            if st.button(L("yes_delete"), use_container_width=True, key="confirm_delete_pot_btn"):
                pots.delete_pot(st.session_state.current_email, pot["name"])
                st.session_state.confirm_delete_pot = False
                st.session_state.selected_pot = None
                st.session_state.diagnosis_result = None
                st.session_state.flash_message = L("pot_deleted_flash").format(name=pot['name'])
                go_to("home")
                st.rerun()
        with cancel_col:
            if st.button(L("cancel"), use_container_width=True, key="cancel_delete_pot_btn"):
                st.session_state.confirm_delete_pot = False
                st.rerun()


def register_plot_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    _topnav()
    lang = current_language()
    st.markdown(f"<h1 style='text-align:center;'>{L('new_plot_title')}</h1>", unsafe_allow_html=True)
    st.write("")

    species_options = list(pots.CROP_GUIDES.keys()) + ["기타"]
    species_choice = st.selectbox(
        L("species_to_plant"), species_options, key="garden_species_select",
        format_func=lambda s: L("other_species") if s == "기타" else i18n.species_name(s, lang),
    )
    species_final = species_choice
    if species_choice == "기타":
        species_final = st.text_input(L("custom_species_prompt"), key="garden_species_custom")

    size = st.selectbox(L("plot_size_label"), gardens.SIZE_OPTIONS, key="garden_size_select", format_func=lambda s: i18n.size_name(s, lang))
    name = st.text_input(L("plot_name_label"), key="garden_name_input")

    st.write("")
    set_location_now = st.checkbox(L("set_location_now"), key="garden_register_set_location")
    location = None
    if set_location_now:
        loc_col1, loc_col2 = st.columns(2)
        with loc_col1:
            province = st.selectbox(L("province_label"), regions.PROVINCES, key="garden_register_province")
        with loc_col2:
            district = st.selectbox(L("district_label"), regions.get_districts(province), key="garden_register_district")
        location = f"{province} {district}"

    st.write("")
    if st.button(L("register_button"), use_container_width=True, key="garden_register_submit", type="primary"):
        if not name or not species_final:
            st.warning(L("register_warning_plot"))
        elif gardens.get_plot(st.session_state.current_email, name.strip()):
            st.warning(L("duplicate_plot_name"))
        else:
            with st.spinner(L("generating_guide_spinner")):
                gardens.add_plot(st.session_state.current_email, name, species_final, size)
            if location:
                gardens.set_location(st.session_state.current_email, name, location)
            st.session_state.flash_message = L("plot_registered_flash").format(name=name)
            st.session_state.selected_plot = name
            st.session_state.diagnosis_result_garden = None
            go_to("plot_detail")
            st.rerun()

    if st.button(L("cancel_and_back"), key="garden_register_cancel"):
        go_to("home")
        st.rerun()


def _weather_check_section(plot, lang, planted, today):
    with st.container(border=True):
        st.markdown(f"<div class='sf-card-title'>{L('weather_check_title')}</div>", unsafe_allow_html=True)
        st.caption(L("weather_check_caption"))
        saved_location = plot.get("location", "")
        saved_province, _, saved_district = saved_location.partition(" ")
        province_index = regions.PROVINCES.index(saved_province) if saved_province in regions.PROVINCES else 0
        loc_col1, loc_col2 = st.columns(2)
        with loc_col1:
            province = st.selectbox(L("province_label"), regions.PROVINCES, index=province_index, key="garden_location_province")
        districts = regions.get_districts(province)
        district_index = districts.index(saved_district) if saved_district in districts else 0
        with loc_col2:
            district = st.selectbox(L("district_label"), districts, index=district_index, key="garden_location_district")
        location = f"{province} {district}"

        if st.button(L("start_weather_check"), use_container_width=True, key="garden_diagnose_btn", type="primary"):
            gardens.set_location(st.session_state.current_email, plot["name"], location)
            elapsed_days = (today - planted).days
            with st.spinner(L("weather_searching_spinner").format(location=location)):
                result = ai.diagnose_location(
                    plot["species"], plot["size"], elapsed_days, plot["milestones"],
                    location, kind="텃밭", language=lang,
                )
            if result:
                st.session_state.diagnosis_result_garden = result
            else:
                st.error(L("diagnosis_failed"))
            st.rerun()

        if st.session_state.diagnosis_result_garden:
            result = st.session_state.diagnosis_result_garden
            st.success(_md_safe(result["diagnosis"]))
            st.caption(L("adjusted_guide_preview"))
            for m in result["milestones"]:
                target = planted + datetime.timedelta(days=m["day"])
                st.markdown(f"• **{target.strftime('%m/%d')}** — {_md_safe(m['title'])}: {_md_safe(m['desc'])}")

            sources = result.get("sources") or []
            if sources:
                with st.expander(L("sources_title")):
                    for s in sources:
                        st.markdown(f"- [{s['title']}]({s['url']})")

            if st.button(L("update_guide_button"), use_container_width=True, key="garden_apply_diagnosis", type="primary"):
                gardens.update_plot_milestones(st.session_state.current_email, plot["name"], result["milestones"])
                st.session_state.diagnosis_result_garden = None
                st.toast(L("guide_updated_flash"))
                go_to("home")
                st.session_state.tab = "home"
                st.rerun()


def plot_detail_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    _topnav()

    plot = gardens.get_plot(st.session_state.current_email, st.session_state.selected_plot)
    lang = current_language()

    if plot is None:
        st.error(L("plot_not_found"))
        if st.button(L("back_to_home"), key="garden_detail_not_found_home"):
            go_to("home")
            st.rerun()
        return

    if st.button(L("back"), key="garden_detail_back"):
        st.session_state.selected_plot = None
        st.session_state.diagnosis_result_garden = None
        st.session_state.editing_plot_name = False
        st.session_state.confirm_delete_plot = False
        go_to("home")
        st.rerun()

    if st.session_state.flash_message:
        st.success(st.session_state.flash_message)
        st.session_state.flash_message = None

    planted = datetime.date.fromisoformat(plot["planted_date"])
    today = datetime.date.today()

    avatar_col, name_col, edit_col = st.columns([1, 4, 2])
    with avatar_col:
        st.markdown(f"<div class='sf-pot-avatar'>{plot['emoji']}</div>", unsafe_allow_html=True)
    with name_col:
        if not st.session_state.editing_plot_name:
            st.markdown(f"<div class='sf-profile-name'>{plot['name']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='sf-pot-meta'>{i18n.species_name(plot['species'], lang)} · {i18n.size_name(plot['size'], lang)}</div>", unsafe_allow_html=True)
    with edit_col:
        if not st.session_state.editing_plot_name:
            if st.button(L("edit_name"), use_container_width=True, key="garden_edit_name_btn"):
                st.session_state.editing_plot_name = True
                st.rerun()

    if st.session_state.editing_plot_name:
        new_name = st.text_input(L("new_plot_name_label"), value=plot["name"], key="garden_rename_input")
        save_col, cancel_col = st.columns(2)
        with save_col:
            if st.button(L("save"), use_container_width=True, key="garden_rename_save"):
                new_name_clean = new_name.strip()
                if new_name_clean and new_name_clean != plot["name"]:
                    if gardens.get_plot(st.session_state.current_email, new_name_clean):
                        st.warning(L("duplicate_plot_name"))
                    else:
                        gardens.rename_plot(st.session_state.current_email, plot["name"], new_name_clean)
                        st.session_state.selected_plot = new_name_clean
                        st.session_state.editing_plot_name = False
                        st.rerun()
                else:
                    st.session_state.editing_plot_name = False
                    st.rerun()
        with cancel_col:
            if st.button(L("cancel"), use_container_width=True, key="garden_rename_cancel"):
                st.session_state.editing_plot_name = False
                st.rerun()

    if plot.get("guide_source") == "ai":
        st.caption(L("guide_ai_caption"))
    else:
        st.caption(L("guide_default_caption"))

    st.write("")

    has_location = bool(plot.get("location"))
    plot_care = care.get_care(plot["species"])
    main_col, side_col = st.columns([2, 1], gap="large")

    with main_col:
        with st.container(border=True):
            st.markdown(f"<div class='sf-card-title'>{L('current_status_memo')}</div>", unsafe_allow_html=True)
            memo = st.text_input(
                L("memo_label"), value=plot.get("memo", ""), label_visibility="collapsed",
                placeholder=L("memo_placeholder"), key="garden_memo_input",
            )
            if memo != plot.get("memo", ""):
                gardens.set_memo(st.session_state.current_email, plot["name"], memo)

        st.write("")

        with st.container(border=True):
            st.markdown(f"<div class='sf-card-title'>{L('guideline_title')}</div>", unsafe_allow_html=True)
            total_steps = len(plot["milestones"])
            done_steps = sum(
                1 for m in plot["milestones"]
                if m.get("done", False) or (planted + datetime.timedelta(days=m["day"])) <= today
            )
            if total_steps:
                st.progress(done_steps / total_steps, text=L("guideline_progress").format(done=done_steps, total=total_steps))
            for m in plot["milestones"]:
                target = planted + datetime.timedelta(days=m["day"])
                mark = "✅" if m.get("done", False) or target <= today else "⏳"
                st.markdown(
                    f"<div class='sf-milestone-row'>{mark} <b>{target.strftime('%m/%d')}</b> — {m['title']}: {m['desc']}</div>",
                    unsafe_allow_html=True,
                )

        if not has_location:
            st.write("")
            _weather_check_section(plot, lang, planted, today)

    with side_col:
        with st.container(border=True):
            st.markdown(f"<div class='sf-card-title'>{L('soil_title')}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='sf-card-empty'>{plot_care['soil']}</div>", unsafe_allow_html=True)

        st.write("")

        with st.container(border=True):
            st.markdown(f"<div class='sf-card-title'>{L('fertilizer_title')}</div>", unsafe_allow_html=True)
            _render_fertilizer_advice(plot["species"], "텃밭")
            st.markdown(f"<div class='sf-card-title' style='margin-top:12px;'>{L('homemade_fertilizer_title')}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='sf-card-empty'>{plot_care['homemade']}</div>", unsafe_allow_html=True)

    if plot["milestones"]:
        last_milestone = plot["milestones"][-1]
        harvest_date = planted + datetime.timedelta(days=last_milestone["day"])
        harvest_reached = last_milestone.get("done", False) or harvest_date <= today
    else:
        harvest_reached = False

    if harvest_reached:
        st.write("")
        with st.container(border=True):
            st.markdown(f"<div class='sf-card-title'>{L('harvest_review_title')}</div>", unsafe_allow_html=True)
            if plot.get("review"):
                difficulty_display = L("difficulty_easy") if plot.get("difficulty") == "쉬웠어요" else L("difficulty_hard") if plot.get("difficulty") == "어려웠어요" else plot.get("difficulty", "-")
                st.markdown(f"<div class='sf-card-empty'>{L('difficulty_label').format(value=difficulty_display)}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='sf-card-empty'>{plot['review']}</div>", unsafe_allow_html=True)
                st.success(_md_safe(plot.get("recommendation")) or L("no_recommendation"))
            else:
                st.caption(L("harvest_reached_caption"))
                if st.button(L("go_write_review"), use_container_width=True, key=f"go_review_plot_{plot['name']}", type="primary"):
                    st.session_state.selected_plot = plot["name"]
                    go_to("plot_review")
                    st.rerun()

    if has_location:
        st.write("")
        _weather_check_section(plot, lang, planted, today)

    st.write("")
    with st.container(key="delete_plot_container"):
        if st.button(L("delete_button"), use_container_width=True, key="delete_plot_btn"):
            st.session_state.confirm_delete_plot = True
            st.rerun()
    st.markdown(
        "<style>.st-key-delete_plot_container button { color: #E53935 !important; "
        "border-color: #E53935 !important; }</style>",
        unsafe_allow_html=True,
    )

    if st.session_state.confirm_delete_plot:
        st.warning(L("confirm_delete_plot").format(name=plot['name']))
        confirm_col, cancel_col = st.columns(2)
        with confirm_col:
            if st.button(L("yes_delete"), use_container_width=True, key="confirm_delete_plot_btn"):
                gardens.delete_plot(st.session_state.current_email, plot["name"])
                st.session_state.confirm_delete_plot = False
                st.session_state.selected_plot = None
                st.session_state.diagnosis_result_garden = None
                st.session_state.flash_message = L("plot_deleted_flash").format(name=plot['name'])
                go_to("home")
                st.rerun()
        with cancel_col:
            if st.button(L("cancel"), use_container_width=True, key="cancel_delete_plot_btn"):
                st.session_state.confirm_delete_plot = False
                st.rerun()


def _split_review_sentences(text: str):
    parts = re.split(r"(?<=[.!?…])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def pot_review_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    _topnav()

    pot = pots.get_pot(st.session_state.current_email, st.session_state.selected_pot)
    lang = current_language()
    if pot is None:
        st.error(L("pot_not_found"))
        if st.button(L("back_to_home")):
            go_to("home")
            st.rerun()
        return

    if st.button(L("back")):
        go_to("pot_detail")
        st.rerun()

    st.markdown(f"<h1 style='text-align:center;'>{L('harvest_review_heading').format(name=pot['name'])}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:gray;'>{i18n.species_name(pot['species'], lang)} · {i18n.size_name(pot['size'], lang)}</p>", unsafe_allow_html=True)
    st.write("")

    st.subheader(L("difficulty_section_title"))
    difficulty = st.radio(
        L("difficulty_question"),
        ["쉬웠어요", "어려웠어요"],
        key="pot_review_difficulty",
        horizontal=True,
        format_func=lambda v: L("difficulty_easy") if v == "쉬웠어요" else L("difficulty_hard"),
    )

    st.write("")
    st.subheader(L("review_section_title"))
    review_text = st.text_area(
        L("review_textarea_label"),
        key="pot_review_text",
        placeholder=L("review_placeholder_pot"),
        height=150,
    )

    st.write("")
    if st.button(L("submit_review_button"), use_container_width=True, type="primary"):
        if not review_text.strip():
            st.warning(L("review_warning_empty"))
        else:
            cleaned = review_text.strip()
            allowed_species = list(pots.CROP_GUIDES.keys())
            with st.spinner(L("analyzing_review_spinner")):
                recommendation = ai.recommend_next_crop(
                    pot["species"], "화분", difficulty, cleaned, language=lang, allowed_species=allowed_species,
                )
                points = []
                for sentence in _split_review_sentences(cleaned):
                    rec = ai.recommend_crop_for_observation(
                        pot["species"], "화분", sentence, language=lang, allowed_species=allowed_species,
                    )
                    if rec:
                        points.append({"text": sentence, **rec})
            pots.set_review(
                st.session_state.current_email, pot["name"], difficulty, cleaned,
                recommendation or L("recommend_failed"),
            )
            st.session_state.review_analysis = {
                "kind": "pot",
                "item_name": pot["name"],
                "difficulty": difficulty,
                "review": cleaned,
                "points": points,
                "overall": recommendation or L("recommend_failed"),
            }
            go_to("review_analysis")
            st.rerun()


def plot_review_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    _topnav()

    plot = gardens.get_plot(st.session_state.current_email, st.session_state.selected_plot)
    lang = current_language()
    if plot is None:
        st.error(L("plot_not_found"))
        if st.button(L("back_to_home")):
            go_to("home")
            st.rerun()
        return

    if st.button(L("back")):
        go_to("plot_detail")
        st.rerun()

    st.markdown(f"<h1 style='text-align:center;'>{L('harvest_review_heading').format(name=plot['name'])}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:gray;'>{i18n.species_name(plot['species'], lang)} · {i18n.size_name(plot['size'], lang)}</p>", unsafe_allow_html=True)
    st.write("")

    st.subheader(L("difficulty_section_title"))
    difficulty = st.radio(
        L("difficulty_question"),
        ["쉬웠어요", "어려웠어요"],
        key="plot_review_difficulty",
        horizontal=True,
        format_func=lambda v: L("difficulty_easy") if v == "쉬웠어요" else L("difficulty_hard"),
    )

    st.write("")
    st.subheader(L("review_section_title"))
    review_text = st.text_area(
        L("review_textarea_label"),
        key="plot_review_text",
        placeholder=L("review_placeholder_plot"),
        height=150,
    )

    st.write("")
    if st.button(L("submit_review_button"), use_container_width=True, type="primary"):
        if not review_text.strip():
            st.warning(L("review_warning_empty"))
        else:
            cleaned = review_text.strip()
            allowed_species = list(pots.CROP_GUIDES.keys())
            with st.spinner(L("analyzing_review_spinner")):
                recommendation = ai.recommend_next_crop(
                    plot["species"], "텃밭", difficulty, cleaned, language=lang, allowed_species=allowed_species,
                )
                points = []
                for sentence in _split_review_sentences(cleaned):
                    rec = ai.recommend_crop_for_observation(
                        plot["species"], "텃밭", sentence, language=lang, allowed_species=allowed_species,
                    )
                    if rec:
                        points.append({"text": sentence, **rec})
            gardens.set_review(
                st.session_state.current_email, plot["name"], difficulty, cleaned,
                recommendation or L("recommend_failed"),
            )
            st.session_state.review_analysis = {
                "kind": "plot",
                "item_name": plot["name"],
                "difficulty": difficulty,
                "review": cleaned,
                "points": points,
                "overall": recommendation or L("recommend_failed"),
            }
            go_to("review_analysis")
            st.rerun()


def review_analysis_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    _topnav()

    data = st.session_state.review_analysis
    if not data:
        st.error(L("info_not_found"))
        if st.button(L("back_to_home")):
            go_to("home")
            st.rerun()
        return

    back_target = "pot_detail" if data["kind"] == "pot" else "plot_detail"
    if st.button(L("back")):
        go_to(back_target)
        st.rerun()

    difficulty_display = L("difficulty_easy") if data["difficulty"] == "쉬웠어요" else L("difficulty_hard")
    st.markdown(
        f"<h1 style='text-align:center;'>{L('review_analysis_heading').format(name=data['item_name'])}</h1>",
        unsafe_allow_html=True,
    )
    st.write("")

    with st.container(border=True):
        st.markdown(f"<div class='sf-card-title'>{data['item_name']} · {difficulty_display}</div>", unsafe_allow_html=True)
        st.markdown(_md_safe(data["review"]))

    st.write("")

    if data["points"]:
        for point in data["points"]:
            with st.container(border=True):
                st.markdown(f"**“{_md_safe(point['text'])}”**")
                st.markdown(f"{point.get('emoji', '🌱')} **{L('recommend_label')} {point['crop']}** — {_md_safe(point['reason'])}")
            st.write("")
    else:
        st.markdown(f"<div class='sf-card-empty'>{L('no_points_found')}</div>", unsafe_allow_html=True)
        st.write("")

    with st.container(border=True):
        st.markdown(f"<div class='sf-card-title'>{L('overall_recommend_heading')}</div>", unsafe_allow_html=True)
        st.success(_md_safe(data["overall"]))


def alarm_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    _topnav()

    if st.button(L("back"), key="alarm_back"):
        go_to(st.session_state.settings_return_page)
        st.rerun()

    st.write("")
    st.markdown(f"<h2 style='text-align:center;'>{L('alarm_title')}</h2>", unsafe_allow_html=True)
    st.write("")

    st.caption(L("alarm_desc"))

    email = st.session_state.current_email
    current = auth.get_alarm_enabled(email)
    new_value = st.checkbox(L("alarm_checkbox"), value=current, key="alarm_toggle")
    if new_value != current:
        auth.set_alarm_enabled(email, new_value)
        if new_value:
            st.info(L("alarm_permission_info"))
        st.rerun()


def icon_screen():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    _topnav()

    if st.button(L("back"), key="icon_back"):
        go_to(st.session_state.settings_return_page)
        st.rerun()

    st.write("")
    st.markdown(f"<h2 style='text-align:center;'>{L('icon_change_title')}</h2>", unsafe_allow_html=True)
    st.write("")

    current = auth.get_icon(st.session_state.current_email)
    if current.get("type") == "photo":
        preview_html = (
            f"<div style='width:80px;height:80px;border-radius:50%;overflow:hidden;margin:0 auto;'>"
            f"<img src='{current['value']}' style='width:100%;height:100%;object-fit:cover;' /></div>"
        )
    elif current.get("type") == "color":
        preview_html = (
            f"<div style='width:80px;height:80px;border-radius:50%;"
            f"background:{current.get('value', '#D9D9D9')};margin:0 auto;'></div>"
        )
    else:
        preview_html = (
            "<div style='width:80px;height:80px;border-radius:50%;background:#E7F2EB;"
            "display:flex;align-items:center;justify-content:center;font-size:36px;margin:0 auto;'>"
            f"{current.get('value', '🙂')}</div>"
        )
    st.markdown(preview_html, unsafe_allow_html=True)
    st.write("")

    if current.get("type") == "photo":
        if st.button(L("reset_to_default_icon"), use_container_width=True, key="icon_reset_default"):
            auth.set_icon(st.session_state.current_email, dict(auth.DEFAULT_ICON))
            go_to(st.session_state.settings_return_page)
            st.rerun()
        st.write("")

    st.markdown(f"<div class='sf-card-title'>{L('photo_set_title')}</div>", unsafe_allow_html=True)
    uploaded = st.file_uploader(L("upload_photo"), type=["png", "jpg", "jpeg"], key="icon_photo_uploader")

    if uploaded is not None:
        image_b64 = base64.standard_b64encode(uploaded.getvalue()).decode("utf-8")
        data_uri = f"data:{uploaded.type};base64,{image_b64}"
        pos_x, pos_y = 50, 50

        st.caption(L("photo_preview_caption"))
        st.markdown(
            f"<div style='width:80px;height:80px;border-radius:50%;overflow:hidden;margin:0 auto;'>"
            f"<img src='{data_uri}' style='width:100%;height:100%;object-fit:cover;"
            f"object-position:{pos_x}% {pos_y}%;' /></div>",
            unsafe_allow_html=True,
        )

        st.write("")
        if st.button(L("save_this_photo"), use_container_width=True, key="icon_photo_save", type="primary"):
            auth.set_icon(
                st.session_state.current_email,
                {"type": "photo", "value": data_uri, "position": {"x": pos_x, "y": pos_y}},
            )
            st.session_state.flash_message = L("icon_saved_flash")
            go_to(st.session_state.settings_return_page)
            st.rerun()


if st.session_state.page == "login":
    login_screen()
elif st.session_state.page == "signup":
    signup_screen()
elif st.session_state.page == "home":
    home_screen()
elif st.session_state.page == "task_detail":
    task_detail_screen()
elif st.session_state.page == "register_plot":
    register_plot_screen()
elif st.session_state.page == "plot_detail":
    plot_detail_screen()
elif st.session_state.page == "plot_review":
    plot_review_screen()
elif st.session_state.page == "register_pot":
    register_pot_screen()
elif st.session_state.page == "pot_detail":
    pot_detail_screen()
elif st.session_state.page == "pot_review":
    pot_review_screen()
elif st.session_state.page == "review_analysis":
    review_analysis_screen()
elif st.session_state.page == "icon_screen":
    icon_screen()
elif st.session_state.page == "alarm_screen":
    alarm_screen()
