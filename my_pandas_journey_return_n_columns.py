# TASK: Create a function which receives a pandas dataframe and nth column as parameters. Return all the columns until nth column from that dataframe.
import pandas as pd
def my_pandas_journey_return_n_columns(df,nth_column):
    return df.iloc[:,:nth_column]
