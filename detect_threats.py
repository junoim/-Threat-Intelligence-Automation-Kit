from app import app, db, Post
import re
import json
import html
import base64
import random
import string

# 📥 Load keyword weights
with open("keywords.json", "r") as f:
    keyword_scores = json.load(f)
keywords = list(keyword_scores.keys())

# ----------------------------
# Preprocessing Function
# ----------------------------
def preprocess(text):
    text = html.unescape(text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    try:
        decoded = base64.b64decode(text).decode("utf-8")
        if len(decoded.strip()) > 10:
            text += " " + decoded
    except Exception:
        pass
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text.lower()

# ----------------------------
# Keyword Mapping
# ----------------------------
keyword_mapping = {
    'passport': ('Fake Document Trade Detected', 'Forgery / Identity Crime'),
    'guns': ('Weapons Deal Activity', 'Arms Trafficking'),
    'malware': ('Malware Distribution Detected', 'Cybercrime / Malware'),
    'exploit': ('Exploitation Tools Offered', 'Hacking / Exploit Trade'),
    'bitcoin': ('Bitcoin Activity in Forum', 'Crypto Financial Abuse'),
    'wallet': ('Crypto Wallet Address Shared', 'Cryptocurrency Movement'),
    'buy': ('Underground Marketplace Activity', 'Dark Web Commerce'),
    'sell': ('Underground Marketplace Activity', 'Dark Web Commerce'),
    'mdma': ('Narcotics Trade on Forum', 'Darknet Drug Activity'),
    'lsd': ('Narcotics Trade on Forum', 'Darknet Drug Activity')
}

# ----------------------------
# Fake IP & ID Helpers
# ----------------------------
def generate_fake_ip():
    return f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"

def generate_user_id(username):
    return f"USR{abs(hash(username)) % 10000:04d}"

# ----------------------------
# Group Posts into Cases
# ----------------------------
case_reports = {}
case_scores = {}

with app.app_context():
    posts = Post.query.all()
    for post in posts:
        cleaned = preprocess(post.content)
        matched = [kw for kw in keywords if re.search(rf"{kw}", cleaned)]
        bitcoin_matches = re.findall(r'\b(?:bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}\b', post.content)

        if matched or bitcoin_matches:
            # Compute confidence score
            score = sum(keyword_scores.get(kw, 1) for kw in matched)

            # Case metadata
            for kw in keywords:
                if kw in matched:
                    case_title, cybercrime_type = keyword_mapping[kw]
                    break
            else:
                case_title, cybercrime_type = ("Suspicious Activity", "Uncategorized")

            key = case_title

            if key not in case_reports:
                case_reports[key] = {
                    "Case Title": case_title,
                    "Cybercrime Type": cybercrime_type,
                    "Environment": "Simulated Flask Forum",
                    "Trigger Keywords": set(),
                    "User Activity": [],
                    "Tool Action": [
                        "Detected keywords in message",
                        "Extracted bitcoin address" if bitcoin_matches else "No bitcoin found",
                        "Captured user handle and timestamp",
                        "Logged post content",
                        "Assigned fake IP and user ID"
                    ],
                    "Evidence Collected": [
                        "Chat log",
                        "Forum post content",
                        "Wallet address" if bitcoin_matches else "No wallet address found"
                    ],
                    "Alert Raised": "MEDIUM",
                    "Flagged Posts": []
                }

            fake_ip = generate_fake_ip()
            user_id = generate_user_id(post.username)

            case_data = case_reports[key]
            case_data["Trigger Keywords"].update(matched)
            case_data["User Activity"].append(
                f"User '{post.username}' (ID: {user_id}) posted about: {', '.join(matched)}"
            )
            case_data["Flagged Posts"].append({
                "username": post.username,
                "user_id": user_id,
                "ip_address": fake_ip,
                "timestamp": post.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                "content": post.content.strip(),
                "keywords": matched,
                "bitcoin_addresses": bitcoin_matches,
                "confidence_score": score
            })
            case_scores.setdefault(key, []).append(score)

            if len(case_data["Flagged Posts"]) > 2:
                case_data["Alert Raised"] = "HIGH"

# ----------------------------
# Finalize & Save
# ----------------------------
final_reports = []
for report in case_reports.values():
    report["Trigger Keywords"] = list(report["Trigger Keywords"])
    final_reports.append(report)

# Add average confidence score per case
for case in final_reports:
    key = case["Case Title"]
    scores = case_scores.get(key, [])
    case["Average Confidence"] = round(sum(scores) / len(scores), 2) if scores else 0

with open("cases_data.json", "w", encoding="utf-8") as f:
    json.dump(final_reports, f, indent=4)

print(f"✅ {len(final_reports)} separate case reports saved to cases_data.json")
