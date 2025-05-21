import pytest
from http import HTTPStatus
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response
from tools.fakers import fake

@pytest.mark.users
@pytest.mark.regression
@pytest.mark.parametrize('email', ['mail.ru', 'gmail.com','example.com'])
def test_create_user(email: str, public_users_client: PublicUsersClient):
    # Формируем тело запроса на создание пользователя
    request = CreateUserRequestSchema(email=fake.email(domain=email))
    # Отправляем запрос на создание пользователя
    response = public_users_client.create_user_api(request)
    # Инициализируем модель ответа на основе полученного JSON в ответе
    # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # Проверяем статус-код ответа
    assert_status_code(response.status_code, HTTPStatus.OK)

    # Проверяем, что данные ответа совпадают с данными запроса
    assert_create_user_response(request, response_data)

    # Проверяем что тела ответа соответсвует ожидаемой JSON-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())
