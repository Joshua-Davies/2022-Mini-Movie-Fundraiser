# functions go here

# main routine goes here
tickets_sold = 0

while True:

    name = input("Enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = int(input("Age: "))

    if 12 <= age <= 120:
        pass
    elif age <12:
        print("sorry you are too young for this movie")
        continue

    tickets_sold += 1

