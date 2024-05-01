import pandas

# imports dataframe from csv file
# trial pandas.read_excel(*args, **kwargs) to
# read in an xlsx file rather than a .csv
df = pandas.read_excel("Assets/03_MM_test_frame.csv")

# df = df.set_index('Item')

print(df)
print()

