from appium import webdriver


class Driver:
    # app驱动对象
    app_driver = None

    @classmethod
    def get_app_driver(cls):
        """声明app driver"""
        # app_driver为空时
        if not cls.app_driver:
            # server 启动参数
            desired_caps = {
                'platformName': "Android",
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.bjcsxq.chat.carfriend',
                'appActivity': '.module_main.activity.MainActivity'
            }

            # 声明我们的driver对象
            cls.app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            return cls.app_driver
        # app_driver不为空
        else:
            return cls.app_driver

    @classmethod
    def quit_app_driver(cls):
        """退出app driver"""
        # 判断app driver有值
        if cls.app_driver:
            # 退出
            cls.app_driver.quit()
            # 重新置为None
            cls.app_driver = None
