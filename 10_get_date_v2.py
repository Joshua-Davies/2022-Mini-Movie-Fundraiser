from datetime import date

# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = "The current date is {}/{}/{}".format(day, month, year)
filename = "MMF_{}_{}_{}",format(year, month, day)

# Heading
print(heading)
print("The filename will be {}.txt".format(filename))