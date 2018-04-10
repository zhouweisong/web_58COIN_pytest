
from selenium import webdriver
from PageObjects.Guide_Page import Guide_Page
from PageObjects.Login_Page import Login_Page
from PageObjects.home_page import Home_Page
from testdata import login_testdata as TD
from testdata import COMM_DATA as CD
from Common.logger import *
import pytest

@pytest.mark.usefixtures('init_driver')
@pytest.mark.login
class Test_Login():

    @pytest.mark.smoke
    def test_login_ok(self,init_driver):

        logging.info("=========测试用例：正常登陆==========")
        guide_page = Guide_Page(init_driver)
        #引导页点击登录
        guide_page.touch_login_icon(CD.web_url)
        login_page = Login_Page(init_driver)
        #登录页登录操作
        login_page.action_login(CD.login_username,CD.login_passwd)
        #校验
        homepage = Home_Page(init_driver)
        logging.debug(TD.check_nickname)
        logging.debug(homepage.get_nickname())

        assert TD.check_nickname in homepage.get_nickname()


    # def test_login_noUsername(self):
    #     logging.info("测试用例：异常用例 - 用户名为空")
    #     # 登陆
    #     self.guide_page.login(CD.web_url, "", TD.login_passwd_ok)
    #     #校验
    #     self.assertEqual(TD.check_noUser_info, self.guide_page.get_wrong_info())
    #
    #
    # def test_login_noPasswd(self):
    #     logging.info("测试用例：异常用例 - 密码为空")
    #     # 登陆
    #     self.guide_page.login(CD.web_url, TD.login_username_ok, "")
    #     #校验
    #     self.assertEqual(TD.check_noPasswd_info, self.guide_page.get_wrong_info())

