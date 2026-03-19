from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import get_settings

settings = get_settings()

# Supabase DB 엔진 가동
engine = create_async_engine(settings.database_url, echo=True)

# DB 접속 세션 공장
AsyncSessionLocal = sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# 모든 DB 모델의 기초가 되는 뼈대 클래스
Base = declarative_base()

# 통신 연결/해제 관리자
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session