def test_case(camera_id, camera_name, description, file_url, algo, algo_version, detect_params, algo_params,
              expected_results):
    # json校验
    case = {
        "id": camera_id,
        "camera_name": camera_name,
        "description": description
    }


import logging

logger = logging.getLogger(__name__)

a='request.method'
b='request.get_full_path()'
logger.error(
    'REST: method=%s,  response=%s' % a,b[:30]
)
