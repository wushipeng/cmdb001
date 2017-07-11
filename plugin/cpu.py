import os
from config import setting




class Cpuinfo(object):
    cpuinfo_f = setting.BASEDIR + "/files/cpuinfo.out"
    def cpu_model(self):
        """
        获取cpu的名字
        :return:
        """
        f = open(self.cpuinfo_f,'r',encoding="utf-8")

        with open(self.cpuinfo_f,'r',encoding="utf-8") as f:
            for line in f:
                line_list = line.split(":")
                # print(line_list)
                if line_list[0].strip() == "model name":
                    # print(line_list[1])
                    return line_list[1].strip()




# d = Cpuinfo()
# print(d.cpu_model())

