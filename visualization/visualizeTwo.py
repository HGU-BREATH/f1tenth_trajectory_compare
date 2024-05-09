import matplotlib.pyplot as plt
import numpy as np
import sys

def main(file1, file2):
    
    data1 = np.genfromtxt(file1, delimiter=',', skip_header=1)  # 헤더가 있다면 skip_header=1을 사용
    if(data1.shape[1] == 2):
        x1 = data1[:, 0]  # x 좌표는 첫 번째 열
        y1 = data1[:, 1]  # y 좌표는 두 번째 열
    else:
        x1 = data1[:, 0] 
        y1 = data1[:, 1] 

    data2 = np.genfromtxt(file2, delimiter=',', skip_header=1)
    if(data2.shape[1] == 2):
        x2 = data2[:, 0]  # x 좌표는 첫 번째 열
        y2 = data2[:, 1]  # y 좌표는 두 번째 열
    else:
        x2 = data2[:, 0] 
        y2 = data2[:, 1] 
    
    
    # 플롯 생성
    plt.figure(figsize=(20, 15))  # 그래프 크기 설정
    
    plt.plot(x1, y1, marker='o', linewidth=5, color='red', alpha=1, label='Accumulated Trajectory')  # 투명도 설정하여 겹치는 부분을 줄임
    plt.plot(x2, y2, marker='o', linewidth=2, color='blue', alpha=0.5, label='Average Trajectory')
    
    plt.title('Trajectory Visualization')  # 그래프 제목
    plt.xlabel('X Position')  # x축 레이블
    plt.ylabel('Y Position')  # y축 레이블
    plt.grid(True)  # 그리드 표시
    plt.show()  # 그래프 표시

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python3 visualizeTwo.py file1.csv file2.csv")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    main(file1, file2)
    
    main(file1, file2)
