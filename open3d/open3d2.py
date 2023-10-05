import open3d as o3d
import numpy as np


# 从CSV文件中读取点云数据
data = np.genfromtxt('C:/Users/liys2/Desktop/11.csv', delimiter=',')

# 提取XYZ坐标
X = data[:, 0]
Y = data[:, 1]
Z = data[:, 2]

# 创建点云对象
pcd = o3d.geometry.PointCloud()

# 加载点云数据
pcd.points = o3d.utility.Vector3dVector(np.column_stack((X, Y, Z)))
# 创建可视化窗口
# vis = o3d.visualization.Visualizer()
# vis.create_window()

# # 添加点云数据
# vis.add_geometry(pcd)

# # 添加坐标轴
# vis.add_geometry(o3d.geometry.TriangleMesh.create_coordinate_frame())

# # 设置相机参数和视角
# vis.get_render_option().point_size = 5
# vis.get_view_control().set_front([0, 0, -1])
# vis.get_view_control().set_up([0, 1, 0])
# vis.get_view_control().set_lookat([0, 0, 0])
# vis.get_view_control().set_zoom(100)


# # 运行可视化窗口
# vis.run()
# vis.destroy_window()
# 可视化点云
o3d.visualization.draw_geometries([pcd])
