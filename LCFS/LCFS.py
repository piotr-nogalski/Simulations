import pandas as pds
import matplotlib.pyplot as plt

# Variables
W_time = []
TA_time = []
timer = 0
counter = 0
avg_W_time = []
avg_TA_time = []
queue = []
t = 0  # <- temporary variable used for counting W_time, TAT_time and timer while not all processes are in queue

processes = pds.read_csv('../Data/generated_data.csv')

# Sorting processes in groups 100 each
for i in range(0, 100):
    # Sort processes by arriving time (from earliest to latest)
    LCFS_Data = processes[counter:counter + 100].sort_values(by='arrive_time', ascending=True)
    listed_data = LCFS_Data.values.tolist()

    # First process comes to CPU
    TA_time.append(listed_data[0][1])
    W_time.append(0)
    timer += listed_data[0][1]
    listed_data.pop(0)

    while len(queue) < 99-t:  # <- loop that waits until all processes are in queue
        # Filter out processes that arrived during first process work and sort them descending by arrive time
        queue = LCFS_Data['arrive_time'] <= timer
        New_DataFrame = LCFS_Data[queue]
        listed_data = New_DataFrame.sort_values(by='arrive_time', ascending=False).values.tolist()
        timer += listed_data[0][1]
        TA_time.append(timer - listed_data[0][0])
        W_time.append(TA_time[t] - listed_data[0][1])
        t += 1
        listed_data.pop(0)

    # Once every process is in queue it's the same counting rule as in LCFS algorithm
    for j in range(t, len(listed_data)):
        timer += listed_data[j][1]
        TA_time.append(timer - listed_data[j][0])
        W_time.append(TA_time[j] - listed_data[j][1])
    print(len(TA_time))

    # Convert W_time and TA_time to dataframe for easier avg count
    TAT = pds.Series(TA_time)
    TAT.columns = 'TAT'

    WT = pds.Series(W_time)
    WT.columns = 'WT'

    avg_W_time.append(round(WT.mean()))
    avg_TA_time.append(round(TAT.mean()))

# Reset variables values for next simulation
    W_time = []
    TA_time = []
    timer = 0
    t = 0

# Increment counter
    counter += 100

# Saving stats to a CSV file
Stats = pds.DataFrame({'avg_turnaround_time': avg_TA_time[0:100], 'avg_wait_time': avg_W_time[0:100]})
Stats.to_csv('LCFS_stats.csv', index=False)
print(Stats)
print(Stats['avg_turnaround_time'].mean())
print(Stats['avg_wait_time'].mean())

# Mat PLot Lib for Tat
x = Stats.avg_turnaround_time
y = 7
plt.xlabel('Time [ms]')
plt.ylabel('Count')
plt.title('Amount of every average turnaround time for LCFS')
plt.hist(x, y, density=False, color='orange')
plt.grid(True)
plt.show()

# Mat plot lib for WT
a = Stats.avg_wait_time
b = 7
plt.xlabel('Time [ms]')
plt.ylabel('Count')
plt.title('Amount of every average waiting time for LCFS')
plt.hist(a, b, density=False, color='green')
plt.grid(True)
plt.show()
