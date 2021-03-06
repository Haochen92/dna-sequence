from sys import argv, exit
import csv

# Print error message for incorrect number of files included
if len(argv) != 3:
    print("Usage: Python dna.py data.csv sequence.txt")
    exit(1)

# Saving the file name
data_file = argv[1]
data_sequence = argv[2]

# Open STR CSV file to read it's contents into memory
dict_data = {}

with open(data_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # initialises the titles
    header = next(csvreader)
    for row in csvreader:
        for column in range(1, len(header)):
            # Hashes using a tuple
            dict_data[(row[0],header[column])] = row[column]

# Open DNA sequence and read it's contents into memory
with open(data_sequence, 'r') as file:
    data = file.read()

del header[0]

list_max = []
dict_str = {}

for i in header:
    # A counter which will reset
    counter = 0
    # A counter which will keep track of the highest count, hence will not reset
    counter_max = 0
    # Getting the length of the Str
    strlen = len(i)
    data_length = len(data)
    j = 0
    while j < data_length: # While iteration has not reached the end of sequence txt file
        if data[j:j+strlen] == i and counter == 0:
            counter = 1
        if data[j:j+strlen] == i and data[j+strlen:j+strlen*2] == i:
            counter += 1
            j += strlen
        else:
            if counter > 0 and counter > counter_max:
                counter_max = counter
                j += strlen
                counter = 0
            else:
                j += 1
    # In this example, i am using two integer counters to keep track. 

    current_list = [i, str(counter_max)]
    list_max.append(current_list)

# Create a dictionary to keep track of scores
list_scores = []

# Print out name of matching individual or otherwise
for key_1, key_2 in dict_data:
    name_counter = 0
    if [key_2, dict_data[key_1,key_2]] in list_max:
        list_scores.append(key_1)

answer = max(list_scores, key=list_scores.count)
number = list_scores.count(answer)

if number == len(list_max):
    print(answer)
else:
    print("No match")