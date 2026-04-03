import pandas as pd

df = pd.read_csv("cleaned_data.csv")

print("📊 Average Points:", df['points'].mean())
print("📊 Max Comments:", df['num_comments'].max())

summary = df.describe()

summary.to_csv("analysis.csv")

print("✅ Analysis completed!")