import matplotlib.pyplot as plt
import pandas as pds
# import matplotlib as mtl

# Variables
W_time = []
TA_time = []
timer = 0
counter = 0
avg_W_time = []
avg_TA_time = []
processes = pds.read_csv('../Data/generated_data.csv')

# Sorting processes in groups 100 each
# After sorting counting average work and wait time using FCFS algorithm
for i in range(0, 100):
    # Sort processes by arriving time (from earliest to latest)
    FCFS_Data = processes[counter:counter + 100].sort_values(by='arrive_time', ascending=True)
    listed_data = FCFS_Data.values.tolist()

    # Saving waiting and working time
    for j in range(0, len(listed_data)):
        timer += listed_data[j][1]
        TA_time.append(timer - listed_data[j][0])
        W_time.append(TA_time[j] - listed_data[j][1])

    # Convert W_time and TA_time to dataframe for easier avg count
    TAT = pds.Series(TA_time)
    TAT.columns = 'TAT'

    WT = pds.Series(W_time)
    WT.columns = 'WT'

    # Add the average wait and turnaround time to table for further analysis
    avg_W_time.append(round(WT.mean()))
    avg_TA_time.append(round(TAT.mean()))

# Reset variables values for next simulation
    W_time = []
    TA_time = []
    timer = 0
# Increment counter
    counter += 100

# Save counted average values to CSV file
Stats = pds.DataFrame({'avg_turnaround_time': avg_TA_time[0:100], 'avg_wait_time': avg_W_time[0:100]})
Stats.to_csv('FCFS_stats.csv', index=False)
print(Stats)
print(Stats['avg_turnaround_time'].mean())
print(Stats['avg_wait_time'].mean())

# Mat PLot Lib for Tat
x = Stats.avg_turnaround_time
y = 7
plt.xlabel('Time [ms]')
plt.ylabel('Count')
plt.title('Amount of every average turnaround time for FCFS')
plt.hist(x, y, density=False, color='orange')
plt.grid(True)
plt.show()

# Mat plot lib for WT
a = Stats.avg_wait_time
b = 7
plt.xlabel('Time [ms]')
plt.ylabel('Count')
plt.title('Amount of every average waiting time for FCFS')
plt.hist(a, b, density=False, color='green')
plt.grid(True)
plt.show()
