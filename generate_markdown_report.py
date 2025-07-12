import json
from datetime import datetime

with open("cases_data.json", "r", encoding="utf-8") as f:
    cases = json.load(f)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

md_lines = [
    "# 📄 Threat Intelligence Summary Report",
    f"**Generated:** {now}",
    "---"
]

for case in cases:
    md_lines.append(f"## 🔐 {case['Case Title']}")
    md_lines.append(f"**Cybercrime Type:** {case['Cybercrime Type']}")
    md_lines.append(f"**Environment:** {case['Environment']}")
    md_lines.append(f"**Alert Level:** {case['Alert Raised']}")
    md_lines.append(f"**Average Confidence:** {case['Average Confidence']}")
    md_lines.append(f"**Trigger Keywords:** {', '.join(case['Trigger Keywords'])}")
    md_lines.append("")

    md_lines.append("### 👤 User Activity")
    for line in case["User Activity"]:
        md_lines.append(f"- {line}")
    
    md_lines.append("")

    md_lines.append("### 🚨 Flagged Posts")
    for post in case["Flagged Posts"]:
        md_lines.append(f"- **User:** {post['username']} (ID: {post['user_id']}, IP: {post['ip_address']})")
        md_lines.append(f"  - **Time:** {post['timestamp']}")
        md_lines.append(f"  - **Content:** {post['content']}")
        md_lines.append(f"  - **Keywords:** {', '.join(post['keywords'])}")
        md_lines.append(f"  - **Confidence Score:** {post['confidence_score']}")
        if post["bitcoin_addresses"]:
            md_lines.append(f"  - **Bitcoin Address:** {', '.join(post['bitcoin_addresses'])}")
        md_lines.append("")

    md_lines.append("---")

# Save to file
with open("report.md", "w", encoding="utf-8") as f:
    f.write('\n'.join(md_lines))

print("✅ Markdown summary saved as report.md")
