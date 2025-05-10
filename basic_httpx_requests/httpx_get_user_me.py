import httpx

# Определяем URL
LOGIN_POST_URL = 'http://localhost:8000/api/v1/authentication/login'
GET_USER_URL = 'http://127.0.0.1:8000/api/v1/users/me'

# Определяем body для аутентификации
payload = {
    'email': 'admin@example.com',
    'password': '123123'
}

# Отправляем запрос и получаем данные
response = httpx.post(LOGIN_POST_URL, json=payload)
auth_data = response.json()
print(f'Status code: {response.status_code}')
print(f'Response: {auth_data}')

# Формируем header для get запроса на получение данных
auth_header = {
    'Authorization': f'Bearer {auth_data.get("token").get("accessToken")}'
}

# Отправляем запрос и получаем данные
response_get_me = httpx.get(GET_USER_URL, headers=auth_header)
print(f'Status code: {response_get_me.status_code}')
print(f'Response: {response_get_me.text}')