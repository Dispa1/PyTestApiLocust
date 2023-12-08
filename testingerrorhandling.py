from locust import HttpUser, task, between
from faker import Faker

fake = Faker()

class MyUser(HttpUser):
    wait_time = between(1, 3)
    current_id = 1

    @task
    def create_success(self):
        url = "/map-products-press-shop"

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

        response = self.client.post(url, json=payload)

        assert response.status_code == 200
        self.current_id += 1

    @task
    def create_failure(self):
        url = "/map-products-press-shop"
        invalid_payload = {"invalid": "data_here"}  # Замените на невалидные данные

        response = self.client.post(url, json=invalid_payload)

        assert response.status_code >= 400 and response.status_code < 500

    @task
    def update_success(self):
        url = f"/map-products-press-shop/{self.current_id}"

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

        response = self.client.patch(url, json=updated_data)

        assert response.status_code == 200

    @task
    def update_failure(self):
        url = f"/map-products-press-shop/{self.current_id}"
        invalid_data = {"invalid": "data_here"}  # Замените на невалидные данные

        response = self.client.patch(url, json=invalid_data)

        assert response.status_code >= 400 and response.status_code < 500

    @task
    def remove_success(self):
        url = f"/map-products-press-shop/{self.current_id}"

        response = self.client.delete(url)

        assert response.status_code == 200

    @task
    def remove_failure(self):
        non_existing_record_id = 999

        url = f"/map-products-press-shop/{non_existing_record_id}"

        response = self.client.delete(url)

        assert response.status_code >= 400 and response.status_code < 500

    @task
    def get_all_records(self):
        self.client.get("/map-products-press-shop/getAll")


# Запускаем через консоль locust -f testingerrorhandling.py --host=http://localhost:5000
# После запуска, вы сможете открыть веб-интерфейс Locust (обычно по адресу http://localhost:8089) и начать выполнение тестов.