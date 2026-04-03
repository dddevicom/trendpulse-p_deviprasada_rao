import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cleaned_data.csv")

# Sort top 10 posts
top_posts = df.sort_values(by='points', ascending=False).head(10)

# Set style
#sns.set(style="whitegrid")
sns.set_theme(style="darkgrid")

# Create plot
plt.figure(figsize=(10, 6))
sns.barplot(x='points', y='title', data=top_posts)

plt.xlabel("Points")
plt.ylabel("Title")
plt.title("Top 10 HackerNews Posts")

plt.tight_layout()

# Save and show
plt.savefig("chart.png")
plt.show()