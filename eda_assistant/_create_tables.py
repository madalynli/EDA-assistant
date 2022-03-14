"""
A python module that generates formatted and consolidated summary tables
containing calculated summary statistic values for the dataset. The
module uses summary statistics calculated from _calc_dataframe_statistics.py
and _calc_variable_statistics.py. The tables produced are added into the final
eda pdf report.
"""

import pandas as pd
from eda_assistant import _calc_dataframe_statistics
from eda_assistant import _calc_variable_statistics
from eda_assistant import _format_tables


def create_df_summary(df):
    """
    Returns a formatted dataframe containing summary statistics values for the
    entire dataset.
        Parameters:
            df (pandas DataFrame): Dataframe to create dataset summary
            statistics table for
        Returns:
            df_summary_formatted (pandas DataFrame): dataframe of formatted
            dataset summary statistics table
    """
    summary_stats = [[_calc_dataframe_statistics.count_cols(df),
                      _calc_dataframe_statistics.count_rows(df),
                      _calc_dataframe_statistics.count_total_values(df),
                      _calc_dataframe_statistics.count_nans(df),
                      _calc_dataframe_statistics.percent_total_nans(df),
                      _calc_dataframe_statistics.count_duplicate_rows(df),
                      _calc_dataframe_statistics.percent_duplicate_rows(df),
                      _calc_dataframe_statistics.count_numeric(df),
                      _calc_dataframe_statistics.count_categorical(df)]]
    df_summary = pd.DataFrame(summary_stats,
                              columns=_format_tables.df_summary_labels,
                              index=['Values'])
    df_summary_formatted = _format_tables.format_df_summary(df_summary)
    return df_summary_formatted


def create_var_summary(df):
    """
    Returns a formatted dataframe containing summary statistics values for the
    variables of the dataset.
        Parameters:
            df (pandas DataFrame): Dataframe to create variable summary
            statistics table for
        Returns:
            var_summary_formatted (pandas DataFrame): dataframe of formatted
            variable summary statistics table
    """
    summary_stats = []
    var_summary_headers = df.columns

    for i in range(len(df.columns)):
        col = df.iloc[:, i]
        summary_stats.append([_calc_variable_statistics.get_type(col),
                              _calc_variable_statistics.get_mean(col),
                              _calc_variable_statistics.get_median(col),
                              _calc_variable_statistics.get_sum(col),
                              _calc_variable_statistics.get_var(col),
                              _calc_variable_statistics.get_std(col),
                              _calc_variable_statistics.get_q25(col),
                              _calc_variable_statistics.get_q75(col),
                              _calc_variable_statistics.get_min(col),
                              _calc_variable_statistics.get_max(col),
                              _calc_variable_statistics.get_skew(col),
                              _calc_variable_statistics.count_col_nans(col),
                              _calc_variable_statistics.perc_col_nans(col),
                              _calc_variable_statistics.count_unique(col)])
    var_summary = pd.DataFrame(summary_stats,
                               columns=_format_tables.var_summary_labels,
                               index=var_summary_headers)
    var_summary_formatted = _format_tables.format_var_summary(var_summary)
    return var_summary_formatted
