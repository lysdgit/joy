import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

# 生成三维空间的点数据
X = np.random.rand(100, 3)

# 使用K-Means聚类算法，将数据聚成3类
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# 可视化聚类结果
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=kmeans.labels_)
plt.show()
