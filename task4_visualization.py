import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations():
    # 1. Load the cleaned data
    input_file = "data/trends_clean.csv"
    if not os.path.exists(input_file):
        print("Error: trends_clean.csv not found. Please run Task 2 first!")
        return
    
    df = pd.read_csv(input_file)
    
    # 2. Setup the Visual Style
    # Seaborn makes charts look more professional than standard Matplotlib
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 6))

    # --- Chart 1: Bar Plot (Engagement by Category) ---
    # This shows which category is getting the most attention
    plt.subplot(1, 2, 1) # Left side
    category_engagement = df.groupby('category')['score'].mean().sort_values(ascending=False)
    sns.barplot(x=category_engagement.index, y=category_engagement.values, palette="magma")
    
    plt.title('Average Score by Category', fontsize=14)
    plt.xticks(rotation=45)
    plt.ylabel('Average Score')

    # --- Chart 2: Pie Chart (Content Distribution) ---
    # This shows the percentage of stories in each category
    plt.subplot(1, 2, 2) # Right side
    counts = df['category'].value_counts()
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', 
            colors=sns.color_palette("Set2"), startangle=140)
    
    plt.title('Story Distribution %', fontsize=14)

    # 3. Finalize and Save
    plt.tight_layout()
    
    # Create a visuals folder if it doesn't exist
    os.makedirs("visuals", exist_ok=True)
    plt.savefig("visuals/trendpulse_report.png")
    
    print("Task 4 Complete!")
    print("Report saved to: visuals/trendpulse_report.png")
    
    # Show the plot window
    plt.show()

if __name__ == "__main__":
    create_visualizations()
