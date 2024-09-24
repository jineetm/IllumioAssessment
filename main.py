import csv
from collections import defaultdict

# Function to load lookup table into a dictionary
def load_lookup_table(lookup_file):
    lookup_table = {}
    with open(lookup_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            port = row['dstport'].strip()
            protocol = row['protocol'].strip().lower()
            tag = row['tag'].strip()
            lookup_table[(port, protocol)] = tag
    return lookup_table

# Function to parse flow logs and map to tags
def parse_flow_logs(flow_log_file, lookup_table):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    untagged_count = 0

    with open(flow_log_file, 'r') as f:
        for line in f:
            fields = line.strip().split()
            if len(fields) < 7:
                continue
            
            # Extract relevant fields (port, protocol)
            dstport = fields[6].strip()
            protocol_num = fields[7].strip()
            protocol = 'tcp' if protocol_num == '6' else 'udp' if protocol_num == '17' else 'icmp'

            # Check for a match in the lookup table
            key = (dstport, protocol)
            if key in lookup_table:
                tag = lookup_table[key]
                tag_counts[tag] += 1
            else:
                untagged_count += 1
                tag_counts['Untagged'] += 1

            # Count port/protocol combinations
            port_protocol_counts[key] += 1

    return tag_counts, port_protocol_counts

# Function to write tag counts to an output file
def write_tag_counts(output_file, tag_counts):
    with open(output_file, 'w') as f:
        f.write('Tag,Count\n')
        for tag, count in tag_counts.items():
            f.write(f'{tag},{count}\n')

# Function to write port/protocol counts to an output file
def write_port_protocol_counts(output_file, port_protocol_counts):
    with open(output_file, 'w') as f:
        f.write('Port,Protocol,Count\n')
        for (port, protocol), count in port_protocol_counts.items():
            f.write(f'{port},{protocol},{count}\n')

# Main function
def main(flow_log_file, lookup_file, tag_output_file, port_protocol_output_file):
    # Load lookup table
    lookup_table = load_lookup_table(lookup_file)
    
    # Parse flow logs and count matches
    tag_counts, port_protocol_counts = parse_flow_logs(flow_log_file, lookup_table)
    
    # Write output
    write_tag_counts(tag_output_file, tag_counts)
    write_port_protocol_counts(port_protocol_output_file, port_protocol_counts)

if __name__ == "__main__":
    # Input files and output files
    flow_log_file = 'flow_logs.txt'
    lookup_file = 'lookup_file.csv'
    tag_output_file = 'tag_counts_output.csv'
    port_protocol_output_file = 'port_protocol_counts_output.csv'
    
    # Run the main program
    main(flow_log_file, lookup_file, tag_output_file, port_protocol_output_file)
