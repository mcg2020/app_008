from Base.base import Base
from Page.pageElements import PageElements


class LoginPage(Base):

    def __init__(self):
        super().__init__()

    def login(self, name, pwd):
        """
        登录操作
        :param name: 账号
        :param pwd: 密码
        :return:
        """
        # 账号
        self.send_ele(PageElements.login_account_id, name)
        # 密码
        self.send_ele(PageElements.login_pwd_id, pwd)
        # 登录按钮
        self.click_ele(PageElements.login_btn_id)

    def login_acc_btn(self):
        """登录成功确认按钮"""
        self.click_ele(PageElements.login_acc_btn_id)

    def login_return_btn(self):
        """登录失败返回按钮"""
        self.click_ele(PageElements.login_return_btn_id)
