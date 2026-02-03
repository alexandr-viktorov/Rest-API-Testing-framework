# REST API Testing Framework

A Python-based automated testing framework for REST API testing using pytest, with integrated Allure reporting and CI/CD pipeline via GitHub Actions.

## Overview

This framework provides comprehensive testing capabilities for RESTful APIs, featuring object-oriented design patterns, detailed test reporting, and automated continuous integration. The framework tests CRUD operations (Create, Read, Update, Delete) on the [RESTful API Dev](https://restful-api.dev) service.

## Features

- **Object-Oriented Architecture**: Clean separation of concerns with endpoint classes
- **Allure Reporting**: Rich, interactive test reports with step-by-step execution details
- **Parametrized Testing**: Data-driven tests using pytest parametrization
- **CI/CD Integration**: Automated testing pipeline with GitHub Actions
- **Fixtures Management**: Reusable test fixtures for setup and teardown
- **Detailed Logging**: Comprehensive logging for debugging and analysis

## Project Structure

```
Rest API Testing framework/
├── endpoints/               # API endpoint classes
│   ├── base_endpoint.py    # Base class with common methods
│   ├── create_object.py    # Create object endpoint
│   ├── get_object.py       # Get object endpoint
│   ├── update_object.py    # Update object endpoint
│   ├── delete_object.py    # Delete object endpoint
│   └── patch_object.py     # Patch object endpoint
├── tests/                  # Test files
│   ├── test_demo.py        # Main test suite
│   └── test_data/          # Test data and expected results
│       ├── payloads.py
│       └── expected_results.py
├── .github/
│   └── workflows/
│       └── run_tests.yml   # CI/CD pipeline configuration
├── allure-results/         # Allure test results (generated)
├── conftest.py            # Pytest fixtures and configuration
└── requirements.txt       # Project dependencies
```

## Prerequisites

- Python 3.14 or higher
- pip (Python package installer)
- Allure CLI (for local report generation)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd "Rest API Testing framework"
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Allure CLI (optional, for local reporting):
   - **Windows**: Download from [Allure releases](https://github.com/allure-framework/allure2/releases)
   - **Mac**: `brew install allure`
   - **Linux**: Download and extract from releases page

## Running Tests

### Run all tests:
```bash
pytest tests/
```

### Run tests with Allure reporting:
```bash
pytest tests/ --alluredir allure-results/
```

### Generate and view Allure report:
```bash
allure serve allure-results/
```

### Run specific test class:
```bash
pytest tests/test_demo.py::TestObjectsAPI
```

### Run specific test:
```bash
pytest tests/test_demo.py::TestObjectsAPI::test_create_object
```

## Test Coverage

The framework includes tests for the following API operations:

- **Create Object** (`POST /objects`): Creates new objects with various payloads
- **Get Object** (`GET /objects/{id}`): Retrieves objects by ID
- **Update Object** (`PUT /objects/{id}`): Fully updates existing objects
- **Delete Object** (`DELETE /objects/{id}`): Deletes objects and verifies removal

## Allure Reporting

The framework integrates Allure for detailed test reporting with:
- Test execution timeline
- Step-by-step test details
- Success/failure statistics
- Severity levels and feature organization
- Parametrized test results

### Report Features:
- **Features**: Organized by API functionality
- **Stories**: Grouped by operation type (Create, Read, Update, Delete)
- **Severity Levels**: Critical, Major, Minor
- **Steps**: Detailed step execution with attachments

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:
1. Sets up Python environment
2. Installs dependencies
3. Creates allure-results directory
4. Runs test suite
5. Uploads test artifacts
6. Installs Allure CLI
7. Generates HTML report
8. Publishes report to GitHub Pages

### Workflow Trigger:
The pipeline runs automatically on every push to the repository.

### Viewing Reports:
After pipeline execution, reports are available:
- As workflow artifacts (downloadable)
- On GitHub Pages (if configured)

## Configuration

### conftest.py
Contains pytest fixtures, including:
- `obj_id`: Creates a test object before tests and cleans up after

### Test Data
Test payloads and expected results are stored in [tests/test_data/](tests/test_data/):
- `payloads.py`: Request payloads for different operations
- `expected_results.py`: Expected API responses

## Dependencies

Key dependencies (see [requirements.txt](requirements.txt) for full list):
- `pytest==9.0.2`: Testing framework
- `allure-pytest==2.15.2`: Allure reporting integration
- `requests==2.32.5`: HTTP library for API calls
- `selenium==4.39.0`: Browser automation (if needed)

## Best Practices

1. **Endpoint Classes**: Each API endpoint has its own class inheriting from `Endpoint`
2. **Allure Steps**: All methods are decorated with `@allure.step()` for detailed reporting
3. **Assertions**: Separate assertion methods for clear test validation
4. **Fixtures**: Use pytest fixtures for test setup and teardown
5. **Parametrization**: Data-driven tests using `@pytest.mark.parametrize`

## Troubleshooting

### Common Issues:

1. **Allure command not found**:
   - Ensure Allure CLI is installed and added to PATH
   - In GitHub Actions, the workflow installs it automatically

2. **Import errors**:
   - Verify virtual environment is activated
   - Run `pip install -r requirements.txt`

3. **API connection issues**:
   - Check internet connectivity
   - Verify API endpoint: https://api.restful-api.dev/objects

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure they pass
5. Submit a pull request

## License

This project is for educational and testing purposes.

## Author

Created as a demonstration of REST API testing automation with Python, pytest, and Allure reporting. Also demonstate implemented CI/CD pipline integration for Github/Actions.