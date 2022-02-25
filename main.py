"""
主程序脚本
"""
# -*- coding: utf8 -*-
# python >=3.8

import json
import random
import re
import json
import sys
import time
from urllib.parse import quote

import requests

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
headers = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; MI 6 MIUI/20.6.18)'
}


def get_code(location):
    """
    获取登录code
    """
    code_pattern = re.compile("(?<=access=).*?(?=&)")
    code = code_pattern.findall(location)[0]
    return code


def login(_user, password):
    """
    登录
    """
    url1 = "https://api-user.huami.com/registrations/+86" + _user + "/tokens"
    _headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "User-Agent": "MiFit/4.6.0 (iPhone; iOS 14.0.1; Scale/2.00)"
    }
    data1 = {
        "client_id": "HuaMi",
        "password": f"{password}",
        "redirect_uri": "https://s3-us-west-2.amazonaws.com/hm-registration/successsignin.html",
        "token": "access"
    }
    r1 = requests.post(url1, data=data1, headers=_headers, allow_redirects=False)
    try:
        location = r1.headers["Location"]
        code = get_code(location)
    except:
        return 0, 0
    # print("access_code获取成功！")
    # print(code)

    url2 = "https://account.huami.com/v2/client/login"
    data2 = {
        "app_name": "com.xiaomi.hm.health",
        "app_version": "4.6.0",
        "code": f"{code}",
        "country_code": "CN",
        "device_id": "2C8B4939-0CCD-4E94-8CBA-CB8EA6E613A1",
        "device_model": "phone",
        "grant_type": "access_token",
        "third_name": "huami_phone",
    }
    r2 = requests.post(url2, data=data2, headers=_headers).json()
    login_token = r2["token_info"]["login_token"]
    # print("login_token获取成功！")
    # print(login_token)
    userid = r2["token_info"]["user_id"]
    # print("userid获取成功！")
    # print(userid)

    return login_token, userid


def main(_user, _passwd, _step):
    """
    主函数
    """
    _user = str(_user)
    password = str(_passwd)
    _step = str(_step)
    if _user == '' or password == '':
        print("用户名或密码不能为空！")
        return "user and passwd not empty！"

    if _step == '':
        print("已设置为随机步数（10000-19999）")
        _step = str(random.randint(10000, 19999))
    login_token, userid = login(_user, password)
    if login_token == 0:
        print("登陆失败！")
        return "login fail!"

    t = get_time()

    app_token = get_app_token(login_token)

    today = time.strftime("%F")

    summary = {
        "v": 6,
        "slp": {
            "st": int(time.time()),
            "ed": int(time.time()),
            "dp": 0,
            "lt": 0,
            "wk": 0,
            "usrSt": -1440,
            "usrEd": -1440,
            "wc": 0,
            "is": 0,
            "lb": 0,
            "to": 0,
            "dt": 0,
            "rhr": 0,
            "ss": 0
        },
        "stp": {
            "ttl": _step,
            "dis": 10627,
            "cal": 510,
            "wk": 41,
            "rn": 50,
            "runDist": 7654,
            "runCal": 397,
            "stage": [
                {
                    "start": 327,
                    "stop": 341,
                    "mode": 1,
                    "dis": 481,
                    "cal": 13,
                    "step": 680
                },
                {
                    "start": 342,
                    "stop": 367,
                    "mode": 3,
                    "dis": 2295,
                    "cal": 95,
                    "step": 2874
                },
                {
                    "start": 368,
                    "stop": 377,
                    "mode": 4,
                    "dis": 1592,
                    "cal": 88,
                    "step": 1664
                },
                {
                    "start": 378,
                    "stop": 386,
                    "mode": 3,
                    "dis": 1072,
                    "cal": 51,
                    "step": 1245
                },
                {
                    "start": 387,
                    "stop": 393,
                    "mode": 4,
                    "dis": 1036,
                    "cal": 57,
                    "step": 1124
                },
                {
                    "start": 394,
                    "stop": 398,
                    "mode": 3,
                    "dis": 488,
                    "cal": 19,
                    "step": 607
                },
                {
                    "start": 399,
                    "stop": 414,
                    "mode": 4,
                    "dis": 2220,
                    "cal": 120,
                    "step": 2371
                },
                {
                    "start": 415,
                    "stop": 427,
                    "mode": 3,
                    "dis": 1268,
                    "cal": 59,
                    "step": 1489
                },
                {
                    "start": 428,
                    "stop": 433,
                    "mode": 1,
                    "dis": 152,
                    "cal": 4,
                    "step": 238
                },
                {
                    "start": 434,
                    "stop": 444,
                    "mode": 3,
                    "dis": 2295,
                    "cal": 95,
                    "step": 2874
                },
                {
                    "start": 445,
                    "stop": 455,
                    "mode": 4,
                    "dis": 1592,
                    "cal": 88,
                    "step": 1664
                },
                {
                    "start": 456,
                    "stop": 466,
                    "mode": 3,
                    "dis": 1072,
                    "cal": 51,
                    "step": 1245
                },
                {
                    "start": 467,
                    "stop": 477,
                    "mode": 4,
                    "dis": 1036,
                    "cal": 57,
                    "step": 1124
                },
                {
                    "start": 478,
                    "stop": 488,
                    "mode": 3,
                    "dis": 488,
                    "cal": 19,
                    "step": 607
                },
                {
                    "start": 489,
                    "stop": 499,
                    "mode": 4,
                    "dis": 2220,
                    "cal": 120,
                    "step": 2371
                },
                {
                    "start": 500,
                    "stop": 511,
                    "mode": 3,
                    "dis": 1268,
                    "cal": 59,
                    "step": 1489
                },
                {
                    "start": 512,
                    "stop": 522,
                    "mode": 1,
                    "dis": 152,
                    "cal": 4,
                    "step": 238
                }
            ]
        },
        "goal": 8000,
        "tz": "28800"
    }

    data_json = [
        {
            "data_hr": "//////9L////////////Vv///////////0v///////////9e/////0n/a///S////////////0b//////////1FK////////////R/////////////////9PTFFpaf9L////////////R////////////0j///////////9K////////////Ov///////////zf///86/zr/Ov88/zf/Pf///0v/S/8/////////////Sf///////////z3//////0r/Ov//////S/9L/zb/Sf9K/0v/Rf9H/zj/Sf9K/0//N////0D/Sf83/zr/Pf9M/0v/Ov9e////////////S////////////zv//z7/O/83/zv/N/83/zr/N/86/z//Nv83/zn/Xv84/zr/PP84/zj/N/9e/zr/N/89/03/P/89/z3/Q/9N/0v/Tv9C/0H/Of9D/zz/Of88/z//PP9A/zr/N/86/zz/Nv87/0D/Ov84/0v/O/84/zf/MP83/zH/Nv83/zf/N/84/zf/Of82/zf/OP83/zb/Mv81/zX/R/9L/0v/O/9I/0T/S/9A/zn/Pf89/zn/Nf9K/07/N/83/zn/Nv83/zv/O/9A/0H/Of8//zj/PP83/zj/S/87/zj/Nv84/zf/Of83/zf/Of83/zb/Nv9L/zj/Nv82/zb/N/85/zf/N/9J/zf/Nv83/zj/Nv84/0r/Sv83/zf/MP///zb/Mv82/zb/Of85/z7/Nv8//0r/S/85/0H/QP9B/0D/Nf89/zj/Ov83/zv/Nv8//0f/Sv9O/0ZeXv///////////1X///////////9B////////////TP///1b//////0////////////9N/////////v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+",
            "date": today,
            "data": [
                {
                    "start": 0,
                    "stop": 1439,
                    "value": "UA8AUBQAUAwAUBoAUAEAYCcAUBkAUB4AUBgAUCAAUAEAUBkAUAwAYAsAYB8AYB0AYBgAYCoAYBgAYB4AUCcAUBsAUB8AUBwAUBIAYBkAYB8AUBoAUBMAUCEAUCIAYBYAUBwAUCAAUBgAUCAAUBcAYBsAYCUAATIPYD0KECQAYDMAYB0AYAsAYCAAYDwAYCIAYB0AYBcAYCQAYB0AYBAAYCMAYAoAYCIAYCEAYCYAYBsAYBUAYAYAYCIAYCMAUB0AUCAAUBYAUCoAUBEAUC8AUB0AUBYAUDMAUDoAUBkAUC0AUBQAUBwAUA0AUBsAUAoAUCEAUBYAUAwAUB4AUAwAUCcAUCYAUCwKYDUAAUUlEC8IYEMAYEgAYDoAYBAAUAMAUBkAWgAAWgAAWgAAWgAAWgAAUAgAWgAAUBAAUAQAUA4AUA8AUAkAUAIAUAYAUAcAUAIAWgAAUAQAUAkAUAEAUBkAUCUAWgAAUAYAUBEAWgAAUBYAWgAAUAYAWgAAWgAAWgAAWgAAUBcAUAcAWgAAUBUAUAoAUAIAWgAAUAQAUAYAUCgAWgAAUAgAWgAAWgAAUAwAWwAAXCMAUBQAWwAAUAIAWgAAWgAAWgAAWgAAWgAAWgAAWgAAWgAAWREAWQIAUAMAWSEAUDoAUDIAUB8AUCEAUC4AXB4AUA4AWgAAUBIAUA8AUBAAUCUAUCIAUAMAUAEAUAsAUAMAUCwAUBYAWgAAWgAAWgAAWgAAWgAAWgAAUAYAWgAAWgAAWgAAUAYAWwAAWgAAUAYAXAQAUAMAUBsAUBcAUCAAWwAAWgAAWgAAWgAAWgAAUBgAUB4AWgAAUAcAUAwAWQIAWQkAUAEAUAIAWgAAUAoAWgAAUAYAUB0AWgAAWgAAUAkAWgAAWSwAUBIAWgAAUC4AWSYAWgAAUAYAUAoAUAkAUAIAUAcAWgAAUAEAUBEAUBgAUBcAWRYAUA0AWSgAUB4AUDQAUBoAXA4AUA8AUBwAUA8AUA4AUA4AWgAAUAIAUCMAWgAAUCwAUBgAUAYAUAAAUAAAUAAAUAAAUAAAUAAAUAAAUAAAUAAAWwAAUAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAeSEAeQ8AcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcBcAcAAAcAAAcCYOcBUAUAAAUAAAUAAAUAAAUAUAUAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcCgAeQAAcAAAcAAAcAAAcAAAcAAAcAYAcAAAcBgAeQAAcAAAcAAAegAAegAAcAAAcAcAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcCkAeQAAcAcAcAAAcAAAcAwAcAAAcAAAcAIAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcCIAeQAAcAAAcAAAcAAAcAAAcAAAeRwAeQAAWgAAUAAAUAAAUAAAUAAAUAAAcAAAcAAAcBoAeScAeQAAegAAcBkAeQAAUAAAUAAAUAAAUAAAUAAAUAAAcAAAcAAAcAAAcAAAcAAAcAAAegAAegAAcAAAcAAAcBgAeQAAcAAAcAAAcAAAcAAAcAAAcAkAegAAegAAcAcAcAAAcAcAcAAAcAAAcAAAcAAAcA8AeQAAcAAAcAAAeRQAcAwAUAAAUAAAUAAAUAAAUAAAUAAAcAAAcBEAcA0AcAAAWQsAUAAAUAAAUAAAUAAAUAAAcAAAcAoAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAYAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcBYAegAAcAAAcAAAegAAcAcAcAAAcAAAcAAAcAAAcAAAeRkAegAAegAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAEAcAAAcAAAcAAAcAUAcAQAcAAAcBIAeQAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcBsAcAAAcAAAcBcAeQAAUAAAUAAAUAAAUAAAUAAAUBQAcBYAUAAAUAAAUAoAWRYAWTQAWQAAUAAAUAAAUAAAcAAAcAAAcAAAcAAAcAAAcAMAcAAAcAQAcAAAcAAAcAAAcDMAeSIAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcBQAeQwAcAAAcAAAcAAAcAMAcAAAeSoAcA8AcDMAcAYAeQoAcAwAcFQAcEMAeVIAaTYAbBcNYAsAYBIAYAIAYAIAYBUAYCwAYBMAYDYAYCkAYDcAUCoAUCcAUAUAUBAAWgAAYBoAYBcAYCgAUAMAUAYAUBYAUA4AUBgAUAgAUAgAUAsAUAsAUA4AUAMAUAYAUAQAUBIAASsSUDAAUDAAUBAAYAYAUBAAUAUAUCAAUBoAUCAAUBAAUAoAYAIAUAQAUAgAUCcAUAsAUCIAUCUAUAoAUA4AUB8AUBkAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAA",
                    "tz": 32,
                    "did": "DA932FFFFE8816E7",
                    "src": 24
                }
            ],
            "summary": json.dumps(summary),
            "source": 24,
            "type": 0
        }
    ]

    url = f'https://api-mifit-cn.huami.com/v1/data/band_data.json?&t={t}'
    head = {
        "apptoken": app_token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = f'userid={userid}&last_sync_data_time=1597306380&device_type=0&last_deviceid=DA932FFFFE8816E7&data_json={quote(json.dumps(data_json))}'
    print(data)
    response = requests.post(url, data=data, headers=head).json()
    print(response)
    result = f"{_user[:4]}****{_user[-4:]}: [{now}] 修改步数（{_step}）" + response['message']
    print(result)
    return result


def get_time():
    """
    获取时间戳
    """
    url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
    response = requests.get(url, headers=headers).json()
    t = response['data']['t']
    return t


def get_app_token(login_token):
    """
    获取app_token
    """
    url = f"https://account-cn.huami.com/v1/client/app_tokens" \
          f"?app_name=com.xiaomi.hm.health&dn=api-user.huami.com%2Capi-mifit.huami.com%2Capp-analytics.huami.com" \
          f"&login_token={login_token}"
    response = requests.get(url, headers=headers).json()
    app_token = response['token_info']['app_token']
    # print("app_token获取成功！")
    # print(app_token)
    return app_token


def push_wx(_sckey, desp=""):
    """
    推送server酱
    """
    if _sckey == '':
        print("[注意] 未提供sckey，不进行推送！")
    else:
        server_url = f"https://sc.ftqq.com/{_sckey}.send"
        params = {
            "text": '小米运动 步数修改',
            "desp": desp
        }

        response = requests.get(server_url, params=params)
        json_data = response.json()

        if json_data['errno'] == 0:
            print(f"[{now}] 推送成功。")
        else:
            print(f"[{now}] 推送失败：{json_data['errno']}({json_data['errmsg']})")


def push_server(_sckey, desp=""):
    """
    推送消息到微信
    """
    if _sckey == '':
        print("[注意] 未提供sckey，不进行微信推送！")
    else:
        server_url = f"https://sctapi.ftqq.com/{_sckey}.send"
        params = {
            "title": '小米运动 步数修改',
            "desp": desp
        }

        response = requests.get(server_url, params=params)
        json_data = response.json()

        if json_data['code'] == 0:
            print(f"[{now}] 推送成功。")
        else:
            print(f"[{now}] 推送失败：{json_data['code']}({json_data['message']})")


def push_pushplus(token, content=""):
    """
    推送消息到pushplus
    """
    if token == '':
        print("[注意] 未提供token，不进行pushplus推送！")
    else:
        server_url = "http://www.pushplus.plus/send"
        params = {
            "token": token,
            "title": '小米运动 步数修改',
            "content": content
        }

        response = requests.get(server_url, params=params)
        json_data = response.json()

        if json_data['code'] == 200:
            print(f"[{now}] 推送成功。")
        else:
            print(f"[{now}] 推送失败：{json_data['code']}({json_data['message']})")


def push_tg(token, chat_id, desp=""):
    """
    推送消息到TG
    """
    if token == '':
        print("[注意] 未提供token，不进行tg推送！")
    elif chat_id == '':
        print("[注意] 未提供chat_id，不进行tg推送！")
    else:
        server_url = f"https://api.telegram.org/bot{token}/sendmessage"
        params = {
            "text": '小米运动 步数修改\n\n' + desp,
            "chat_id": chat_id
        }

        response = requests.get(server_url, params=params)
        json_data = response.json()

        if json_data['ok']:
            print(f"[{now}] 推送成功。")
        else:
            print(f"[{now}] 推送失败：{json_data['error_code']}({json_data['description']})")


def wxpush(msg, usr, corpid, corpsecret, agentid=1000002):
    """
    企业微信推送
    """
    base_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
    req_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
    corpid = corpid
    corpsecret = corpsecret
    agentid = agentid

    if agentid == 0:
        agentid = 1000002

    def get_access_token(_base_url, _corpid, _corpsecret):
        """
        获取access_token，每次的access_token都不一样，所以需要运行一次请求一次
        """
        urls = _base_url + 'corpid=' + _corpid + '&corpsecret=' + _corpsecret
        resp = requests.get(urls).json()
        access_token = resp['access_token']
        return access_token

    def send_message(_msg, _usr):
        """
        发送消息
        """
        data = get_message(_msg, _usr)
        req_urls = req_url + get_access_token(base_url, corpid, corpsecret)
        res = requests.post(url=req_urls, data=data)
        ret = res.json()
        if ret["errcode"] == 0:
            print(f"[{now}] 企业微信推送成功")
        else:
            print(f"[{now}] 推送失败：{ret['errcode']} 错误信息：{ret['errmsg']}")

    def get_message(_msg, _usr):
        """
        获取消息
        """
        data = {
            "touser": _usr,
            "toparty": "@all",
            "totag": "@all",
            "msgtype": "text",
            "agentid": agentid,
            "text": {
                "content": _msg
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        data = json.dumps(data)
        return data

    msg = msg
    usr = usr
    if corpid == '':
        print("[注意] 未提供corpid，不进行企业微信推送！")
    elif corpsecret == '':
        print("[注意] 未提供corpsecret，不进行企业微信推送！")
    else:
        send_message(msg, usr)


class ToPush:
    """
    推送接口类
    处理pkey并转发推送消息到推送函数
    """
    push_msg: str

    def __init__(self, _pkey):
        self.pkey = _pkey

    def to_push_wx(self):
        """
        推送server酱接口
        """
        if str(self.pkey) == '0':
            self.pkey = ''
        push_wx(self.pkey, self.push_msg)

    def to_push_server(self):
        """
        推送消息到微信接口
        """
        if str(self.pkey) == '0':
            self.pkey = ''
        push_server(self.pkey, self.push_msg)

    def to_push_tg(self):
        """
        推送消息到TG接口
        """
        try:
            token, chat_id = self.pkey.split('@')
            push_tg(token, chat_id, self.push_msg)
        except ValueError:
            print('tg推送参数有误！')

    def to_wxpush(self):
        """
        企业微信推送接口
        """
        try:
            usr, corpid, corpsecret, *agentid = self.pkey.split('-')
            if agentid:
                wxpush(self.push_msg, usr, corpid, corpsecret, int(agentid[0]))
            else:
                wxpush(self.push_msg, usr, corpid, corpsecret)
        except ValueError:
            print('企业微信推送参数有误！')

    def to_push_pushplus(self):
        """
        接口
        """
        if self.pkey == '':
            print('pushplus token错误')
        else:
            push_pushplus(self.pkey, self.push_msg)

    @staticmethod
    def no_push():
        """
        不推送
        """
        print('不推送')


if __name__ == "__main__":
    # Push Mode
    # print(sys.argv)
    try:
        Pm = sys.argv[1]
        pkey = sys.argv[2]

        to_push = ToPush(pkey)

        # 用户名（格式为 13800138000）
        user = sys.argv[3]
        # 登录密码
        passwd = sys.argv[4]
        # 要修改的步数，直接输入想要修改的步数值，0为随机步数
        step = sys.argv[5].replace('[', '').replace(']', '')
    except IndexError as e:
        print("参数有误: " + str(e))
        exit(1)

    user_list = user.split('#')
    passwd_list = passwd.split('#')
    setp_array = step.split('-')

    if len(user_list) == len(passwd_list):
        to_push.push_msg = ''
        for user, passwd in zip(user_list, passwd_list):
            if len(setp_array) == 2:
                step = str(random.randint(int(setp_array[0]), int(setp_array[1])))
                print(f"已设置为随机步数（{setp_array[0]}-{setp_array[1]}）")
            elif str(step) == '0':
                step = ''
            to_push.push_msg += main(user, passwd, step) + '\n'

        push = {
            'wx': to_push.to_push_wx,
            'nwx': to_push.to_push_server,
            'tg': to_push.to_push_tg,
            'qwx': to_push.to_wxpush,
            'pp': to_push.to_push_pushplus,
            'off': to_push.no_push
        }
        try:
            push[Pm]()
        except KeyError:
            print('推送选项有误！')
            exit(0)
    else:
        print('用户名和密码数量不对')
