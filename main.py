"""
Student Performance Analyzer
----------------------------
Loads the N23 batch data, runs analysis, generates charts, and
demonstrates the rank estimation feature.

Run:  python main.py
"""

from analyzer.loader import DataLoader
from analyzer.stats import StudentAnalyzer
from analyzer.visualizer import Visualizer


def main():
    # ---- 1. Load the data ----------------------------------------------
    print("=" * 60)
    print("STUDENT PERFORMANCE ANALYZER")
    print("=" * 60)

    loader = DataLoader("data/rgukt_23batch_branch_data.csv")
    df = loader.load()
    loader.get_summary()

    # ---- 2. Analyse ----------------------------------------------------
    analyzer = StudentAnalyzer(df)

    print("\n--- Tier Distribution ---")
    print(analyzer.df['Tier'].value_counts())

    print("\n--- Campus Averages ---")
    print(analyzer.df.groupby('Campus')['PUC_GPA'].mean().round(3))

    # ---- 3. Rank estimation demo --------------------------------------
    print("\n--- Rank Estimation ---")
    for campus, gpa in [('Nuzvid', 9.4),
                        ('Nuzvid', 8.5),
                        ('Ongole', 9.0),
                        ('RK_Valley', 9.8)]:
        result = analyzer.estimate_rank(campus, gpa)
        print(f"  {result['interpretation']}")

    # ---- 4. Generate charts --------------------------------------------
    print("\n--- Generating Charts ---")
    viz = Visualizer(analyzer.df)
    viz.plot_gpa_distribution()
    viz.plot_campus_boxplot()
    viz.plot_correlation_heatmap()
    viz.plot_tier_distribution()

    print("\nDone. Charts saved in outputs/charts/")


if __name__ == "__main__":
    main()