"""
Unit tests for _format_graphs.py
"""

import unittest
import os
import pandas as pd
from eda_assistant import _format_graphs


class TestFormatGraphs(unittest.TestCase):
    """
    Tests the categorical bar plot criteria functions in _format_graphs.py
    """

    def setUp(self):
        package_file_path = os.path.dirname(os.path.dirname(os.getcwd()))
        dataset_path_name = package_file_path + '/data/cereal.csv'
        self.df = pd.read_csv(dataset_path_name)

    def test_is_categorical_bar(self):
        """
        Tests is_categorical_bar function
        """
        self.assertFalse(_format_graphs.is_categorical_bar(self.df['name']))

    def test_count_categorical_bar(self):
        """
        Tests count_categorical_bar function
        """
        self.assertEqual(_format_graphs.count_categorical_bar(self.df), 2)
