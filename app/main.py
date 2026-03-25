from fastapi import FastAPI, Depends
from app.schemas import ChatRequest, ChatResponse
from app.services.ai_service import get_counseling_response
from fastapi.middleware.cors import CORSMiddleware # ✨ 필수 부품 추가!

app = FastAPI(title="MindCare Backend")

# ==========================================
# 🚨 CORS 설정 (이 부분이 없어서 계속 에러가 났습니다!)
# ==========================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 주소 허용
    allow_credentials=False,
    allow_methods=["*"],  # OPTIONS, POST 등 모든 통신 허용
    allow_headers=["*"],  # 모든 헤더 허용
)
# ==========================================

# 1. 가이드의 1번 항목: Health Check 엔드포인트
@app.get("/health")
def health_check():
    return {"status": "ok"}

# 2. 기본 접속 확인 (테스트 문구 포함)
@app.get("/")
def root():
    return {"message": "MindCare API Server is running with CORS!"}

# 참고: /auth/signup 등 나머지 기능은 다음 단계에서 
# 실제 로직(routers) 파일을 만든 후 연결할 예정입니다.
@app.post("/chat/counsel", response_model=ChatResponse)
async def chat_counsel(request: ChatRequest):
    content, emotion = await get_counseling_response(request.message, request.history)
    return ChatResponse(content=content, emotion_tag=emotion)