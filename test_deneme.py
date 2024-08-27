from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    # Webdriver'ı başlat
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Test tamamlandıktan sonra tarayıcıyı kapat
    driver.quit()

def test_profil(browser, dropdown=None):
    # Adım 1: Basarili giris yap.
    browser.get("https://tobeto.com/giris")
    # Kullanıcı adı ve şifre girme işlemi
    email_input = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
    email_input.send_keys("fatmabetulsebat@gmail.com")
    password_input = browser.find_element(By.XPATH,"//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
    password_input.send_keys("172915ymz")
    login_button = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
    login_button.click()
    # Platform açılmalıdır.
    platform_title = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")))
    sleep(4)
    # Adim 2: 'Profilim" alanindan profil bilgilerim butonuna tikla.
    profilalani = browser.find_element(By.XPATH, "//*[@id='__next'] / div/nav/div[1]/div/div/div[2]/button").click()
    profilbilgileri = browser.find_element(By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a").click()

    # Adım 3: “Adınız” alanına adını gir
    sleep(2)
    adiniz = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")
    browser.execute_script("arguments[0].value = ' '", adiniz)
    sleep(2)
    adiniz = browser.find_element(By.NAME, "name").send_keys("fatma betül sebat")
    sleep(1)
    # Adım 4: “Soyadınız” alanına soyadını gir.
    browser.find_element(By.NAME,"surname").clear()
    sleep(1)
    soyadiniz = browser.find_element(By.NAME, "surname").send_keys("tanır")
    sleep(1)
    # Adım5: Telefon numarası kısmından ülke kodu alanından inputu seç.
    ulke_kodu = browser.find_element(By.NAME, "phoneNumberCountry").click()
    alan_kodu = browser.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div/div/select/option[225]").click()

    # Adım6: “Telefon Numaranız” alanına numara gir.
    sleep(2)
    telefon_numaraniz = browser.find_element(By.XPATH, '//*[@id="phoneNumber"]')
    browser.execute_script("arguments[0].value = ' '", telefon_numaraniz)
    sleep(5)
    telefon_numaraniz = browser.find_element(By.XPATH, '//*[@id="phoneNumber"]').send_keys(+905556652655)
    sleep(1)
    # Adım7: “Doğum Tarihiniz” alanına inputu gir ya da takvim işaretine tıkla takvimden seç.
    dogum_tarihiniz= browser.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/input").send_keys(24091990)
    sleep(1)
    # Adım8: “T.C. Kimlik No” ve ‘Ülke’ alanını gir.
    identifier_input = browser.find_element(By.NAME, 'identifier')
    identifier_input.clear()
    eleven_digit_number = '43231624072'
    identifier_input.send_keys(eleven_digit_number)
    entered_value = identifier_input.get_attribute('value')

    # # BU KISIM CASELERDE YOK
    # cinsiyet = browser.find_element(By.XPATH, "//*[@id='react-select-2-input']")
    # cinsiyet.send_keys("Erkek")
    # cinsiyet.send_keys(Keys.RETURN)
    #
    # askerlik = browser.find_element(By.XPATH, "//*[@id='react-select-3-input']")
    # askerlik.send_keys("yapti")
    # askerlik.send_keys(Keys.RETURN)
    #
    # engellilik = browser.find_element(By.XPATH, "//*[@id='react-select-4-input']")
    # engellilik.send_keys("var")
    # engellilik.send_keys(Keys.RETURN)
    #
    # github_adresi = browser.find_element(By.NAME, "githubAddress")
    # github_adresi.send_keys("blablabla")
    #
    # ulke = browser.find_element(By.NAME, "country").send_keys("Turkiye")

    # Adım9: “İl” alanına tıkla ve listeden ili seç.
    il = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[13]/select").click()
    sleep(2)
    istanbul = browser.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[13]/select/option[41]").click()
    sleep(2)
    # Adım10: “İlçe” alanına tıkla ve listeden ilçeyi seç.
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # sayfa sonuna gelmeden butonu bulamiyor
    sleep(5)
    ilce = browser.find_element(By.NAME, "district").click()
    sleep(2)
    avcilar = browser.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[14]/select/option[5]").click()
    sleep(2)

    #Adım11: “Mahalle / Sokak” alanına bilgileri gir.
    browser.execute_script("window.scrollBy(0, 500)")   #Sayfa kaymadigindan bulamiyor
    mahalle_sokak = browser.find_element(By.NAME, "address").send_keys("Murat Mah. Sancar Sok.")

    # Adım 12: “Hakkımda” alanına bilgileri gir.
    hakkinda = browser.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[16]/textarea").send_keys("Yazılım Test mühendisliği alanında Tobetoda eğitim alıyorum.")
    sleep(2)

    # Adım 13: Kaydet butonuna tıklayın.

    buton = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button").click()

    sleep(10)
