import base64
import json
import os
import time

import anthropic
import streamlit as st

import i18n

MODEL = "claude-opus-5"


def _lang_suffix(language: str) -> str:
    if language == "ko":
        return ""
    name = i18n.LANGUAGE_NAMES_FOR_AI.get(language, "Korean")
    return f"\n\n(Important: Write your entire response in {name}, not Korean.)"

_RETRYABLE_ERRORS = (
    anthropic.OverloadedError,
    anthropic.RateLimitError,
    anthropic.InternalServerError,
    anthropic.APIConnectionError,
)


def _create_with_retry(client, retries=3, base_delay=1.5, **kwargs):
    """Anthropic 서버가 일시적으로 과부하(529)거나 응답이 불안정할 때 짧게 재시도한다.

    인증 오류 등 재시도해도 소용없는 에러는 즉시 올려보낸다.
    """
    for attempt in range(retries + 1):
        try:
            return client.messages.create(**kwargs)
        except _RETRYABLE_ERRORS:
            if attempt == retries:
                raise
            time.sleep(base_delay * (2**attempt))

MILESTONES_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "day": {"type": "integer", "description": "심은 날로부터 경과 일수"},
            "title": {"type": "string", "description": "단계명 (한국어, 10자 이내)"},
            "desc": {"type": "string", "description": "초보자용 한 문장 설명 (한국어)"},
        },
        "required": ["day", "title", "desc"],
        "additionalProperties": False,
    },
}

GUIDE_SCHEMA = {
    "type": "object",
    "properties": {
        "emoji": {"type": "string", "description": "이 작물을 대표하는 이모지 1개"},
        "milestones": MILESTONES_SCHEMA,
    },
    "required": ["emoji", "milestones"],
    "additionalProperties": False,
}

DIAGNOSIS_SCHEMA = {
    "type": "object",
    "properties": {
        "diagnosis": {"type": "string", "description": "사진 분석 결과 요약 (한국어, 2~4문장)"},
        "milestones": MILESTONES_SCHEMA,
    },
    "required": ["diagnosis", "milestones"],
    "additionalProperties": False,
}

FERTILIZER_SCHEMA = {
    "type": "object",
    "properties": {
        "feature": {"type": "string", "description": "이 작물이 필요로 하는 핵심 영양 성분과 특징 (한국어, 2문장 이내)"},
        "tip": {"type": "string", "description": "이 작물의 비료 관리 팁 (한국어, 1~2문장)"},
        "base": {"type": "string", "description": "추천 밑거름의 특징 (한국어, 1문장)"},
        "top": {"type": "string", "description": "추천 웃거름의 특징 (한국어, 1문장)"},
        "extra": {"type": "string", "description": "주의사항이나 꼭 보충해야 할 성분이 있으면 1문장, 없으면 빈 문자열"},
    },
    "required": ["feature", "tip", "base", "top", "extra"],
    "additionalProperties": False,
}

WEATHER_RISK_SCHEMA = {
    "type": "object",
    "properties": {
        "risk": {"type": "boolean", "description": "폭염·한파·태풍·병해충 경보 등 긴급 위기 상황이 있으면 true"},
        "message": {"type": "string", "description": "risk가 true면 초보자에게 보낼 한 문장 경고 메시지(한국어), false면 빈 문자열"},
    },
    "required": ["risk", "message"],
    "additionalProperties": False,
}

ROOM_PERSONA = {
    "화분": (
        "당신은 '화분봇'입니다. 화분에서 채소·작물을 키우는 초보자들의 대화방에서 질문에 답하는 AI 도우미예요. "
        "화분 재배(물주기, 화분 크기, 실내·베란다 환경, 병충해 등)에 특화해서 친절하고 간결하게(3~5문장 이내) 답변하세요."
    ),
    "텃밭": (
        "당신은 '텃밭봇'입니다. 텃밭에서 작물을 키우는 사용자들의 대화방에서 질문에 답하는 AI 도우미예요. "
        "텃밭 재배(노지 환경, 토양, 배수, 날씨 대응, 병충해 등)에 특화해서 친절하고 간결하게(3~5문장 이내) 답변하세요."
    ),
}


def _get_api_key():
    try:
        key = st.secrets.get("ANTHROPIC_API_KEY")
        if key:
            return key
    except Exception:
        pass
    return os.environ.get("ANTHROPIC_API_KEY")


def generate_guideline(species: str, size: str, kind: str = "화분", language: str = "ko"):
    api_key = _get_api_key()
    if not api_key:
        return None

    client = anthropic.Anthropic(api_key=api_key)

    try:
        response = _create_with_retry(
            client,
            model=MODEL,
            max_tokens=2000,
            output_config={"format": {"type": "json_schema", "schema": GUIDE_SCHEMA}, "effort": "low"},
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"작물 '{species}'을(를) '{size}' {kind}에서 키우는 초보자를 위한 재배 가이드를 만들어줘. "
                        "심기(day 0)부터 수확 시작까지 5~8개의 핵심 관리 단계(예: 활착 확인, 지지대 설치, "
                        "웃거름 주기, 개화·착과, 수확 시작 등)를 이 작물의 특성에 맞게 만들어줘. "
                        "day는 정식/파종일로부터 경과 일수(정수), title은 10자 이내의 단계명, "
                        "desc는 초보자가 바로 실행할 수 있는 구체적인 한 문장 설명이어야 해."
                        f"{_lang_suffix(language)}"
                    ),
                }
            ],
        )
        text = next(b.text for b in response.content if b.type == "text")
        data = json.loads(text)
        if data.get("milestones"):
            return data
        return None
    except Exception:
        return None


def continue_ai_chat(room: str, messages: list, language: str = "ko"):
    """messages: [{"role": "user"|"assistant", "content": str}, ...] 전체 대화 기록 (마지막이 최신 사용자 메시지)"""
    api_key = _get_api_key()
    if not api_key:
        return None

    client = anthropic.Anthropic(api_key=api_key)
    persona = ROOM_PERSONA.get(room, ROOM_PERSONA["화분"]) + _lang_suffix(language)

    try:
        response = _create_with_retry(
            client,
            model=MODEL,
            max_tokens=1000,
            system=persona,
            output_config={"effort": "low"},
            messages=messages,
        )
        text = next((b.text for b in response.content if b.type == "text"), None)
        return text
    except Exception:
        return None


NEXT_CROP_LABEL = {
    "ko": "추천 작물", "en": "Recommended crop", "ja": "おすすめの作物",
    "zh": "推荐作物", "fr": "Culture recommandée",
}


def _crop_schema(allowed_species, extra_properties, required):
    crop_field = {"type": "string", "description": "추천 작물명 (목록 중 하나, 한국어)"}
    if allowed_species:
        crop_field["enum"] = list(allowed_species)
    return {
        "type": "object",
        "properties": {"crop": crop_field, **extra_properties},
        "required": ["crop", *required],
        "additionalProperties": False,
    }


def recommend_next_crop(species: str, kind: str, difficulty: str, review: str, language: str = "ko", allowed_species: list = None):
    """다음 작물을 하나 추천한다. allowed_species를 넘기면 그 목록 안에서만 고르도록 강제한다."""
    api_key = _get_api_key()
    if not api_key:
        return None

    client = anthropic.Anthropic(api_key=api_key)

    if difficulty == "쉬웠어요":
        difficulty_instruction = "이번 작물보다 살짝 더 도전적인(관리가 더 까다로운) 작물을 추천해줘."
    else:
        difficulty_instruction = "이번 작물보다 관리하기 더 쉬운 작물을 추천해줘."

    crop_choices = [c for c in (allowed_species or []) if c != species] or allowed_species
    schema = _crop_schema(
        crop_choices,
        {"reason": {"type": "string", "description": "왜 이 작물을 추천하는지, 후기와 난이도를 반영한 2~3문장 (한국어)"}},
        ["reason"],
    )

    try:
        response = _create_with_retry(
            client,
            model=MODEL,
            max_tokens=600,
            output_config={"format": {"type": "json_schema", "schema": schema}, "effort": "low"},
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"사용자가 '{kind}'에서 '{species}'를 재배했어요. "
                        f"난이도는 '{difficulty}'라고 느꼈고, 전체적인 후기는 다음과 같아요: \"{review}\"\n\n"
                        f"이 정보를 참고해서 다음에 키우기 좋은 작물을 하나 추천해줘. {difficulty_instruction} "
                        "reason은 왜 이 작물을 추천하는지 후기 내용과 난이도를 반영해서 "
                        "초보자가 이해하기 쉽게 2~3문장으로 설명해줘."
                        f"{_lang_suffix(language)}"
                    ),
                }
            ],
        )
        text = next((b.text for b in response.content if b.type == "text"), None)
        if not text:
            return None
        data = json.loads(text)
        crop, reason = data.get("crop"), data.get("reason")
        if not crop or not reason:
            return None
        label = NEXT_CROP_LABEL.get(language, NEXT_CROP_LABEL["ko"])
        return f"{label}: {crop}\n\n{reason}"
    except Exception:
        return None


def recommend_crop_for_observation(species: str, kind: str, observation: str, language: str = "ko", allowed_species: list = None):
    """후기에서 뽑아낸 문장 하나(관찰 포인트)에 집중해서 그 포인트에 맞는 작물을 하나 추천한다.
    allowed_species를 넘기면 그 목록 안에서만 고르도록 강제한다."""
    api_key = _get_api_key()
    if not api_key:
        return None

    client = anthropic.Anthropic(api_key=api_key)

    crop_choices = [c for c in (allowed_species or []) if c != species] or allowed_species
    schema = _crop_schema(
        crop_choices,
        {
            "emoji": {"type": "string", "description": "추천 작물을 대표하는 이모지 1개"},
            "reason": {"type": "string", "description": "이 관찰 포인트와 왜 잘 맞는지 1문장 (한국어)"},
        },
        ["emoji", "reason"],
    )

    try:
        response = _create_with_retry(
            client,
            model=MODEL,
            max_tokens=400,
            output_config={"format": {"type": "json_schema", "schema": schema}, "effort": "low"},
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"사용자가 '{kind}'에서 '{species}'를 키운 후기 중 이런 문장을 남겼어요: \"{observation}\"\n\n"
                        "이 문장이 나타내는 '좋았던 포인트' 하나에만 집중해서, 그 포인트를 가장 잘 살릴 수 있는 "
                        "다음 작물을 하나 추천해줘. crop은 작물명만 적고, reason은 왜 이 포인트에 이 작물이 "
                        "잘 맞는지 한 문장으로 설명해줘."
                        f"{_lang_suffix(language)}"
                    ),
                }
            ],
        )
        text = next((b.text for b in response.content if b.type == "text"), None)
        if not text:
            return None
        return json.loads(text)
    except Exception:
        return None


def diagnose_photo(species: str, size: str, elapsed_days: int, current_milestones: list, image_bytes: bytes, media_type: str, kind: str = "화분", history: list = None, language: str = "ko"):
    api_key = _get_api_key()
    if not api_key:
        return None

    client = anthropic.Anthropic(api_key=api_key)
    image_b64 = base64.standard_b64encode(image_bytes).decode("utf-8")
    milestones_json = json.dumps(current_milestones, ensure_ascii=False)

    if history:
        history_lines = "\n".join(
            f"- {h['date']} (심은 지 {h['elapsed_days']}일째): {h['diagnosis']}" for h in history
        )
        history_instruction = (
            f"\n\n이전 정밀검사 기록(시간순):\n{history_lines}\n\n"
            "위 이전 기록과 이번 사진을 비교해서 잎 크기·색깔·병충해 등에서 달라진 점이 있으면 "
            "diagnosis에 자연스럽게 포함해줘(예: '지난 검사 때보다 잎이 커지고 색이 진해졌어요')."
        )
    else:
        history_instruction = ""

    try:
        response = _create_with_retry(
            client,
            model=MODEL,
            max_tokens=2000,
            output_config={"format": {"type": "json_schema", "schema": DIAGNOSIS_SCHEMA}, "effort": "low"},
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {"type": "base64", "media_type": media_type, "data": image_b64},
                        },
                        {
                            "type": "text",
                            "text": (
                                f"이 사진은 '{species}'({size} {kind}, 심은 지 {elapsed_days}일째)의 현재 상태입니다. "
                                f"기존 재배 가이드라인: {milestones_json}\n\n"
                                "사진을 보고 생육 상태, 병충해, 영양 상태 등을 간단히 진단해줘(diagnosis, 2~4문장). "
                                "진단 결과를 반영해서 앞으로의 관리 일정을 필요하면 조정한 전체 가이드라인을 "
                                "milestones로 다시 만들어줘. day는 여전히 심은 날(day 0)로부터의 경과 일수 기준이야."
                                f"{history_instruction}"
                                f"{_lang_suffix(language)}"
                            ),
                        },
                    ],
                }
            ],
        )
        text = next(b.text for b in response.content if b.type == "text")
        data = json.loads(text)
        if data.get("milestones"):
            return data
        return None
    except Exception:
        return None


def diagnose_location(species: str, size: str, elapsed_days: int, current_milestones: list, location: str, kind: str = "텃밭", language: str = "ko"):
    api_key = _get_api_key()
    if not api_key:
        return None

    client = anthropic.Anthropic(api_key=api_key)
    milestones_json = json.dumps(current_milestones, ensure_ascii=False)

    try:
        response = _create_with_retry(
            client,
            model=MODEL,
            max_tokens=2000,
            tools=[{"type": "web_search_20260209", "name": "web_search", "max_uses": 1}],
            output_config={"format": {"type": "json_schema", "schema": DIAGNOSIS_SCHEMA}, "effort": "low"},
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"웹 검색을 1회만 사용해서 '{location}' 지역의 최근·앞으로 며칠간의 날씨(강수 여부, 흐림, 기온 등)를 확인해줘. "
                        f"그 날씨 정보를 바탕으로 '{species}'({size} {kind}, 심은 지 {elapsed_days}일째)의 관리 일정을 "
                        "실용적으로 조정해줘.\n\n"
                        f"기존 재배 가이드라인: {milestones_json}\n\n"
                        "날씨를 반영한 진단(diagnosis, 2~4문장 — 예: '비 예보가 있어 물주기를 이틀 미루세요' 처럼 "
                        "구체적인 조언)과, 조정된 전체 가이드라인(milestones)을 만들어줘. "
                        "day는 여전히 심은 날(day 0)로부터의 경과 일수 기준이야."
                        f"{_lang_suffix(language)}"
                    ),
                }
            ],
        )
        text = next((b.text for b in response.content if b.type == "text"), None)
        if not text:
            return None
        data = json.loads(text)
        if not data.get("milestones"):
            return None
        data["sources"] = _extract_web_sources(response)
        return data
    except Exception:
        return None


def _extract_web_sources(response):
    """web_search 도구 호출 결과에서 참고한 출처(제목·URL)를 뽑아낸다. 실패해도 진단 자체엔 영향 없음."""
    sources = []
    seen = set()
    try:
        for block in response.content:
            if getattr(block, "type", None) != "web_search_tool_result":
                continue
            for item in getattr(block, "content", None) or []:
                url = getattr(item, "url", None)
                title = getattr(item, "title", None)
                if url and url not in seen:
                    seen.add(url)
                    sources.append({"title": title or url, "url": url})
    except Exception:
        return []
    return sources[:5]


def explain_task(species: str, kind: str, size: str, title: str, desc: str, api_key: str = None, language: str = "ko"):
    """'오늘 할 일' 항목 하나를 완전 초보자도 따라할 수 있게 단계별로 자세히 설명해준다.

    api_key를 명시적으로 넘기면 그 값을 쓴다. 백그라운드 스레드에서는 st.secrets가
    스크립트 실행 컨텍스트 없이 접근되어 실패하므로(StreamlitSecretNotFoundError),
    메인 스레드에서 미리 키를 읽어 넘겨야 한다.
    """
    api_key = api_key or _get_api_key()
    if not api_key:
        return None

    client = anthropic.Anthropic(api_key=api_key)

    try:
        response = _create_with_retry(
            client,
            model=MODEL,
            max_tokens=2000,
            output_config={"effort": "low"},
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"'{species}'을(를) '{size}' {kind}에서 키우는 완전 초보자가 지금 해야 할 작업은 "
                        f"'{title}'({desc})입니다.\n\n"
                        "태어나서 처음 식물을 키워보는 사람도 그대로 따라할 수 있도록, 마크다운 번호 목록으로 "
                        "4~6단계로 아주 구체적으로 설명해줘. 각 단계는 짧게 끝내지 말고 다음 형식을 정확히 지켜줘:\n"
                        "1. **[단계 제목]**\n"
                        "   - 방법: 무엇을 어떤 도구로, 어느 정도(수량·길이·깊이·시간 등 구체적인 수치)로 하는지\n"
                        "   - 이유: 왜 이 작업이 필요한지 초보자가 이해할 수 있게 한 문장으로\n\n"
                        "이런 식으로 각 단계마다 '방법'과 '이유'를 별도의 하위 글머리 기호(-)로 나눠서 줄바꿈해줘. "
                        "본문 하나로 길게 이어쓰지 마.\n\n"
                        "마지막에는 '흔한 실수'라는 소제목(굵은 글씨) 아래에 초보자가 자주 하는 실수 1~2가지를 "
                        "글머리 기호로 알려줘.\n\n"
                        "형식 규칙을 반드시 지켜줘:\n"
                        "- 맨 위에 제목(#, ## 같은 마크다운 헤더)을 달지 마. 번호 목록으로 바로 시작해줘.\n"
                        "- 이모지나 이모티콘을 전혀 사용하지 마.\n"
                        "- 숫자 범위를 표기할 때 물결표(~) 대신 하이픈(-)을 써줘. 예: '90~120cm'가 아니라 '90-120cm'. "
                        "물결표는 마크다운에서 취소선으로 잘못 렌더링될 수 있어.\n"
                        "- 답변은 반드시 끝까지 완결된 문장으로 마무리해줘. 중간에 끊기지 않게 전체를 간결하게 써줘.\n"
                        "친절하고 쉬운 말로, 전문 용어는 풀어서 설명해줘."
                        f"{_lang_suffix(language)}"
                    ),
                }
            ],
        )
        return next((b.text for b in response.content if b.type == "text"), None)
    except Exception:
        return None


def generate_fertilizer_advice(species: str, kind: str = "화분", language: str = "ko"):
    """미리 정의된 그룹(잎채소/열매채소/알뿌리/고구마)에 없는 작물에 대해 비료 추천을 즉석에서 생성한다."""
    api_key = _get_api_key()
    if not api_key:
        return None

    client = anthropic.Anthropic(api_key=api_key)

    try:
        response = _create_with_retry(
            client,
            model=MODEL,
            max_tokens=800,
            output_config={"format": {"type": "json_schema", "schema": FERTILIZER_SCHEMA}, "effort": "low"},
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"작물 '{species}'을(를) '{kind}'에서 키우는 초보자를 위한 비료 추천 정보를 만들어줘. "
                        "이 작물이 잘 자라기 위해 필요한 핵심 영양 성분(질소·인산·칼륨 등)과 특징, "
                        "비료를 줄 때 주의할 팁, 추천 밑거름과 웃거름의 특징을 초보자가 이해하기 쉽게 설명해줘. "
                        "특별히 조심해야 할 점이나 꼭 보충해야 할 성분이 있으면 extra에 한 문장으로 적고, "
                        "없으면 빈 문자열로 둬."
                        f"{_lang_suffix(language)}"
                    ),
                }
            ],
        )
        text = next((b.text for b in response.content if b.type == "text"), None)
        if not text:
            return None
        return json.loads(text)
    except Exception:
        return None


def check_weather_risk(species: str, kind: str, location: str, language: str = "ko"):
    """텃밭 위치의 실시간 날씨를 검색해서 폭염·한파·태풍·병해충 등 긴급 위기 상황이 있는지 확인한다."""
    api_key = _get_api_key()
    if not api_key:
        return None

    client = anthropic.Anthropic(api_key=api_key)

    try:
        response = _create_with_retry(
            client,
            model=MODEL,
            max_tokens=600,
            tools=[{"type": "web_search_20260209", "name": "web_search", "max_uses": 1}],
            output_config={"format": {"type": "json_schema", "schema": WEATHER_RISK_SCHEMA}, "effort": "low"},
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"웹 검색을 1회만 사용해서 '{location}' 지역의 오늘·내일 날씨와 특보(폭염·한파·태풍·호우 등)를 확인해줘. "
                        f"그리고 이 지역에서 '{species}'({kind})를 키우는 사람에게 지금 당장 알려야 할 만큼 "
                        "긴급한 날씨 위기나 병해충 확산 위험이 있는지 판단해줘. "
                        "위기가 있으면 risk를 true로 하고 message에 초보자가 바로 이해하고 대응할 수 있는 "
                        "한 문장 경고를 적어줘(예: '내일 폭염특보가 있으니 한낮 물주기를 피하고 그늘막을 준비하세요'). "
                        "단순히 흐리거나 약간의 비 정도로는 risk를 true로 하지 말고, "
                        "실제로 작물에 피해를 줄 수 있는 수준일 때만 true로 해줘."
                        f"{_lang_suffix(language)}"
                    ),
                }
            ],
        )
        text = next((b.text for b in response.content if b.type == "text"), None)
        if not text:
            return None
        return json.loads(text)
    except Exception:
        return None
