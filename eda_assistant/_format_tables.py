"""
A python module that formats the summary table containing calculated summary
statistic values for the dataset and its variables. The module contains the
summary table labels and format standards for the data set summary statistics
table and the variable summary statistics table in _create_tables.py.
"""

df_summary_labels = ['No. of Columns', 'No. of Rows', 'Total Value Count',
                     'Count of NaNs', 'Percent of NaNs',
                     'Count of Duplicate Rows', 'Percent of Duplicate Rows',
                     'Count of Numerical Variables',
                     'Count of Categorical Variables']

var_summary_labels = ['Variable Type', 'Mean', 'Median', 'Sum', 'Variance',
                      'Standard Deviation', '25 Percentile', '75 Percentile',
                      'Min', 'Max', 'Skew', 'Count of NaNs', 'Percent of NaNs',
                      'Count of Unique Values']


def format_df_summary(df):
    """
    Returns a formatted dataframe for the dataset summary statistics
    table. Converts count values to integers and percentage values
    to a percent format.
        Parameters:
            df (pandas DataFrame): Dataframe to format for dataset summary
            statistics table
        Returns:
            formatted_df (pandas DataFrame): formatted dataset summary
            statistics table
    """
    df[['No. of Columns', 'No. of Rows', 'Total Value Count',
        'Count of NaNs', 'Count of Duplicate Rows',
        'Count of Numerical Variables', 'Count of Categorical Variables']] = \
        df[['No. of Columns', 'No. of Rows', 'Total Value Count',
            'Count of NaNs', 'Count of Duplicate Rows',
            'Count of Numerical Variables',
            'Count of Categorical Variables']].astype(int)

    df[['Percent of NaNs', 'Percent of Duplicate Rows']] = \
        df[['Percent of NaNs', 'Percent of Duplicate Rows']].astype(str) + '%'

    formatted_df = df.transpose()
    return formatted_df


def format_var_summary(df):
    """
    Returns a formatted dataframe for the variable summary statistics table.
    Rounds float values to 2 decimal places, converts count values to integers,
    changes percentage values to a percent format, and replaces NaNs in the
    table with '-' for categorical variables that do not apply to numeric
    calculations.
        Parameters:
            df (pandas DataFrame): Dataframe to format for variable summary
            statistics table
        Returns:
            formatted_var (pandas DataFrame): formatted variable summary
            statistics table
    """
    df[['Mean', 'Median', 'Sum', 'Variance', 'Standard Deviation',
        '25 Percentile', '75 Percentile', 'Min', 'Max', 'Skew']] = \
        df[['Mean', 'Median', 'Sum', 'Variance', 'Standard Deviation',
            '25 Percentile', '75 Percentile', 'Min', 'Max', 'Skew']].round(2)
    df[['Percent of NaNs']] = df[['Percent of NaNs']].astype(str) + '%'
    df[['Count of NaNs', 'Count of Unique Values']] = \
        df[['Count of NaNs', 'Count of Unique Values']].astype(int)
    df = df.fillna('-')
    formatted_var = df.transpose()
    return formatted_var
