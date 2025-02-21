#1)Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class test_login:
   
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() #ekranı büyütür
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        self.driver.quit()

    def test_invalid_login(self):
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys()
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys()
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        expected_message = "Epic sadface: Username is required" # beklenen hata mesajı alanı 
        actual_message = self.driver.find_element(By.XPATH, "//div[contains(@class, 'error-message-container')]").text # sayfadaki hata mesajını yakalar ve actual_message adlı değişkende saklar.
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}" # bu kısımda Actual Mesajda sakladığı mesajı alır Expected mesaj ile karşılaştırır
        assert expected_message  ==  "Epic sadface: Username is required"
        

#2) Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import openpyxl

class Test_Sauce:
    def setup_method(self):
        #her test başlangıcında çalışacak fonksiyon
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() 
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        #her test bitiminde çalışacak fonksiyon
        self.driver.quit()

    def test_invalid_login(self):
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys()
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("irem")
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        assert errorMessage.text == "Epic sadface: Password is required" 

#3)Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import openpyxl
     
     
class Test_Sauce:
    def setup_method(self):
        #her test başlangıcında çalışacak fonksiyon
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() 
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        #her test bitiminde çalışacak fonksiyon
        self.driver.quit()
        
    def test_invalid_Login(self):
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("locked_out_user")
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
     
#4)Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 


class Test_Login:
    def setup_method(self):
        #her test başlangıcında çalışacak fonksiyon
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() 
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        #her test bitiminde çalışacak fonksiyon
        self.driver.quit()

    def test_valid_login(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click() 
        appLogo = self.driver.find_element(By.CLASS_NAME, "app_logo")
        testResult = appLogo.text == "Swag Labs"
        
        inventoryİtemName = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name ")
        print(f"TEST SONUCU:  {testResult}")
        self.driver.execute_script("window.scrollTo(0,500)") 
        self.driver.get("https://www.saucedemo.com/inventory-item.html?id=4")    

    time.sleep(5)
     
#5)Add to cart butonuna tıkladığında sepete gidip eklenip eklenmediğini kontrol etmek

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TestSepetKontrol:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_valid_login(self):
        self.login("standard_user", "secret_sauce")
        assert "inventory.html" in self.driver.current_url
    
    def test_add_to_cart(self):
        self.login("standard_user", "secret_sauce")
        self.add_to_cart()
        assert self.is_cart_contains_item(), "Ürün sepete eklenemedi."
    
    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys(username)
        
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.send_keys(password)
        
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        
    def add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        add_to_cart_button.click()

    def is_cart_contains_item(self):
        shopping_cart_container = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        shopping_cart_container.click()
        cart_items = self.driver.find_elements(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]')
        return len(cart_items) > 0

