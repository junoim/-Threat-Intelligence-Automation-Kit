import hashlib
import os
import json
from datetime import datetime



# 🧮 Compute SHA256 hash of a file
def compute_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

# 📝 Log dictionary
log_entries = []

# 📂 Files to hash
target_files = ["cases_data.json"]
pdf_dir = "pdf_reports"

# ➕ Include PDFs if folder exists
if os.path.exists(pdf_dir):
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            target_files.append(os.path.join(pdf_dir, file))

# 📅 Timestamp
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 🧾 Log hash for each file
for filepath in target_files:
    if os.path.exists(filepath):
        hash_value = compute_hash(filepath)
        log_entries.append({
            "file": filepath,
            "hash": hash_value,
            "timestamp": now
        })
    else:
        log_entries.append({
            "file": filepath,
            "error": "File not found",
            "timestamp": now
        })

# 💾 Save to evidence log
with open("evidence_log.json", "w") as f:
    json.dump(log_entries, f, indent=4)

print("✅ Evidence hashes saved to evidence_log.json")
