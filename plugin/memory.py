from config.setting import BASEDIR
def os_mem():
    """
    系统总内存
    :return:
    """
    with open(BASEDIR+"/files/meminfo.out","r",encoding="utf-8") as f:
        for line in f:
            mem = round(int(line.split()[1])/1024/1024)
    return str(mem)+"G"



