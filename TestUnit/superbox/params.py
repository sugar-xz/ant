CREATE_CAMERA = {
    "name": 'test_camera',
    "uri": "rtsp://admin:TuringVideo@192.168.2.64:554/h264/ch1/sub/av_stream",
    "mode": "off",
    "detect_params": {"threshold": 0.5},
    "default_params": {},
    "rules": [{"name": "人群聚集", "mode": "off", "algo": "person:512"}],
    "should_push": 'false',
    "config_params": {},
    "sampling": 'false'
}
CREATE_EVENT = {
    "camera_id": 1,
    "started_at": "2020-09-04T03:58:05.718661Z",
    "ended_at": "2020-09-04T03:58:06.718661Z",
    "mediums": [],
    "types": "person",
    "status": "pending",
    "should_push": 'false'
}
PATCH_EVENT = {
    "types": "person",
    "status": "pending",
    "should_push": 'false'
}
CREATE_RULE = {
    "camera": 1,
    "name": "人群疏散",
    "mode": "off",
    "algo": "person:513",
    "params": {},
    "params_base": "",
    "event_types": {
        "person:513": "人群疏散"
    },
    "schedule": {}
}
CREATE_SAMPLE = {
    "id": "674cc883-ea19-4feb-83e4-f4705a23545a",
    "started_at": "2020-09-07T09:08:48.252575Z",
    "ended_at": "2020-09-07T09:08:49.252575Z",
    "notified_cloud": 'false',
    "expired": 1,
    "file_count": 1,
    "types": "person:512",
    "types_at": "2020-09-07T09:18:49.252575Z",
    "notified_guardian": 'false',
    "event_at": "2020-09-07T09:08:48.252575Z",
    "camera_id": 1
}
SAMPLE_UPLOAD_FILE = {
  "content_type": "image/jpeg",
  "s3_data": {},
  "uploaded_at": "2020-09-07T09:09:49.252575Z",
  "file_deleted": 'false',
  "sample": "674cc883-ea19-4feb-83e4-f4705a23544a"
}
CREATE_SETTING = {
    "value": "test12",
    "name": "test12"
}
CREATE_WEBHOOK = {
    "types": "camera_health",
    "url": "https://www.baidu.com"
}