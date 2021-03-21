import pandas as pd
import numpy as np


# make 3 element ndarray
my_numpy_array = np.random.rand(3)

# make pandas series
# my_first_series = pd.Series(np.random.rand(3))
my_series = pd.Series(my_numpy_array)

# Fails because there are 4 labes, and 3 items
# my_series = pd.Series(my_numpy_array, index = ["First", "Second","Third", "Fourth"])

my_series = pd.Series(my_numpy_array, index=["First", "Second", "Third"])
print(my_series)
print(my_series.index)

# Create Array (rows/colums of data)
array_2d = np.random.rand(3, 2)
print(array_2d)
print(array_2d[0, 0])

# Create pandas data frame out of the array
df = pd.DataFrame(array_2d)

print(df.columns)
df.columns = ["first_column", 'second_column']
print(df)
df.index = ['1st row', '2nd row', '3rd row']
print(df)
# Doesn't work
# print(df['1st row', 'first_column'])
# print(df['first_column', '1st row', ])


# make data frame
# my_first_data_frame = pd.DataFramenp.random.rand(3, 2)

def read_in_csv(file_name, columns_wanted):

    data = pd.read_csv(file_name,
                       # Read 5 rows of CSV into DataFrame
                       #    nrows=5,
                       # Column with ID is the index
                       index_col='id',
                       #    Only pull the colums witht he ID and artist
                       usecols=columns_wanted)
    return data


csv_file_name = 'artwork_data.csv'
columns_wanted = ['id', 'artist', 'title', 'medium',
                  'year', 'acquisitionYear', 'height', 'width', 'units']
csv_data = read_in_csv(csv_file_name, columns_wanted)
print(csv_data.index)
print(csv_data)


def pickle_data(data_frame, file_name):
    data_frame.to_pickle(file_name)


pickle_data(csv_data, 'data_pickle.pickle')
