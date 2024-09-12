#! python3

import json
import sys

def process_json_file(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    abi_data = data.get('abi', {})
    
    output_file_path = '{}.abi'.format(json_file_path)
    with open(output_file_path, 'w') as f:
        json.dump(abi_data, f, indent=4)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file_path>")
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    process_json_file(json_file_path)