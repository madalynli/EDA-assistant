"""
A python module containing an EDA class that can perform various EDA tasks
and techniques such as creating an EDA report pdf file with all standard
exploratory data analysis summary statistics and graphs.
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from eda_assistant import _create_tables
from eda_assistant import _create_graphs
from eda_assistant import _format_eda_report
import os
import webbrowser


class EDA:
    """
    A class representing an instance of EDA. This can be used to create
    an eda report.
    ...

        Attributes:
        ----------
            file_name: str
                File name of dataset to perform EDA on

        Methods:
        -------
            create_eda_report(save_file_name):
                Generates a pdf file containing eda summary statistic
                calculation tables and graphs for the dataset. Saves file
                as a pdf named save_file_name and opens the report
    """

    def __init__(self, file_path_name):
        """
        Constructs all necessary attributes for the EDA object.

            Parameters:
            ----------
                file_path_name : str
                    File path name of data set to perform EDA on
        """

        if not os.path.exists(file_path_name):
            raise Exception('Could not find file. File does not exist')
        else:
            df = pd.read_csv(file_path_name)
            self.df = df

    def create_eda_report(self, save_file_name):
        """
        Generates a pdf file containing eda summary statistic calculation
        tables and graphs for the dataset. Saves eda pdf file to current
        working directory named save_file_name. Opens file for user to
        preview information.
            Parameters:
                save_file_name (str): Name of file to save pdf report as.
                File name must end in '.pdf'
            Returns:
                None
        """
        if len(self.df) == 0:
            raise Exception('DataFrame is empty. Unable to create report.')
        else:
            with PdfPages(save_file_name) as pdf:
                df_summary = _create_tables.create_df_summary(self.df)
                df_summary_table = _format_eda_report.\
                    format_report_df_table(df_summary)
                pdf.savefig(df_summary_table, bbox_inches='tight',
                            pad_inches=2.5)
                plt.close()

                var_summary = _create_tables.create_var_summary(self.df)
                var_summary_table = _format_eda_report.\
                    format_report_var_table(var_summary)
                pdf.savefig(var_summary_table, bbox_inches='tight',
                            pad_inches=2)
                plt.close()

                numeric_hist = _create_graphs.plot_numeric_hist(self.df)
                if numeric_hist is not None:
                    pdf.savefig(numeric_hist, bbox_inches='tight',
                                pad_inches=2.5)
                    plt.close()

                categorical_bar = _create_graphs.plot_categorical_bar(self.df)
                if categorical_bar is not None:
                    pdf.savefig(categorical_bar, bbox_inches='tight',
                                pad_inches=2.5)
                    plt.close()

                corr_graph = _create_graphs.plot_corr_graph(self.df)
                if corr_graph is not None:
                    pdf.savefig(corr_graph, bbox_inches='tight',
                                pad_inches=1.5)
                    plt.close()

                pair_graph = _create_graphs.plot_pair_graph(self.df)
                if pair_graph is not None:
                    pdf.savefig(pair_graph, bbox_inches='tight',
                                pad_inches=1.5)
                    plt.close()

            save_file_location = os.getcwd() + '/' + save_file_name
            webbrowser.open_new(r'file://C:' + save_file_location)
