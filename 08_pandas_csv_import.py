import pandas

# imports dataframe from csv file
# trial pandas.read_excel(*args, **kwargs) to
# read in an xlsx file rather than a .csv
df = pandas.read_csv("Assets/02_MM_price_list.csv")

print(df)


# writes csv file to csv file...
# you can use .to_excel() to create .xlsx files

df.to_csv(r'Assets/test_export.csv', index=False, header=True)
