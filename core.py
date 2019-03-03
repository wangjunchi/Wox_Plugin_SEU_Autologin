import requests
import base64
import time
import json


def login(username: str, b64password: str,
          macauth=False) -> bool:
    sess = requests.session()
    sess.verify = False

    '''
    request异常捕获
    '''
    try:
        res = sess.get('https://w.seu.edu.cn/index.php/index/init?_={}'.format(
        time.time_ns() // 1000),timeout=1)
        resjson = json.loads(res.text)
    except:
        return False
        

    # print(resjson['info'])
    if resjson['status'] == 1:
        return True, resjson['info'], resjson['logout_ip']
    if type(username) != str:
        raise Exception()
    if type(b64password) != str:
        raise Exception()
    form = {
        'username': username,
        'password': b64password,
        'enablemacauth': (1 if macauth else 0)
    }
    '''
    request异常捕获
    '''
    try:
        res = sess.post('https://w.seu.edu.cn/index.php/index/login', data=form,timeout=1)
        resjson = json.loads(res.text)
    except:
        return False 
        
    # print(resjson['info'])
    if resjson['status'] == 1:
        return True, resjson['info'], resjson['logout_ip']
    return False, resjson['info']

