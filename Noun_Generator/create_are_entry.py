import json

# Create the entry for "are" with minimal fields due to low pos_frequency
are_entry = {
    "word": "are",
    "pos": "noun",
    "inflections": {
        "plural": "ares",
        "possessive": "are's"
    },
    "pos_frequency": 0.001,
    "meanings": []
}

# Read existing entries
with open('Noun-Entries.json', 'r') as f:
    entries = json.load(f)

# Add the new entry
entries.append(are_entry)

# Write back to file
with open('Noun-Entries.json', 'w') as f:
    json.dump(entries, f, indent=2)

print("Entry for 'are' has been added to Noun-Entries.json")
print(json.dumps(are_entry, indent=2))