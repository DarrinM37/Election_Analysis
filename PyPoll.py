# The data we need to retrieve    
# Total Number of votes cast
# A complete list of candidates who recieved votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

#add our dependencies. 
import csv
import os

# Assign a variable to laod a file from a path
file_to_load= os.path.join("resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save= os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    
    # Read and print the header row
    headers = next(file_reader)
    print(headers)
