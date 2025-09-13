#!/usr/bin/env python3
"""
Script to remove all ionizationEnergy fields from all_elements.json.
"""

import json

def remove_ionization_energies():
    # Load the all_elements.json file
    with open('all_elements.json', 'r') as f:
        elements = json.load(f)
    
    # Remove ionizationEnergy field from each element
    removed_count = 0
    for element in elements:
        if 'ionizationEnergy' in element:
            del element['ionizationEnergy']
            removed_count += 1
    
    # Save the updated file
    with open('all_elements.json', 'w') as f:
        json.dump(elements, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully removed {removed_count} ionizationEnergy fields.")
    print(f"Total elements in file: {len(elements)}")

if __name__ == "__main__":
    remove_ionization_energies()
