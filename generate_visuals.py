import json
from collections import Counter, defaultdict
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime

# Load flagged case data
with open("cases_data.json", "r", encoding="utf-8") as f:
    cases = json.load(f)

# -------------------------------
# 1. WORD CLOUD OF KEYWORDS
# -------------------------------
keyword_counter = Counter()
for case in cases:
    for post in case["Flagged Posts"]:
        keyword_counter.update(post["keywords"])

# Create word cloud image
wc = WordCloud(width=800, height=400, background_color="white")
wc.generate_from_frequencies(keyword_counter)

# Save image
wc.to_file("wordcloud.png")
print("✅ Word cloud saved as wordcloud.png")

# -------------------------------
# 2. TIMELINE PLOT
# -------------------------------
# Group timestamps per user
user_times = defaultdict(list)

for case in cases:
    for post in case["Flagged Posts"]:
        timestamp = datetime.strptime(post["timestamp"], "%Y-%m-%d %H:%M:%S")
        user_times[post["username"]].append(timestamp)

# Plot
plt.figure(figsize=(10, 5))
for user, times in user_times.items():
    y = [user] * len(times)
    plt.scatter(times, y, label=user)

plt.xlabel("Time")
plt.ylabel("Users")
plt.title("Timeline of Flagged Activity")
plt.tight_layout()
plt.savefig("timeline.png")
print("✅ Timeline chart saved as timeline.png")
