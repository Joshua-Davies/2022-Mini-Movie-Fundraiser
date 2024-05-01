#  Functions go here


def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry - this can’t be blank, "
                 "please enter your name")


# Main Routine goes here
name = not_blank("Name: ")
