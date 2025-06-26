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
        return wikibio["train"][index]
        return persona


def main():
    from datasets import load_dataset
    import csv
    from tqdm import tqdm

    # Load dataset
    wikibio = load_dataset("wiki_bio", split="test")  # You can change to "validation" or "test"

    # Collect all unique column headers from tables
    all_columns = set()

    for row in tqdm(wikibio, desc="Collecting headers"):
        table = row["input_text"]["table"]
        headers = table["column_header"]
        all_columns.update(headers)

    # Add target_text to the columns
    all_columns = sorted(all_columns)
    all_columns.append("target_text")

    # Write to CSV
    output_file = "wikibio_train.csv"
    all_columns = all_columns[:50]
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=all_columns)
        writer.writeheader()

        for row in tqdm(wikibio, desc="Writing rows"):
            table = row["input_text"]["table"]
            row_dict = dict(zip(table["column_header"], table["content"]))
            row_dict["target_text"] = row["target_text"]

            # Fill in missing columns with empty string
            full_row = {col: row_dict.get(col, "") for col in all_columns}
            writer.writerow(full_row)

    print(f"✅ Export complete: {output_file}")

