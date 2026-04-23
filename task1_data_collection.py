import requests
import json
import os
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# category keywords - assigned based on project requirements
CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm", "programming", "developer", "open source", "linux", "python", "startup"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global", "china", "india", "europe", "ukraine", "policy", "law", "court", "military", "sanctions"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship", "match", "tournament", "athlete", "cricket", "football", "tennis", "olympic", "racing", "marathon", "coach", "stadium", "cup", "medal", "baseball"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome", "quantum", "health", "medicine", "brain", "scientist", "experiment", "asteroid", "gene", "vaccine", "fossil", "telescope"],
    "entertainment": ["movie", "film", "music", "netflix", "book", "show", "award", "streaming", "podcast", "youtube", "album", "cinema", "tv", "series", "comedy", "game", "fiction", "actor", "director", "trailer"],
}

headers = {"User-Agent": "TrendPulse/1.0"}

def get_category(title):
    """Checks story title against keywords to assign a category."""
    title = title.lower()
    for cat, words in CATEGORIES.items():
        if any(word in title for word in words):
            return cat
    return None

def fetch_story(sid):
    """Task 1: Fetches a single story detail from HN API."""
    try:
        url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
        resp = requests.get(url, headers=headers, timeout=10)
        return resp.json()
    except Exception as e:
        # Task 1 requirement: If request fails, print message and move on
        print(f"Failed to fetch {sid}: {e}")
        return None

# --- Step 1: Get top story IDs ---
print("Fetching top story IDs...")
try:
    r = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", headers=headers)
    story_ids = r.json()[:500]
except Exception as e:
    print(f"Error getting IDs: {e}")
    exit()

# --- Step 2: Fetch and Extract Fields ---
# Using threads for speed, but keeping logic compliant with field requirements
with ThreadPoolExecutor(max_workers=20) as executor:
    all_stories = list(executor.map(fetch_story, story_ids))

final_results = []
category_counts = {cat: 0 for cat in CATEGORIES}

# Process categories one by one to respect the time.sleep(2) requirement
for category in CATEGORIES:
    found_for_cat = 0
    for story in all_stories:
        if found_for_cat >= 25:
            break
        
        if not story or story.get("type") != "story":
            continue
        
        title = story.get("title", "")
        if get_category(title) == category:
            # Task 2: Extract the 7 specific fields
            final_results.append({
                "post_id": story.get("id"),
                "title": title,
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", ""),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            })
            found_for_cat += 1
    
    # Task 1 requirement: Wait 2 seconds between each category loop
    time.sleep(2)

# --- Step 3: Save to JSON ---
# Requirement: Create data/ folder if it doesn't exist
os.makedirs("data", exist_ok=True)
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(final_results, f, indent=2)

# Requirement: Print specific console message
print(f"Collected {len(final_results)} stories. Saved to {filename}")
