import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline

# CSV 파일 읽기
data = pd.read_csv('/home/onebean/sim_ws/src/racelines/cps_2023.csv', header=None)

# x, y 데이터 추출
x = data[0].values
y = data[1].values

# 보간 수행
cs_x = CubicSpline(np.arange(len(x)), x, bc_type='periodic')
cs_y = CubicSpline(np.arange(len(y)), y, bc_type='periodic')

# 2000개의 새로운 포인트 생성
new_indices = np.linspace(0, len(x) - 1, 2000)

# 새로운 x, y 값 보간
new_x = cs_x(new_indices)
new_y = cs_y(new_indices)

# 새로운 데이터 프레임 생성
interpolated_data = pd.DataFrame({
    'x': new_x,
    'y': new_y
})

# 결과를 새로운 CSV 파일로 저장
interpolated_data.to_csv('/home/onebean/f1tenth_trajectory_cmp/trajectory/interpolated_data.csv', index=False)
