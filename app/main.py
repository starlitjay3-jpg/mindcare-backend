from fastapi import FastAPI, Depends
from app.schemas import ChatRequest, ChatResponse
from app.services.ai_service import get_counseling_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MindCare Backend")

# ==========================================
# 🚨 CORS 설정 (프론트엔드 통신 허락)
# ==========================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 주소 허용
    allow_credentials=False, # 인증 정보 포함 여부 (False로 해야 에러가 안 납니다)
    allow_methods=["*"],  # 모든 통신 방법(GET, POST 등) 허용
    allow_headers=["*"],  # 모든 헤더 허용
)
# ==========================================

# 1. 가이드의 1번 항목: Health Check 엔드포인트
@app.get("/health")
def health_check():
    return {"status": "ok"}

# 2. 기본 접속 확인
# 2. 기본 접속 확인
@app.get("/")
def root():
    return {"message": "MindCare API Server is running with CORS!"} # ✨ 뒤에 글자를 추가합니다!

# 참고: /auth/signup 등 나머지 기능은 다음 단계에서 
# 실제 로직(routers) 파일을 만든 후 연결할 예정입니다.
@app.post("/chat/counsel", response_model=ChatResponse)
async def chat_counsel(request: ChatRequest):
    content, emotion = await get_counseling_response(request.message, request.history)
    return ChatResponse(content=content, emotion_tag=emotion)