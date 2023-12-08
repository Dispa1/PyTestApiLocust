from locust import HttpUser, task, between
from faker import Faker

fake = Faker()

class MyUser(HttpUser):
    wait_time = between(1, 3)
    record_id = 1

    @task
    def create_record(self):
        # Генерация случайных данных для создания записи, соответствующих модели
        payload = {
            "date": fake.date_this_year().strftime("%Y-%m-%d"),
            "time": fake.time(),
            "brazier_1_Humidity": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "brazier_2_Humidity": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "press_1_Fat_Content": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "press_2_Fat_Content": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "press_1_Moisture_content": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "press_2_Moisture_content": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "humidity": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "protein": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "non_fat_after": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "acid_number": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "note": fake.text(),
        }

        # Запрос на создание записи
        self.client.post("/map-products-press-shop", json=payload)
        self.record_id += 1

    @task
    def update_record(self):
        # Генерация случайных данных для обновления записи, соответствующих модели
        updated_data = {
            "brazier_1_Humidity": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "brazier_2_Humidity": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "press_1_Fat_Content": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "press_2_Fat_Content": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "press_1_Moisture_content": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "press_2_Moisture_content": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "humidity": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "protein": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "non_fat_after": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "acid_number": fake.pyfloat(min_value=4, max_value=10, precision=2),
            "note": fake.text(),
        }

        # Запрос на обновление записи
        self.client.patch(f"/map-products-press-shop/{self.record_id}", json=updated_data)
        self.record_id += 1

    @task
    def remove_record(self):
        # Запрос на удаление записи
        self.client.delete(f"/map-products-press-shop/{self.record_id}")
        self.record_id += 1

    @task
    def get_all_records(self):
        # Запрос на получение всех записей
        self.client.get("/map-products-press-shop/getAll")

# Запускаем через консоль locust -f performance.py --host=http://localhost:5000
# После запуска, вы сможете открыть веб-интерфейс Locust (обычно по адресу http://localhost:8089) и начать выполнение тестов.