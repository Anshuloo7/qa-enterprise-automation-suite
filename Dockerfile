# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install OS dependencies for UI tests
RUN apt-get update && apt-get install -y \
    curl unzip wget chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install additional reporting tools
RUN pip install behave-html-formatter allure-behave

# Copy project files
COPY . .

# Default entrypoint runs Behave with Allure & HTML reports
ENTRYPOINT ["behave", "--junit", "--junit-directory=reports/junit", "--format", "behave_html_formatter:HTMLFormatter", "--outfile", "reports/html/report.html", "--format", "allure_behave.formatter:AllureFormatter", "--outfile", "reports/allure-results"]