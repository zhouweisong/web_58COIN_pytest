"""
-------------------------------------------------
   File Name：     conftest
   Description :
   Author :       zws
   date：          2018/4/6
-------------------------------------------------
   Change Activity:
                   2018/4/6:
-------------------------------------------------
"""
__author__ = 'zws'
import pytest
from selenium import webdriver


@pytest.fixture
def init_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()
    driver.quit()