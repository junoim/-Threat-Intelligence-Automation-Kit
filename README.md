# -Threat-Intelligence-Automation-Kit
A Flask-based web application designed to simulate dark web forum activity, detect suspicious posts, and assist law enforcement in passive cybercrime detection. This tool performs automated keyword-based threat scoring, evidence hashing, and provides exportable threat reports.

## Features
-  **Login-protected fake forum** for simulation
-  Users can **post messages** (simulated threat actors)
-  Intelligent **keyword-based detection engine** using weights
-  Each post is **hashed (SHA-256)** for evidence preservation
-  Randomized **fake IPs, User IDs**
-  **Threat confidence scoring**
-  **Export forum posts and scores to PDF**
-  Visualizations: **Word Cloud, Timeline View**
-  Built-in **ruleset system** for dynamic keyword weights

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (simple)
- **Database**: SQLite (via SQLAlchemy)
- **Other**: `hashlib`, `base64`, `random`, `re`, `json`, `matplotlib`, `wordcloud`, `pdfkit`




