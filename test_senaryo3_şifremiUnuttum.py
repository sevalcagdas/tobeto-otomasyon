
from time import sleep
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

def test_password_reset(browser):
    #  Tobeto giriş sayfasına git
    browser.get("https://tobeto.com/giris")
    # Şifremi Unuttum butonuna tıkla.
    sifremi_unuttum_button = WebDriverWait(browser, 10).until( EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/label/small/button")))
    browser.execute_script("arguments[0].click();", sifremi_unuttum_button)
    # Adım 2: E-posta kısmına kayıtlı bir e-posta adresi gir
    email_input = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/input")))
    email_input.send_keys("christoper.wylder@floodouts.com")
    # Adım 3: Gönder butonuna tıkla
    send_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/button")))
    send_button.click()
# : Gönder butonuna tıkladıktan sonra “Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin.” pop-up bildirim olarak çıkmalıdır.
    success_message = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div[2]")))
    assert "Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin." in success_message.text

#Adım 4: Şifre sıfırlama isteği gönderilen mail adresinin gelen kutusunu kontrol et.
#Adım 5: Tobeto tarafından gönderilen mail içeriğinde ki linke tıkla.
#Adım 6: Yönlendirilen şifre sıfırlama sayfasında yeni şifreni gir.

def test_link(browser):
    browser.get("https://tobeto.com/reset-password")
    yenisifre_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/form/div/div/input[1]")
    yenisifre_input.send_keys("100")
    yenisifre_tekrar_input = browser.find_element(By.XPATH,   "//*[@id='__next']/div/main/section/div/form/div/div/input[2]")
    yenisifre_tekrar_input.send_keys("100")
    gonder_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/form/div/div/button")
    gonder_button.click()
    sleep(5)

    #Mesaj eklenecek

def test_hatalımail_sifreSıfırlama(browser):
    #  Tobeto giriş sayfasına git
    browser.get("https://tobeto.com/giris")
    # Şifremi Unuttum butonuna tıkla.
    sifremi_unuttum_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/label/small/button")))
    browser.execute_script("arguments[0].click();", sifremi_unuttum_button)
    # Adım 2: E-posta kısmına kayıtlı bir e-posta adresi gir
    email_input = WebDriverWait(browser, 10).until(  EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/input")))
    email_input.send_keys("christopercom")
    # Adım 3: Gönder butonuna tıkla
    send_button = WebDriverWait(browser, 10).until( EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/button")))
    send_button.click()
    sleep(3)

    #hata mesajı ekle






































