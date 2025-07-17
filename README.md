# QA Enterprise Automation Suite

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Behave](https://img.shields.io/badge/BDD-Behave-green)
![API](https://img.shields.io/badge/API-Testing-orange)

---

## ✅ Project Overview

An **enterprise-grade automation suite** demonstrating best practices for **multi-layer testing**:

* UI + API + DB validation
* Service virtualization & contract testing
* Performance and CI/CD integration

This project is designed for **SDET roles**, showcasing capabilities beyond simple test automation, including **test architecture, scalability, and environment strategy**.

---

## ✅ Current Features (Stage 2)

✔ **Environment-driven config** using YAML (QA/Staging)
✔ **BDD Framework** with Behave
✔ **API Testing**:

* `GET /products` → Validate list of products
* `POST /products` → Create a new product and verify details

---

## ✅ Tech Stack

* **Language:** Python 3.x
* **Framework:** Behave (BDD)
* **API Testing:** Requests
* **Config Management:** YAML + Hooks
* **Future Add-ons:** Pact (Contract Testing), FastAPI (Mocks), Locust (Performance)

---

## ✅ Project Structure

```
qa-enterprise-automation-suite/
├── features/
│   ├── api.feature
│   ├── environment.py
│   └── steps/
│       └── api_steps.py
├── config/
│   └── config.yaml
├── utils/
│   └── config_loader.py
├── requirements.txt
└── README.md
```

---

## ✅ How to Run

1. **Clone the repository**

```bash
git clone git@github.com:Anshuloo7/qa-enterprise-automation-suite.git
cd qa-enterprise-automation-suite
```

2. **Create Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run Tests**

```bash
behave features/api.feature
```

✅ To run in a different environment:

```bash
behave features/api.feature --define env=staging
```