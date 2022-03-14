"""
Unit tests for _calc_variable_statistics.py
"""

import unittest
import os
import pandas as pd
from eda_assistant import _calc_variable_statistics


class TestCalcVariableStatistics(unittest.TestCase):
    """
    Tests the variable summary statistic calculations in
    _calc_variable_statistics.py
    """

    def setUp(self):
        package_file_path = os.path.dirname(os.path.dirname(os.getcwd()))
        dataset_path_name = package_file_path + '/data/cereal.csv'
        self.df = pd.read_csv(dataset_path_name)

    def test_get_type(self):
        """
        Tests get_type function
        """
        self.assertEqual(_calc_variable_statistics.
                         get_type(self.df['name']), 'object')

    def test_is_numeric(self):
        """
        Tests is_numeric function
        """
        self.assertTrue(_calc_variable_statistics.
                        is_numeric(self.df['calories']))

    def test_get_mean(self):
        """
        Tests get_mean function
        """
        self.assertAlmostEqual(_calc_variable_statistics.
                               get_mean(self.df['calories']), 106.883116883)

    def test_get_median(self):
        """
        Tests get_median function
        """
        self.assertEqual(_calc_variable_statistics.
                         get_median(self.df['calories']), 110)

    def test_get_sum(self):
        """
        Tests get_sum function
        """
        self.assertEqual(_calc_variable_statistics.
                         get_sum(self.df['calories']), 8230)

    def test_get_var(self):
        """
        Tests get_var function
        """
        self.assertAlmostEqual(_calc_variable_statistics.
                               get_var(self.df['calories']), 379.6308954, 3)

    def test_get_std(self):
        """
        Tests get_std function
        """
        self.assertAlmostEqual(_calc_variable_statistics.
                               get_std(self.df['calories']), 19.4841190568)

    def test_get_q25(self):
        """
        Tests get_q25 function
        """
        self.assertEqual(_calc_variable_statistics.
                         get_q25(self.df['calories']), 100)

    def test_get_q75(self):
        """
        Tests get_q75 function
        """
        self.assertEqual(_calc_variable_statistics.
                         get_q75(self.df['calories']), 110)

    def test_get_min(self):
        """
        Tests get_min function
        """
        self.assertEqual(_calc_variable_statistics.
                         get_min(self.df['calories']), 50)

    def test_get_max(self):
        """
        Tests get_max function
        """
        self.assertEqual(_calc_variable_statistics.
                         get_max(self.df['calories']), 160)

    def test_get_skew(self):
        """
        Tests get_skew function
        """
        self.assertAlmostEqual(_calc_variable_statistics.
                               get_skew(self.df['calories']), -0.4454067, 3)

    def test_count_col_nans(self):
        """
        Tests count_col_nans function
        """
        self.assertEqual(_calc_variable_statistics.
                         count_col_nans(self.df['calories']), 0)

    def test_perc_col_nans(self):
        """
        Tests perc_col_nans function
        """
        self.assertEqual(_calc_variable_statistics.
                         perc_col_nans(self.df['calories']), 0)

    def test_count_unique(self):
        """
        Tests count_unique function
        """
        self.assertEqual(_calc_variable_statistics.
                         count_unique(self.df['calories']), 11)
