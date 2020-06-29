import yaml, os


class GetData:

    def get_yml_data(self, name):
        """
        读取yaml数据
        :param name: 文件名字
        :return: 返回yaml数据
        """

        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
            # 返回读取数据
            return yaml.safe_load(f)
