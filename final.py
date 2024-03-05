import os
import subprocess

# Step 1: Convert Parquet to CSV
parquet_to_csv_script = 'parquet_to_csv.py'
parquet_file_path = 'list_of_company_websites.snappy.parquet'
csv_file_path = 'output_final.csv'
subprocess.run(['python3', parquet_to_csv_script, parquet_file_path, csv_file_path])

# Step 2: Extract data from CSV and create a new CSV file
scrappin_script = 'scrappin2_0.py'
company_name_file_path = 'companyName_file.csv'
subprocess.run(['python3', scrappin_script, csv_file_path, company_name_file_path])

# Step 3: Run the final maps scrapping script
maps_scrapping_script = 'maps_scrapper.py'
final_result_file_path = 'final_result.csv'
subprocess.run(['python3', maps_scrapping_script, company_name_file_path, final_result_file_path])

print(f"Final result file generated at: {final_result_file_path}")