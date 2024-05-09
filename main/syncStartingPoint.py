import pandas as pd
import numpy as np
import sys
import os

def find_nearest_point(base_point, points):

    distances = np.sqrt((points['x'] - base_point[0])**2 + (points['y'] - base_point[1])**2)
    return distances.idxmin()

def rearrange_data(data, start_index):
    return pd.concat([data.iloc[start_index:], data.iloc[:start_index]]).reset_index(drop=True)

def process_files(input1, input2):
    
    data1 = pd.read_csv(input1, header=0)
    data2 = pd.read_csv(input2, header=0, dtype={'x': float, 'y': float})
    
    # 첫 번째 파일의 첫 번째 포인트 가져오기
    start_point = data1.iloc[0, :2].values  # x, y 값만 추출
    
    # 두 번째 파일에서 가장 가까운 포인트 찾기
    nearest_index = find_nearest_point(start_point, data2)
    print(nearest_index)

    # 두 번째 데이터 재정렬
    rearranged_data = rearrange_data(data2, nearest_index)
    
    output_dir = './trajectory/startingPointSet'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_file = os.path.join(output_dir, f"set_{os.path.basename(input2)}")

    # 결과를 새로운 파일로 저장
    rearranged_data.to_csv(output_file, index=False)
    print(f"{input2}'s starting point is adjusted! File saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py file1.csv file2.csv")
        sys.exit(1)

    input1, input2 = sys.argv[1], sys.argv[2]
    process_files(input1, input2)