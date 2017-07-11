# from config.setting import BASEDIR
# from plugin.hostname import os_hostname
#
#
# def os_ip():
#     """

#     :return:
#     """
#     # print(os_hostname().strip())
#     with open(BASEDIR+'/files/hosts.out','r',encoding="utf-8") as f:
#         for line in f:
#             if os_hostname().strip() in line:
#                 return line.split()[0]
#
#
#

import socket


def os_ip():
    """
    获取serverIP地址
    :return:
    """
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip
