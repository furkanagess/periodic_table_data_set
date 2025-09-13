#!/usr/bin/env python3
"""
Script to add electronegativity values to all element type JSON files.
"""

import json
import os

def add_electronegativity_to_file(filename, electronegativity_mapping):
    """Add electronegativity fields to a specific JSON file."""
    if not os.path.exists(filename):
        print(f"Warning: File {filename} does not exist.")
        return 0
    
    # Load the JSON file
    with open(filename, 'r') as f:
        elements = json.load(f)
    
    # Add electronegativity field to each element
    updated_count = 0
    for element in elements:
        atomic_number = str(element['number'])
        if atomic_number in electronegativity_mapping:
            element['electronegativity'] = electronegativity_mapping[atomic_number]
            updated_count += 1
    
    # Save the updated file
    with open(filename, 'w') as f:
        json.dump(elements, f, indent=2, ensure_ascii=False)
    
    return updated_count

def main():
    # Load the electronegativity mapping
    with open('electronegativity_mapping.json', 'r') as f:
        electronegativity_mapping = json.load(f)
    
    # List of all element type JSON files
    type_files = [
        'actinides.json',
        'alkali_metal.json',
        'alkaline_earth_metal.json',
        'halogens.json',
        'lanthanides.json',
        'metalloid.json',
        'noble_gases.json',
        'post_transition_metal.json',
        'reactive_nonmetal.json',
        'transition_metal.json',
        'unknown.json'
    ]
    
    total_updated = 0
    
    print("Adding electronegativity values to all element type files...")
    print("-" * 60)
    
    for filename in type_files:
        updated = add_electronegativity_to_file(filename, electronegativity_mapping)
        total_updated += updated
        print(f"{filename:25} : {updated:2} elements updated")
    
    print("-" * 60)
    print(f"Total elements updated with electronegativity: {total_updated}")
    print("All element type files have been updated!")

if __name__ == "__main__":
    main()
