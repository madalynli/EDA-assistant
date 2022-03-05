"""
A python module that generates uni-variate and multi-variate analysis graphs for exploratory data
analysis. Specifically, the module contains functions to graph histograms for numeric data, bar
plots for categorical data, a correlation matrix heat map, and a pair plot. The graphs produced
are added into the final eda pdf report.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from eda_assistant import calc_dataframe_statistics
from eda_assistant import calc_variable_statistics
from eda_assistant import format_graphs


def plot_numeric_hist(df):
    """
    Returns histogram plot(s) for all numeric data in the data set. If there are no numeric variables,
    function will return None.
        Parameters:
            df (pandas DataFrame): Data frame to create histogram plot(s) for numeric variables in
            the data set
        Returns:
            fig (figure): figure containing histogram plot(s) for numeric variables in df
    """
    n = calc_dataframe_statistics.count_numeric(df)
    if n == 0:
        return None
    else:
        fig, ax = plt.subplots(n, 1, figsize=(10, n * 10))
        counter = 0
        for i in range(len(df.columns)):
            col = df.iloc[:, i]
            if calc_variable_statistics.is_numeric(col):
                if n == 1:
                    plot = sns.histplot(data=df, x=col.name)
                else:
                    plot = sns.histplot(data=df, x=col.name, ax=ax[counter])
                format_graphs.format_numeric(fig, plot, col)
                counter += 1
    return fig


def plot_categorical_bar(df):
    """
    Returns count bar plot(s) for all categorical data in the data set. Criteria for a categorical
    variable when graphing the bar plot is determined by a set_limit of unique values in the column
    which is defaulted to equal 10 because anything greater than this would result in a very compact,
    condensed, and messy figure displayed. Function returns None if there are no categorical variables.
        Parameters:
            df (pandas DataFrame): Data frame to create count bar plot(s) for categorical variables
            in data set
        Returns:
            fig (figure): figure containing count bar plot(s) for categorical variables in df
    """
    n = format_graphs.count_categorical_bar(df)
    if n == 0:
        return None
    else:
        fig, ax = plt.subplots(n, 1, figsize=(10, n * 10))
        counter = 0
        for i in range(len(df.columns)):
            col = df.iloc[:, i]
            if format_graphs.is_categorical_bar(col, set_limit=10):
                if n == 1:
                    plot = sns.countplot(data=df, x=col.name)
                else:
                    plot = sns.countplot(data=df, x=col.name, ax=ax[counter])
                format_graphs.format_categorical(fig, plot, col)
                counter += 1
    return fig


def plot_corr_graph(df):
    """
    Returns correlation matrix heat map plot for the data set. If data frame is empty, or if
    the number of numeric variables in the dataset is less than or equal to 1, the function
    returns None.
        Parameters:
            df (pandas DataFrame): Data frame to create correlation matrix heat map plot for the
            data set
        Returns:
            plot_corr (figure): figure containing correlation matrix heat map plot for df
    """
    if len(df) == 0 or calc_dataframe_statistics.count_numeric(df) <= 1:
        return None
    else:
        corr = df.corr()
        plot_corr = sns.heatmap(corr, annot=True, fmt='.0f')
        format_graphs.format_corr()
        return plot_corr.figure


def plot_pair_graph(df, set_limit=10):
    """
    Returns pair plots for the data set. If data frame is empty or if there are greater than
    the set_limit of numerical variables in the data set (processing time is too long), the
    function returns None.
        Parameters:
            df (pandas DataFrame): Data frame to create pair plots for the data set
            set_limit (int): the set limit for the number of numerical variables in a data set
        Returns:
            plot_pair (figure): figure containing pair plots for df
    """
    if len(df) == 0 \
            or calc_dataframe_statistics.count_numeric(df) >= set_limit \
            or calc_dataframe_statistics.count_numeric(df) <= 1:
        return None
    else:
        plot_pair = sns.pairplot(data=df)
        format_graphs.format_pair(plot_pair, df)
        return plot_pair.figure
