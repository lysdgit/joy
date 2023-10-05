ALPHA = 0.7
gravity = [0, 0, 0]
filteredValues = [0, 0, 0]

def onSensorChanged(event):
    global gravity, filteredValues

    gravity[0] = ALPHA * gravity[0] + (1 - ALPHA) * event[0]
    gravity[1] = ALPHA * gravity[1] + (1 - ALPHA) * event[1]
    gravity[2] = ALPHA * gravity[2] + (1 - ALPHA) * event[2]

    filteredValues[0] = event[0] - gravity[0]
    filteredValues[1] = event[1] - gravity[1]
    filteredValues[2] = event[2] - gravity[2]


# 示例用法
event = [1.2, 2.5, 3.8]  # 假设传感器事件的原始值
onSensorChanged(event)

print("Gravity:", gravity)
print("Filtered Values:", filteredValues)
