import os
import sys
import requests
from plugin import cpu, hostname, ip, memory, platform
from config import setting


BASEDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASEDIR)

# 获取cpu信息
# os.system("cat /proc/cpuinfo>/XX/XX/files/cpuinfo.out")

# 获取内存信息
# os.system("cat /proc/meminfo | grep MemT" >> /xx/xx/cpuinfo.out)

# 获取平台信息
# os.system("cat /etc/issue >> /xx/xx/platform.out")


sys_info = {"cpu_mode": cpu.Cpuinfo().cpu_model(),
            "hostname": hostname.os_hostname(),
            "ip": ip.os_ip(),
            "memory": memory.os_mem(),
            "platform": platform.os_platform()
            }


def postinfo():
    """
    提交信息到API
    :return:
    """

    sesstion = requests.Session()
    rep = sesstion.get(setting.API_URL)
    csrf = rep.cookies["csrftoken"]
    cookie = {"csrftoken": csrf}
    header_csrf = {"X-CSRFToken": csrf}
    requests.post(setting.API_URL, headers=header_csrf, cookies=cookie, json=sys_info)


if __name__ == "__main__":
    postinfo()
