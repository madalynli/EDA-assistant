"""
A python module that generates uni-variate and bi-variate analysis graphs for
exploratory data analysis. Specifically, the module contains functions to
graph histograms for numeric data, bar plots for categorical data, a
correlation matrix heat map, and a scatter pair plot. The graphs produced
are added into the final eda pdf report.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from eda_assistant import _calc_dataframe_statistics
from eda_assistant import _calc_variable_statistics
from eda_assistant import _format_graphs


def plot_numeric_hist(df):
    """
    Returns histogram plot(s) for all numeric data in the dataset. If there
    are no numeric variables, function will return None.
        Parameters:
            df (pandas DataFrame): Dataframe to create histogram plot(s) for
            numeric variables in the dataset
        Returns:
            fig (figure): figure containing histogram plot(s) for numeric
            variables in df
    """
    n = _calc_dataframe_statistics.count_numeric(df)
    if n == 0:
        return None
    else:
        fig, ax = plt.subplots(n, 1, figsize=(10, n * 10))
        counter = 0
        for i in range(len(df.columns)):
            col = df.iloc[:, i]
            if _calc_variable_statistics.is_numeric(col):
                if n == 1:
                    plot = sns.histplot(data=df, x=col.name)
                else:
                    plot = sns.histplot(data=df, x=col.name, ax=ax[counter])
                _format_graphs.format_numeric(fig, plot, col)
                counter += 1
    return fig


def plot_categorical_bar(df, set_limit=10):
    """
    Returns count bar plot(s) for all categorical data in the dataset. Criteria
    for a categorical variable when graphing the bar plot is determined by a
    set_limit of unique values in the column which is default set to 10 because
    anything greater than this would result in a very compact, condensed, and
    messy figure displayed. Function returns None if there are no categorical
    variables.
        Parameters:
            df (pandas DataFrame): Dataframe to create count bar plot(s) for
            categorical variables in dataset
            set_limit (int): set limit for number of unique values in a
            categorical variable column. Default is set to 10
        Returns:
            fig (figure): figure containing count bar plot(s) for categorical
            variables in df
    """
    n = _format_graphs.count_categorical_bar(df)
    if n == 0:
        return None
    else:
        fig, ax = plt.subplots(n, 1, figsize=(10, n * 10))
        counter = 0
        for i in range(len(df.columns)):
            col = df.iloc[:, i]
            if _format_graphs.is_categorical_bar(col, set_limit=set_limit):
                if n == 1:
                    plot = sns.countplot(data=df, x=col.name)
                else:
                    plot = sns.countplot(data=df, x=col.name, ax=ax[counter])
                _format_graphs.format_categorical(fig, plot, col)
                counter += 1
    return fig


def plot_corr_graph(df):
    """
    Returns correlation matrix heat map plot for the dataset. If dataframe is
    empty, or if the number of numeric variables in the dataset is less than
    or equal to 1, the function returns None.
        Parameters:
            df (pandas DataFrame): Dataframe to create correlation matrix heat
            map plot for the dataset
        Returns:
            plot_corr (figure): figure containing correlation matrix heat map
            plot for df
    """
    if len(df) == 0 or _calc_dataframe_statistics.count_numeric(df) <= 1:
        return None
    else:
        corr = df.corr()
        plot_corr = sns.heatmap(corr, annot=True, fmt='.0f')
        _format_graphs.format_corr()
        return plot_corr.figure


def plot_pair_graph(df, set_limit=10):
    """
    Returns scatter pair plots for the dataset. If dataframe is empty, or if
    there are greater than the set_limit of numerical variables in the dataset
    (processing time is too long for this instance), or if the number of
    numeric variables in the dataset is less than or equal to 1, the function
    returns None.
        Parameters:
            df (pandas DataFrame): Dataframe to create pair plots
            for the dataset
            set_limit (int): the set limit for the number of numeric
            variables in a dataset. Default is set to 10
        Returns:
            plot_pair (figure): figure containing pair plots for df
    """
    if len(df) == 0 \
            or _calc_dataframe_statistics.count_numeric(df) >= set_limit \
            or _calc_dataframe_statistics.count_numeric(df) <= 1:
        return None
    else:
        plot_pair = sns.pairplot(data=df)
        _format_graphs.format_pair(plot_pair, df)
        return plot_pair.figure
