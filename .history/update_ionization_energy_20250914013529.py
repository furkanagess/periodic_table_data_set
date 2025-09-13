#!/usr/bin/env python3
"""
Script to update all JSON files with ionization energy values.
"""

import json
import os
import glob

def update_ionization_energy():
    # Load the ionization energy mapping
    with open('ionization_energy_mapping.json', 'r') as f:
        ionization_mapping = json.load(f)
    
    # Get all JSON files in the directory
    json_files = glob.glob('*.json')
    
    # Exclude the mapping file itself and script files
    exclude_files = ['ionization_energy_mapping.json', 'update_ionization_energy.py', 'atomic_radius_mapping.json', 'update_atomic_radius.py']
    json_files = [f for f in json_files if f not in exclude_files]
    
    total_updated = 0
    
    for file_name in json_files:
        print(f"Processing {file_name}...")
        
        try:
            # Load the JSON file
            with open(file_name, 'r', encoding='utf-8') as f:
                elements = json.load(f)
            
            # Update each element with its ionization energy
            file_updated = 0
            for element in elements:
                atomic_number = str(element['number'])
                if atomic_number in ionization_mapping:
                    element['ionizationEnergy'] = ionization_mapping[atomic_number]
                    file_updated += 1
                else:
                    print(f"Warning: No ionization energy found for element {atomic_number} ({element.get('enName', 'Unknown')}) in {file_name}")
            
            # Save the updated file
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(elements, f, indent=2, ensure_ascii=False)
            
            print(f"  Updated {file_updated} elements in {file_name}")
            total_updated += file_updated
            
        except Exception as e:
            print(f"Error processing {file_name}: {e}")
    
    print(f"\nSuccessfully updated {total_updated} elements with ionization energy values across {len(json_files)} files.")

if __name__ == "__main__":
    update_ionization_energy()
