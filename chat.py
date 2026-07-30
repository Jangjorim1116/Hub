import json
import os
import datetime

CHAT_FILE = os.path.join(os.path.dirname(__file__), "chat.json")


def _load():
    if not os.path.exists(CHAT_FILE):
        return {}
    with open(CHAT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(data):
    with open(CHAT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_messages(room: str):
    data = _load()
    return data.get(room, [])


def add_message(room: str, sender: str, text: str, is_ai: bool = False):
    data = _load()
    room_messages = data.setdefault(room, [])
    room_messages.append(
        {
            "sender": sender,
            "text": text,
            "is_ai": is_ai,
            "timestamp": datetime.datetime.now().strftime("%m/%d %H:%M"),
        }
    )
    _save(data)


def rename_owner(old_email: str, new_email: str):
    """이메일이 바뀌면 그 사용자의 AI 1:1 대화방 키(ai::방이름::이메일)도 함께 옮겨준다."""
    data = _load()
    meta = data.setdefault("_meta", {})
    changed = False

    for room in ("화분", "텃밭"):
        old_key = f"ai::{room}::{old_email}"
        new_key = f"ai::{room}::{new_email}"
        if old_key in data:
            data[new_key] = data.pop(old_key)
            changed = True
        if old_key in meta:
            meta[new_key] = meta.pop(old_key)
            changed = True

    if changed:
        _save(data)


def delete_owner(email: str):
    """계정 삭제 시 그 사용자의 AI 1:1 대화방(ai::방이름::이메일)을 지운다."""
    data = _load()
    meta = data.setdefault("_meta", {})
    changed = False

    for room in ("화분", "텃밭"):
        key = f"ai::{room}::{email}"
        if key in data:
            del data[key]
            changed = True
        if key in meta:
            del meta[key]
            changed = True

    if changed:
        _save(data)


def maybe_reset_daily(room: str):
    """사용자 대화방을 하루에 한 번, 날짜가 바뀌면 자동으로 비워준다."""
    data = _load()
    meta = data.setdefault("_meta", {})
    today = datetime.date.today().isoformat()

    if meta.get(room) != today:
        data[room] = []
        meta[room] = today
        _save(data)
