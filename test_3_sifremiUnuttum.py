from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_password_reset(browser):

    browser.get("https://tobeto.com/sifremi-unuttum")

    # Adım 3: E-posta kısmına kayıtlı bir e-posta adresi gir
    email_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/input")))
    email_input.send_keys("christoper.wylder@floodouts.com")
    # Adım 4: Gönder butonuna tıkla
    send_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/button")))
    send_button.click()
    # Adım 5: Gönder butonuna tıkladıktan sonra başarı mesajını kontrol et
    success_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div[2]")))
    assert "Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin." in success_message.text

    # Adım 6: E-posta kontrolü (manuel olarak yapılacak)


def test_reset_password_with_new_password(browser):
    # Adım 7: Şifre sıfırlama linkine tıkla ve yeni şifre sayfasına git
    browser.get("https://tobeto.com/reset-password")
    # Adım 8: Yeni şifreyi gir
    new_password_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/form/div/div/input[1]")))
    new_password_input.send_keys("yeniSifre123")
    # Yeni şifrenin tekrarını gir
    new_password_confirm_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/form/div/div/input[2]")))
    new_password_confirm_input.send_keys("yeniSifre123")
    # Adım 9: Gönder butonuna tıkla
    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/section/div/form/div/div/button")))
    submit_button.click()
    # Beklenen sonuç: Şifre sıfırlama işlemi başarılı bildirimi alınmalıdır
    success_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div[2]")))
    assert "Şifre sıfırlama işlemi başarılı" in success_message.text


def test_invalid_email_password_reset(browser):

    browser.get("https://tobeto.com/sifremi-unuttum")

    # Adım 3: E-posta kısmına geçersiz bir e-posta adresi gir
    email_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/input")))
    email_input.send_keys("gecersiz@gmail")
    # Adım 4: Gönder butonuna tıkla
    send_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/button")))
    send_button.click()
    # Beklenen sonuç: Geçersiz e-posta mesajını kontrol et
    error_message = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body[style*='color: white;']")))
    assert "Başarısız" in error_message.text































