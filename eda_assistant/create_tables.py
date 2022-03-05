"""
A python module that generates formatted and consolidated summary tables containing calculated
summary statistic values for the data set. The module uses summary statistics calculated from
calc_dataframe_statistics.py and calc_variable_statistics.py. The tables produced are added into
the final eda pdf report.
"""

import pandas as pd
from eda_assistant import calc_dataframe_statistics
from eda_assistant import calc_variable_statistics
from eda_assistant import format_tables


def create_df_summary(df):
    """
    Returns a formatted data frame containing summary statistics values for the entire data set.
        Parameters:
            df (pandas DataFrame): Data frame to create data set summary statistics table for
        Returns:
            df_summary_formatted (pandas DataFrame): data frame of formatted data set summary statistics table
    """
    summary_stats = [[calc_dataframe_statistics.count_cols(df),
                      calc_dataframe_statistics.count_rows(df),
                      calc_dataframe_statistics.count_total_values(df),
                      calc_dataframe_statistics.count_nans(df),
                      calc_dataframe_statistics.percent_total_nans(df),
                      calc_dataframe_statistics.count_duplicate_rows(df),
                      calc_dataframe_statistics.percent_duplicate_rows(df),
                      calc_dataframe_statistics.count_numeric(df),
                      calc_dataframe_statistics.count_categorical(df)]]
    df_summary = pd.DataFrame(summary_stats, columns=format_tables.df_summary_labels, index=['Values'])
    df_summary_formatted = format_tables.format_df_summary(df_summary)
    return df_summary_formatted


def create_var_summary(df):
    """
    Returns a formatted data frame containing summary statistics values for the variables of the data set.
        Parameters:
            df (pandas DataFrame): Data frame to create variable summary statistics table for
        Returns:
            var_summary_formatted (pandas DataFrame): data frame of formatted variable summary statistics table
    """
    summary_stats = []
    var_summary_headers = df.columns

    for i in range(len(df.columns)):
        col = df.iloc[:, i]
        summary_stats.append([calc_variable_statistics.get_type(col),
                              calc_variable_statistics.get_mean(col),
                              calc_variable_statistics.get_median(col),
                              calc_variable_statistics.get_sum(col),
                              calc_variable_statistics.get_var(col),
                              calc_variable_statistics.get_std(col),
                              calc_variable_statistics.get_q25(col),
                              calc_variable_statistics.get_q75(col),
                              calc_variable_statistics.get_min(col),
                              calc_variable_statistics.get_max(col),
                              calc_variable_statistics.get_skew(col),
                              calc_variable_statistics.count_col_nans(col),
                              calc_variable_statistics.perc_col_nans(col),
                              calc_variable_statistics.count_unique(col)])
    var_summary = pd.DataFrame(summary_stats, columns=format_tables.var_summary_labels, index=var_summary_headers)
    var_summary_formatted = format_tables.format_var_summary(var_summary)
    return var_summary_formatted
