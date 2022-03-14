"""
A python module that calculates all summary statistics for variables within the
dataset. This is used to create the variable summary statistics table in the
final eda pdf report.
"""


def get_type(col):
    """
    Returns the data type of the column in the dataset.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_type (string): Name of data type in col. Returns other if not
            an integer, object, or float
    """
    if col.dtype.name == 'int64':
        col_type = 'integer'
    elif col.dtype.name == 'float64':
        col_type = 'float'
    elif col.dtype.name == 'object':
        col_type = 'object'
    else:
        col_type = 'other'
    return col_type


def is_numeric(col):
    """
    Returns the boolean value of whether a specific column in the dataset
    is numeric.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            True if col is numeric and False otherwise
    """
    if get_type(col) == 'integer' or get_type(col) == 'float':
        return True
    else:
        return False


def get_mean(col):
    """
    Returns the mean of a specific column in the dataset if it is numeric.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_mean (float): Mean of col
    """
    if is_numeric(col):
        col_mean = col.mean()
    else:
        col_mean = None
    return col_mean


def get_median(col):
    """
    Returns the median of a specific column in the dataset if it is numeric.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_median (float): Median of col
    """
    if is_numeric(col):
        col_median = col.median()
    else:
        col_median = None
    return col_median


def get_sum(col):
    """
    Returns the sum of a specific column in the dataset if it is numeric.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_sum (float): Sum of col
    """
    if is_numeric(col):
        col_sum = col.sum()
    else:
        col_sum = None
    return col_sum


def get_var(col):
    """
    Returns the variance of a specific column in the data set if it is numeric.
        Parameters:
            col (pandas Series): Column in the data set
        Returns:
            col_var (float): Variance of col
    """
    if is_numeric(col):
        col_var = col.var()
    else:
        col_var = None
    return col_var


def get_std(col):
    """
    Returns the standard deviation of a specific column in the dataset if it
    is numeric.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_std (float): Standard deviation of col
    """
    if is_numeric(col):
        col_std = col.std()
    else:
        col_std = None
    return col_std


def get_q25(col):
    """
    Returns the 25th percentile of a specific column in the dataset if it
    is numeric.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_q25 (float): 25th percentile of col
    """
    if is_numeric(col):
        col_q25 = col.quantile(q=0.25)
    else:
        col_q25 = None
    return col_q25


def get_q75(col):
    """
    Returns the 75th percentile of a specific column in the dataset if it
    is numeric.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_q75 (float): 75th percentile of col
    """
    if is_numeric(col):
        col_q75 = col.quantile(q=0.75)
    else:
        col_q75 = None
    return col_q75


def get_min(col):
    """
    Returns the minimum value of a specific column in the dataset if it
    is numeric.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_min (float): Min of col
    """
    if is_numeric(col):
        col_min = col.min()
    else:
        col_min = None
    return col_min


def get_max(col):
    """
    Returns the maximum value of a specific column in the dataset if it
    is numeric.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_max (float): Max of col
    """
    if is_numeric(col):
        col_max = col.max()
    else:
        col_max = None
    return col_max


def get_skew(col):
    """
    Returns the skew of a specific column in the dataset if it is numeric.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_skew (float): Skew of col
    """
    if is_numeric(col):
        col_skew = col.skew()
    else:
        col_skew = None
    return col_skew


def count_col_nans(col):
    """
    Returns the number of NaNs of a specific column in the dataset.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_count_nans (float): Count of NaNs in col
    """
    col_count_nans = col.isna().sum()
    return col_count_nans


def perc_col_nans(col):
    """
    Returns the percent of NaNs of a specific column in the dataset.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_perc_nans (float): Percent of NaNs in col
    """
    col_perc_nans = count_col_nans(col) / len(col)
    return col_perc_nans


def count_unique(col):
    """
    Returns the number of unique values of a specific column in the dataset.
        Parameters:
            col (pandas Series): Column in the dataset
        Returns:
            col_count_unique (float): Count of unique values in col
    """
    col_count_unique = len(col.unique())
    return col_count_unique
