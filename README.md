# appium_mobile_app_automation_framework
An industry-standard mobile app automation testing framework using Appium and Python. Designed for scalability and maintainability, it includes robust configurations, page object models, and comprehensive test cases. Integrated with GitHub Actions for continuous integration.

### **Project Structure**

    MobileAppTestingFramework/
    │
    ├── config/
    │   ├── config.py
    │   ├── driver_setup.py
    │
    ├── tests/
    │   ├── test_login.py
    │   ├── test_signup.py
    │
    ├── pages/
    │   ├── base_page.py
    │   ├── login_page.py
    │   ├── signup_page.py
    │
    ├── utils/
    │   ├── locators.py
    │   ├── common.py
    │
    ├── screenshots/
    │   ├── login_tests/
    │   ├── signup_tests/
    │
    ├── reports/
    │   ├── latest/
    │   ├── history/
    │
    ├── .github/
    │   ├── workflows/
    │   │   ├── ci.yml
    │
    ├── .gitignore
    ├── pytest.ini
    ├── requirements.txt
    └── README.md


### **Continuous Integration (CI) with GitHub Actions**

#### `.github/workflows/ci.yml`

Set up a GitHub Actions workflow for CI:

### **Enhanced Reporting**

Integrate coverage and better HTML reporting:


### **Running Tests**

Run your tests locally with coverage:

```sh
pytest --maxfail=1 --disable-warnings --cov=.
```