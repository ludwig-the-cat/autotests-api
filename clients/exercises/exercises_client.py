from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class GetExerciseQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка уроков в курсе
    """
    courseId: str

class CreateExerciseQueryDict(TypedDict):
    """
    Описание структуры запроса на создание урока
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseQueryDict(TypedDict):
    """
    Описание структуры запроса на изменение урока
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExerciseQueryDict) -> Response:
        """
        Метод получения списка упражнений в курсе
        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/exercises', params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения урока.
        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseQueryDict) -> Response:
        """
        Метод создания урока
        :param request: Словарь с title, courseId, maxScore, minScore,
        orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseQueryDict ) -> Response:
        """
        Метод обновления урока
        :param exercise_id: Словарь с title, maxScore, minScore,
        orderIndex, description, estimatedTime.
        :param request:  Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления урока
        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')