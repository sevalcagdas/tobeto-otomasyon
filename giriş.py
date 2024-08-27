from telnetlib import EC
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser():
    # Webdriver'ı başlat
    driver = webdriver.Chrome()
    yield driver
    # Test tamamlandıktan sonra tarayıcıyı kapat
    driver.quit()

def test_giris(browser):
    # Adım 1: Sitenin giriş sayfasına git
    browser.get("https://tobeto.com/giris")
    browser.maximize_window()
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("christoper.wylder@floodouts.com")
    password_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("123456")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()

    # Google ReCAPTCHA iframe'i bul
    iframe = WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
    # "Ben robot değilim" checkbox'ını işaretle
    robot_checkbox = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='recaptcha-anchor']")))
    robot_checkbox.click()
    giris_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]"))).click()
    # Ana frame'e geri dön
    browser.switch_to.default_content()





