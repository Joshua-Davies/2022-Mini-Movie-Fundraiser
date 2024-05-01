# checks that users enter a valid response (eg yes / no
#  cash / credit) based on a list of options
from numpy.version import short_version


def string_checker(question, num_letter, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)

        print("Please enter a valid response")


# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0,5):
    want_instructions = string_checker("Do you want to read the instructions (y/n): ",
                                       "instructions (y/n): ",
                                       1)
    print("You chose", want_instructions)

for case in range(0, 5):
    pay_method = string_checker("choose a payment method (cash / credit)",
                                2, payment_list)
    print("You chose", pay_method)