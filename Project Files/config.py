from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ibm_api_key: str
    ibm_project_id: str
    ibm_endpoint_url: str
    pinecone_api_key: str

    model_config = SettingsConfigDict(env_file=".env", extra="allow")  # 👈 allow extra env variables

settings = Settings()
