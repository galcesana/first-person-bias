from datasets import load_dataset

# Load the dataset
wikibio = load_dataset("wiki_bio")

def extract_fields(entry):
    table = entry["input_text"]["table"]
    headers = table["column_header"]
    contents = table["content"]
    
    # Create a dict mapping each field to its value
    info = dict(zip(headers, contents))
    
    return {
        "name": info.get("name", "").strip(),
        "birth_date": info.get("birth_date", "").strip(),
        "nationality": info.get("nationality", "").strip(),
        "occupation": info.get("occupation", "").strip()
    }

index = -1
def get_next_persona():
    global index
    while True:
        index += 1
        fields = extract_fields(wikibio["train"][index])
        if not fields['nationality'] or not fields['occupation']:
            continue

        persona = f'{fields['name']}, born in {fields['birth_date']} and {fields['nationality']}'#, Occupation: {fields['occupation']}")
        print(f"Persona {index}: {persona}")
        
        return persona
    