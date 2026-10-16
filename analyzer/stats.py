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

    def estimate_rank(self, campus, puc_gpa):
        """
        Given a campus name and a PUC GPA, estimate the rank, percentile,
        and tier that GPA would correspond to, based on the N23 batch data.
        """

        # Step 1: keep only rows from teh requested campus
        campus_df = self.df[self.df['Campus'] == campus]

        # Step 2: count how many students scored higher than the input GPA
        higher_count = (campus_df['PUC_GPA'] > puc_gpa).sum()
        estimated_rank = higher_count + 1

        # Step 3: total students in that campus
        total = len(campus_df)

        # step 4: percentile : fraction of students with GPA <= input
        percentile = round((campus_df['PUC_GPA'] <= puc_gpa).sum() / total * 100, 1)

        # step 5: determine the tire using the same bins we use everywhere
        tier = pd.cut(
            [puc_gpa],
            bins=self.TIER_BINS,
            labels=self.TIER_LABELS,
            right=False
        )[0]

        # Step 6: build a human-readable summary
        interpretation = (
            f"A PUC GPA of {puc_gpa} at {campus} would place a student "
            f"approximately at rank {estimated_rank} out of {total},"
            f"in the top {round(100 - percentile, 1)}% - Tier: {tier}."
        )
        
        return {
            'campus': campus,
            'input_gpa': puc_gpa,
            'estimated_rank': estimated_rank,
            'total_in_campus': total,
            'percentile': percentile,
            'tier': str(tier),
            'interpretation': interpretation
        }

