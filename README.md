# AutoScaleML: Auto-Scaling ML Model Serving Platform

A Django-based platform to serve ML models with automatic scaling, observability, and seamless CI/CD deployment. Built to solve the problem of spiky traffic handling in real-world ML applications (e.g., demand forecasting during holidays).

---

## 🚀 Features

- 🔮 **ML Inference API**: Exposes `/predict` for real-time predictions using pre-trained models.
- 🛠️ **Admin Panel**: Django Admin to manage logs and model metadata.
- 🗃️ **MySQL Logging**: Stores input/output/latency for every prediction.
- 🐳 **Dockerized**: Fully containerized using Docker.
- 🔁 **CI/CD with Jenkins**: Automates build, test, and deployment.
- ☸️ **Kubernetes Deployment**: Runs on a K8s cluster for orchestration.
- 📈 **Auto-Scaling**: Kubernetes HPA dynamically scales pods based on CPU.
- 👀 **Observability**: Endpoints like `/health` and `/metrics` for monitoring.

---

## 🧱 Tech Stack

| Layer       | Technology         |
|------------|--------------------|
| API Server | Django + Django REST Framework |
| Model      | scikit-learn (example) |
| Database   | MySQL              |
| Container  | Docker             |
| CI/CD      | Jenkins            |
| Orchestration | Kubernetes       |
| Metrics    | Custom endpoints (Prometheus-ready) |

---

## 🧩 Architecture

1. User sends a request to `/predict`
2. Django loads the model and returns a prediction
3. Logs are written to MySQL
4. Jenkins automates deployments
5. Kubernetes runs the app with auto-scaling enabled
6. Observability endpoints and dashboards show system metrics

---

## 📦 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/AutoScaleML.git
cd AutoScaleML
```

### 2. Configure Environment
Create a .env file or update settings.py with:
- MySQL credentials
- Model path

### 3. Build & Run (Docker)
```bash
docker build -t autoscaleml-api .
docker run -p 8000:8000 autoscaleml-api
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Access Admin Panel
Visit http://localhost:8000/admin

Create superuser: python manage.py createsuperuser

---

## 📊 Observability

| Endpoint  |	Description                        |
|------------|--------------------|
| /health  |	Returns model/server status       |
| /metrics  |	Shows latency, request rate, etc.  |
