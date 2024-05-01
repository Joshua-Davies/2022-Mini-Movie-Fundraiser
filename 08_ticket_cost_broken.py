# Next steps
# Add currency formatting & Headings
# integrate this component with the base component
# show student that they can use comments at the top
# of a component at the # end of a period so that they
# know what they got and what they need to do next
# add this idea to the last discussion slide!

# PA: In base component remember to calculate surcharge
# once payment method has been chosen
import pandas


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_tickets_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_tickets_costs,
    "Surcharge": surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the profit for rach ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item].apply(currency)

print("---- Ticket Data ----")
print()

# output table with ticket data
print(mini_movie_frame)

print()
print("----- Ticket Cost / Profit -----")

# output total ticket sales and profit
print("Total Ticket Sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f}".format(profit))
