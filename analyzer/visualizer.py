import matplotlib.pyplot as plt
import pandas as pd
import os

class Visualizer:
    """
    Generates charts from the student DataFrame and saves them to disk.
    """
    def __init__(self, df, output_dir='outputs/charts'):
        self.df = df
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def _save(self, filename):
        """Save the current figure to the output folder and close it."""
        plt.tight_layout()
        path = os.path.join(self.output_dir, filename)
        plt.savefig(path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"Chart saved: {path}")

    def plot_gpa_distribution(self):
        """Histogram of PUC GPA across all students."""
        plt.figure(figsize=(10, 6))
        plt.hist(self.df['PUC_GPA'], bins=25, color='#58A6FF', edgecolor='white')
        plt.title('Distribution of PUC GPA', fontsize=14, fontweight='bold')
        plt.xlabel('PUC GPA')
        plt.ylabel('Number of Students')
        plt.grid(axis='y', alpha=0.3)
        self._save('gpa_distribution.png')

    def plot_campus_boxplot(self):
        """Box plot of PUC GPA for each campus."""
        campuses = self.df['Campus'].unique()
        data = [self.df[self.df['Campus'] == c]['PUC_GPA'].values for c in campuses]

        plt.figure(figsize=(10, 6))
        plt.boxplot(data, labels=campuses, patch_artist=True,
                    medianprops=dict(color='black', linewidth=2))
        plt.title('PUC GPA by Campus', fontsize=14, fontweight='bold')
        plt.xlabel('Campus')
        plt.ylabel('PUC GPA')
        plt.grid(axis='y', alpha=0.3)
        self._save('campus_boxplot.png')

    def plot_correlation_heatmap(self):
        """Heatmap of correlations between subject GPAs and PUC GPA."""
        cols = ['Maths_GPA', 'Physics_GPA', 'Chem_GPA', 'PUC_GPA']
        corr = self.df[cols].corr()

        plt.figure(figsize=(7, 6))
        im = plt.imshow(corr.values, cmap='coolwarm', vmin=-1, vmax=1)
        labels = ['Maths', 'Physics', 'Chem', 'PUC']
        plt.xticks(range(len(labels)), labels)
        plt.yticks(range(len(labels)), labels)
        plt.colorbar(im, label='Correlation')

        for i in range(len(labels)):
            for j in range(len(labels)):
                val = corr.values[i, j]
                color = 'white' if abs(val) > 0.6 else 'black'
                plt.text(j, i, f'{val:.2f}', ha='center', va='center',
                         color=color, fontsize=10, fontweight='bold')

        plt.title('Subject GPA Correlations', fontsize=14, fontweight='bold')
        self._save('correlation_heatmap.png')

    def plot_tier_distribution(self):
        """Bar chart of how many students fall into each performance tier."""
        counts = self.df['Tier'].value_counts()

        plt.figure(figsize=(8, 6))
        plt.bar(counts.index.astype(str), counts.values,
                color='#7b2fff', edgecolor='white')
        plt.title('Tier Distribution', fontsize=14, fontweight='bold')
        plt.xlabel('Tier')
        plt.ylabel('Number of Students')

        for i, val in enumerate(counts.values):
            plt.text(i, val + 10, str(val), ha='center', fontsize=10)

        self._save('tier_distribution.png')