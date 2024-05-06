import numpy as np
import pandas as pd
import sys
from scipy.interpolate import interp1d

# 유클리드 거리 계산 함수
def euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_cumulative_distance(x, y):
    distances = np.sqrt(np.diff(x)**2 + np.diff(y)**2)
    return np.concatenate(([0], np.cumsum(distances)))

# 랩 시작점을 찾는 함수
def find_lap_starts(x, y, initial_point_index, min_distance=0.04, search_start_offset=300, search_range=500):

    lap_starts = [initial_point_index]
    current_start = initial_point_index
    n = len(x)
    
    while True:
        
        # t 지점 찾기
        search_start = current_start + search_start_offset
        if search_start >= n:
            break

        # s와 t 후보들의 거리를 계산하며 조건을 만족하는 첫 번째 지점 찾기
        first_close_index = None
        for i in range(search_start, n):
            distance = euclidean_distance(x[initial_point_index], y[initial_point_index], x[i], y[i])
            if distance <= min_distance:
                first_close_index = i
                break

        # 조건을 만족하는 지점이 없으면 루프 종료
        if first_close_index is None:
            break


        # s와 최소 거리를 갖는 지점 찾기
        end_search = first_close_index + search_range
        if end_search >= n:
            end_search = n - 1
        min_distance_index = first_close_index + np.argmin([euclidean_distance(x[initial_point_index], y[initial_point_index], x[i], y[i]) for i in range(first_close_index, end_search + 1)])

        # 새로운 랩 시작점 추가
        lap_starts.append(min_distance_index)
        current_start = min_distance_index

    return lap_starts

def resample_by_distance(x, y, num_points=2000):
    cumulative_distance = calculate_cumulative_distance(x, y)
    total_distance = cumulative_distance[-1]
    
    distance_new = np.linspace(0, total_distance, num_points)
    fx = interp1d(cumulative_distance, x, kind="quadratic")
    fy = interp1d(cumulative_distance, y, kind="quadratic")
    
    x_new = fx(distance_new)
    y_new = fy(distance_new)
    
    return x_new, y_new


# 메인 실행 함수
def main(input_file, output_file):
    # CSV 파일 로드, 헤더 없다고 가정
    df = pd.read_csv(input_file, header=None)
    
    # x와 y 좌표 추출
    t = df[0].values
    x = df[1].values
    y = df[2].values
    
    # 초기 시작점 설정
    initial_point_index = 50 # For avoiding inaccuracy of starting point. (Since the trejctory file is accumulated by repeating, removing the first some data is ok.)
    
    # 랩 시작점 찾기
    lap_start_indices = find_lap_starts(x, y, initial_point_index)
    
    # 각 랩의 데이터 출력
    for i, start_index in enumerate(lap_start_indices[:-1]):
        end_index = lap_start_indices[i + 1]
        print(f"Lap {i + 1}: Start at index {start_index}, End at index {end_index} | Time: {round(t[end_index]-t[start_index], 5)} | Number of index {end_index - start_index + 1} | Starting point accuracy {round(euclidean_distance(x[initial_point_index], y[initial_point_index], x[start_index], y[start_index]), 4)}")
    
    resampled_x = []
    resampled_y = []
    
    for i in range(len(lap_start_indices) - 1):
        start_idx = lap_start_indices[i]
        end_idx = lap_start_indices[i + 1]
        
        x_lap = x[start_idx:end_idx]
        y_lap = y[start_idx:end_idx]
        
        x_new, y_new = resample_by_distance(x_lap, y_lap)
        resampled_x.append(x_new)
        resampled_y.append(y_new)
    
    # 평균 트랙 계산
    x_mean = np.mean(resampled_x, axis=0)
    y_mean = np.mean(resampled_y, axis=0)
    
    # 새로운 DataFrame 생성
    df_mean = pd.DataFrame({'x_avg': x_mean, 'y_avg': y_mean})
    # 새로운 CSV 파일로 저장
    df_mean.to_csv(output_file, index=False)

    print("Calculating is done!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python calMeanOfAccumTrajectory.py input.csv output.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)
    print("End of the script")