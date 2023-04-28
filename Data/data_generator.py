# ModulesD
import pandas as pds
import random

# Variables
process = []


# Function to generate processes
def generate():
    # Generates 10000 processes with pseudo random execution time and arrival time in ms
    for i in range(1, 10001):
        process.append([random.randrange(0, 12), random.randrange(1, 17)])
    # Saves array as DataFrame
    process_data = pds.DataFrame(process, columns=['arrive_time', 'duration_time'])
    # Saves DataFrame to csv file
    process_data.to_csv('generated_data.csv', index=False)


generate()
