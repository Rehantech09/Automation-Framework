## WorkflowPro Automation Framework

## Overview

This repository contains an automation testing framework built for a **B2B multi-tenant SaaS platform (WorkflowPro)**.
The framework demonstrates **UI testing, API testing, and API + UI integration testing** using **Playwright with Python and Pytest**.

The goal of this project is to showcase:

* Reliable test automation practices
* Handling of multi-tenant applications
* Cross-layer validation (Backend + Frontend)
* Scalable and maintainable framework design

## Tech Stack Used

* **Language:** Python
* **UI Automation:** Playwright
* **Test Runner:** Pytest
* **API Testing:** Requests (conceptual / mocked)
* **Design Pattern:** Modular test structure with fixtures
* **Version Control:** Git & GitHub



## Project Structure

automation-framework/
│
├── tests/
│   └── integration/
│       └── test_project_creation_flow.py
│
├── fixtures/
│   ├── browser.py
│   └── api_client.py
│
├── api_clients/
│   └── project_api.py
│
├── requirements.txt
└── pytest.ini


## Folder Explanation

* **tests/** → All test cases
* **fixtures/** → Pytest fixtures for browser and API setup
* **api_clients/** → Backend API interaction logic
* **requirements.txt** → Project dependencies
* **pytest.ini** → Pytest configuration



## Test Scenario Covered

### API + UI Integration Test

The main test validates the **end-to-end project creation flow**:

1. **Create a project via API**
2. **Verify the project appears on Web UI**
3. **Ensure project is not visible to another tenant (tenant isolation)**

This approach ensures:

* Backend and frontend consistency
* Data visibility across layers
* Security boundaries in a multi-tenant system

---

## Test Design Approach

* **API-first strategy** is used to create test data quickly and reliably
* **UI validation** confirms correct rendering of backend data
* **Tenant isolation checks** ensure data security between companies
* **Explicit waits and controlled setup** reduce test flakiness


##  Assumptions Made

* Real backend APIs are not accessible, so API responses are **mocked** to demonstrate integration logic
* BrowserStack mobile testing is represented conceptually (not executed)
* Authentication and 2FA flows are assumed to be handled outside test scope
* Credentials and URLs are dummy placeholders

These assumptions are common and acceptable for take-home assignments.

---

## How to Run the Tests

### 1. Install dependencies

pip install -r requirements.txt

### 2. Install Playwright browsers

playwright install


### 3. Run tests

pytest

## Why This Framework

* Clear separation of concerns (UI, API, fixtures)
* Easy to extend for more tests and environments
* CI/CD friendly structure
* Designed with real-world SaaS testing challenges in mind


## Future Enhancements

* Add Page Object Model for UI pages
* Integrate BrowserStack for real mobile testing
* Add reporting (Allure / HTML reports)
* Enable parallel execution in CI/CD


