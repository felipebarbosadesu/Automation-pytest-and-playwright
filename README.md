# Automation with Pytest & Playwright

## End-to-End Web Testing Framework — Swag Labs (SauceDemo)

This repository contains an **end-to-end (E2E) web test automation framework** built with **Python**, using **Pytest** and **Playwright**, focused on **e-commerce testing**.

The project was created as part of my **Python and QA Automation studies**, applying industry best practices such as **Page Object Model**, **CI/CD with GitHub Actions**, **automated test reports**, and **evidence collection**.

Target application: [https://www.saucedemo.com/](https://www.saucedemo.com/)

---

## Scope of tests

The framework currently covers real e-commerce scenarios:

* **Authentication**

  * Valid users
  * Locked user (`locked_out_user`)
* **Cart**

  * Add products (Smoke tests)
* **Checkout**

  * Complete happy path (Regression / E2E)
* **Test evidences**

  * Screenshot on failure
  * Execution video
  * Playwright trace for execution replay

---

## Tech stack

* Python
* Pytest
* Playwright
* Page Object Model (POM)
* GitHub Actions (CI/CD)
* HTML Test Report
* JUnit (test result summary)

---

## Local execution

### 1) Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -U pip
pip install -r requirements.txt
playwright install
```

### 3) Environment configuration

Create a `.env` file from the example:

```bash
cp .env.example .env
```

### 4) Run tests

```bash
pytest
```

### Run smoke tests only

```bash
pytest -m smoke
```

### Run regression / E2E tests

```bash
pytest -m regression
```

---

## Reports and evidences

### HTML report

```bash
pytest --html=artifacts/reports/report.html --self-contained-html
```

### Generated evidences

* Screenshots (only on failure):
  `artifacts/screenshots/`
* Execution videos:
  `artifacts/videos/`
* Playwright traces:
  `artifacts/traces/`

To open a trace:

```bash
playwright show-trace artifacts/traces/<file>.zip
```

---

## CI/CD — GitHub Actions

The project includes automated workflows using **GitHub Actions**:

* Daily scheduled execution
* Automated test result summary
* Upload of reports and evidences as artifacts
* Execution summary available directly in the workflow **Summary** tab

Workflow files:

```text
.github/workflows/
├── tests.yml        # runs on push / pull request
└── daily-tests.yml  # daily scheduled execution
```

---

## Test credentials (SauceDemo)

Accepted usernames:

* `standard_user`
* `locked_out_user`
* `problem_user`
* `performance_glitch_user`
* `error_user`
* `visual_user`

Password for all users:

```text
secret_sauce
```

---

## Project goal

The main goals of this project are:

* Strengthen Python skills applied to QA automation
* Demonstrate modern and reliable web test automation
* Apply real CI/CD practices
* Serve as a professional QA automation portfolio project
