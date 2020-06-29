# [(name, pwd, toast, exp)]
import yaml

# 空列表
login_list = []

with open("./login.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    for i in data.values():
        login_list.append((i.get("name"), i.get("pwd"), i.get("toast"), i.get("exp")))

    print(login_list)
"""
{'login_001': {'name': '15537398867', 'pwd': 'mcg1007895', 'exp':旧时代的残党'}, 
'login_002': {'name': ' 15537398867', 'pwd': 'mcg1007895', 'exp': 'LZL911'}, 
'login_003': {'name': '15537398867 ', 'pwd': 'mcg1007895', 'exp': 'LZL911'}, 
'login_005': {'name': '13488834010', 'pwd': 'mcg10078', 'toast': '错误', 'exp': '账号或密码错误'}, 
'login_007': {'name': '13877771111', 'pwd': 'mcg100789', 'toast': '请您', 'exp': '账号还未注册，请您先进行注册'}}

"""
