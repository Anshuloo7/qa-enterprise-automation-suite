# QA Enterprise Automation Suite

---

## Project Overview

Automation suite for API testing and service virtualization using **Behave**, **FastAPI**, and **Docker**.

---

## Features

* API Testing with Behave (GET & POST scenarios)
* Config-driven environments (QA/Staging)
* Mock Payment Service using FastAPI
* Positive & Negative scenarios for payment
* Dockerized mock service for consistent execution

---

## Project Structure

```
qa-enterprise-automation-suite/
├── features/
│   ├── api.feature
│   ├── payment.feature
│   ├── environment.py
│   └── steps/
│       ├── api_steps.py
│       └── payment_steps.py
├── mocks/
│   ├── payment_service.py
│   └── Dockerfile
├── config/
│   └── config.yaml
├── testdata/
│   └── payments.yaml
├── utils/
│   ├── config_loader.py
│   └── data_loader.py
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## How to Run

### 1. Clone the repository

```bash
git clone git@github.com:Anshuloo7/qa-enterprise-automation-suite.git
cd qa-enterprise-automation-suite
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run API Tests

```bash
behave features/api.feature
```

To run in a different environment:

```bash
behave features/api.feature --define env=staging
```

---

## Run Mock Service with Docker

Start the mock service:

```bash
docker compose up --build -d
```

Verify service:

```bash
curl -X POST http://127.0.0.1:8000/process-payment \
-H "Content-Type: application/json" \
-d '{"amount": 100, "currency": "USD"}'
```

Expected:

```json
{"status":"success","message":"Payment processed successfully"}
```

Run payment scenarios:

```bash
behave features/payment.feature
```

Stop the mock service:

```bash
docker compose down
```
