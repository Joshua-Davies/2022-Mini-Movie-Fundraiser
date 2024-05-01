import pandas
import random   
from datetime import date


# dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_tickets_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_tickets_costs,
    "Surcharge": surcharge
}

# create data frame 
mini_movie_frame = pandas.DataFrame(mini_movie_dict)


# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the profit for rach ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# choose winner and look up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.at('Name')

# **** Get current date for headind and filename ****
# get today's date
today = date.strftime()

# Get day, month and year as individual strings 
day = date.strftime("%d")
month = date.strftime("%m")
year = date.strftime("%y")

heading = "---- Mini Movie Fundraiser Ticket Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# create strings for printing.....
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = "Total Ticket Sales: ${}".format(total)
tal_profit = "Total Profit : ${}".format(profit)

# edit text below!! It needs to work if we have unsold tickets
sales_status = "\n*** All the tickets have been sold ***"

winner_heading = "\n---- Raffle Winner ----"
winner_text = "The winner of the raffle is {}. " \
              "They have won ${}.  ie: Their ticket is " \
              "free!".format(winner_name, total_won)

# lists holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# print output
for item in to_write:
    print(item)


# write output to file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()