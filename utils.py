# coding:utf-8

import re
import os
import sys
import json
import socket
import logging
import getpass
import tempfile
import traceback


# env_config_path = os.environ.get('ENV_CONFIG_PATH') or r'D:/code/git/pipe_config/configuration/env_config'
# if env_config_path not in sys.path:
#     sys.path.insert(0, env_config_path)
# import ff_env
# ff_env.set_environ()


def seqs():
    result = []
    for i in range(100):
        result.append(str(i))
    # return ['010', '020', '030']
    return result


def shots():
    pass


def asset_names():
    pass


def steps():
    pass


def tasks():
    pass


def projs():
    return ['kingkong 金刚', 'avatar 阿凡达']


def get_path():
    pass


