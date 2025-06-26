# Kafka App — учебный проект

## 📁 Структура проекта

```
my-kafka-app/
├── app/
│   ├── main.py              # Точка входа приложения
│   ├── kafka_client.py      # Продюсер и консюмер Kafka
├── tests/
│   ├── unit/
│   │   └── test_kafka_client.py      # Юнит-тесты для клиента Kafka
│   └── integration/
│       └── test_integration.py       # Интеграционные тесты Kafka
├── Dockerfile                # Сборка образа для деплоя
├── requirements.txt          # Python-зависимости
├── docker-compose.yml        # Запуск Kafka и app локально
├── kafka-deployment.yaml     # Kubernetes Deployment приложения
└── .gitlab-ci.yml            # CI/CD pipeline
```

---

## 📜 Описание файлов

### 🔹 `app/main.py`
Точка входа в приложение. Запускает продюсер и консюмер Kafka.

### 🔹 `app/kafka_client.py`
Реализация KafkaProducer и KafkaConsumer. Использует `kafka-python` для подключения к топику.

---

### 🔹 `tests/unit/test_kafka_client.py`
Модульные тесты. Проверяют работу продюсера/консьюмера в изоляции.

### 🔹 `tests/integration/test_integration.py`
Интеграционные тесты. Проверяют работу Kafka с реальным брокером.

---

### 🔹 `Dockerfile`
Инструкция для сборки образа.

---

### 🔹 `requirements.txt`
Зависимости.

---

### 🔹 `docker-compose.yml`
Локальный запуск Kafka и сервиса.

---

### 🔹 `kafka-deployment.yaml`
Kubernetes Deployment для развертывания приложения.

---

### 🔹 `.gitlab-ci.yml`
Автоматизация CI/CD.

---

## ▶️ Запуск проекта

### 🔹 1. Локально через Docker Compose
```bash
docker-compose up --build
```

### 🔹 2. В Kubernetes (Minikube)
```bash
minikube start --driver=docker
& minikube -p minikube docker-env | Invoke-Expression
docker build -t kafka-app:latest .
kubectl create namespace kafka
kubectl apply -f kafka-deployment.yaml
kubectl get pods -n kafka
```

---

## ✅ Задание выполнено:
- [x] Повторено и запущено локально и в Minikube
- [x] Все файлы описаны

