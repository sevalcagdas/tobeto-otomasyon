

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_chatbot(browser):

    # Adım 1: Tobeto anasayfasına git
    browser.get("https://tobeto.com/giris")

    #chatbot tıkla
    # Chatbot ikonunu bul
    chatbot_icon = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".exw-open-launcher")))

    # Chatbot ikonuna tıkla
    chatbot_icon.click()





