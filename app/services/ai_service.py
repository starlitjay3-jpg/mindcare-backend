import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

async def get_counseling_response(message: str, history: list = []):
    # 상담사 페르소나 설정 (System Prompt)
    system_prompt = (
        "당신은 공감 능력이 뛰어난 전문 심리 상담사입니다. "
        "사용자의 고민을 경청하고, 따뜻하게 위로하며, 실질적인 심리적 조언을 제공하세요. "
        "답변 끝에는 반드시 [감정: 기쁨/슬픔/불안/분노/평온] 중 하나를 태그로 달아주세요."
    )

    messages = [{"role": "system", "content": system_prompt}]
    
    # 이전 대화가 있다면 추가
    for h in history:
        messages.append(h)
    
    messages.append({"role": "user", "content": message})

    response = await openai.ChatCompletion.acreate(
        model=settings.OPENAI_MODEL,
        messages=messages,
        temperature=0.7,  # 창의성과 일관성의 균형
    )

    full_content = response.choices[0].message.content
    
    # 감정 태그 추출 (예시 로직)
    emotion = "평온"
    if "[감정:" in full_content:
        emotion = full_content.split("[감정:")[1].replace("]", "").strip()
        full_content = full_content.split("[감정:")[0].strip()

    return full_content, emotion