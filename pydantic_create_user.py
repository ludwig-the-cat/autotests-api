from pydantic import BaseModel, Field, HttpUrl, EmailStr

# Добавили описание структуры пользователя
class UserSchema(BaseModel):
    """
    Описание структуры пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestDictSchema(BaseModel):
    """
    Описание структуры запроса для создания запроса
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseDictSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя
    """
    user: UserSchema
