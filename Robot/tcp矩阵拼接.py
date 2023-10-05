    def get_TCPposetion(self, array_one, array_two, array_three):
        postureMatrix_one = array_one[:3, :3]  # 姿态1
        postureMatrix_two = array_two[:3, :3]  # 姿态2
        postureMatrix_three = array_three[:3, :3]  # 姿态2
        postureMatrix = np.concatenate((postureMatrix_one, postureMatrix_two, postureMatrix_three), axis=0)  # 拼接3个姿态
        postureMatrix_T = np.transpose(postureMatrix)  # 置换矩阵
        posetion_one = array_one[0:3, 3:4]  # 位置1
        posetion_two = array_two[0:3, 3:4]  # 位置2
        posetion_three = array_three[0:3, 3:4]  # 位置3
        posetionMatrix = np.concatenate((posetion_one, posetion_two, posetion_three), axis=0)  # 拼接位置矩阵
        result = np.dot(np.dot(np.linalg.inv(np.dot(postureMatrix_T, postureMatrix)), postureMatrix_T), posetionMatrix)  #矩阵最小二乘解

        return result