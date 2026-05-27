import csv

def load_students(filepath):
    """Read the CSV file and return a list of dicts with proper types."""
    students = []
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields from string to appropriate type
            row['Rank'] = int(row['Rank'])
            row['Maths_GPA'] = float(row['Maths_GPA'])
            row['Physics_GPA'] = float(row['Physics_GPA'])
            row['Chem_GPA'] = float(row['Chem_GPA'])
            row['PUC_GPA'] = float(row['PUC_GPA'])
            students.append(row)
    return students
