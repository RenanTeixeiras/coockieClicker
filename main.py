from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


class CookieClicker:
    def __init__(self):
        self.SITE_LINK = 'https://orteil.dashnet.org/cookiecliker/'
        self.SITE_MAP = {} # coordenadas dos objetos
        self.options = Options()
        self.options.add_experimental_option("detach", True)

        self.driver = driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.driver.maximize_window


    
    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)


biscoito = CookieClicker()
biscoito.abrir_site()