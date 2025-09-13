#!/usr/bin/env python3
"""
Script to add electronegativity values to all elements in all_elements.json.
"""

import json

def add_electronegativity_to_all_elements():
    # Load the electronegativity mapping
    with open('electronegativity_mapping.json', 'r') as f:
        electronegativity_mapping = json.load(f)
    
    # Load the all_elements.json file
    with open('all_elements.json', 'r') as f:
        elements = json.load(f)
    
    # Update each element with its electronegativity value
    updated_count = 0
    null_count = 0
    
    for element in elements:
        atomic_number = str(element['number'])
        if atomic_number in electronegativity_mapping:
            electronegativity_value = electronegativity_mapping[atomic_number]
            element['electronegativity'] = electronegativity_value
            updated_count += 1
            if electronegativity_value is None:
                null_count += 1
        else:
            print(f"Warning: No electronegativity value found for element {atomic_number} ({element.get('enName', 'Unknown')})")
    
    # Save the updated file
    with open('all_elements.json', 'w') as f:
        json.dump(elements, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully updated {updated_count} elements with electronegativity values.")
    print(f"Elements with null electronegativity (noble gases, etc.): {null_count}")
    print(f"Total elements in file: {len(elements)}")

if __name__ == "__main__":
    add_electronegativity_to_all_elements()
