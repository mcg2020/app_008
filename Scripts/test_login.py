from Base.driver import Driver
from Base.page import Page
from Base.getData import GetData
import pytest


def login_data():
    # 空列表
    login_list = []

    data = GetData().get_yml_data("login.yml")
    for i in data.values():
        login_list.append((i.get("name"), i.get("pwd"), i.get("toast"), i.get("exp")))

    return login_list


class TestLogin:

    @pytest.fixture(scope="class", autouse=True)
    def home_click_my_btn(self):
        """首页点击我 -一次"""
        Page.get_home().click_my_btn()

    @pytest.fixture(autouse=True)
    def person_click_login_sign(self):
        """个人中心 点击登录/注册 每次"""
        Page.get_person().click_login_sign_btn()

    @pytest.mark.parametrize("name, pwd, toast, exp", login_data())
    def test_login(self, name, pwd, toast, exp):
        """
        测试方法
        :param name: 账号
        :param pwd: 密码
        :param toast: toast拼接文本
        :param exp: 预期结果
        :return:
        """
        # 登录
        Page.get_login().login(name, pwd)
        # 判断
        if toast:
            """预期失败用例"""
            # 获取toast消息
            message = Page.get_login().get_toast(toast)
            try:
                # 断言toast消息
                assert message == exp
            except AssertionError:  # AssertionError断言失败异常
                # 截图
                Page.get_setting().screen_image()

                # 抛出异常
                raise
            finally:
                # 点击返回按钮
                Page.get_login().login_return_btn()
        else:
            """预期通过数据"""
            # 登录确认按钮
            Page.get_login().login_acc_btn()
            # 获取用户名
            user_name = Page.get_person().get_user_name()
            try:
                # 断言
                assert user_name == exp
            except AssertionError:
                # 截图
                Page.get_setting().screen_image()
                # 抛出异常
                raise
            finally:
                # 点击设置
                Page.get_person().click_setting_btn()
                # 点击退出
                Page.get_setting().logout()

    def teardown_class(self):
        """退出driver"""
        Driver.quit_app_driver()
