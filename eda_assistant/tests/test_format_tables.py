"""
Unit tests for _format_tables.py
"""

import unittest
import pandas as pd
import numpy as np
from eda_assistant import _format_tables

index_labels_df = _format_tables.df_summary_labels
index_labels_var = _format_tables.var_summary_labels
df_summary = pd.DataFrame([[16.123, 77, 1232, 0, 0.0, 0, 0.0, 13, 3]],
                          index=['Values'], columns=index_labels_df)
var_summary = pd.DataFrame([['object', np.nan, np.nan, np.nan, np.nan, np.nan,
                             np.nan, np.nan, np.nan, np.nan, np.nan,
                             0.123, 0.0, 77.4],
                            ['integer', 106.88123, 110.0, 8230.0, 379.63,
                             19.48, 100.0, 110.0, 50.0, 160.0, -0.45123,
                             0.123, 0.0, 11.123]],
                           index=['name', 'calories'],
                           columns=index_labels_var)


class TestFormatTables(unittest.TestCase):
    """
    Tests formatting summary statistics tables in _format_tables.py
    """

    def setUp(self):
        self.df_summary = df_summary
        self.var_summary = var_summary

    def test_format_df_summary(self):
        """
         Tests format_df_summary function. This function compares the results
         of a default created dataframe passed through the function to ensure
         specific values are correctly formatted as integers in the resulting
         dataframe.
         """
        formatted_df = _format_tables.format_df_summary(self.df_summary)
        self.assertTrue(type(formatted_df.
                             loc['No. of Columns', 'Values']) is int)

    def test_format_var_summary(self):
        """
        Tests format_var_summary function. This function compares the results
        of a default created dataframe passed through the function to ensure
        specific values are correctly formatted as integers, floats and NaNs.
        """
        formatted_var = _format_tables.format_var_summary(self.var_summary)
        self.assertTrue(type(formatted_var.loc['Min', 'calories']) is float)
        self.assertTrue(type(formatted_var.
                             loc['Count of NaNs', 'name']) is int)
        self.assertEqual(formatted_var.loc['Mean', 'name'], '-')
