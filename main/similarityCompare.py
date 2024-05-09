import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def main(input1, input2):
    trajectory1 = pd.read_csv(input1)
    trajectory2 = pd.read_csv(input2)

    differences = trajectory1.values - trajectory2.values # Calculate the difference between each point correspoinding to same order of row.
    squared_differences = np.square(differences)

    distances = np.sqrt(np.sum(squared_differences, axis=1))
    total_euclidean_distance = np.sum(distances)
    mean_euclidean_distance = np.mean(distances)
    max_euclidean_distance = np.max(distances)
    rmsd = np.sqrt(np.mean(np.sum(squared_differences, axis=1)))

    # Metric result 
    print(f'Total Euclidean Distance: {total_euclidean_distance}')
    print(f'Mean Euclidean Distance: {mean_euclidean_distance}')
    print(f'Maximum Euclidean Distance: {max_euclidean_distance}')
    print(f'RMSD: {rmsd}')

    # Visulization start
    fig, ax = plt.subplots(2, 2, figsize=(14, 10))

    # Trajectories Plot
    ax[0, 0].plot(trajectory1['x'].values, trajectory1['y'].values, label='Trajectory 1')
    ax[0, 0].plot(trajectory2['x'].values, trajectory2['y'].values, label='Trajectory 2')
    
    for i in range(100, len(trajectory1), 100):

        ax[0, 0].scatter(trajectory1['x'].values[i], trajectory1['y'].values[i], color='blue', zorder=5, s=20)
        ax[0, 0].scatter(trajectory2['x'].values[i], trajectory2['y'].values[i], color='orange', zorder=5, s=20)

    # Add an arrow indicating the direction of driving
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 similarityCompare.py input1.csv input2.csv")
        sys.exit(1)
    
    input_file1 = sys.argv[1]
    input_file2 = sys.argv[2]
    main(input_file1, input_file2)