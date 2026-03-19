from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = "development"
    secret_key: str
    aes_key: str
    database_url: str
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    algorithm: str = "HS256"

    class Config:
        env_file = ".env"
        extra = "ignore"  # 👈 추가된 부분: 모르는 변수는 무시하라는 명령어

def get_settings():
    return Settings()