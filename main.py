from analyzer.loader import load_students

students = load_students("data/rgukt_23batch_branch_data.csv")
print(f"Total students loaded: {len(students)}")
# Print first student to check types
first = students[0]
print(first)
print(f"PUC GPA of first student: {first['PUC_GPA']} (type: {type(first['PUC_GPA'])})")
