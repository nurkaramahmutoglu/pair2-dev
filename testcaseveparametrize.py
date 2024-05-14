#1) Başarılı giriş yaptıktan sonra sepete ekleyip satın alma işlemini tamamlar.
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TestProductPurchase:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        self.driver.quit()
    
    def test_invalid_login(self):
        username = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "user-name")))
        username.send_keys("standard_user")
        password = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "password")))
        password.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
    
    def test_add_to_cart(self):
        
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        add_to_cart_button.click()
        go_to_basket = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        go_to_basket.click()
        checkout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]')))
        checkout_button.click()

    def test_checkout_information(self):
        first_name = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "first-name")))
        first_name.send_keys("Furkan")
        last_name = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "last-name")))
        last_name.send_keys("Gümüşkaya")
        postal_code = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "postal-code")))
        postal_code.send_keys("34250")
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]')))
        continue_button.click()

    def test_finish_shopping(self):
        finish_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]')))
        finish_button.click()
        thank_you_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_complete_container"]/h2')))
        assert thank_you_message.text == "Thank you for your order!"
        print("Alışveriş işlemi başarıyla tamamlandı.")

        

#2)Parametrize fonksiyonu ile 3 farklı veriyle test

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class test_SauceDemo:
    def setup_method(self):
        # her test başlangıcında çalışacak fonksiyon
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        # her test bitiminde çalışacak fonksiyon
        self.driver.quit()

    @pytest.mark.parametrize("credentials", [
        {"username": "standard_user", "password": "secret_sauce", "expected_success": True, "error_message": ""},
        {"username": "locked_out_user", "password": "secret_sauce", "expected_success": False, "error_message": "Epic sadface: Sorry, this user has been locked out."},
        {"username": "deneme_test", "password": "secret_sauce", "expected_success": False, "error_message": "Epic sadface: Username and password do not match any user in this service"},
    ])
    def test_login(self, credentials):
        usernameInput = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name")))
        usernameInput.send_keys(credentials["username"])
        passwordInput = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password")))
        passwordInput.send_keys(credentials["password"])
        loginButton = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()

        # Başarılı veya başarısız giriş durumunu kontrol et
        if credentials["expected_success"]:
            assert "inventory.html" in self.driver.current_url
            print(f"{credentials['username']} kullanıcısı başarıyla giriş yaptı.")
        else:
            # Hata mesajını kontrol et ve doğru mesajı yazdır
            error_message_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')))
            assert error_message_element.text == credentials["error_message"]
            print(f"{credentials['username']} kullanıcısı giriş yapamadı. Hata Mesajı: {credentials['error_message']}")

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])

#3)Başarılı giriş yapar ardından çıkış yapar.

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support import expected_conditions as EC


class Test_sauceDemo:
    def setup_method(self): 
        # peş peşe testlerde, her test öncesi çalışacak fonksiyon
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() 
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):  
        # her test bitiminde çalılacak fonksiyon.
        self.driver.quit()   
    def test_exit_login(self):
        username = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"user-name")))
        username.send_keys("standard_user") # kullanıcı başarılı girer
        password = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
        password.send_keys("secret_sauce") # şifre girer 
        login_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"login-button")))
        login_button.click()

        assert "inventory.html" in self.driver.current_url
        print("successful entry")

    #def test_successful_logout(self):
            
        # self.test_valid_login()

        burger_menu = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]')))
        burger_menu.click()
        logout_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
        logout_button.click()

        assert "https://www.saucedemo.com/" in self.driver.current_url

        print("successful exit")

    