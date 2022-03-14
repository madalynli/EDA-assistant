"""
Unit tests for eda_assistant.py
"""

import unittest
import os
import pathlib as pl
from eda_assistant import eda_assistant


class TestEDAAssistant(unittest.TestCase):
    """
    Tests the EDA class construction and create_eda_report method
    within the eda_assistant module.
    """

    def setUp(self):
        package_file_path = os.path.dirname(os.path.dirname(os.getcwd()))
        dataset_path_name = package_file_path + '/data/cereal.csv'
        self.df_path_name = dataset_path_name

    def tearDown(self):
        try:
            test_report_path_name = os.getcwd() + '/test_cereal_eda_report.pdf'
            os.remove(test_report_path_name)
        except OSError as error:
            print(error)

    def test_create_eda_report(self):
        """
        Tests create_eda_report method in EDA class
        """
        # if not os.path.exists(self.df_path_name):
        #    self.assertRaises(eda_assistant.EDA(self.df_path_name), Exception)
        eda_object = eda_assistant.EDA(self.df_path_name)
        eda_object.create_eda_report('test_cereal_eda_report.pdf')
        path = pl.Path(os.getcwd() + '/test_cereal_eda_report.pdf')
        self.assertEqual(path.is_file(), True)
