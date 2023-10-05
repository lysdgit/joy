import open3d as o3d
import numpy as np

# 从CSV文件中读取点云数据
data = np.genfromtxt('C:/Users/liys2/Desktop/11.csv', delimiter=',')

# 提取XYZ坐标
X = data[:, 0]
Y = data[:, 1]
Z = data[:, 2]

vis = o3d.visualization.Visualizer()
vis.create_window()

points = []
colors = []    
for i in range(5000):
    # 获取数据至 x,y,z r,g,b ,其中rgb范围为0-1.0
    x = X
    y = Y
    z = Z
    points.append([x,y,z]) 
    colors.append([121,101,123])


pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors)   

  
vis.add_geometry(pcd)
vis.poll_events()
vis.update_renderer()
vis.run()
