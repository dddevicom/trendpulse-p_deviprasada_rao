import pandas as pd

df = pd.read_csv("raw_data.csv")

df = df[['title', 'points', 'num_comments', 'created_at']]

df = df.dropna()

df['created_at'] = pd.to_datetime(df['created_at'])

df.to_csv("cleaned_data.csv", index=False)

print("✅ Data cleaned successfully!")