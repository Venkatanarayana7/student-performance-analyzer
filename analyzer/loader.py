import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load(self):
        self.df = pd.read_csv(self.filepath)
        self._validate()
        return self.df

    def _validate(self):
        required = {'Campus', 'Student_ID', 'Rank', 'Maths_GPA', 'Physics_GPA', 'Chem_GPA', 'PUC_GPA', 'Gender'}
        missing  = required - set(self.df.columns)
        if missing:
            raise ValueError(f"Missing columns is CSV: {missing}")

        for col in ['Maths_GPA', 'Physics_GPA', 'Chem_GPA', 'PUC_GPA']:
            invalid = self.df[(self.df[col] < 0) | (self.df[col] > 10)]
            if len(invalid) > 0:
                print(f"Warning: {len(invalid)} rows have out-of-range values in {col}")

    def get_summary(self):
        """Print basic info about the loaded data."""
        if self.df is None:
            raise RuntimeError("Data not loaded. Call load() first.")
        print(f"Rows: {len(self.df)}")
        print(f"Columns: {list(self.df.columns)}")
        print(f"Average PUC GPA: {self.df['PUC_GPA'].mean():.2f}")
        
        


        

