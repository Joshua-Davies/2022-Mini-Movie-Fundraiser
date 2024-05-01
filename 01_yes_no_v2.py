# Fuctions go here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

# main routine goes here 

while True:

    want_instructions = yes_no("Do you want to read the" 
                                " instructions? ").lower()

    if want_instructions == "yes":
        print("Instructions go here")
    elif want_instructions == "no":
        pass
    else:
     print("Please answer yes / no")

    print("we are done")