import numpy as np
import roboticstoolbox as rtb
from roboticstoolbox.tools.trajectory import jtraj

# 创建机器人对象
robot =  rtb.models.DH.Panda()

# 设置初始关节角度
qz = np.array([0, 0, 0, 0, 0, 0])

# 设置目标关节角度
q_pickup = np.array([30, 45, 60, 0, 0, 0])

# 生成插值轨迹
qt = jtraj(qz, q_pickup, 100)

print(qt.q)  # 打印关节轨迹
robot.plot(qt.q)
