"""
A python module that formats the uni-variate and bi-variate graphs for
the dataset. This module contains the format standards for the histogram
plot(s) on numerical data, the format standards for count bar plot(s) on
categorical data, the set criteria for graphing the count bar plot(s) for
categorical data in _create_graphs.py, the format standards for the correlation
matrix heat map plot, and the format standards for the scatter pair plot.

The reason for setting a limit on the categorical data criteria for graphing
count bar plot(s) is because we want to limit the number of variables that are
plotted onto the bar graph to avoid a compact, condensed, and messy figure
displayed on the report. The number of unique variables for the categorical
data criteria is default set to less than or equal to 10.
"""

import matplotlib.pyplot as plt
from eda_assistant import _calc_dataframe_statistics
from eda_assistant import _calc_variable_statistics


def format_numeric(fig, plot, col):
    """
    Returns a formatted histogram plot for numeric data in the dataset.
        Parameters:
            fig: figure to be formatted
            plot: plot to be formatted
            col (pandas Series): Numeric variable column in df to plot
            histogram for
        Returns:
            plot (figure): formatted histogram plot for numeric variable col
    """
    fig.suptitle('Numerical Histogram Plot(s):', weight='bold', size=30,
                 color='k', x=0.5, y=0.965)
    plot = plot.set(title='Count of {}'.format(col.name))
    return plot


def is_categorical_bar(col, set_limit=10):
    """
    Returns the boolean value of whether the specific variable column in the
    dataset is categorical and if the number of unique values in the column
    is less than the set_limit value (default of 10).
        Parameters:
            col: Column in the dataset
            set_limit (int): set limit for number of unique values in a
            categorical variable column. Default is set to 10.
        Returns:
            True if variable column is categorical and if the number of unique
            values in it is less than set_limit and False otherwise
    """
    if _calc_variable_statistics.get_type(col) == 'object' and \
            _calc_variable_statistics.count_unique(col) <= set_limit:
        return True
    else:
        return False


def count_categorical_bar(df):
    """
    Returns the number of categorical variables in the dataset based on the
    criteria that the number of unique values in the categorical column is
    less than set_limit which is default set to 10 and determined by the
    is_categorical_bar function.
        Parameters:
            df (pandas DataFrame): Dataset to perform calculation on
        Returns:
            counter_categorical_hist (int): number of categorical variable
            columns in the data set that also have a number of unique values
            less than the set_limit
    """
    counter_categorical_hist = 0
    for i in range(len(df.columns)):
        col = df.iloc[:, i]
        if is_categorical_bar(col):
            counter_categorical_hist += 1
    return counter_categorical_hist


def format_categorical(fig, plot, col):
    """
    Returns a formatted bar count plot for categorical data in the dataset.
        Parameters:
            fig: figure to be formatted
            plot: plot to be formatted
            col (pandas Series): Categorical variable column in df to plot
            histogram for
        Returns:
            plot (figure): formatted count bar plot for categorical
            variable col
    """
    fig.suptitle('Categorical Histogram Plot(s):', weight='bold', size=30,
                 color='k', x=0.5, y=0.935)
    plot = plot.set(title='Count of {}'.format(col.name))
    return plot


def format_corr():
    """
    Returns a formatted correlation matrix heat map plot for numeric data in
    the dataset.
        Returns:
            plot_corr: formatted correlation matrix heat map plot
    """
    plot_corr = plt.title('Correlation Matrix Heat Map:', fontsize=30,
                          weight='bold', color='k', x=0.5, y=1.1)
    return plot_corr


def format_pair(plot_pair, df):
    """
    Returns a formatted pair plot for numeric data in the data set.
        Parameters:
            plot_pair: pair plot figure to be formatted
            df (pandas DataFrame): Dataset used to create pair plot
        Returns:
            plot_pair: formatted pair plot figure
    """
    for axes in plot_pair.axes.flat:
        axes.set_ylabel(axes.get_ylabel(), rotation=0,
                        horizontalalignment='right')
        axes.set_xlabel(axes.get_xlabel(), rotation=90,
                        horizontalalignment='right')
    plot_pair = plt.title('Pair Plots:', fontsize=30, weight='bold',
                          color='k',
                          x=-1*_calc_dataframe_statistics.count_numeric(df)/2,
                          y=_calc_dataframe_statistics.count_numeric(df)*1.1)
    return plot_pair.figure
