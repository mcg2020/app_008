import allure


class Test001:

    def test_001(self):
        # 测试报告 添加步骤描述信息 生成附件
        # allure.attach("附件内容", "附件名字", attachment_type=allure.attachment_type.TEXT)

        # allure.attach("图片内容", "图片名字", "图片类型")

        with open(r"./Image\1593438063.png", "rb") as f:
            allure.attach(f.read(), "截图", attachment_type=allure.attachment_type.PNG)
