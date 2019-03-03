#import subprocess
#import platform
#import re
import json
import core

#Wox内无法运行系统命令
'''
def CheckSeu():
    #osName = platform.system()
    osName = "Windows"

    if osName == "Windows":
        res = subprocess.run(
            "netsh WLAN show interfaces", capture_output=True)
        res = res.stdout.decode('gb2312')
        ifSeu = re.search("seu-wlan", res) or re.search("seu-wlan_5G", res)
        return ifSeu
    elif osName == "Linux":
        #waiting for code
        return False
    else:
        return False
'''
def main():
    #ifSeu = self.CheckSeu()
    #Wox无法获取SSID，但其实如果没连上内网的话也打不开登录页面
    ifSeu = True
    #读取用户名和密码
    try:
        f = open("login.json", encoding='utf-8')
        myJson = json.load(f)
        myUsername = myJson['username']
        myPassword = myJson['b64password']
    except:
        return False
    if ifSeu:
        return core.login(username=myUsername, b64password=myPassword)
    else:
        #for debug
        return False
