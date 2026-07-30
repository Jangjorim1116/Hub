import json
import os
import datetime

import ai
import auth

POTS_FILE = os.path.join(os.path.dirname(__file__), "pots.json")

CROP_GUIDES = {
    "토마토": {
        "emoji": "🍅",
        "milestones": [
            (0, "정식", "모종을 심었어요. 물을 충분히 주세요."),
            (7, "활착 확인", "새 잎이 나오는지 확인하고, 흙이 마르면 물을 주세요."),
            (14, "지지대 설치", "줄기가 자라기 전에 지지대를 세워주세요."),
            (21, "첫 웃거름", "비료를 한 번 주세요."),
            (35, "곁순 제거", "잎겨드랑이에서 나오는 곁순을 정리해주세요."),
            (60, "개화·착과", "꽃이 피고 열매가 맺히기 시작해요."),
            (90, "수확 시작", "빨갛게 익은 열매부터 수확하세요!"),
        ],
    },
    "가지": {
        "emoji": "🍆",
        "milestones": [
            (0, "정식", "모종을 심고 물을 충분히 주세요."),
            (10, "활착 확인", "잎이 시들지 않는지 확인해주세요."),
            (20, "첫 웃거름", "비료를 한 번 주세요."),
            (40, "지지대 설치", "가지가 무거워지기 전에 지지대를 세워주세요."),
            (70, "개화·착과", "보라색 꽃이 피고 열매가 맺혀요."),
            (85, "수확 시작", "윤기 나는 가지를 수확하세요!"),
        ],
    },
    "고추": {
        "emoji": "🌶️",
        "milestones": [
            (0, "정식", "모종을 심고 물을 충분히 주세요."),
            (10, "활착 확인", "새 잎이 나오는지 확인해주세요."),
            (25, "첫 웃거름", "비료를 한 번 주세요."),
            (45, "지지대 설치", "쓰러지지 않게 지지대를 세워주세요."),
            (70, "개화·착과", "흰 꽃이 피고 고추가 맺혀요."),
            (90, "수확 시작", "짙은 초록색 고추부터 수확하세요!"),
        ],
    },
    "상추": {
        "emoji": "🥬",
        "milestones": [
            (0, "파종/정식", "씨앗을 뿌리거나 모종을 심었어요."),
            (7, "발아·활착 확인", "떡잎이나 새 잎을 확인해주세요."),
            (20, "솎아주기", "촘촘한 곳은 솎아서 간격을 넓혀주세요."),
            (30, "첫 웃거름", "비료를 한 번 주세요."),
            (45, "수확 시작", "바깥쪽 잎부터 뜯어서 수확하세요!"),
        ],
    },
    "오이": {
        "emoji": "🥒",
        "milestones": [
            (0, "정식", "모종을 심고 물을 충분히 주세요."),
            (10, "활착 확인", "잎 상태를 확인해주세요."),
            (15, "지지대·유인줄 설치", "덩굴이 타고 오를 지지대를 세워주세요."),
            (25, "첫 웃거름", "비료를 한 번 주세요."),
            (45, "개화·착과", "노란 꽃이 피고 열매가 맺혀요."),
            (55, "수확 시작", "가시가 살아있을 때 수확하세요!"),
        ],
    },
    "깻잎": {
        "emoji": "🌿",
        "milestones": [
            (0, "파종/정식", "씨앗을 뿌리거나 모종을 심었어요. 물을 충분히 주세요."),
            (10, "발아·활착 확인", "새 잎이 나오는지 확인해주세요."),
            (20, "솎아주기", "촘촘한 곳은 솎아서 간격을 넓혀주세요."),
            (30, "첫 웃거름", "질소가 든 액체비료를 희석해서 주세요."),
            (40, "수확 시작", "아래쪽 큰 잎부터 뜯어서 수확하세요. 계속 새 잎이 자라요!"),
        ],
    },
    "파": {
        "emoji": "🧅",
        "milestones": [
            (0, "정식", "모종을 심고 물을 충분히 주세요."),
            (15, "활착 확인", "새 잎이 곧게 자라는지 확인해주세요."),
            (30, "첫 웃거름·북주기", "비료를 주고 흙을 살짝 북돋아주세요(북주기)."),
            (60, "2차 북주기", "대가 자라면 다시 흙을 북돋아 밑동을 하얗게 키우세요."),
            (90, "수확 시작", "흰 대가 길게 자라면 뿌리째 뽑아 수확하세요!"),
        ],
    },
    "애호박": {
        "emoji": "🎃",
        "milestones": [
            (0, "정식", "모종을 심고 물을 충분히 주세요."),
            (10, "활착 확인", "새 잎이 나오는지 확인해주세요."),
            (20, "지지대·유인줄 설치", "덩굴이 뻗어나갈 공간이나 지지대를 마련해주세요."),
            (30, "첫 웃거름", "비료를 한 번 주세요."),
            (45, "개화·착과", "노란 꽃이 피고 애호박이 맺히기 시작해요."),
            (55, "수확 시작", "길이 20cm 정도로 자라면 수확하세요!"),
        ],
    },
    "감자": {
        "emoji": "🥔",
        "milestones": [
            (0, "씨감자 심기", "싹을 틔운 씨감자를 심고 물을 충분히 주세요."),
            (20, "싹 확인", "새싹이 흙 위로 올라오는지 확인해주세요."),
            (35, "북주기", "줄기 밑동에 흙을 북돋아 감자가 햇빛에 녹색으로 변하지 않게 해주세요."),
            (50, "개화", "보라색·흰색 꽃이 피기 시작해요."),
            (90, "수확 시작", "잎이 누렇게 마르기 시작하면 캐보세요!"),
        ],
    },
    "당근": {
        "emoji": "🥕",
        "milestones": [
            (0, "파종", "씨앗을 흩뿌리거나 줄뿌림하고 물을 충분히 주세요."),
            (15, "발아 확인", "가는 떡잎이 올라오는지 확인해주세요."),
            (30, "솎아주기", "촘촘한 곳은 솎아서 포기 사이를 5~8cm로 넓혀주세요."),
            (50, "뿌리 비대기", "당근 머리가 흙 위로 드러나면 흙을 덮어 녹변을 막아주세요."),
            (100, "수확 시작", "뿌리 어깨 굵기를 확인하고 수확하세요!"),
        ],
    },
    "고구마": {
        "emoji": "🍠",
        "milestones": [
            (0, "순 심기", "고구마 순을 비스듬히 눕혀 심고 물을 충분히 주세요."),
            (15, "활착 확인", "순이 시들지 않고 새 잎이 나오는지 확인해주세요."),
            (40, "덩굴 걷기", "웃자란 덩굴이 다른 곳에 뿌리내리지 않게 가끔 들어 뒤집어주세요."),
            (70, "비대기 관리", "물과 거름을 최소한으로 줄이고 그대로 두세요."),
            (120, "수확 시작", "잎이 노랗게 변하기 시작하면 서리 오기 전에 캐세요!"),
        ],
    },
    "마늘": {
        "emoji": "🧄",
        "milestones": [
            (0, "종구 심기", "마늘 한 쪽을 뾰족한 쪽이 위로 오게 5cm 깊이, 10cm 간격으로 심고 물을 충분히 주세요."),
            (20, "싹 확인", "초록 싹이 올라왔는지 확인하고, 안 난 자리는 새 종구로 보충해 심으세요."),
            (40, "겨울 덮기", "짚이나 낙엽을 덮어 언 피해를 막아주세요."),
            (150, "봄 웃거름", "날이 풀려 새 잎이 자라기 시작하면 복합비료를 한 번 주세요."),
            (200, "마늘종 제거", "가운데서 꽃대(마늘종)가 올라오면 잘라내 알이 굵어지게 하세요."),
            (230, "수확 시작", "아래 잎이 반 이상 노랗게 마르면 맑은 날 뽑아서 그늘에 2주간 말리세요."),
        ],
    },
    "바질": {
        "emoji": "🍃",
        "milestones": [
            (0, "파종/정식", "씨앗을 뿌리거나 모종을 심었어요. 물을 충분히 주세요."),
            (12, "발아·활착 확인", "새 잎이 나오는지 확인해주세요."),
            (25, "순지르기", "줄기 끝의 순을 잘라주면 곁가지가 풍성해지고 잎이 더 많이 자라요."),
            (35, "첫 웃거름", "질소가 든 액체비료를 희석해서 주세요."),
            (45, "수확 시작", "윗잎부터 조금씩 뜯어서 수확하세요. 계속 새 잎이 자라요!"),
        ],
    },
}

DEFAULT_GUIDE = {
    "emoji": "🌱",
    "milestones": [
        (0, "심기", "모종이나 씨앗을 심고 물을 충분히 주세요."),
        (7, "발아·활착 확인", "새 잎이 나오는지 확인해주세요."),
        (21, "첫 웃거름", "비료를 한 번 주세요."),
        (60, "수확 예상", "이 시기부터 수확을 기대해볼 수 있어요. (일반적인 기준이며 작물마다 달라요)"),
    ],
}

SIZE_OPTIONS = [
    "소형 (지름 20cm 이하)",
    "중형 (지름 20~40cm)",
    "대형 (지름 40cm 이상)",
]


def _load():
    if not os.path.exists(POTS_FILE):
        return {}
    with open(POTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(pots):
    with open(POTS_FILE, "w", encoding="utf-8") as f:
        json.dump(pots, f, ensure_ascii=False, indent=2)


def get_guide(species: str):
    return CROP_GUIDES.get(species, DEFAULT_GUIDE)


def add_pot(email: str, name: str, species: str, size: str):
    pots = _load()
    user_pots = pots.setdefault(email, [])

    language = auth.get_language(email)
    ai_guide = ai.generate_guideline(species, size, language=language)
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

    pot = {
        "name": name,
        "species": species,
        "size": size,
        "emoji": emoji,
        "planted_date": planted_date,
        "milestones": milestones,
        "guide_source": guide_source,
        "diagnosis_history": [],
    }
    user_pots.append(pot)
    _save(pots)
    return pot


def get_pots(email: str):
    pots = _load()
    return pots.get(email, [])


def rename_owner(old_email: str, new_email: str):
    pots = _load()
    if old_email in pots:
        pots[new_email] = pots.pop(old_email)
        _save(pots)


def delete_owner(email: str):
    pots = _load()
    if email in pots:
        del pots[email]
        _save(pots)


def get_pot(email: str, pot_name: str):
    for pot in get_pots(email):
        if pot["name"] == pot_name:
            return pot
    return None


def set_memo(email: str, pot_name: str, memo: str):
    pots = _load()
    for pot in pots.get(email, []):
        if pot["name"] == pot_name:
            pot["memo"] = memo
    _save(pots)


def rename_pot(email: str, old_name: str, new_name: str):
    pots = _load()
    for pot in pots.get(email, []):
        if pot["name"] == old_name:
            pot["name"] = new_name
    _save(pots)


def delete_pot(email: str, pot_name: str):
    pots = _load()
    user_pots = pots.get(email, [])
    pots[email] = [p for p in user_pots if p["name"] != pot_name]
    _save(pots)


def update_pot_milestones(email: str, pot_name: str, new_milestones: list):
    pots = _load()
    for pot in pots.get(email, []):
        if pot["name"] == pot_name:
            pot["milestones"] = new_milestones
            pot["guide_source"] = "ai"
    _save(pots)


def add_diagnosis_record(email: str, pot_name: str, date_iso: str, elapsed_days: int, diagnosis: str):
    pots = _load()
    for pot in pots.get(email, []):
        if pot["name"] == pot_name:
            history = pot.setdefault("diagnosis_history", [])
            history.append({"date": date_iso, "elapsed_days": elapsed_days, "diagnosis": diagnosis})
            pot["diagnosis_history"] = history[-5:]
    _save(pots)


def set_review(email: str, pot_name: str, difficulty: str, review: str, recommendation: str):
    pots = _load()
    for pot in pots.get(email, []):
        if pot["name"] == pot_name:
            pot["difficulty"] = difficulty
            pot["review"] = review
            pot["recommendation"] = recommendation
    _save(pots)


def is_harvested(pot: dict) -> bool:
    if not pot["milestones"]:
        return False
    last = pot["milestones"][-1]
    if last.get("done", False):
        return True
    planted = datetime.date.fromisoformat(pot["planted_date"])
    target = planted + datetime.timedelta(days=last["day"])
    return target <= datetime.date.today()


def todays_tasks(email: str):
    today = datetime.date.today()
    tasks = []
    for pot in get_pots(email):
        planted = datetime.date.fromisoformat(pot["planted_date"])
        for m in pot["milestones"]:
            target_date = planted + datetime.timedelta(days=m["day"])
            if target_date == today:
                tasks.append({
                    "pot_name": pot["name"],
                    "day": m["day"],
                    "title": m["title"],
                    "desc": m["desc"],
                    "done": m.get("done", False),
                })
    return tasks


def set_task_done(email: str, pot_name: str, day: int, done: bool):
    pots = _load()
    for pot in pots.get(email, []):
        if pot["name"] == pot_name:
            for m in pot["milestones"]:
                if m["day"] == day:
                    m["done"] = done
    _save(pots)
