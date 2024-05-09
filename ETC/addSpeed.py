import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv('~/sim_ws/src/racelines/interpolated_data1.csv')

# 모든 행에 1.0 추가
df['speed'] = 1.0

# 수정된 데이터프레임을 새로운 CSV 파일로 저장
df.to_csv('~/sim_ws/src/racelines/interpolated_data.csv', index=False)