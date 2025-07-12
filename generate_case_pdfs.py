import json
import os
from fpdf import FPDF

# 🧼 Clean any unsupported characters
def clean(text):
    return str(text).replace("–", "-").replace("’", "'").replace("“", '"').replace("”", '"')

# 🗂 Create folder for reports
os.makedirs("pdf_reports", exist_ok=True)

# 📥 Load case data
with open("cases_data.json", "r", encoding="utf-8") as f:
    cases = json.load(f)

# 📄 Generate one PDF per case
for case in cases:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # 🏷 Header
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, clean(case["Case Title"]), ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Cybercrime Type: {case['Cybercrime Type']}", ln=True)
    pdf.cell(0, 10, f"Environment: {case['Environment']}", ln=True)
    pdf.cell(0, 10, f"Alert Level: {case['Alert Raised']}", ln=True)
    pdf.cell(0, 10, "", ln=True)

    # 🧠 Keywords
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Trigger Keywords:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, ", ".join(case["Trigger Keywords"]))
    pdf.cell(0, 10, "", ln=True)

    # 🧑‍💻 User Activity
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "User Activity:", ln=True)
    pdf.set_font("Arial", size=12)
    for activity in case["User Activity"]:
        pdf.multi_cell(0, 10, f"- {clean(activity)}")
    pdf.cell(0, 10, "", ln=True)

    # ⚙️ Tool Actions
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Tool Actions:", ln=True)
    pdf.set_font("Arial", size=12)
    for action in case["Tool Action"]:
        pdf.multi_cell(0, 10, f"- {clean(action)}")
    pdf.cell(0, 10, "", ln=True)

    # 📁 Evidence
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Evidence Collected:", ln=True)
    pdf.set_font("Arial", size=12)
    for ev in case["Evidence Collected"]:
        pdf.multi_cell(0, 10, f"- {clean(ev)}")
    pdf.cell(0, 10, "", ln=True)

    # 🧾 Flagged Posts
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Flagged Posts:", ln=True)
    pdf.set_font("Arial", size=12)
    for post in case["Flagged Posts"]:
        pdf.multi_cell(0, 10, f"User: {post['username']} | Time: {post['timestamp']}")
        pdf.multi_cell(0, 10, f"Content: {clean(post['content'])}")
        pdf.multi_cell(0, 10, f"Keywords: {', '.join(post['keywords'])}")
        if post["bitcoin_addresses"]:
            pdf.multi_cell(0, 10, f"Bitcoin Address(es): {', '.join(post['bitcoin_addresses'])}")
        pdf.cell(0, 5, "", ln=True)

    # 💾 Save PDF file
    filename = f"{clean(case['Case Title']).replace(' ', '_')}.pdf"
    pdf.output(os.path.join("pdf_reports", filename))

print("✅ All PDF reports saved in the 'pdf_reports' folder.")
