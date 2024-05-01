import pandas

# dictionary to hold snack prices
snack_prices = {
    "Popcorn": 2.5,
    "M&Ms": 3,
    "Pita Chips": 4.5,
    "Orange Juice": 3.25,
    "Water": 2
}


# data-frame to hold snack numbers,
# initially set amounts to zero
data = {'Snack':  ['Popcorn', 'M&Ms','Pita Chips', 'Orange Juice', 'Water'],
        'Amount': [0, 0, 0, 0, 0]
        }

df_i = pandas.DataFrame(data, columns=['Snack', 'Amount'])

print(df_i)

print()

# Sets index to snack name
# Making editing easier
df_i = df_i.set_index('Snack')

# identify row using index and change it
df_i.at['Pita Chips', 'Amount'] = 5

print(df_i)

print()

print("*** add to popcorn count ***")
popcorn_count = df_i.at['Popcorn', 'Amount']
popcorn_count += 3
df_i.at['Popcorn', 'Amount'] = popcorn_count

print(df_i)
