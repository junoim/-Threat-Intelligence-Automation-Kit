# 🕵️‍♀️ Threat Intelligence Automation Kit

The **Threat Intelligence Automation Kit** is a Flask-based web app that simulates a dark web forum and helps identify potential cybercrime-related posts. It uses keyword-based detection, threat scoring, and digital evidence hashing to assist in passive cybercrime monitoring and reporting.

This tool is built to **simulate** how suspicious content might appear in online forums or marketplaces, and how an analyst or law enforcement agency might automate the detection and documentation of such threats.

---

##  Features

-  **Fake dark web forum simulation**
-  Users can **post messages** (simulated actors)
-  **Automated keyword detection** with confidence scoring
-  **SHA-256 hashing** of each post for tamper-proof records
-  Generates **fake IP addresses** and **user IDs**
-  **Threat scoring** with configurable weights
-  **Markdown to PDF export** of posts with scores
-  Visual tools: **word cloud** and **timeline charts**
-  Easily update **rulesets (keywords and weights)** via JSON

---

##  Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Database:** SQLite (SQLAlchemy ORM)
- **Other Tools/Libraries:**
  - `hashlib` for evidence hashing
  - `random`, `re`, `json` for simulation and logic
  - `matplotlib`, `wordcloud` for visualization
  - `pdfkit` / `markdown2` for PDF export

---

##  Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/threat-intel-kit.git
cd threat-intel-kit
```

2. **Create a virtual environment and activate it**
```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

---

##  Running the App

1. **Run the Flask server**
```bash
python app.py
```

2. **Open your browser and visit:**
```
http://127.0.0.1:5000/
```

---

## How It Works

- When a user **posts a message**, the system:
  1. Scans the text using a **customizable keyword ruleset** (in `keywords.json`)
  2. Assigns a **threat score** based on keyword weightings
  3. Computes a **SHA-256 hash** of the post for evidence preservation
  4. Simulates a **random IP address** and **user identity**
  5. Displays the threat level (Low, Medium, High)

- Posts and their scores can be:
  - **Exported as PDFs**
  - **Visualized as a word cloud**
  - **Plotted over time (timeline graph)**

---

## 📁 Project Structure

```
threat-intel-kit/
├── app.py                  # Main Flask app
├── templates/              # HTML pages
│   ├── login.html
│   ├── forum.html
│   ├── dashboard.html
│   └── export.html
├── static/                 # CSS and JS (if any)
│   └── style.css
├── keywords.json           # List of suspicious keywords with weights
├── hash_store/             # Stores hash of each post
├── exports/                # Exported PDFs or markdown
├── requirements.txt        # Python dependencies
└── README.md
```

---


##  Disclaimer

This project is created **strictly for educational and research purposes**. It simulates how dark web forums can be monitored and does **not** access or analyze real dark web content.

Do **not** use this for unauthorized surveillance or unethical purposes.

---

##  Author

**Shradha Mohanty**  
Cybersecurity & Threat Intelligence Enthusiast  
[GitHub](https://github.com/junoim) • [Email](mailto:shradhamohanty790@gmail.com)

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).
