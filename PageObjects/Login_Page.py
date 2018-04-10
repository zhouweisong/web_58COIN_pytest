"""
-------------------------------------------------
   File Name：     Login_Page
   Description :
   Author :       zws
   date：          2018/4/3
-------------------------------------------------
   Change Activity:
                   2018/4/3:
-------------------------------------------------
"""
__author__ = 'zws'

from Common.BasePage import BasePage
from selenium.webdriver.common.by import By


class Login_Page(BasePage):
    #用户名输入框
    user_input ='//*[@placeholder="请输入账号"]'
    #密码输入框
    password_input = '//*[@placeholder="请输入密码"]'
    #登录按钮
    login = '//*[@value="登录"]'

    #登录流程
    def action_login(self,user_name,password):
        self.find_element(By.XPATH,self.user_input).send_keys(user_name)
        self.find_element(By.XPATH,self.password_input).send_keys(password)
        self.find_element(By.XPATH,self.login).click()
