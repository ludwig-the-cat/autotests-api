from pydantic import BaseModel, Field

from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    Описание схемы токена
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginResponseSchema(BaseModel):
    """
    Описание схемы ответа схемы
    """
    token: TokenSchema

class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence) # Название ключа совпадает с API