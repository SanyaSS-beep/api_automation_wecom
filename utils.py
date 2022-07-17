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



