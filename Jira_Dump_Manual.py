import subprocess
import requests
import csv

# Set your Jira credentials and URL
username = "saldardery"  #Jira Username
password = "Ahly_12345"  #Jira Password
jira_url = "https://jira.pscoe.vmware.com/sr/jira.issueviews:searchrequest-csv-current-fields/19048/SearchRequest-19048.csv" #DO NOT CHANGE THIS URL

# Set the output file path
output_file_path = r'C:\Users\saldardery\OneDrive - VMware, Inc\Live PowerBi Dashboard\Migration Jira Dump.csv' # CHANGE THE PATH TO REFLECT YOUR LOCAL ONEDRIVE PATH , DO NOT CHANGE FILENAME

# Run the cURL command using subprocess
curl_command = f'curl.exe -u {username}:{password} {jira_url}'
process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, shell=True)
output, _ = process.communicate()

# Check if the cURL command was successful
if process.returncode == 0:
    # Save the output to the specified CSV file
    with open(output_file_path, 'wb') as csv_file:
        csv_file.write(output)
    print(f"Data saved to {output_file_path}")
else:
    print("Error executing cURL command")
