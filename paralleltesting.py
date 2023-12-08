from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Время ожидания между запросами в секундах

    @task
    def get_map_products(self):
        # Задаем URL, к которому будем делать запрос
        url = "/map-products-press-shop/getAll"

        # Отправляем GET-запрос по указанному URL
        response = self.client.get(url)

        # Выводим информацию о выполненном запросе (необязательно)
        print(f"Response status code: {response.status_code}")

# Запускаем через консоль locust -f paralleltesting.py --host=http://localhost:5000
# После запуска, вы сможете открыть веб-интерфейс Locust (обычно по адресу http://localhost:8089) и начать выполнение тестов.
