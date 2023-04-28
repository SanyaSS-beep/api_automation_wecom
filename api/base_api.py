"""
@Description:
@Time: 2022/6/25 21:07
"""
import json
import logging
import os

import requests
import yaml
from requests import Response

from constants import ROOT_PATH
from utils_hep import lower_dict_keys

log = logging.getLogger(__name__)

class BaseApi:
    env = yaml.safe_load(open(os.path.join(ROOT_PATH, r'config/env.yaml')))

    def __init__(self):
        self.url = None
        self.method = None
        self.params = None
        self.headers = None

    def send(self):
        data = {
            "url": self.url,
            "method": self.method,
            "params": self.params,
            "headers": self.headers
        }
        data["url"] = str(data["url"]).replace("env_path", self.env[self.env["default"]])
        r = requests.request(method=data['method'],
                             url=data['url'],
                             headers=data['headers'])
        # print log
        get_req_resp_record(r)
        return r


def get_req_resp_record(resp_obj: Response):
    """ get request and response info from Response() object.
    """

    def log_print(req_or_resp, r_type):
        msg = f"\n================== {r_type} details ==================\n"
        for key, value in req_or_resp.items():
            if isinstance(value, dict) or isinstance(value, list):
                value = json.dumps(value, indent=4, ensure_ascii=False)

            msg += "{:<8} : {}\n".format(key, value)
        log.info(msg)

    request_headers = dict(resp_obj.request.headers)
    request_body = resp_obj.request.body

    if request_body is not None:
        try:
            request_body = json.loads(request_body)
        except json.JSONDecodeError:
            # str: a=1 & b=2
            pass
        except UnicodeDecodeError:
            # bytes/bytesarray: request body in protobuf
            pass
        except TypeError:
            # neither str or bytes/bytearray, eg. <MultipartEncoder>
            pass

    request_content_type = lower_dict_keys(request_headers).get("content-type")
    if request_content_type and "multipart/form-data" in request_content_type:
        request_body = "upload file stream (OMITTED)"

    request_data = {
        "method": resp_obj.request.method,
        "url": resp_obj.request.url,
        "headers": request_headers,
        "body": request_body
    }

    log_print(request_data, "request")

    resp_headers = dict(resp_obj.headers)
    lower_resp_headers = lower_dict_keys(resp_headers)
    content_type = lower_resp_headers.get("content-type", "")

    if "image" in content_type:
        # response is image type, record bytes content only
        response_body = resp_obj.content
    else:
        try:
            response_body = resp_obj.json()
        except ValueError:
            resp_text = resp_obj.text
            response_body = resp_text

    response_data = {
        "status_code": resp_obj.status_code,
        "cookies": resp_obj.cookies or {},
        "encoding": resp_obj.encoding,
        "headers": resp_headers,
        "content_type": content_type,
        "body": response_body
    }

    log_print(response_data, "response")