import open3d as o3d
import numpy as np

# 创建一个空的点云对象
line_set = o3d.geometry.LineSet()

# 定义线段的起点和终点坐标
points = np.array([[55, 63, 70], [55+1, 63, 70],    # x轴方向线段
                   [55, 63, 70], [55, 63+1, 70],    # y轴方向线段
                   [55, 63, 70], [55, 63, 70+1]])  # z轴方向线段

# 定义线段的连接关系
lines = np.array([[0, 1], [2, 3], [4, 5]])

# 设置线段的坐标和颜色属性
line_set.points = o3d.utility.Vector3dVector(points)
line_set.lines = o3d.utility.Vector2iVector(lines)
line_set.colors = o3d.utility.Vector3dVector(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])) # 红绿蓝三色

# 创建可视化窗口并添加线段
vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(line_set)

# 设置观察视角
opt = vis.get_render_option()
opt.viewpoint_intrinsic = vis.get_window().get_view_control().convert_to_pinhole_camera_parameters()

# 显示可视化窗口
vis.run()
vis.destroy_window()
