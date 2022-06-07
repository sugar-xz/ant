# -*- coding: utf-8 -*-
import json
from flask import Flask, request, make_response
from passlib.apps import custom_app_context as pwd_context
import sys

sys.path.append('..')

app = Flask(__name__)

HASH_PASSWORD = '$6$rounds=656000$Msc/bxpMT4Hrxkar$QLKe9Ls/QHI4BHKuoihInjsDohJs1IHe' \
                '/w7Miwk1p2CJ1dtAmsjaGqi9MFEqGquP789Ae4v/MbFsmoppqYVf/0'


def _hash_password(password):
    return pwd_context.encrypt(password)


def _verify_password(password, password_hash):
    return pwd_context.verify(password, password_hash)


@app.route('/login', methods=['POST'])
def login():
    request_data = json.loads(request.data)

    username = request_data.get('username')
    password = request_data.get('password')
    if username is None or password is None:
        return {'code': 401, 'message': '登录失败'}, 401
    aa = _verify_password(password, HASH_PASSWORD)
    if aa:
        res = make_response({'code': 200, 'message': '登录成功'})
        res.set_cookie("sugar", HASH_PASSWORD, max_age=36000)
        return res
    else:
        return {'code': 400, 'message': '登录失败'}


@app.route('/logout', methods=['POST'])
def logout():
    res = make_response({'code': 200, 'message': '登出成功'})
    res.delete_cookie("sugar")
    return res


from app import execute
