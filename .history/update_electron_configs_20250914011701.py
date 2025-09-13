#!/usr/bin/env python3
"""
Script to update all_elements.json with electron configurations from the mapping.
"""

import json
import os

def update_electron_configurations():
    # Load the electron configuration mapping
    with open('electron_config_mapping.json', 'r') as f:
        config_mapping = json.load(f)
    
    # Load the all_elements.json file
    with open('all_elements.json', 'r') as f:
        elements = json.load(f)
    
    # Update each element with its electron configuration
    updated_count = 0
    for element in elements:
        atomic_number = str(element['number'])
        if atomic_number in config_mapping:
            element['electronConfiguration'] = config_mapping[atomic_number]
            updated_count += 1
        else:
            print(f"Warning: No electron configuration found for element {atomic_number} ({element.get('enName', 'Unknown')})")
    
    # Save the updated file
    with open('all_elements.json', 'w') as f:
        json.dump(elements, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully updated {updated_count} elements with electron configurations.")
    print(f"Total elements in file: {len(elements)}")

if __name__ == "__main__":
    update_electron_configurations()
