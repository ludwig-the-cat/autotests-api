from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
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

# Инициализируем клиенты
authentication_user = AuthenticationUserDict(
    email=create_user_request.get('email'),
    password=create_user_request.get('password')
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercise_client = get_exercises_client(authentication_user)

# Создаем файл
create_file_request = CreateFileRequestDict(
    filename='image.jpg',
    directory='courses',
    upload_file='./basic_httpx_requests/test-data/files/test_image.jpg'
)
# Отправляем запрос
create_file_response = files_client.create_file(create_file_request)
print(f'Created file data: {create_file_response}')

# Создаем курс
create_course_request = CreateCourseRequestDict(
    title='Python',
    maxScore=100,
    minScore=10,
    description='Python API course',
    estimatedTime="2 weeks",
    previewFileId=create_file_response.get('file').get('id'),
    createdByUserId=create_user_response.get('user').get('id')
)
# Отправляем запрос
create_course_response = courses_client.create_course(create_course_request)
print(f'Created course data: {create_course_response}')

# Создаем урок
create_exercise_request = CreateExerciseRequestDict(
    title="Primitives",
    courseId=create_course_response.get('course').get('id'),
    maxScore=10,
    minScore=1,
    orderIndex=1,
    description='The lesson about primitives',
    estimatedTime='3 mins'
)
# Отправляем запрос
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print(f'Created exercise data: {create_exercise_response}')
