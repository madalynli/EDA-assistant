"""
Unit tests for calc_dataframe_statistics.py
"""

import unittest
import pandas as pd
from eda_assistant import calc_dataframe_statistics


class TestCalcDataFrameStatistics(unittest.TestCase):
    """
    Tests the dataframe summary statistic calculations in calc_dataframe_statistics.py
    """

    def setUp(self):
        self.df = pd.read_csv('test_example_datasets/cereal.csv')

    def tearDown(self):
        self.df = None

    def test_count_cols(self):
        """
        Tests count_cols function
        """
        self.assertEqual(calc_dataframe_statistics.count_cols(self.df), 16)

    def test_count_rows(self):
        """
        Tests count_rows function
        """
        self.assertEqual(calc_dataframe_statistics.count_rows(self.df), 77)

    def test_count_total_values(self):
        """
        Tests count_total_values function
        """
        self.assertEqual(calc_dataframe_statistics.count_total_values(self.df), 1232)

    def test_count_nans(self):
        """
        Tests count_total_nans function
        """
        self.assertEqual(calc_dataframe_statistics.count_nans(self.df), 0)

    def test_percent_total_nans(self):
        """
        Tests percent_total_nans function
        """
        self.assertEqual(calc_dataframe_statistics.percent_total_nans(self.df), 0)

    def test_count_duplicate_rows(self):
        """
        Tests count_duplicate_rows function
        """
        self.assertEqual(calc_dataframe_statistics.count_duplicate_rows(self.df), 0)

    def test_percent_duplicate_rows(self):
        """
        Tests percent_duplicate_rows function
        """
        self.assertEqual(calc_dataframe_statistics.percent_duplicate_rows(self.df), 0)

    def test_count_numeric(self):
        """
        Tests count_numeric function
        """
        self.assertEqual(calc_dataframe_statistics.count_numeric(self.df), 13)

    def test_count_categorical(self):
        """
        Tests count_count_categorical function
        """
        self.assertEqual(calc_dataframe_statistics.count_categorical(self.df), 3)
