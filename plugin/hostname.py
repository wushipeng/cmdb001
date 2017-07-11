import os


def os_hostname():
    """
    获取主机名
    :return:
    """
    name = os.popen("hostname")
    hostname = name.read().strip()
    return hostname
