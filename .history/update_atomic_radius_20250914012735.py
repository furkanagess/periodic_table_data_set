#!/usr/bin/env python3
"""
Script to update all JSON files with atomic radius values.
"""

import json
import os
import glob

def update_atomic_radius():
    # Load the atomic radius mapping
    with open('atomic_radius_mapping.json', 'r') as f:
        radius_mapping = json.load(f)
    
    # Get all JSON files in the directory
    json_files = glob.glob('*.json')
    
    # Exclude the mapping file itself
    if 'atomic_radius_mapping.json' in json_files:
        json_files.remove('atomic_radius_mapping.json')
    if 'update_atomic_radius.py' in json_files:
        json_files.remove('update_atomic_radius.py')
    
    total_updated = 0
    
    for file_name in json_files:
        print(f"Processing {file_name}...")
        
        try:
            # Load the JSON file
            with open(file_name, 'r', encoding='utf-8') as f:
                elements = json.load(f)
            
            # Update each element with its atomic radius
            file_updated = 0
            for element in elements:
                atomic_number = str(element['number'])
                if atomic_number in radius_mapping:
                    element['atomicRadius'] = radius_mapping[atomic_number]
                    file_updated += 1
                else:
                    print(f"Warning: No atomic radius found for element {atomic_number} ({element.get('enName', 'Unknown')}) in {file_name}")
            
            # Save the updated file
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(elements, f, indent=2, ensure_ascii=False)
            
            print(f"  Updated {file_updated} elements in {file_name}")
            total_updated += file_updated
            
        except Exception as e:
            print(f"Error processing {file_name}: {e}")
    
    print(f"\nSuccessfully updated {total_updated} elements with atomic radius values across {len(json_files)} files.")

if __name__ == "__main__":
    update_atomic_radius()
