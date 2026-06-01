import json

# Opens and reads .json file
def load_any_json(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: '{filepath}' is not a valid JSON file.")
        return {}

# Streamlines text and removes special characters and spaces
def clean_text(text):
    text = text.lower()
    # Basic punctuation removal
    for char in ".,!?;":
        text = text.replace(char, "")
    return text

# Searches and id HPO in cleaned notes, matches stored in a list
def map_note_to_reference(note, reference):
    found_terms = {}
    cleaned_note = clean_text(note)
    
    for term, hpo_id in reference.items():
        if term in cleaned_note:
            found_terms[term] = hpo_id
            
    return found_terms


# Load the dictionary from the external file
my_file = 'hpo_data.json' 

reference_data = load_any_json(my_file)
clinical_note = "Patient presents with scoliosis."

results = map_note_to_reference(clinical_note, reference_data)
print(f"Results using {my_file}: {results}")