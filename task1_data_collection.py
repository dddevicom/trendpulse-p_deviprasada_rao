import requests
import pandas as pd

url = "https://hn.algolia.com/api/v1/search?query=python"
response = requests.get(url)
data = response.json()

# Convert to DataFrame
hits = data['hits']
df = pd.DataFrame(hits)

# Save raw data
df.to_csv("raw_data.csv", index=False)

print("Data fetched and saved!")