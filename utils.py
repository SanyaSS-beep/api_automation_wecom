"""
@Description:
@Time: 2022/7/17 20:45
"""
import json

from requests import Response


def lower_dict_keys(origin_dict):
    if not origin_dict or not isinstance(origin_dict, dict):
        return origin_dict

    return {key.lower: value for key, value in origin_dict.items()}


def omit_long_data(body, omit_len=512):
    """omit too long str/bytes
    """
    if not isinstance(body, (str, bytes)):
        return body

    body_len = len(body)
    if body_len <= omit_len:
        return body

    omitted_body = body[0:omit_len]

    appendix_str = f" ... OMITTED {body_len - omit_len} CHARACTORS ... "
    if isinstance(body, bytes):
        appendix_str = appendix_str.encode("utf-8")

    return omitted_body + appendix_str