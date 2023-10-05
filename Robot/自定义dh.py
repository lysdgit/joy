import roboticstoolbox as rtb
from math import pi
import numpy as np

L1=0.40
L2=0.39
L3=0.37
L4=0.08 # 末端执行器

leg = rtb.DHRobot(
    [
        rtb.RevoluteMDH(alpha=0,    a=0,    offset=0,   d=L1),
        rtb.RevoluteMDH(alpha=pi/2, a=0,    offset=pi/2,d=0 ),
        rtb.RevoluteMDH(alpha=0,    a=L2,   offset=0,   d=0 ),
        rtb.RevoluteMDH(alpha=pi/2, a=0,    offset=0,   d=0 ),
        rtb.RevoluteMDH(alpha=0,    a=0,    offset=0,   d=L3),
        rtb.RevoluteMDH(alpha=pi/2, a=0,    offset=0,   d=0 )
    ],name="six link")

init_T = np.array([90,0,0,0,0,0])
leg.plot(init_T, movie='six link.png')

input()

print(leg)
