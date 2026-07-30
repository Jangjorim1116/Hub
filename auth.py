import base64
import json
import os
import hashlib
import re
import secrets
import threading

USERS_FILE = os.path.join(os.path.dirname(__file__), "users.json")
ICONS_DIR = os.path.join(os.path.dirname(__file__), "icons")
_LOCK = threading.Lock()


def _load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)


def _hash_password(password: str, salt: str) -> str:
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), bytes.fromhex(salt), 100_000).hex()


def register_user(name: str, email: str, password: str):
    with _LOCK:
        users = _load_users()
        email_key = email.strip().lower()

        if email_key in users:
            return False, "이미 가입된 이메일입니다."

        salt = secrets.token_hex(16)
        users[email_key] = {
            "name": name,
            "email": email,
            "salt": salt,
            "password_hash": _hash_password(password, salt),
        }
        _save_users(users)
        return True, "가입이 완료되었습니다."


def authenticate(email: str, password: str):
    users = _load_users()
    user = users.get(email.strip().lower())

    if not user:
        return None
    if _hash_password(password, user["salt"]) != user["password_hash"]:
        return None
    return user


def change_email(current_email: str, password: str, new_email: str):
    with _LOCK:
        users = _load_users()
        old_key = current_email.strip().lower()
        user = users.get(old_key)
        if not user:
            return False, "사용자를 찾을 수 없습니다."
        if _hash_password(password, user["salt"]) != user["password_hash"]:
            return False, "비밀번호가 일치하지 않습니다."

        new_key = new_email.strip().lower()
        if not new_key or "@" not in new_key:
            return False, "올바른 이메일 형식이 아닙니다."
        if new_key == old_key:
            return False, "현재 이메일과 동일합니다."
        if new_key in users:
            return False, "이미 사용 중인 이메일입니다."

        user["email"] = new_email.strip()
        del users[old_key]
        users[new_key] = user
        _save_users(users)
        return True, "이메일이 변경되었습니다."


def change_password(email: str, current_password: str, new_password: str):
    with _LOCK:
        users = _load_users()
        key = email.strip().lower()
        user = users.get(key)
        if not user:
            return False, "사용자를 찾을 수 없습니다."
        if _hash_password(current_password, user["salt"]) != user["password_hash"]:
            return False, "현재 비밀번호가 일치하지 않습니다."
        if len(new_password) < 4:
            return False, "비밀번호는 4자 이상이어야 합니다."

        salt = secrets.token_hex(16)
        user["salt"] = salt
        user["password_hash"] = _hash_password(new_password, salt)
        _save_users(users)
        return True, "비밀번호가 변경되었습니다."


def delete_account(email: str, password: str):
    with _LOCK:
        users = _load_users()
        key = email.strip().lower()
        user = users.get(key)
        if not user:
            return False, "사용자를 찾을 수 없습니다."
        if _hash_password(password, user["salt"]) != user["password_hash"]:
            return False, "비밀번호가 일치하지 않습니다."

        del users[key]
        _save_users(users)
        return True, "계정이 삭제되었습니다."


def get_language(email: str) -> str:
    if not email:
        return "ko"
    users = _load_users()
    user = users.get(email.strip().lower())
    return (user or {}).get("language", "ko")


def set_language(email: str, language: str):
    with _LOCK:
        users = _load_users()
        key = email.strip().lower()
        if key in users:
            users[key]["language"] = language
            _save_users(users)


DEFAULT_ICON = {"type": "color", "value": "#D9D9D9"}


def _icon_filename(email_key: str, media_type: str) -> str:
    ext = re.sub(r"[^a-z0-9]", "", media_type.split("/")[-1].lower()) or "png"
    safe_key = hashlib.sha256(email_key.encode("utf-8")).hexdigest()[:16]
    return f"{safe_key}.{ext}"


def get_icon(email: str) -> dict:
    """아이콘 사진은 users.json에 base64로 통째로 저장하지 않고 icons/ 폴더의
    파일을 가리키는 참조만 저장한다. 여기서 파일을 읽어 기존 형태(data URI)로 복원해준다."""
    if not email:
        return DEFAULT_ICON
    users = _load_users()
    user = users.get(email.strip().lower())
    icon = (user or {}).get("icon")
    if icon is None:
        return DEFAULT_ICON
    if isinstance(icon, str):
        return {"type": "emoji", "value": icon}
    if icon.get("type") == "photo" and icon.get("file"):
        try:
            with open(os.path.join(ICONS_DIR, icon["file"]), "rb") as f:
                image_b64 = base64.standard_b64encode(f.read()).decode("utf-8")
        except OSError:
            return DEFAULT_ICON
        media_type = icon.get("media_type", "image/png")
        return {
            "type": "photo",
            "value": f"data:{media_type};base64,{image_b64}",
            "position": icon.get("position", {"x": 50, "y": 50}),
        }
    return icon


def set_icon(email: str, icon: dict):
    with _LOCK:
        users = _load_users()
        key = email.strip().lower()
        if key not in users:
            return

        if icon.get("type") == "photo" and icon.get("value", "").startswith("data:"):
            header, _, b64data = icon["value"].partition(",")
            media_type = header[5:].split(";")[0] if header.startswith("data:") else "image/png"
            os.makedirs(ICONS_DIR, exist_ok=True)
            filename = _icon_filename(key, media_type)
            with open(os.path.join(ICONS_DIR, filename), "wb") as f:
                f.write(base64.standard_b64decode(b64data))
            icon = {
                "type": "photo",
                "file": filename,
                "media_type": media_type,
                "position": icon.get("position", {"x": 50, "y": 50}),
            }

        users[key]["icon"] = icon
        _save_users(users)


def get_alarm_enabled(email: str) -> bool:
    if not email:
        return False
    users = _load_users()
    user = users.get(email.strip().lower())
    return (user or {}).get("alarm_enabled", False)


def set_alarm_enabled(email: str, enabled: bool):
    with _LOCK:
        users = _load_users()
        key = email.strip().lower()
        if key in users:
            users[key]["alarm_enabled"] = enabled
            _save_users(users)
