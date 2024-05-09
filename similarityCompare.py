import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV 파일 로드
trajectory1 = pd.read_csv('./trajectory/avg_cps.csv')
trajectory2 = pd.read_csv('./trajectory/newInterp1d.csv')

# 각 좌표의 차이 계산
differences = trajectory1.values - trajectory2.values

# 각 차이의 제곱 계산
squared_differences = np.square(differences)

# 유클리드 거리 계산
distances = np.sqrt(np.sum(squared_differences, axis=1))
total_euclidean_distance = np.sum(distances)
mean_euclidean_distance = np.mean(distances)
max_euclidean_distance = np.max(distances)
rmsd = np.sqrt(np.mean(np.sum(squared_differences, axis=1)))

# 결과 출력
print(f'Total Euclidean Distance: {total_euclidean_distance}')
print(f'Mean Euclidean Distance: {mean_euclidean_distance}')
print(f'Maximum Euclidean Distance: {max_euclidean_distance}')
print(f'RMSD: {rmsd}')

# 시각화
fig, ax = plt.subplots(2, 2, figsize=(14, 10))

# Trajectories Plot
ax[0, 0].plot(trajectory1['x'].values, trajectory1['y'].values, label='Trajectory 1')
ax[0, 0].plot(trajectory2['x'].values, trajectory2['y'].values, label='Trajectory 2')
 
# 0번째 포인트 및 100번째마다 포인트 찍기
for i in range(100, len(trajectory1), 100):

    ax[0, 0].scatter(trajectory1['x'].values[i], trajectory1['y'].values[i], color='blue', zorder=5, s=20)
    ax[0, 0].scatter(trajectory2['x'].values[i], trajectory2['y'].values[i], color='orange', zorder=5, s=20)

#ax[0, 0].scatter(trajectory1['x'].values[len(trajectory1)-100], trajectory1['y'].values[len(trajectory1)-100], color='blue', zorder=5, s=20)
#ax[0, 0].scatter(trajectory2['x'].values[len(trajectory2)-100], trajectory2['y'].values[len(trajectory2)-100], color='orange', zorder=5, s=20)

# 시작점 방향을 나타내는 화살표 추가
arrowprops = dict(facecolor='red', edgecolor='red', arrowstyle='->', lw=1.5, mutation_scale=20)
ax[0, 0].annotate('', xy=(trajectory1['x'].values[1], trajectory1['y'].values[1]), 
                  xytext=(trajectory1['x'].values[0], trajectory1['y'].values[0]),
                  arrowprops=arrowprops, annotation_clip=False)
ax[0, 0].annotate('', xy=(trajectory2['x'].values[1], trajectory2['y'].values[1]), 
                  xytext=(trajectory2['x'].values[0], trajectory2['y'].values[0]),
                  arrowprops=arrowprops, annotation_clip=False)


ax[0, 0].set_title('Trajectories')
ax[0, 0].legend()
ax[0, 0].set_xlabel('X')
ax[0, 0].set_ylabel('Y')

# Euclidean Distances Plot
ax[0, 1].plot(distances)
ax[0, 1].set_title('Euclidean Distances')
ax[0, 1].set_xlabel('Point Index')
ax[0, 1].set_ylabel('Distance (m)')

# Histogram of Euclidean Distances
ax[1, 0].hist(distances, bins=30, edgecolor='black')
ax[1, 0].set_title('Histogram of Euclidean Distances')
ax[1, 0].set_xlabel('Distance (m)')
ax[1, 0].set_ylabel('Frequency')

# Summary Statistics Bar Plot
summary_stats = {
    # 'Total Distance': total_euclidean_distance,
    'Mean Distance': mean_euclidean_distance,
    'RMSD': rmsd,
    'Max Distance': max_euclidean_distance
    
}
bars = ax[1, 1].bar(summary_stats.keys(), summary_stats.values(), color=['blue', 'green', 'purple'])
ax[1, 1].set_title('Summary Statistics')
ax[1, 1].set_xlabel('Metric')
ax[1, 1].set_ylabel('Distance (m)')

for bar in bars:
    height = bar.get_height()
    ax[1, 1].text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()