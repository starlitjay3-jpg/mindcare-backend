from fastapi import FastAPI

app = FastAPI(title="MindCare Backend")

# 1. 가이드의 1번 항목: Health Check 엔드포인트
@app.get("/health")
def health_check():
    return {"status": "ok"}

# 2. 기본 접속 확인
@app.get("/")
def root():
    return {"message": "MindCare API Server is running!"}

# 참고: /auth/signup 등 나머지 기능은 다음 단계에서 
# 실제 로직(routers) 파일을 만든 후 연결할 예정입니다.