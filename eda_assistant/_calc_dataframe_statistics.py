"""
A python module that calculates all summary statistics for the overall dataset.
This is used to create the dataframe summary statistics table in the final eda
pdf report.
"""


def count_cols(df):
    """
    Returns the number of columns in the dataset.
        Parameters:
            df (pandas DataFrame): Dataset to perform calculation on
        Returns:
            num_cols (int): Number of columns in df
    """
    num_cols = len(df.columns)
    return num_cols


def count_rows(df):
    """
    Returns the number of rows in the dataset.
        Parameters:
            df (pandas DataFrame): Dataset to perform calculation on
        Returns:
            num_rows (int): Number of rows in df
    """
    num_rows = len(df)
    return num_rows


def count_total_values(df):
    """
    Returns the total number of values in the dataset. Includes NaNs.
        Parameters:
            df (pandas DataFrame): Dataset to perform calculation on
        Returns:
            num_vals (int): Number of total values in df
    """
    num_vals = count_cols(df) * count_rows(df)
    return num_vals


def count_nans(df):
    """
    Returns the number of NaN values in the dataset.
        Parameters:
            df (pandas DataFrame): Dataset to perform calculation on
        Returns:
            num_nans (int): Number of NaN values in df
    """
    num_nans = df.isnull().sum().sum()
    return num_nans


def percent_total_nans(df):
    """
    Returns the percent of NaN values in the dataset.
        Parameters:
            df (pandas DataFrame): Dataset to perform calculation on
        Returns:
            perc_nans (float): Percent of NaN values in df
    """
    perc_nans = round(count_nans(df) / count_total_values(df) * 100, 2)
    return perc_nans


def count_duplicate_rows(df):
    """
    Returns the number of duplicate rows in the dataset.
        Parameters:
            df (pandas DataFrame): Dataset to perform calculation on
        Returns:
            num_duplicate (int): Number of duplicate rows in df
    """
    num_duplicates = df.duplicated().sum()
    return num_duplicates


def percent_duplicate_rows(df):
    """
    Returns the percent of duplicate rows in the dataset.
        Parameters:
            df (pandas DataFrame): Dataset to perform calculation on
        Returns:
            perc_duplicates (float): Percent of duplicate rows in df
    """
    perc_duplicates = round(count_duplicate_rows(df) /
                            count_total_values(df) * 100, 2)
    return perc_duplicates


def count_numeric(df):
    """
    Returns the number of numeric variables in the dataset.
        Parameters:
            df (pandas DataFrame): Dataset to perform calculation on
        Returns:
            counter_numeric (int): Number of numeric variables in df
    """
    counter_numeric = 0
    for i in range(len(df.columns)):
        col = df.iloc[:, i]
        if col.dtype.name == 'int64' or col.dtype.name == 'float64':
            counter_numeric += 1
    return counter_numeric


def count_categorical(df):
    """
    Returns the number of categorical variables in the dataset.
        Parameters:
            df (pandas DataFrame): Dataset to perform calculation on
        Returns:
            counter_categorical (int): Number of categorical variables in df
    """
    counter_categorical = 0
    for i in range(len(df.columns)):
        col = df.iloc[:, i]
        if col.dtype.name == 'object':
            counter_categorical += 1
    return counter_categorical
