import pandas as pd
import os
import json

def process_data():
    # --- Task 1: Load the JSON File (4 marks) ---
    input_dir = "data"
    # Find the most recent json file in the data folder
    json_files = [f for f in os.listdir(input_dir) if f.endswith('.json') and 'trends_' in f]
    
    if not json_files:
        print("No JSON data found. Please run Task 1 first.")
        return
    
    latest_json = os.path.join(input_dir, sorted(json_files)[-1])
    
    with open(latest_json, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    print(f"Loaded {len(df)} stories from {latest_json}")
    print("")

    # --- Task 2: Clean the Data (10 marks) ---
    
    # 1. Duplicates — remove rows with same post_id
    df = df.drop_duplicates(subset=['post_id'])
    print(f"After removing duplicates: {len(df)}")
    
    # 2. Missing values — drop rows where post_id, title, or score is missing
    df = df.dropna(subset=['post_id', 'title', 'score'])
    print(f"After removing nulls: {len(df)}")
    
    # 3. Data types — ensure score and num_comments are integers
    df['score'] = df['score'].astype(int)
    df['num_comments'] = df['num_comments'].astype(int)
    
    # 4. Low quality — remove stories where score is less than 5
    df = df[df['score'] >= 5]
    print(f"After removing low scores: {len(df)}")
    
    # 5. Whitespace — strip extra spaces from the title column
    df['title'] = df['title'].str.strip()

    # --- Task 3: Save as CSV (6 marks) ---
    output_file = "data/trends_clean.csv"
    df.to_csv(output_file, index=False)
    
    print(f"\nSaved {len(df)} rows to {output_file}")
    
    # Print summary: stories per category
    print("\nStories per category:")
    print(df['category'].value_counts().to_string())

if __name__ == "__main__":
    process_data()
