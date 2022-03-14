"""
A python module that formats the eda pdf report file. The module contains
functions that format the summary statistics tables to fit nicely into
the pdf file.
"""

import matplotlib.pyplot as plt


def format_report_df_table(df):
    """
    Returns a formatted table figure for the eda pdf file on the dataset
    summary statistics table.
        Parameters:
            df (pandas DataFrame): Dataframe of the dataset summary
            statistics calculations table
        Returns:
            fig (figure): formatted table figure of df for the eda pdf file
    """
    fig, ax = plt.subplots()
    ax.set_axis_off()
    table_figure = ax.table(cellText=df.values,
                            rowLabels=list(df.index),
                            colLabels=list(df.columns),
                            cellLoc='center',
                            loc='center')
    ax.set_title('Data Set Summary Statistics:', weight='bold', size=30,
                 color='k', x=0, y=1.9)
    table_figure.set_fontsize(20)
    table_figure.scale(3, 4)
    table_figure.auto_set_column_width(col=(list(range(len(df.columns)))))
    return fig


def format_report_var_table(df):
    """
    Returns a formatted table figure for the eda pdf file on the variable
    summary statistics table.
        Parameters:
            df (pandas DataFrame): Dataframe of the variable summary
            statistics calculations table
        Returns:
            fig (figure): formatted table figure of df for the eda pdf file
    """
    fig, ax = plt.subplots()
    ax.set_axis_off()
    table_figure = ax.table(cellText=df.values,
                            rowLabels=list(df.index),
                            colLabels=list(df.columns),
                            cellLoc='center',
                            loc='center')
    ax.set_title('Variable Summary Statistics:', weight='bold', size=30,
                 color='k', x=0, y=2.5)
    table_figure.set_fontsize(20)
    table_figure.scale(3, 4)
    table_figure.auto_set_column_width(col=(list(range(len(df.columns)))))
    return fig
