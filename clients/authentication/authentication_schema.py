from pydantic import BaseModel, Field

class TokenSchema(BaseModel):
    """
    Описание модели токена
    """
    tokenType: str = Field(alias=)
    accessToken: str
    refreshToken: str
