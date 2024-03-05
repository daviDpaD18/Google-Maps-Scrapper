from flask import Flask 
import pandas as pd 
import os

relative_path = "list_of_company_websites.snappy.parquet"

# Get the absolute path using os.path.abspath
absolute_path = os.path.abspath(relative_path)



# Load the parquet file into a pandas DataFrame
df = pd.read_parquet(absolute_path)
#make it into a csv file
csv_file_path = "output_data.csv"
df.to_csv(csv_file_path, index=False)



