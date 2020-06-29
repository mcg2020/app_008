from Base.base import Base
from Page.pageElements import PageElements
from selenium.common.exceptions import TimeoutException


class HomePage(Base):

    def __init__(self):
        super().__init__()

    def click_my_btn(self):
        """点击我的"""
        try:
            # 点击稍后更新
            self.click_ele(PageElements.home_update_later_xpath)
        except TimeoutException:
            print("当前版本app没有更新提示框")
        # 点击我的
        self.click_ele(PageElements.home_my_btn_id)
