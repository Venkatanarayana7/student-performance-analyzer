import matplotlib.pyplot as plt
import numpy as np
import os

def plot_gpa_distribution(students):
    # Extract all PUC GPAs
    puc_gpas = [s['PUC_GPA'] for s in students]

    # Create figure
    plt.figure(figsize=(10, 6)) # 10 inches wide, 6 inches tall

    # Draw histogram: bins=20 divides teh range into 20 bars
    plt.hist(puc_gpas, bins=20, color="#58A6FF", edgecolor='white', alpha=0.9)

    # Add vertical line for the mean
    mean_gpa = np.mean(puc_gpas)
    plt.axvline(mean_gpa, color='#F0B429', linestyle='dashed', linewidth=2, label=f'Mean = {mean_gpa:.2f}')

    # Labels and title
    plt.title('Distribution of PUC GPA (N23 Batch)', fontsize=16, fontweight='bold')
    plt.xlabel('PUC GPA', fontsize=12)
    plt.ylabel('Number of Students', fontsize=12)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()

    # Save
    plt.savefig('outputs/charts/gpa_distribution.png', dpi=150)
    plt.close()
    print("Chart saved: outputs/charts/gpa_distribution.png")

def plot_campus_comparision(students):
    # Group GPAs by campus (we can reuse your stats logic)
    campuses = {}
    for s in students:
        c = s['Campus']
        campuses.setdefault(c, []).append(s['PUC_GPA'])

    # Calculate average per campus
    campus_names = list(campuses.keys())
    avg_gpas = [np.mean(campuses[name]) for name in campus_names]

    # Colors for each campus (using the same palette as earlier)
    colors = ['#58A6FF', '#F0B429', '#8B949E'] # blue, gold, grey

    plt.figure(figsize=(8, 6))
    bars = plt.bar(campus_names, avg_gpas,  color=colors, edgecolor='white', linewidth=1.2)

    # Add data labels on top of each bar
    for bar, avg in zip(bars, avg_gpas):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02, f'{avg:.2f}', ha='center', fontsize=12, fontweight='bold')

    plt.title('Average PUC GPA by Campus', fontsize=16, fontweight='bold')
    plt.xlabel('Campus', fontsize=12)
    plt.ylabel('Average PUC GPA', fontsize=12)
    plt.tight_layout()
    plt.savefig('outputs/charts/campus_comparion.png', dpi=150)
    plt.close()
    print("Chart saved: outputs/charts/campus_comparison.png")


def plot_gender_distribution(students):
    # Count genders
    counts = {}
    for s in students:
        g = s['Gender']
        counts[g] = counts.get(g, 0) + 1

    labels = list(counts.keys())
    sizes = list(counts.values())
    # Convert 'M' and 'F' to full names for readability
    labels_names = [('Male' if l == 'M' else 'Female') for l in labels]

    colors = ['#58A6FF', '#F0B429'] # blue for male, gold for female

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels_names, autopct='%1.1f%%', startangle=90, colors=colors, explode=(0, 0.05), shadow=True, textprops={'fontsize': 12})
    plt.title('Gender Distribution (N23 Batch)', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('outputs/charts/gender_distribution.png', dpi=150)
    plt.close()
    print("Chart saved: outputs/charts/gender_distribution.png")