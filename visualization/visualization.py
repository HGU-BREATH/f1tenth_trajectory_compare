import matplotlib.pyplot as plt
import numpy as np
import sys

def main(file_path):
    # CSV 파일 로드
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1)  # 헤더가 있다면 skip_header=1을 사용

    # if(data.shape[1] == 2):
    #     x = data[:, 0]  # x 좌표는 첫 번째 열
    #     y = data[:, 1]  # y 좌표는 두 번째 열
    # else:
    #     x = data[:, 1] 
    #     y = data[:, 2] 

    x = data[:, 0]  # x 좌표는 첫 번째 열
    y = data[:, 1]  # y 좌표는 두 번째 열
    
    # 플롯 생성
    plt.figure(figsize=(10, 5))  # 그래프 크기 설정
    plt.plot(x, y, marker='o', linewidth=1, color='red', alpha=0.5)  # 선 그래프와 데이터 포인트에 마커 추가
    plt.title('Trajectory Visualization')  # 그래프 제목
    plt.xlabel('X Position')  # x축 레이블
    plt.ylabel('Y Position')  # y축 레이블
    plt.grid(True)  # 그리드 표시
    plt.show()  # 그래프 표시

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 visualization.py path_to_your_file.csv")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)


