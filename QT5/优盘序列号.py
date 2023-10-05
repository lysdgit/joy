import psutil
import win32api
from io import StringIO

def run():
    uf = StringIO()
    while True:
        disk_list = []
        for item in psutil.disk_partitions():
            # 判断是不是U盘
            if "removable" in item.opts:
                # 获取U盘的盘符
                disk_list.append(item.mountpoint)
        # 把盘符写入内存，为了不持续请求
        if disk_list != []:
            for pf in disk_list:
                if pf not in uf.getvalue():
                    print("U盘插入")
                    uf.write(disk_list[0])
                    """考虑插多个u盘"""
                    seriaNumber = win32api.GetVolumeInformation(pf)
                    print(f"U盘序列号:{seriaNumber[1]}")

        else:
            # 拔出u盘初始化内存
            uf = StringIO('hello')
            print("U盘拔出")


if __name__ == "__main__":
    run()