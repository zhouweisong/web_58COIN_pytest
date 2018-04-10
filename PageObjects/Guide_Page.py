from Common.BasePage import BasePage
from selenium.webdriver.common.by import By


class Guide_Page(BasePage):
    #登录按钮
    login_icon = '//*[@style="margin-top:7px;font-weight:700;"]'
    #注册按钮
    regis_icon = 'margin-top: 7px; font-weight: 700;'

    #点击登录按钮
    def touch_login_icon(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.find_element(By.XPATH,self.login_icon).click()

    #点击注册按钮
    def touch_regis_icon(self,url):
        self.driver.get(url)
        self.find_element(By.XPATH, self.regis_icon).click()




