from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema()

# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercise_client = get_exercises_client(authentication_user)

# Создаем файл
create_file_request = CreateFileRequestSchema(upload_file='./basic_httpx_requests/test-data/files/test_image.jpg')
# Отправляем запрос
create_file_response = files_client.create_file(create_file_request)
print(f'Created file data: {create_file_response}')

# Создаем курс
create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
# Отправляем запрос
create_course_response = courses_client.create_course(create_course_request)
print(f'Created course data: {create_course_response}')

# Создаем урок
create_exercise_request = CreateExerciseRequestSchema(course_id=create_course_response.course.id)
# Отправляем запрос
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print(f'Created exercise data: {create_exercise_response}')
