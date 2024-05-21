import csv

# Define the file path
file_path = r'C:\Users\yunna\Data_bootcamp\Homework\Challenge 3\PyPoll\Resources\election_data.csv'

# Creat variables
# Use to count the total number of votes
total_votes = 0

# Use to store the number votes each candidate received
candidate_votes = {}

# Read the CSV file
with open(file_path, mode='r') as file:

    csv_reader = csv.reader(file)
    header = next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1
        
        candidate = row[2]
        # if the candidate is already in the dictionary, add it to their vote count, otherwise, add the candidate to the dictionary with 1 vote
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate]= 1

# Calculate the percentage of votes each cnadidate won
candidate_percentages = {candidate:(votes/total_votes)*100 for candidate, votes in candidate_votes.items()}
# Find out the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)
# Print the output
print(f"Total voters: {total_votes}")
print("Candidates and their vote counts:")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes} votes, {candidate_percentages[candidate]:.2f}%")
print(f"Winner:{winner}")
