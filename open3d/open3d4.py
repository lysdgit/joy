import plotly.graph_objects as go

# 二十个点的坐标数据
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
z = [3, 6, 9, 12, 15, 2, 5, 8, 11, 14, 3, 6, 9, 12, 15, 2, 5, 8, 11, 14]

# 创建一个散点图
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])

# 设置图形布局和样式
fig.update_layout(
    scene=dict(
        xaxis=dict(title='X轴'),
        yaxis=dict(title='Y轴'),
        zaxis=dict(title='Z轴')
    ),
    width=700,
    height=500,
    title='二十个三维点的坐标'
)

# 显示图形
fig.show()

# import plotly.graph_objects as go
# import numpy as np
# import pandas as pd

# # 20个三维点坐标的示例数据
# data = pd.read_csv('C:/Users/liys2/Desktop/12.csv')
# data = data[~(data == 0).all(axis=1)]
# # 创建散点图对象
# fig = go.Figure(data=[go.Scatter3d(x= data['x'].values, y= data['y'].values, z= data['z'].values, mode='markers')])

# # 设置图表布局和样式
# fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

# # 显示图表
# fig.show()
