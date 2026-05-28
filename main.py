from analyzer.loader import load_students
from analyzer.stats import compute_basic_stats, get_campus_summary

# 1. Load data
students = load_students("data/rgukt_23batch_branch_data.csv")

# 2. Compute basic statistics
stats = compute_basic_stats(students)

print("=" * 60)
print("N23 BATCH BASIC STATISTICS")
print("=" * 60)
print(f"Total students: {stats['total_students']}")
print(f"PUC GPA Mean: {stats['puc_mean']:.2f}")
print(f"PUC GPA Max: {stats['puc_max']:.2f}")
print(f"PUC GPA Min: {stats['puc_min']:.2f}")
print(f"PUC GPA Std Dev: {stats['puc_std']:.2f}")
print(f"Students with PUC >= 9.0: {stats['above_9_count']}")
print(f"Students with PUC < 7.0: {stats['below_7_count']}")
print(f"Subject means (Maths, Physics, Chem): {[f'{x:.2f}' for x in stats['subject_means']]}")

# 3. Campus-wise summary
campus_summary = get_campus_summary(students)
print("\nCAMPUS-WISE SUMMARY")
print("-" * 60)
for campus, info in campus_summary.items():
    print(f"{campus:12} | Students: {info['count']:4d} | Avg PUC GPA: {info['avg_puc_gpa']:.2f} | Max: {info['max_puc_gpa']:.2f} | Min: {info['min_puc_gpa']:.2f}")
