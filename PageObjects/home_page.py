from Common.BasePage import BasePage
from selenium.webdriver.common.by import By

class Home_Page(BasePage):
    # 首页 - 法币OTC交易(mainNav)
    home_mainNav_fbDeal_locator= "//div[@class = 'main-nav flex-box flex-direction-row flex-justify-start flex-align-item-start flex-wrap-nowrap']/a[@href = 'https://c2c.58coin.com']"
    # 首页 - 币币交易(mainNav)
    home_mainNav_BbDeal_locator= "//div[@class = 'main-nav flex-box flex-direction-row flex-justify-start flex-align-item-start flex-wrap-nowrap']/a[@href = 'https://spot.58coin.com/']"
    # 首页 - 云算力交易(mainNav)
    home_mainNav_CCPDeal_locator = "//div[@class = 'main-nav flex-box flex-direction-row flex-justify-start flex-align-item-start flex-wrap-nowrap']/a[@href = 'https://hash.58coin.com/']"
    # 首页 - 杠杆交易(mainNav)
    home_mainNav_leverDeal_locator ="//div[@class = 'main-nav flex-box flex-direction-row flex-justify-start flex-align-item-start flex-wrap-nowrap']/a[@href = 'https://www.58coin.com/coming/experience']"
    # 首页 - 高杠杆交易(mainNav)
    home_mainNav_highLeverDeal_locator ="//div[@class = 'main-nav flex-box flex-direction-row flex-justify-start flex-align-item-start flex-wrap-nowrap']/a[@href = 'https://www.58coin.com/coming/coming-soon']"
    # 首页 - 账户昵称
    home_userInfoLink_locator = '//a[@href="/users"]'
    # 首页 - 退出
    home_esc_locator = "//div[@class = 'common-header flex-box flex-direction-row flex-justify-start flex-align-item-start flex-wrap-nowrap']/a[text()='退出']"
    # 首页 - 立即购买立即收益
    home_immediatelyIncome_locator = "//div[@class='carousel']/a[@href = 'https://hash.58coin.com/']"
    # 首页 - 在线客服
    home_onlineService_locator = "//span[text()='在线客服']"



    #获取当前登陆的用户名昵称
    def get_nickname(self):
        return self.find_element(By.XPATH,self.home_userInfoLink_locator,40).text

    #


