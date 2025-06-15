# Финальная работа по курсу "Автоматизация тестирования с помощью Selenium и Python" на Stepik - https://stepik.org/course/575/info

## Начало работы

### 1. Клонируйте репозиторий

Для начала работы клонируйте репозиторий проекта с помощью Git:

```bash
    git clone https://github.com/brizyriot/final_course_stepik
    cd final_course_stepik
```

### 2. Создайте виртуальную среду

Рекомендуется использовать виртуальную среду для управления зависимостями проекта. Следуйте инструкциям для вашей операционной
системы:

#### Linux / MacOS

```bash
  python3 -m venv venv
  source venv/bin/activate
```

#### Windows

```bash
  python -m venv venv
  venv\Scripts\activate
```

### 3. Установить зависимости

Как только виртуальная среда будет активирована, установите зависимости проекта, перечисленные в `requirements.txt`:

```bash
  pip install -r requirements.txt
```

### 4. Запустите тесты

Чтобы запустить тесты, используйте следующую команду:

```bash
  python -m pytest -v --tb=line --language=en -m need_review
```

Это запустит тесты, нуждающиеся в ревью и отобразит результаты в терминале.
