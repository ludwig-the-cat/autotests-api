import socket


def server():
    """Создаем серверный сокет. Взаимодействие по IPv4, и TCP соединение (SOCK_STREAM)
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address) # привязываем socket к IP

    server_socket.listen(10) # определяем 10 соединений для сервера
    print('Сервер запущен и ждет подключения')

    users_messages = list()

    while True:
        # ждем клиентское соединение
        client_soket, client_address = server_socket.accept()
        print(f'Пользователь с адресом: {client_address} подключился к серверу')
        # получаем данные от клиента
        data = client_soket.recv(1024).decode()
        users_messages.append(data)
        print(f'Пользователь с адресом: {client_address} отправил сообщение: {data}')
        # формируем ответ клиенту
        client_soket.send('\n'.join(users_messages).encode())

        client_soket.close()


if __name__ == '__main__':
    server()
