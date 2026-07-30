import json
import os
import datetime

import ai
import auth
from pots import CROP_GUIDES, DEFAULT_GUIDE, get_guide

GARDENS_FILE = os.path.join(os.path.dirname(__file__), "gardens.json")

SIZE_OPTIONS = [
    "소형 (1평 이하)",
    "중형 (1~3평)",
    "대형 (3평 이상)",
]


def _load():
    if not os.path.exists(GARDENS_FILE):
        return {}
    with open(GARDENS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(gardens):
    with open(GARDENS_FILE, "w", encoding="utf-8") as f:
        json.dump(gardens, f, ensure_ascii=False, indent=2)


def add_plot(email: str, name: str, species: str, size: str):
    gardens = _load()
    user_plots = gardens.setdefault(email, [])

    language = auth.get_language(email)
    ai_guide = ai.generate_guideline(species, size, kind="텃밭", language=language)
    if ai_guide:
        emoji = ai_guide["emoji"]
        milestones = ai_guide["milestones"]
        guide_source = "ai"
    else:
        preset_guide = get_guide(species)
        emoji = preset_guide["emoji"]
        milestones = [
            {"day": day, "title": title, "desc": desc}
            for day, title, desc in preset_guide["milestones"]
        ]
        guide_source = "preset"

    planted_date = datetime.date.today().isoformat()

    plot = {
        "name": name,
        "species": species,
        "size": size,
        "emoji": emoji,
        "planted_date": planted_date,
        "milestones": milestones,
        "guide_source": guide_source,
    }
    user_plots.append(plot)
    _save(gardens)
    return plot


def get_plots(email: str):
    gardens = _load()
    return gardens.get(email, [])


def rename_owner(old_email: str, new_email: str):
    gardens = _load()
    if old_email in gardens:
        gardens[new_email] = gardens.pop(old_email)
        _save(gardens)


def delete_owner(email: str):
    gardens = _load()
    if email in gardens:
        del gardens[email]
        _save(gardens)


def get_plot(email: str, plot_name: str):
    for plot in get_plots(email):
        if plot["name"] == plot_name:
            return plot
    return None


def set_memo(email: str, plot_name: str, memo: str):
    gardens = _load()
    for plot in gardens.get(email, []):
        if plot["name"] == plot_name:
            plot["memo"] = memo
    _save(gardens)


def set_location(email: str, plot_name: str, location: str):
    gardens = _load()
    for plot in gardens.get(email, []):
        if plot["name"] == plot_name:
            plot["location"] = location
    _save(gardens)


def set_weather_alert(email: str, plot_name: str, date_iso: str, risk: bool, message: str):
    gardens = _load()
    for plot in gardens.get(email, []):
        if plot["name"] == plot_name:
            plot["weather_check_date"] = date_iso
            plot["weather_risk"] = risk
            plot["weather_message"] = message
    _save(gardens)


def rename_plot(email: str, old_name: str, new_name: str):
    gardens = _load()
    for plot in gardens.get(email, []):
        if plot["name"] == old_name:
            plot["name"] = new_name
    _save(gardens)


def delete_plot(email: str, plot_name: str):
    gardens = _load()
    user_plots = gardens.get(email, [])
    gardens[email] = [p for p in user_plots if p["name"] != plot_name]
    _save(gardens)


def update_plot_milestones(email: str, plot_name: str, new_milestones: list):
    gardens = _load()
    for plot in gardens.get(email, []):
        if plot["name"] == plot_name:
            plot["milestones"] = new_milestones
            plot["guide_source"] = "ai"
    _save(gardens)


def set_review(email: str, plot_name: str, difficulty: str, review: str, recommendation: str):
    gardens = _load()
    for plot in gardens.get(email, []):
        if plot["name"] == plot_name:
            plot["difficulty"] = difficulty
            plot["review"] = review
            plot["recommendation"] = recommendation
    _save(gardens)


def is_harvested(plot: dict) -> bool:
    if not plot["milestones"]:
        return False
    last = plot["milestones"][-1]
    if last.get("done", False):
        return True
    planted = datetime.date.fromisoformat(plot["planted_date"])
    target = planted + datetime.timedelta(days=last["day"])
    return target <= datetime.date.today()


def this_month_tasks(email: str):
    """텃밭은 매일 방문하기 어려운 경우가 많아, 오늘이 아니라 이번 달 전체 일정을 보여준다."""
    today = datetime.date.today()
    tasks = []
    for plot in get_plots(email):
        planted = datetime.date.fromisoformat(plot["planted_date"])
        for m in plot["milestones"]:
            target_date = planted + datetime.timedelta(days=m["day"])
            if target_date.year == today.year and target_date.month == today.month:
                tasks.append({
                    "pot_name": plot["name"],
                    "day": m["day"],
                    "title": m["title"],
                    "desc": m["desc"],
                    "done": m.get("done", False),
                    "date": target_date,
                })
    tasks.sort(key=lambda t: t["date"])
    return tasks


def set_task_done(email: str, plot_name: str, day: int, done: bool):
    gardens = _load()
    for plot in gardens.get(email, []):
        if plot["name"] == plot_name:
            for m in plot["milestones"]:
                if m["day"] == day:
                    m["done"] = done
    _save(gardens)
