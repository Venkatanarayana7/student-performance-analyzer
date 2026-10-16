from analyzer.loader import DataLoader
from analyzer.stats import StudentAnalyzer

# 1. Load data
loader = DataLoader("data/rgukt_23batch_branch_data.csv")
df = loader.load()

# 2. Create analyzer (this automatically adds Tier and Percentile columns)
analyzer = StudentAnalyzer(df)

#loader.get_summary()
#print(df.head())

#3. Check the new columns 
#print(analyzer.df[['PUC_GPA', 'Tier', 'Campus_Percentile']].head(10))
#print(analyzer.df['Tier'].value_counts())

# Test estimate_rank
print(analyzer.estimate_rank('RK_Valley', 8.0)['interpretation']) 