from httpx import Client, QueryParams, URL, Response
from httpx._types import RequestData, RequestFiles

from typing import Any


class APIClient:
    def __init__(self, client: Client):
        """
        Базовые API клиент, принимающий объект httpx.Client.
        :param client: Экземпляр httpx.Client для выполнения HTTP-запросов
        """
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Выполняет  GET-запрос.
        :param url: URL эндпоинта
        :param params: GET-параметр запроса (например, ?key=value).
        :return: Объект Response c данными ответа
        """
        return self.client.get(url, params=params)

    def post(self, url: URL | str,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None
             ) -> Response:
        """
        Выполняет POST-запрос
        :param url: URL эндпоинта
        :param json: Данные в формате JSON
        :param data: Форматированные данные формы (например, application/x-www-form-urlencoded)
        :param files: Файлы для загрузки на сервер
        :return: Объект Response с данными ответа
        """
        return self.client.post(url, data=data, files=files, json=json)

    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Выполняет PATCH-запрос (частичное обновление данных).
        :param url: URL эндпоинта
        :param json:  Данные в формате JSON
        :return: Объект Response с данными ответа
        """
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str) -> Response:
        """
        Выполняет DELETE-запрос (удаление данных).
        :param url: URL-адрес эндпоинта.
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(url)