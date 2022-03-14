# EDA-assistant
## Background
The goal of this project is to help data scientists or data analysts perform easy and 
quick exploratory data analysis in Python. With the current process for EDA in Python 
involving importing many packages and writing multiple lines of code, the EDA-assistant 
package makes this process more simple for the end user with just a single import and 
two lines of code to produce a PDF report containing all standard EDA summary statistics 
and graphs. Specifically, the EDA PDF report produced currently contains tables for 
dataset and variable summary statistics calculations, bar graphs for visualizing data 
distribution, a correlation matrix heat map plot, and a scatter pair plot. 

## Data
The datasets used in this repository for testing and demonstration are listed 
along with their sources below:

1. Iris Flower Dataset<br>
   - **File Name:** [IRIS.csv](https://github.com/madalynli/EDA-assistant/blob/master/data/IRIS.csv) <br>
   - **Source:** [Kaggle Iris Flower Dataset](https://www.kaggle.com/arshid/iris-flower-dataset) <br>
   - **Purpose:** This file is used for the [demonstration](https://github.com/madalynli/EDA-assistant/blob/master/examples/demo_EDA_assistant.ipynb) of the package <br>
2. Wine Quality Dataset
   - **File Name:** [WineQT.csv](https://github.com/madalynli/EDA-assistant/blob/master/data/WineQT.csv) <br>
   - **Source:** [Kaggle Wine Quality Dataset](https://www.kaggle.com/beerhan/wine-quality/data) <br>
   - **Purpose:** This file is used for the [demonstration](https://github.com/madalynli/EDA-assistant/blob/master/examples/demo_EDA_assistant.ipynb) of the package <br>
3. Cereal Dataset 
   - **File Name:** [cereal.csv](https://github.com/madalynli/EDA-assistant/blob/master/data/cereal.csv) <br>
   - **Source:** [Kaggle 80 Cereals Dataset](https://www.kaggle.com/crawford/80-cereals) <br>
   - **Purpose:** This file is used for the [test code](https://github.com/madalynli/EDA-assistant/tree/master/eda_assistant/tests) in the package

## Software

**Programming Language(s):** <br>
[Python](https://www.python.org/)

**Python Packages:** <br>
cycler==0.11.0 <br>
fonttools==4.29.1 <br>
kiwisolver==1.3.2 <br>
matplotlib==3.5.1 <br>
numpy==1.22.2 <br>
packaging==21.3 <br>
pandas==1.4.1 <br>
Pillow==9.0.1 <br>
pyparsing==3.0.7 <br>
python-dateutil==2.8.2 <br>
pytz==2021.3 <br>
scipy==1.8.0 <br>
seaborn==0.11.2 <br>
six==1.16.0 <br>

## Package Structure
```
EDA-assistant/
  |- eda_assistant/
    |- __init__.py
    |- _calc_dataframe_statistics.py
    |- _calc_variable_statistics.py
    |- _create_graphs.py
    |- _create_tables.py
    |- _format_eda_report.py
    |- _format_graphs.py
    |- _format_tables.py
    |- eda_eassistant.py
    |- tests/
      |- __init__.py
      |- test_calc_dataframe_statistics.py
      |- test_calc_variable_statistics.py
      |- test_create_tables.py
      |- test_eda_assistant.py
      |- test_format_graphs.py
      |- test_format_tables.py
      |- test_create_tables_results/
        |- test_create_df_summary_cereal_results.csv
        |- test_create_var_summary_cereal_results.csv
  |- data/
    |- IRIS.csv
    |- WineQT.csv
    |- cereal.csv
  |- docs/
    |- EDA_assistant_final_presentation.pdf
    |- EDA_assistant_written_report.pdf
  |- examples/
    |- demo_EDA_assistant.ipynb
    |- demo_iris_eda_report.pdf
    |- demo_iris_eda_report_cat_hist.png
    |- demo_iris_eda_report_corr.png
    |- demo_iris_eda_report_df_table.png
    |- demo_iris_eda_report_num_hist.png
    |- demo_iris_eda_report_pair.png
    |- demo_iris_eda_report_var_table.png
    |- demo_wine_eda_report.pdf
  |- LICENSE
  |- README.md
  |- requirements.txt
  |- setup.py
```

## Installation
To install this package, simply enter the following command: 
```
pip install EDA-assistant
```

## Assumptions and Dependencies
- Dataset file to create an EDA class must be in a .csv file format
- The variable types in the dataset are determined with Panda’s dtype function, which may not always identify the correct variable type 100% of the time 
- The categorical bar plots in the EDA report will not be plotted unless the number of unique variables in the categorical column is less than or equal to 10. This is because as the number of bars surpass 10, the bar plot becomes more compressed and thus harder to read 
- The scatter pair plot in the EDA report will not be plotted unless the number of numeric variables in the dataset is less than or equal to 10. This is because as the number of variables surpass 10, the processing time for the plot takes much longer to produce 
- The PDF format of the EDA report may vary widely; the title of the pages may sometimes overlap the title of the graphs or have a large white-space gap between them


## Usage
To see how to use the package to create the EDA report, refer to the [example notebook](https://github.com/madalynli/EDA-assistant/blob/master/examples/demo_EDA_assistant.ipynb)

## Output Preview
Below contains some screenshots for the sample output of the EDA report created with this package. 
These tables and graphs seen below are associated with the data set IRIS.csv (source listed above):
![Data Set Summary Statistics](https://github.com/madalynli/EDA-assistant/blob/master/examples/demo_iris_eda_report_df_table.png?raw=true)
![Variable Summary Statistics](https://github.com/madalynli/EDA-assistant/blob/master/examples/demo_iris_eda_report_var_table.png?raw=true)
![Numerical Histogram Plots](https://github.com/madalynli/EDA-assistant/blob/master/examples/demo_iris_eda_report_num_hist.png?raw=true)
![Categorical Histogram Plots](https://github.com/madalynli/EDA-assistant/blob/master/examples/demo_iris_eda_report_cat_hist.png?raw=true)
![Correlation Matrix](https://github.com/madalynli/EDA-assistant/blob/master/examples/demo_iris_eda_report_corr.png?raw=true)
![Scatter Pair Plot](https://github.com/madalynli/EDA-assistant/blob/master/examples/demo_iris_eda_report_pair.png?raw=true)


## License
[MIT License](https://github.com/madalynli/EDA-assistant/blob/master/LICENSE)

