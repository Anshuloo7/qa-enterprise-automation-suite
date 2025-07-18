# QA Enterprise Automation Suite
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Behave](https://img.shields.io/badge/BDD-Behave-green)
![Docker](https://img.shields.io/badge/Containerized-Docker-blue)
![GitHub Actions](https://img.shields.io/badge/CI-CD-yellow)
## **Overview**

The **QA Enterprise Automation Suite** is a robust, scalable automation framework built using **Python + Behave (BDD)**, integrated with **Docker** and **GitHub Actions** for CI/CD. It supports:

* **UI + API Testing**
* **Mocked Services** for isolated testing
* **Detailed HTML and Allure Reports**
* **Dynamic Logging with Full Request/Response Tracing**

This solution is designed for **enterprise-grade test automation** with full CI/CD integration, environment configuration, and artifact management.

---

## **Key Features**

✅ **BDD with Behave** – Human-readable scenarios for better collaboration.

✅ **API & UI Validation** – Multi-layer testing with reusable steps.

✅ **Mock Services** – Custom mock server for external dependencies.

✅ **Advanced Logging** – Captures:

* Request & Response Details
* Headers, Status Codes, and Payload
* Full Error Tracebacks for failures

✅ **Reporting** –

* **Behave HTML Report**
* **JUnit XML** (CI Integration)
* **Allure Report with Attachments**

✅ **Dockerized Execution** – Consistent environment across local and CI.

✅ **CI/CD Integration** – GitHub Actions pipeline with artifact uploads & GitHub Pages deployment.

---

## **Tech Stack**

* **Language:** Python 3.11
* **Framework:** Behave (BDD)
* **Reports:** Behave HTML Formatter, Allure
* **Containerization:** Docker, Docker Compose
* **CI/CD:** GitHub Actions

---

## **Project Structure**

```
qa-enterprise-automation-suite/
│
├── features/                 # BDD Feature files
│   ├── steps/                # Step Definitions
│   └── api.feature           # API Test Scenarios
│
├── mocks/                    # Mock Payment Service (FastAPI)
│   └── Dockerfile
│
├── utils/                    # Helpers (logging, config, retry)
│   ├── logger_setup.py
│   ├── config_loader.py
│   └── retry.py
│
├── reports/                  # Test Reports (HTML, Allure)
│
├── Dockerfile                # Automation container build
├── docker-compose.yml        # Service orchestration
├── requirements.txt          # Python dependencies
└── README.md
```

---

## **Getting Started**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/qa-enterprise-automation-suite.git
cd qa-enterprise-automation-suite
```

### **2. Run with Docker**

```bash
docker compose down -v
docker compose up --build --abort-on-container-exit
```

Reports will be generated under `reports/html` and `reports/allure-results`.

---

## **Reporting**

### **HTML Report**

Located at: `reports/html/report.html`

### **Allure Report**

Generate Allure Report locally:

```bash
allure serve reports/allure-results
```

---

## **CI/CD Workflow**

* **Pipeline File:** `.github/workflows/ci.yml`
* **Steps:**

  * Build & Run Tests in Docker
  * Upload HTML & Allure Reports as artifacts
  * Deploy HTML Report to **GitHub Pages**

Reports can be accessed via the **gh-pages** branch URL.

---

## **Environment Variables**

* `ENV` – Target environment (e.g., qa)
* `PAYMENT_URL` – Mock Payment Service endpoint

---

## **Key Commands**

### **Run Behave Tests with Reports**

```bash
behave \
  --junit --junit-directory=reports/junit \
  --format behave_html_formatter:HTMLFormatter --outfile reports/html/report.html \
  --format allure_behave.formatter:AllureFormatter --outfile reports/allure-results
```

---

## **Future Enhancements**

* ✅ Allure Report Hosting on GitHub Pages
* ✅ Add Docker support for Allure Serve
* ✅ Integration with Slack for notifications
* ✅ Add UI Test Scenarios using Selenium/Playwright




