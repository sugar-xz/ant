import json
from flask import request, send_from_directory
from app import app
from run_test import runTest
from config.setting import REPORT_NAME
from testframe.common.base_common import BaseCommon


@app.route('/execute/report', methods=['get'])
def execute_report():
    # request.cookies
    verify = _verify_auth()
    if not verify:
        return {'code': 401, 'message': '请登录'}, 401

    # request.args
    required = ['filepath', 'filename']
    if not all(k in request.args for k in required):
        return {'Params': '`filepath` and `filename` are required.'}, 400

    return send_from_directory(request.args['filepath'], request.args['filename'])


@app.route('/execute/case', methods=['post'])
def execute_case():
    # request.cookies
    verify = _verify_auth()
    if not verify:
        return {'code': 401, 'message': '请登录'}, 401

    def _run_report(cases, dirs):
        report = runTest().run(case=cases, test_dir=dirs)
        report_path = BaseCommon.logPath
        report_name = REPORT_NAME
        res = {
            "execute_count": report.testsRun,
            "success_count": report.success_count,
            "error_count": report.error_count,
            "error_info": _get_errors_info(report.errors),
            "failure_count": report.failure_count,
            "fail_info": _get_errors_info(report.failures),
            # "result": _get_errors_info(report.result),
            "report_path": {"filepath": report_path, "filename": report_name}
        }
        return res

    _params_check = request.form or json.loads(request.data)
    required = ['cases', 'case_dir']
    if not all(k in _params_check for k in required):
        return {'message': 'Mandatory body parameter missing.',
                'detail': 'required fields `mode` and `case_dir`'}, 400
    if request.mimetype in ['application/x-www-form-urlencoded', 'multipart/form-data']:
        test_cases = json.loads(request.form.get('cases'))
        case_dir = request.form.get('case_dir')
    else:
        request_data = json.loads(request.data)
        test_cases = request_data.get('cases')
        case_dir = request_data.get('case_dir')

    if not isinstance(test_cases, list):
        return {'message': 'Mandatory body have incorrect type.',
                'detail': {'cases': 'Must be a list!'}}, 400
    return _run_report(test_cases, case_dir)


def _get_errors_info(infos):
    errors = []
    if len(infos) > 0:
        for i in infos:
            errors.append(str(i))
        return errors
    else:
        return infos


def _verify_auth():
    try:
        verify = request.cookies.get("sugar")
    except (BaseException, KeyError):
        verify = None
    return verify


if __name__ == '__main__':
    pass
