# Import the csv module
import csv
# Define the file path
file_path = r'C:\Users\yunna\Data_bootcamp\Homework\Challenge 3\PyBank\Resources\budget_data.csv'

# Creat variables
# To count the number of months
total_months = 0
# To sum up the total progit/losses
net_total = 0
# To store the changes
changes = []
# To store the dats associated with the changes
dates = []
# To keep track of profit/losses
previous_profit_losses = None
# To store the date and amount of the greatest increase in profits
greatest_increase = {'date': None, 'change': float('-inf')}
# To store the date and amount of the greatest decrease in profits
greatest_decrease = {'date': None, 'change': float('inf')}

# Read the CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader) 
    
    for row in csv_reader:
        date = row[0]
        profit_losses = int(row[1])
        
        # Count the total number of months
        total_months += 1
                
        # Sum the total profit/losses
        net_total += profit_losses
        
        # Check if this is not the first row
        if previous_profit_losses is not None:
            # Calculate the change
            change = profit_losses - previous_profit_losses
            # Add the change to the list
            changes.append(change)
            # Add the data to the list
            dates.append(date)

            # Check for the greatest increase in profits
            if change > greatest_increase['change']:
                #update the greatest increase
                greatest_increase['change'] = change
                #update the associated date of the greatest increase
                greatest_increase['date'] = date

            # Check for the greatest decrease in profits
            if change < greatest_decrease['change']:
                #update the greatest decrease
                greatest_decrease['change'] = change
                #update the associated date of the greatest decrease
                greatest_decrease['date'] = date
                
        previous_profit_losses = profit_losses

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# Print the results
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['change']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['change']})")