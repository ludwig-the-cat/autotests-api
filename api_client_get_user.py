from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_user_client, CreateUserRequestDict
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_user_client = get_public_user_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestDict(
  email=get_random_email(),
  password="string",
  lastName="string",
  firstName="string",
  middleName="string"
)

# Отправляем POST запрос на создание пользователя
create_user_response = public_user_client.create_user(create_user_request)
print(f'Created user data: {create_user_response}')

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(authentication_user)

# Отправляем GET запрос на получение данных пользователя
get_user_response = private_users_client.get_user(create_user_response.get('user').get('id'))
print(f'Get user data: {get_user_response}')
