import math

def gps_repeatability(n, coords):
    """
    计算GPS重复定位精度

    参数:
    n: 重复定位次数
    coords: 一个包含n个坐标元组的列表，每个坐标元组包含三个分量，分别代表x、y、z坐标

    返回值:
    GPS重复定位精度，单位为米
    """
    # 计算每个坐标分量的平均值
    X = sum(coord[0] for coord in coords) / n
    Y = sum(coord[1] for coord in coords) / n
    Z = sum(coord[2] for coord in coords) / n

    # 计算每个坐标分量的方差
    var_x = sum((coord[0] - X) ** 2 for coord in coords) / (n - 1)
    var_y = sum((coord[1] - Y) ** 2 for coord in coords) / (n - 1)
    var_z = sum((coord[2] - Z) ** 2 for coord in coords) / (n - 1)

    # 计算三个方差的平均值
    var_avg = (var_x + var_y + var_z) / 3

    # 计算GPS重复定位精度
    return math.sqrt(var_avg)

# 示例用法
coords = [(65.4,69.619,68.11),(65.43,69.619,68.189), (65.42,69.61,68.189),(65.41,69.619,68.2),(65.34,69.619,68.18),(65.35,69.619,68.189),(65.4,69.49,68.189), (65.269,69.6,68.18), (65.38,69.619,68.18), (65.41,69.619,68.2)]
n = len(coords)
repeatability = gps_repeatability(n, coords)
print("GPS重复定位精度为：", repeatability, "米")
