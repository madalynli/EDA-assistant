"""
Unit tests for _create_tables.py
"""

import unittest
import os
import pandas as pd
from eda_assistant import _create_tables

TEST_DIR = 'test_create_tables_results'


class TestCreateTables(unittest.TestCase):
    """
    Tests creating summary statistics tables in _create_tables.py
    """

    def setUp(self):
        package_file_path = os.path.dirname(os.path.dirname(os.getcwd()))
        dataset_path_name = package_file_path + '/data/cereal.csv'
        self.df = pd.read_csv(dataset_path_name)

    def test_create_df_summary(self):
        """
        Tests create_df_summary function. This function compares the results
        of the cereal.csv dataset passed through the function to another csv
        file containing the correct format and values for the df summary table.
        """
        test_create_df_summary_file_name = \
            'test_create_df_summary_cereal_results.csv'
        test_data_df_summary = pd.read_csv(TEST_DIR + '/' +
                                           test_create_df_summary_file_name,
                                           index_col=0)
        comparison_df_summary = _create_tables.\
            create_df_summary(self.df).astype(str)
        pd.testing.assert_frame_equal(test_data_df_summary,
                                      comparison_df_summary, atol=0.1)

    def test_create_var_summary(self):
        """
        Tests create_var_summary function. This function compares the results
        of the cereal.csv dataset passed through the function to another csv
        file containing the correct format and values for the var summary
        table.
        """
        test_create_var_summary_file_name = \
            'test_create_var_summary_cereal_results.csv'
        test_data_var_summary = pd.read_csv(TEST_DIR + '/' +
                                            test_create_var_summary_file_name,
                                            index_col=0)
        comparison_var_summary = _create_tables.\
            create_var_summary(self.df).astype(str)
        pd.testing.assert_frame_equal(test_data_var_summary,
                                      comparison_var_summary,
                                      atol=0.1)
