import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: en, ru, fr, etc."
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print(f"\nЗапуск браузера для языка: {user_language}")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless=new")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nЗакрытие браузера..")
    driver.quit()