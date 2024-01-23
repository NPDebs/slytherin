# import panda library => for data manipulation/analysis
import pandas as pd

'''
Define a function that accepts two parameters: csv_file & md_output
csv_file => path to the CSV file & md_output => path to the Markdown file
'''

def csv_to_markdown(csv_file, md_output):
    # Read the CSV file into a Pandas DataFrame, df
    df = pd.read_csv(csv_file)
