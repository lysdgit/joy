#include <stdio.h>

// 定义卡尔曼滤波的数据结构
typedef struct {
	float x;    // 状态估计值
	float P;    // 状态估计误差协方差
	float F;    // 状态转移矩阵
	float H;    // 观测矩阵
	float R;    // 观测噪声协方差
} KalmanFilter;

// 初始化卡尔曼滤波器
void kalman_init(KalmanFilter* kf, float x, float P, float F, float H, float R) {
	kf->x = x;
	kf->P = P;
	kf->F = F;
	kf->H = H;
	kf->R = R;
}

// 卡尔曼滤波的预测步骤
float kalman_predict(KalmanFilter* kf) {
	kf->x = kf->F * kf->x;
	kf->P = kf->F * kf->P * kf->F;
	return kf->x;
}

// 卡尔曼滤波的观测更新步骤
float kalman_update(KalmanFilter* kf, float z) {
	float y = z - kf->H * kf->x;
	float S = kf->H * kf->P * kf->H + kf->R;
	float K = kf->P * kf->H / S;
	
	kf->x = kf->x + K * y;
	kf->P = kf->P - K * kf->H * kf->P;
	
	return kf->x;
}

// 示例使用卡尔曼滤波器对温度数据进行滤波
int main() {
	KalmanFilter kf;
	float measurements[] = {78.194, 78.195, 78.192, 78.192, 78.189, 78.192, 78.192, 78.193, 78.196, 78.193, 78.192, 78.192, 78.192, 78.192, 78.194, 78.191, 78.193, 78.194, 78.194, 78.192, 78.195, 78.193, 78.193, 78.193, 78.194, 78.19, 78.192, 78.191, 78.192, 78.192, 78.194};
	int num_measurements = sizeof(measurements) / sizeof(float);
	
	// 初始化卡尔曼滤波器
	kalman_init(&kf, measurements[0], 1, 1, 1, 1);
	
	// 对每个测量值进行卡尔曼滤波
	for (int i = 0; i < num_measurements; ++i) {
		float prediction = kalman_predict(&kf);
		float filtered_data = kalman_update(&kf, measurements[i]);
		printf("%f\n", filtered_data);
	}
	
	return 0;
}
