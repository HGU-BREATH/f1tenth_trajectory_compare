#!/bin/bash

input1=$1
input2=$2

# Step 1: Generate average trajectories
python3 ./main/getAvgTrajectory.py "$input1"
python3 ./main/getAvgTrajectory.py "$input2"

# Assumed output filenames
avg_input1="./trajectory/avg/avg_$(basename "$input1")"
avg_input2="./trajectory/avg/avg_$(basename "$input2")"

# Step 2: Sync starting point of avg_input2 to avg_input1
python3 ./main/syncStartingPoint.py $avg_input1 $avg_input2

# Assumed output filename
set_avg_input2="./trajectory/startingPointSet/set_avg_$(basename "$input2")"

# Step 3: Compare the synchronized files
python3 ./main/similarityCompare.py $avg_input1 $set_avg_input2
