import open3d as o3d
import numpy as np

# 创建立方体的顶点坐标
vertices = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
                    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]])

# 创建立方体的面索引
triangles = np.array([[0, 1, 2], [2, 3, 0], [3, 2, 6], [6, 7, 3],
                      [7, 6, 5], [5, 4, 7], [4, 5, 1], [1, 0, 4],
                      [1, 5, 6], [6, 2, 1], [4, 0, 3], [3, 7, 4]])

# 创建Open3D的TriangleMesh对象
mesh = o3d.geometry.TriangleMesh()

# 设置顶点和面索引
mesh.vertices = o3d.utility.Vector3dVector(vertices)
mesh.triangles = o3d.utility.Vector3iVector(triangles)

# 保存为PLY文件
o3d.io.write_triangle_mesh("cube.ply", mesh)

print("PLY文件已保存为 cube.ply")
