#  import statements
import random
import pandas
from datetime import date


# functions go here

def show_instructions():
    print('''\n
***** Instructions *****

For each ticket, enter...
- The person's name (can't be blank)
- Age (between 12 and 120)
- Payment method (cash / credit)

when you have entered all the users, press 'xxx' to quit.

The program will then display the ticket details
including the cost of each ticket, the total cost 
and the total profit.

The information will also be automatically written to
a text file.

*************************''')

# checks user has entered an integer
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")


# checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # If name is not blank, program continues
        if response != "":
            return response

        # If name is blank, show error (& repeat loop)
        else:
            print("Sorry - this can’t be blank, "
                  "please enter your name")


# Checks for an integer more than 0
def int_check(question):
    error = "Please enter a whole number that is more than 0"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error message
        except ValueError:
            print(error)


# Calculate the tickets price based on the age
def calc_ticket_price(var_age):
    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

        # ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# checks that users enter a valid response (eg yes / no
#  cash / credit) based on a list of options
def string_checker(question, num_letter, valid_responses):
    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    if num_letter == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)

        print("Please enter a valid response")


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# set maximum number of tickets below
MAX_TICKETS = 5
tickets_sold = 0

# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary used to create data frame ie: column_name:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# Ask user if they want to see the instructions
want_instructions = string_checker("Do you wan to read the "
                                   "instructions (y/n): ",
                                   1, yes_no_list)

if want_instructions == "yes":
    show_instructions()

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    Name = not_blank("Enter your name (or 'xxx' to quit)")

    # exit loop if users type 'xxx' and have sold at lease 
    # one ticket
    if Name == 'xxx' and len(all_names) > 0:
        break
    elif Name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

    age = num_check("Age: ")

    # check user is between 12 and 120 (inclusive)
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are to young for this movie")
        continue
    else:
        print("?? That look like a typo, please try again")
        continue

    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)

    # get payment method
    pay_method = string_checker("choose a payment method (cash / "
                                "credit): ",
                                2, payment_list)

    print(f"You are paying {pay_method}")

    if pay_method == "cash":
        surcharge = 0
    else:
        # calculate 5% surcharge if users are playing by credit card
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # add ticket name, cost and surcharge to lists
    all_names.append(Name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

# create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the profit for reach ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# choose winner and look up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = "---- Mini Movie Fundraiser Ticket Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# create strings for printing.....
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
total_profit = "Total Profit : ${:.2f}".format(profit)

# edit text below!! It needs to work if we have unsold tickets
# show users how many tickets have been sold
if tickets_sold == MAX_TICKETS:
    sales_status = "\n*** All the tickets have been sold ***"
else:
    sales_status = "\n *** You have sold {} out of {} " \
                   "tickets *****".format(tickets_sold, MAX_TICKETS)

# Output raffle results
winner_heading = "\n---- Raffle Winner ----"
winner_text = "The winner of the raffle is {}. " \
              "They have won ${:.2f}  ie: Their ticket is " \
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
