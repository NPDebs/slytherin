# import panda library => for data manipulation/analysis
import pandas as pd

'''
Define a function that accepts two parameters: csv_file & md_output
csv_file => path to the CSV file & md_output => path to the Markdown file
'''

def csv_to_markdown(csv_file, md_output):
    # Read the CSV file into a Pandas DataFrame, df
    df = pd.read_csv(csv_file)

    '''
    Use the "to_markdown" method of the DataFrame (df) to convert it into a Markdown table.
    The "index=False" parameter specifies that the DataFrame index should not be included in the Markdown table.
    '''
    
    markdown_table = df.to_markdown(index=False)

    # Open the specified md file (md_output) in write mode; write the md table content into it
    with open(md_output, 'w') as md_file:
        md_file.write(markdown_table)

# Check if the script is being run as the main program (not imported as a module).
if __name__ == "__main__":
    # Allow user specify paths for the input CSV file (input_csv_file) and the output Markdown file (output_md_file).
    input_csv_file = input("Enter path to the CSV file: ")
    output_md_file = input("Enter path for the output md file: ")

    # Call the function with specified paths
    csv_to_markdown(input_csv_file, output_md_file)
