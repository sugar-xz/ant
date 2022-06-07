import requests
from testframe.interface.interface_base import InterfaceBase


# login
def login():
    """
    login
    :return: token/cookie
    """
    # url = ConfigUtil.get_ini("urls", "login_url")
    # json = ConfigUtil.get_ini_dict("urls", "login_data")
    data = {
        'method': 'post',
        'url': 'https://dev-api.turingvideo.cn/api/v1/user/auth/login',
        'body': {"username": "dev@turingvideo.net", "password": "$Turin9Vide0"}
    }
    res = InterfaceBase().request(data)

    res_cookies = requests.utils.dict_from_cookiejar(res.cookies)
    cookies = get_cookie(res_cookies)
    cookie = {'Cookie': cookies}
    print("Add cookie: %s" % cookie)
    return cookie


def get_cookie(cookies):
    cookie = ''
    if len(cookies) > 0:
        cookie = []
        for k, v in cookies.items():
            cookie.append('%s=%s' % (k, v))
        cookie = ';'.join(cookie)
    return cookie


# # logout
# def logout(token):
#     """
#     logout
#     :param token: login token
#     :return:
#     """

login()
