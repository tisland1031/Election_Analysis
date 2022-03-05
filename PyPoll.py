import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Print the file object.
    print(election_data)

#Add our dependencies.
import csv
import os

#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the file object with the reader function.
    headers = next(file_reader)

    #Print the header row.
    print(headers)

import os
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")
#Using the open ()function with the "w"mode we will write data to the file
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","Election_Analysis.txt")

#Using the with statement open the file s a text file.
with open(file_to_save, "w") as txt_file:
    #Write some data to the file.
    txt_file.write("Araphoe\n Denver\n Jefferson")
    




#The data we need to retrieve.
#1.The total number of votes casts
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.