# PrestaShop Test Automation Framework

## 1. What is this project

This project is an automated testing framework for the **PrestaShop e-commerce platform**.  
It combines **UI testing, API testing, and infrastructure automation** in a single repository.

The framework is designed to demonstrate a **complete QA automation environment**, including:

- UI testing with **Selenium + Pytest**
- API testing with **Requests**
- **Selenoid** for remote browser execution
- **Allure reports** for test results
- **Jenkins CI pipeline** for automated test execution

---

## Project Structure

```
├── api/                # API testing layer
│   ├── endpoints/      # API endpoints wrappers
│   ├── helpers/        # factories for test data
│   ├── models/         # builders for API objects
│   └── scenarios/      # business logic scenarios
│
├── page_objects/       # UI Page Object Model
├── steps/              # reusable UI test steps
│
├── tests/
│   ├── api/            # API tests
│   └── ui/             # UI tests
│
├── setup/              # scripts for PrestaShop initialization
│
├── selenoid/           # Selenoid configuration
│
├── docker-compose.yml  # test environment
├── Jenkinsfile         # CI pipeline
└── config.py           # project configuration
```

---

## Running Tests

The project supports multiple ways of running tests:


## 1. Locally run devcontainer

Export environment parameters:
```bash
export ADMIN_EMAIL={email} ADMIN_PASSWORD={password} \
API_KEY={key} API_URL={url}/api
```
Run tests:
```bash
pytest -m {test type} -v -s --executor=local --browser={browser} --headless
```
test type: api or ui

browser: ch = chrome or ff = firefox

## 2. Locally run by docker

Build docker image:
```bash
docker build -t {image}:{version} .
```

Run tests:
```bash
docker run -it --rm --network=host -e ADMIN_EMAIL={email} -e ADMIN_PASSWORD={password} -e API_KEY={key} image:version pytest -m {test type} -v -s --executor=local --browser={browser} --headless
```
test type: api or ui

browser: ch = chrome or ff = firefox

## 3. Running tests with Selenoid
Tests can run in remote browsers using Selenoid.

Run tests:
```bash
make run-all ADMIN_EMAIL={email} ADMIN_PASSWORD={password}
```

## 4. Running tests in CI

The project includes a Jenkins pipeline that:

1. clones the repository
2. starts the Docker environment
3. prepares PrestaShop (API setup)
4. runs UI and API tests
5. publishes an Allure report

## 5. Test Reports

Test results are stored in the `allure-results` directory.

Generate and view the report:

```bash
allure serve
```

## 1. Что это за проект?

Этот проект представляет собой автоматизированную среду тестирования для **платформы электронной коммерции PrestaShop**.
Он объединяет **тестирование UI, тестирование API и автоматизацию развёртывания инфраструктуры** в одном репозитории.

Среда тестирования включает в себя:

- Тестирование пользовательского интерфейса с помощью **Selenium + Pytest**
- Тестирование API с помощью **Requests**
- **Selenoid** для удаленного выполнения тестов в браузере
- **Allure reports** для отображения результатов тестирования
- **Конвейер CI Jenkins** для автоматизированного выполнения тестов

---

## Структура проекта

```
├── api/                # слой тестирования API
│   ├── endpoints/      # обертки для эндпоинтов API
│   ├── helpers/        # factories для тестовых данных
│   ├── models/         # builders для объектов API
│   └── scenarios/      # сценарии бизнес-логики
│
├── page_objects/       # UI Page Object модель
├── steps/              # многократно используемые шаги тестирования пользовательского интерфейса
│
├── tests/
│   ├── api/            # API тесты
│   └── ui/             # UI тесты
│
├── setup/              # скрипты для инициализации PrestaShop
│
├── selenoid/           # конфигурация Selenoid
│
├── docker-compose.yml  # тестовое окружение
├── Jenkinsfile         # CI pipeline
└── config.py           # конфигурационный файл проекта
```

---

## Запуск тестов

Проект поддерживает несколько способов запуска тестов:


## 1. Запуск локально в devcontainer

Экспорт параметров окружения:
```bash
export ADMIN_EMAIL={email} ADMIN_PASSWORD={password} \
API_KEY={key} API_URL={url}/api
```
Run tests:
```bash
pytest -m {test_type} -v -s --executor=local --browser={browser} --headless
```
{test_type} - api or ui

{browser} -  ch = chrome or ff = firefox

## 2. Запуск тестов локально с помощью Docker

Собрать образ:
```bash
docker build -t {image}:{version} .
```

Запустить тесты:
```bash
docker run -it --rm --network=host -e ADMIN_EMAIL={email} -e ADMIN_PASSWORD={password} -e API_KEY={key} image:version pytest -m {test_type} -v -s --executor=local --browser={browser} --headless
```
{test_type} - api or ui

{browser} - ch = chrome or ff = firefox

## 3. Запуск тестов с помощью Selenoid
Тесты можно запускать в удаленных браузерах с помощью Selenoid.

Run tests:
```bash
make run-all ADMIN_EMAIL={email} ADMIN_PASSWORD={password}
```

## 4. Запуск тестов в CI

Проект включает в себя конвейер Jenkins, который:

1. клонирует репозиторий
2. запускает среду Docker
3. подготавливает PrestaShop (настройка API)
4. запускает тесты пользовательского интерфейса и API
5. публикует отчет Allure

## 5. Test Reports

Результаты тестов хранятся в каталоге `allure-results`.

Сгенерируйте и просмотрите отчет:

```bash
allure serve
```