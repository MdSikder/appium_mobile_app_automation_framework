# Mobile App Automation Framework

## Overview
This repository contains an industry-standard mobile app automation testing framework powered by Appium and Pytest. It is designed for scalability, maintainability, and ease of integration with continuous integration systems such as GitHub Actions.

## Features
- **Appium & Pytest Integration**: Leverage the power of Appium for mobile automation and Pytest for testing.
- **Page Object Model**: Maintainable and scalable code structure.
- **Continuous Integration**: Integrated with GitHub Actions for seamless CI/CD.
- **Comprehensive Reporting**: Detailed HTML reports and test coverage metrics.
- **Robust Configuration**: Easily configurable using YAML files.

## Project Structure
```
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
```

## Getting Started

### Prerequisites
- Python 3.8+
- Appium server
- Android SDK

### Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/Mobile-Automation-Projects.git
   cd Mobile-Automation-Projects
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up the Appium server**:
   Ensure the Appium server is running:
   ```sh
   appium
   ```

4. **Configure the environment**:
   Update `config/config.yaml` with your device and app details:
   ```yaml
   Config:
     APPIUM_SERVER_URL: "http://localhost:4723/wd/hub"
     PLATFORM_NAME: "Android"
     DEVICE_NAME: "YourDeviceName"
     APP_PACKAGE: "com.example.yourapp"
     APP_ACTIVITY: ".MainActivity"
     TIMEOUT: 30
   ```

### Running Tests
To execute the test suite, run:
```sh
pytest
```

### Continuous Integration
This project is configured to use GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/ci.yml`.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries or issues, please contact [rased.sikder.kc@gmail.com].