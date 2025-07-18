# QA Enterprise Automation Suite

## **Overview**

A **comprehensive enterprise-grade automation framework** combining **API Testing**, **UI Testing**, **Contract Testing**, and **Database Validation** in one solution. Built with **Python + Behave (BDD)**, fully **Dockerized**, and integrated into **GitHub Actions** for CI/CD pipelines.

✨ **Live Reports:** [View Test Reports](https://anshuloo7.github.io/qa-enterprise-automation-suite/)

---

## ✅ **Key Differentiators**

* **Database Validation (SQLite)** – Verify API transactions with persistent DB checks.
* **Contract Testing with Pact** – Ensure microservice compatibility with consumer-driven contracts.
* **Unified API + UI Testing** – Behave BDD + Selenium (POM design) for seamless multi-layer coverage.
* **Mock Services** – FastAPI-powered mocks for isolated and reliable tests.
* **Docker-Native Execution** – Run anywhere with consistent environments.
* **Enterprise-Level Reporting** – Allure, HTML, and JUnit with screenshots and logs.

---

## **Core Features**

* **BDD Test Scenarios:** Gherkin syntax for better collaboration.
* **Multi-Layer Validation:** API, UI, Contract Testing, and DB checks.
* **Advanced Logging:** Full tracebacks, request-response capture.
* **CI/CD Ready:** Automated Docker builds, report hosting, and artifact management.

---

## **Tech Stack**

* **Language:** Python 3.11
* **Framework:** Behave (BDD)
* **UI Automation:** Selenium + Page Object Model
* **Contract Testing:** Pact
* **Database:** SQLite for validation
* **Reports:** Allure, Behave HTML, JUnit XML
* **Containers:** Docker & Docker Compose
* **CI/CD:** GitHub Actions

---

## **Detailed Project Structure**

```
qa-enterprise-automation-suite/
├── .github/workflows/         # CI/CD pipeline
├── config/                    # Environment configs
├── contract_tests/            # Pact contract test scripts
├── contracts/pacts/           # Generated Pact contract files
├── db/                        # SQLite database for validations
├── features/                  # BDD feature files & steps
│   ├── api_tests/             # API scenarios
│   ├── ui_tests/              # UI scenarios
│   └── steps/                 # Step definitions
├── mocks/                     # FastAPI-based mock payment service
├── pages/                     # Selenium Page Object Model classes
├── utils/                     # Logging, drivers, config loaders
├── reports/                   # HTML & Allure reports
├── testdata/                  # Test data files (YAML)
├── Dockerfile                 # Automation container
├── docker-compose.yml         # Orchestration for mocks + tests
└── requirements.txt           # Python dependencies
```

---

## **How to Run**

### **1. Clone Repo**

```bash
git clone https://github.com/Anshuloo7/qa-enterprise-automation-suite.git
cd qa-enterprise-automation-suite
```

### **2. Run Tests in Docker**

```bash
docker compose down -v
docker compose up --build --abort-on-container-exit
```

Reports will be stored under `reports/`.

---

## **Reporting**

* **HTML Report:** `reports/html/report.html`
* **Allure Report:** `reports/allure-results/`

```bash
allure serve reports/allure-results
```

✅ **Live Hosted Reports:** [GitHub Pages](https://anshuloo7.github.io/qa-enterprise-automation-suite/)

---

## **CI/CD Pipeline Highlights**

* Full regression in Docker
* Uploads JUnit, Allure, HTML reports as artifacts
* Deploys HTML report to GitHub Pages

Pipeline file: `.github/workflows/ci-tests.yml`