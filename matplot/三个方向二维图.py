import matplotlib.pyplot as plt

# create some data
x = [1 , 2, 1, 5, 2]
y = [1, 2, 2, 2, 2]
z = [2, 3, 3, 7, 2]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 7))


# plot the xy plane on the first subplot
ax1.scatter(x, y, label='XY Plane')

# plot the xz plane on the second subplot
ax2.scatter(x, z, label='XZ Plane')

# plot the yz plane on the third subplot
ax3.scatter(y, z, label='YZ Plane')

# add a legend to each subplot
ax1.legend()
ax2.legend()
ax3.legend()

# show the plot
plt.show()
