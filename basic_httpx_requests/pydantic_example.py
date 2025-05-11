from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias='isActive')

user_data = {
    'id': 1,
    'name': 'A',
    'email': '@',
    'isActive': True
}

user=User(**user_data)
print(user.model_dump())
print(user.model_dump_json())