from analyzer.loader import DataLoader

loader = DataLoader("data/rgukt_23batch_branch_data.csv")
df = loader.load()
loader.get_summary()
print(df.head())