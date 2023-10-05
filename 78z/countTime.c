#include <stdio.h>
#include <time.h>

int main() {
	time_t start_time, current_time;
	double elapsed_time;
	int i;
	
	start_time = time(NULL);  // 获取当前时间
	
	for (i = 0; ; i++) {
		printf("%d",i);
		
		current_time = time(NULL);  // 获取当前时间
		elapsed_time = difftime(current_time, start_time);  // 计算经过的时间
		
		if (elapsed_time >= 3) {
			printf("Loop executed for 3 seconds.\n");
			break;
		}
	}
	
	return 0;
}
