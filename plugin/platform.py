from config.setting import BASEDIR


def os_platform():
    """
    获取系统版本
    :return:
    """
    with open(BASEDIR+"/files/platform.out",'r',encoding="utf-8") as f:
        plat = f.readlines()[0].strip()

    return plat



