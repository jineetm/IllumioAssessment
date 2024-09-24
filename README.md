# IllumioAssessment
Flow Log Parser with Lookup Table
This project is a Python-based tool for parsing network flow logs and mapping them to tags based on a lookup table. The tool generates statistics for tag counts and port/protocol combinations and outputs the results into CSV files.

Features
Flow Log Parsing: Reads flow logs in a specified format and extracts key information.
Lookup Table Matching: Maps flow logs to tags using a lookup_file.csv file containing port and protocol information.
Tag Count Generation: Outputs the count of flow logs associated with each tag.
Port/Protocol Combination Count: Outputs the count of each unique port and protocol combination found in the flow logs.
Sample Lookup Table Generation: If the lookup_table.csv file is missing or empty, the script automatically generates a sample lookup table.


Clone the repository or download the script:
git clone https://github.com/your-repo/flow-log-parser.git
cd flow-log-parser

Usage
Prepare Input Files: Make sure you have the flow logs file (flow_logs.txt) and the lookup table file (lookup_table.csv).

If the lookup_table.csv is missing or empty, the script will automatically create a sample lookup table.

Run the Script:
python3 main.py

The script will generate two output files:

tag_counts_output.csv: Contains counts of each tag found in the flow logs.
port_protocol_counts_output.csv: Contains counts of each port/protocol combination found in the flow logs.

Input Files
Flow Log File (flow_logs.txt):

A space-separated text file containing flow log entries. Each entry must have fields including destination port and protocol number.
Sample flow log entry format:
2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK

Lookup Table (lookup_table.csv):

A CSV file that maps destination ports and protocols to tags.
Format: dstport,protocol,tag
Sample data:
dstport,protocol,tag
25,tcp,sv_P1
443,tcp,sv_P2
993,tcp,email
110,tcp,email
143,tcp,email

Output Files
Tag Counts (tag_counts_output.csv):

Contains a count of how many times each tag appeared in the flow logs.
Format: Tag,Count
Tag,Count
sv_P1,2
email,3
Untagged,5

Port/Protocol Combination Counts (port_protocol_counts_output.csv):

Contains a count of each port and protocol combination found in the flow logs.
Format: Port,Protocol,Count
Port,Protocol,Count
25,tcp,1
443,tcp,1
110,tcp,1

Error Handling
Missing or Empty Lookup Table: If the lookup_table.csv is missing or empty, the script automatically generates a sample lookup table with common ports and protocols.
File Not Found: If the flow log file or lookup table file is not found, an appropriate error message will be displayed.
Incorrect Lookup Table Format: The script expects the lookup table to contain three columns: dstport, protocol, and tag. If these are missing, an error will be reported.


License
This project is licensed under the MIT License.
