# -*- coding: utf-8 -*-
from wox import Wox
#from login import Login
import login
import core

class Main(Wox):
    def query(self, query):
        results = []
        res = login.main()
        if res:
            results.append({
            "Title": res[1],
            "SubTitle": res[2],
            "IcoPath":"Images/app.ico",
            })
        else:
            results.append({
            "Title": "登录失败",
            "SubTitle": "请检查网络连接",
            "IcoPath":"Images/app.ico",
            })
        return results

if __name__ == "__main__":
    Main()