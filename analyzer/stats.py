import pandas as pd

class StudentAnalyzer:
    """
    Adds analytical columns (Tier, Campus Percentile) to the student DataFrame
    and provides methods for statistics and rank estimation.
    """

    # The boundaries for our tiers, defiend once here for easy changes
    TIER_BINS = [0, 7.0, 8.0, 9.0, 9.5, 10.01] # 10.01 to include 10.0
    TIER_LABELS = ['Below Average', 'Average', 'Strong', 'High', 'Elite']

    def __init__(self, df):
        # Make a copy so we don't alter the original DataFrame
        self.df = df.copy()
        # Automatically add the Tier and Percentile columns
        self._add_tier_column()
        self._add_percentile_column()

    def _add_tier_column(self):
        """Assign each student to a performance tier based on PUC_GPA."""
        self.df['Tier'] = pd.cut(
            self.df['PUC_GPA'],
            bins = self.TIER_BINS,
            labels = self.TIER_LABELS,
            right = False  # left edge inclusive: 9.0 goes to 'String', 9.5 to 'High'
        )

    def _add_percentile_column(self):
        """Calculate the percentile ran within each campus."""
        self.df['Campus_Percentile'] = (
            self.df.groupby('Campus')['PUC_GPA']
            .rank(pct=True)   # returns fraction ( 0 to 1)
            .round(3) * 100   # convert to precentage (0-100)
        )   

    
        


