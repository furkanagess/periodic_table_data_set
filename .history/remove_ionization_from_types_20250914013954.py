#!/usr/bin/env python3
"""
Script to remove all ionizationEnergy fields from all element type JSON files.
"""

import json
import os

def remove_ionization_energies_from_file(filename):
    """Remove ionizationEnergy fields from a specific JSON file."""
    if not os.path.exists(filename):
        print(f"Warning: File {filename} does not exist.")
        return 0
    
    # Load the JSON file
    with open(filename, 'r') as f:
        elements = json.load(f)
    
    # Remove ionizationEnergy field from each element
    removed_count = 0
    for element in elements:
        if 'ionizationEnergy' in element:
            del element['ionizationEnergy']
            removed_count += 1
    
    # Save the updated file
    with open(filename, 'w') as f:
        json.dump(elements, f, indent=2, ensure_ascii=False)
    
    return removed_count

def main():
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
    
    total_removed = 0
    
    print("Removing ionizationEnergy fields from all element type files...")
    print("-" * 60)
    
    for filename in type_files:
        removed = remove_ionization_energies_from_file(filename)
        total_removed += removed
        print(f"{filename:25} : {removed:2} fields removed")
    
    print("-" * 60)
    print(f"Total ionizationEnergy fields removed: {total_removed}")
    print("All element type files have been cleaned!")

if __name__ == "__main__":
    main()
