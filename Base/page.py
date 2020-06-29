from Page.homePage import HomePage
from Page.loginPage import LoginPage
from Page.personPage import PersonPage
from Page.settingPage import SettingPage


class Page:

    @classmethod
    def get_home(cls):
        """返回首页对象"""
        return HomePage()

    @classmethod
    def get_login(cls):
        """返回登录页对象"""
        return LoginPage()

    @classmethod
    def get_person(cls):
        """返回个人中心页对象"""
        return PersonPage()

    @classmethod
    def get_setting(cls):
        """返回设置页对象"""
        return SettingPage()
