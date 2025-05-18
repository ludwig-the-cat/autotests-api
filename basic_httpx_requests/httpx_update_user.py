import httpx

import tools.fakers

# Определяем URL
CREATE_USER_URL = 'http://localhost:8000/api/v1/users'
AUTH_URL = 'http://localhost:8000/api/v1/authentication/login'
UPDATE_USER_URL = f'http://localhost:8000/api/v1/users/'

# Создаем пользователя
create_user_payload = {
    "email": tools.fakers.fake.email(),
    "password": "321321",
    "lastName": "lName",
    "firstName": "fName",
    "middleName": "mName"
}

# Отправляем запрос на создание пользователя и получаем данные
creating_user_response = httpx.post(CREATE_USER_URL, json=create_user_payload)
created_user_data = creating_user_response.json()
print(f'Status: {creating_user_response.status_code}')
print(f'Created user data: {creating_user_response.text}')

# получаем id пользователя для patch
user_id = created_user_data.get('user').get('id')

# формируем body для Auth
created_user_email = created_user_data.get('user').get('email')
created_user_password = create_user_payload.get('password')
auth_payload = {
    'email': created_user_email,
    'password': created_user_password
}

auth_response = httpx.post(AUTH_URL, json=auth_payload)
print(f'Status code: {auth_response.status_code}')
print(f'Response: {auth_response.text}')

# Получаем токен пользователя
auth_header = {
    "Authorization": f"Bearer {auth_response.json().get('token').get('accessToken')}"
}

# формируем body для обновления пользователя
update_payload = {
    "email": tools.fakers.fake.email(),
    "lastName": "lName",
    "firstName": "fName",
    "middleName": "mName"
}

# выполняем обновление
url = UPDATE_USER_URL + user_id
user_update_response = httpx.patch(url, json=update_payload, headers=auth_header)
print(f'Status: {user_update_response.status_code}')
print(f'Updated user data: {user_update_response.text}')