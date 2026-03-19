from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str  # 사용자가 입력한 고민 내용
    history: Optional[List[dict]] = []  # 이전 대화 내역 (선택 사항)

class ChatResponse(BaseModel):
    content: str  # AI 상담사의 답변
    emotion_tag: str  # 분석된 사용자의 감정 (예: 슬픔, 기쁨, 불안)