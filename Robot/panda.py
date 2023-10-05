# import roboticstoolbox as rtb
# from spatialmath import SE3

# # robot = rtb.models.DH.Panda()
# robot = rtb.models.DH.moka()
# print(robot)

# T = SE3(1, 0, 0) * SE3.OA([0, 1, 0], [0, 0, -1])
# sol = robot.ikine_LM(T)         # solve IK
# print(sol)
 
# q_pickup = sol.q
# print(robot.fkine(q_pickup))    # FK shows that desired end-effector pose was achieved

# # qt = rtb.jtraj(robot.qz, q_pickup, 100)
# # robot.plot(qt.q, movie='panda1.gif')
# # robot.plot(qt.q)
import roboticstoolbox as rtb
from spatialmath import SE3
import math

# 创建机器人模型
robot = rtb.models.DH.moka()
print(robot)

qz_deg = [0, 90, 0, 0, 0, 0]#zero零位
qz_rad = [math.radians(angle) for angle in qz_deg]#zero零位角度转弧度

# q_deg = [-93, 80, 0, 90, 0, 0]
q_deg = [13.1969 , -61.9686, 4.5775, 18.5776, 62.0886, 37.7717]

q_rad = [math.radians(angle) for angle in q_deg]#角度转弧度
print("角度转弧度")
print(q_rad)

# 正解
fk = robot.fkine(q_rad)
print(f"正解输出末端的姿态矩阵The forward kienmatics is:\n {fk}")

# 生成插值轨迹
qt = rtb.jtraj(qz_rad, q_rad, 100); #从qz_rad到q_rad
robot.plot(qt.q, movie='panda1.gif')

ik = robot.ikine_NR(fk)
print("逆解算出弧度")
print(ik)
print("------------------------")
# # # 定义目标位姿矩阵
print("打印目标矩阵")
T = SE3(708.0277, 210.1518, 1782.5341) * SE3.OA([1, 1, 1], [-2.3017, 0.8869, -1.6083])
print(T)
# # 使用逆运动学求解
sol = robot.ikine_LM(T)

# # 打印逆运动学解
print(sol)
