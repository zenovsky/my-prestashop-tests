# PrestaShop Test Automation Framework

## 1. Что это за проект?

Этот проект представляет собой автоматизированную среду тестирования для **платформы электронной коммерции PrestaShop**.
Он объединяет **тестирование UI, тестирование API и автоматизацию инфраструктуры** в одном репозитории.

Среда тестирования предназначена для демонстрации **полной среды автоматизации QA**, включая:

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


## 1. Запущенный локально контейнер для разработки devcontainer

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