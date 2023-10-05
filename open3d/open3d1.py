import open3d as o3d

# 创建一个空的点云对象
point_cloud = o3d.geometry.PointCloud()

# 从文件加载点云数据
point_cloud = o3d.io.read_point_cloud("C:/Users/liys2/Desktop/PYRD/ply/test.ply")

# 创建一个可视化窗口
vis = o3d.visualization.Visualizer()
vis.create_window(width=800, height=600)  # 设置窗口大小为800x600

# 添加点云数据到可视化窗口
vis.add_geometry(point_cloud)

# 添加xyz坐标轴
vis.add_geometry(o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.1))

# 设置相机的初始位置和方向
ctr = vis.get_view_control()
ctr.set_lookat([60, 0, 0])  # 设置相机的观察点
ctr.set_front([0, 60, 0])  # 设置相机的正方向
ctr.set_up([0, 0, 60])  # 设置相机的上方向

# 运行可视化窗口
vis.run()
vis.destroy_window()




