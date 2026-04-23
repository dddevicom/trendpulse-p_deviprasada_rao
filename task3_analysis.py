import pandas as pd
import numpy as np
import os

def run_analysis():
    # 1. Load the cleaned CSV file from Task 2
    input_file = "data/trends_clean.csv"
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Please run Task 2 first!")
        return
    
    df = pd.read_csv(input_file)
    print(f"Reading cleaned data for analysis...")

    # 2. Performance Analysis using NumPy
    # Calculate basic statistics for the entire dataset
    avg_score = np.mean(df['score'])
    median_comments = np.median(df['num_comments'])
    total_engagement = np.sum(df['score']) + np.sum(df['num_comments'])

    print(f"--- Global Statistics ---")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Median Comments: {median_comments}")
    print(f"Total Network Engagement: {total_engagement}")
    print("-" * 30)

    # 3. Category Insights (Grouped Analysis)
    # Task: Find the average score and total comments for each category
    category_analysis = df.groupby('category').agg({
        'score': 'mean',
        'num_comments': 'sum'
    }).rename(columns={'score': 'average_score', 'num_comments': 'total_comments'})

    # Round results to 2 decimal places
    category_analysis = category_analysis.round(2)

    print("Category Performance Analysis:")
    print(category_analysis)
    print("-" * 30)

    # 4. Identify Top Performers
    # Finding the single highest-rated story in the dataset
    top_story = df.loc[df['score'].idxmax()]
    
    print("Top Trending Story:")
    print(f"Title: {top_story['title']}")
    print(f"Category: {top_story['category']}")
    print(f"Score: {top_story['score']}")

if __name__ == "__main__":
    run_analysis()
