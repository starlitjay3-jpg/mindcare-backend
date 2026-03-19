from openai import AsyncOpenAI
from app.core.config import settings

# 1. 클라이언트를 생성합니다 (최신 방식)
client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

async def get_counseling_response(message: str, history: list = []):
    system_prompt = (
        "당신은 공감 능력이 뛰어난 전문 심리 상담사입니다. "
        "따뜻하게 위로하며, 답변 끝에는 반드시 [감정: 기쁨/슬픔/불안/분노/평온] 중 하나를 태그로 달아주세요."
    )

    messages = [{"role": "system", "content": system_prompt}]
    for h in history:
        messages.append(h)
    messages.append({"role": "user", "content": message})

    # 2. 호출 방식이 client.chat.completions.create로 바뀌었습니다.
    response = await client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=messages,
        temperature=0.7,
    )

    full_content = response.choices[0].message.content
    
    emotion = "평온"
    if "[감정:" in full_content:
        emotion = full_content.split("[감정:")[1].replace("]", "").strip()
        full_content = full_content.split("[감정:")[0].strip()

    return full_content, emotion