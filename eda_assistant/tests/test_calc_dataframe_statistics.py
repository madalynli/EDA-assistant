"""
Unit tests for _calc_dataframe_statistics.py
"""

import unittest
import os
import pandas as pd
from eda_assistant import _calc_dataframe_statistics


class TestCalcDataFrameStatistics(unittest.TestCase):
    """
    Tests the dataframe summary statistic calculations in
    _calc_dataframe_statistics.py
    """

    def setUp(self):
        package_file_path = os.path.dirname(os.path.dirname(os.getcwd()))
        dataset_path_name = package_file_path + '/data/cereal.csv'
        self.df = pd.read_csv(dataset_path_name)

    def test_count_cols(self):
        """
        Tests count_cols function
        """
        self.assertEqual(_calc_dataframe_statistics.
                         count_cols(self.df), 16)

    def test_count_rows(self):
        """
        Tests count_rows function
        """
        self.assertEqual(_calc_dataframe_statistics.
                         count_rows(self.df), 77)

    def test_count_total_values(self):
        """
        Tests count_total_values function
        """
        self.assertEqual(_calc_dataframe_statistics.
                         count_total_values(self.df), 1232)

    def test_count_nans(self):
        """
        Tests count_total_nans function
        """
        self.assertEqual(_calc_dataframe_statistics.
                         count_nans(self.df), 0)

    def test_percent_total_nans(self):
        """
        Tests percent_total_nans function
        """
        self.assertEqual(_calc_dataframe_statistics.
                         percent_total_nans(self.df), 0)

    def test_count_duplicate_rows(self):
        """
        Tests count_duplicate_rows function
        """
        self.assertEqual(_calc_dataframe_statistics.
                         count_duplicate_rows(self.df), 0)

    def test_percent_duplicate_rows(self):
        """
        Tests percent_duplicate_rows function
        """
        self.assertEqual(_calc_dataframe_statistics.
                         percent_duplicate_rows(self.df), 0)

    def test_count_numeric(self):
        """
        Tests count_numeric function
        """
        self.assertEqual(_calc_dataframe_statistics.
                         count_numeric(self.df), 13)

    def test_count_categorical(self):
        """
        Tests count_count_categorical function
        """
        self.assertEqual(_calc_dataframe_statistics.
                         count_categorical(self.df), 3)
