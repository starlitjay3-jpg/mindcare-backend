from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = "development"
    secret_key: str
    aes_key: str
    database_url: str
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    algorithm: str = "HS256"
    OPENAI_API_KEY: str  # 이 줄이 반드시 있어야 Render의 값을 읽어옵니다!
    OPENAI_MODEL: str = "gpt-4o-mini"

    class Config:
        env_file = ".env"
        extra = "ignore"  # 👈 추가된 부분: 모르는 변수는 무시하라는 명령어

def get_settings():
    return Settings()

# 🚨 이 한 줄이 생명줄입니다! 
# 함수를 실행해서 'settings'라는 실제 객체를 만들어 수출(Export)합니다.
settings = get_settings()