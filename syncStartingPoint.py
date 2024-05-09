import pandas as pd
import numpy as np
import sys

def load_data(file_path):
    return pd.read_csv(file_path)

def find_nearest_point(base_point, points):

    distances = np.sqrt((points['x'] - base_point[0])**2 + (points['y'] - base_point[1])**2)
    return distances.idxmin()

def rearrange_data(data, start_index):
    return pd.concat([data.iloc[start_index:], data.iloc[:start_index]]).reset_index(drop=True)

def process_files(file1, file2, output_file):
    
    data1 = pd.read_csv(file1, header=0)
    data2 = pd.read_csv(file2, header=0, dtype={'x': float, 'y': float})
    
    # 첫 번째 파일의 첫 번째 포인트 가져오기
    start_point = data1.iloc[0, :2].values  # x, y 값만 추출
    
    # 두 번째 파일에서 가장 가까운 포인트 찾기
    nearest_index = find_nearest_point(start_point, data2)
    print(nearest_index)

    # 두 번째 데이터 재정렬
    rearranged_data = rearrange_data(data2, nearest_index)
    
    # 결과를 새로운 파일로 저장
    rearranged_data.to_csv(output_file, index=False)
    print(f"File saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py file1.csv file2.csv output.csv")
        sys.exit(1)

    file1, file2, output_file = sys.argv[1], sys.argv[2], sys.argv[3]
    process_files(file1, file2, output_file)
