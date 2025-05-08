from locust import HttpUser, task, between


# Use the following commands to run locust
# locust -f locustfile.py --host=http://localhost:30080
# locust -f locustfile.py --host=http://127.0.0.1:30080
class MLModelUser(HttpUser):
    wait_time = between(1, 3)  # simulates user think time

    @task
    def predict(self):
        payload = {
            "features": [6.0, 2.9, 4.5, 1.5]
        }
        headers = {'Content-Type': 'application/json'}
        self.client.post("/predict/", json=payload, headers=headers)