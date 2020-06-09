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
list_data = []

with open(data_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # initialises the titles
    header = next(csvreader)
    for row in csvreader:
        for column in range(1, len(header)):
            # Hashes using a tuple
            list_data.append((row[0],header[column],row[column]))

# Open DNA sequence and read it's contents into memory
with open(data_sequence, 'r') as file:
    data = file.read()

del header[0]

dict_str = {}

for i in header:
    # Getting the length of the Str
    strlen = len(i)
    data_length = len(data)
    j = 0
    # counter to keep track of the maximum counter of the current Str 
    counter = 0
    while j in range(data_length):
        if data[j:j+strlen] == i:
            if i not in dict_str:
                # dict_str[i] here serves as an integer counter to keep track of current repetition before reset
                dict_str[i] = 1
            else:
                dict_str[i] += 1

            if dict_str[i] > counter:
                counter = dict_str[i]

            j += strlen

        else:
            dict_str[i] = 0
            j += 1
# In this example I am using 1 integer and 1 dictionary value to keep track.
    dict_str[i] = str(counter)

scores = {}
winner = 0

for name in list_data:
    if dict_str[name[1]] == name[2]:
        if name[0] in scores:
            scores[name[0]] += 1
        else:
            scores[name[0]] = 1

for names in scores:
    if scores[names] == len(header):
        winner = names

if winner != 0:
    print(winner)
else:
    print("No match")