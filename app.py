from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ── KLEIT Knowledge Base ───────────────────────────────────────────
KLEIT_INFO = {
    "about": """
KLE Institute of Technology (KLEIT) is a premier engineering college located in 
Hubli, Karnataka, India. It is run by the KLE Society and is affiliated to 
Visvesvaraya Technological University (VTU). KLEIT is ISO 21001:2018 certified 
and consistently ranks well in NIRF rankings.
📍 Location: Hubli, Karnataka, India
📞 Phone: 0836 223 2681
🌐 Website: https://kleit.ac.in
    """,

    "courses_ug": """
KLEIT offers the following Undergraduate (B.E.) programmes:
1. 💻 Computer Science & Engineering (CSE)
2. ⚡ Electronics & Communication Engineering (ECE)
3. 🔧 Mechanical Engineering (ME)
4. ⚙️ Electrical & Electronics Engineering (EEE)
5. 🏗️ Civil Engineering (CE)
All UG programmes are 4-year full-time B.E. degrees affiliated to VTU.
    """,

    "courses_pg": """
KLEIT offers the following Postgraduate programme:
1. 🖥️ Master of Computer Applications (MCA)
This is a 2-year full-time programme affiliated to VTU.
    """,

    "admission_process": """
Admission Process at KLEIT:

For B.E. (Undergraduate):
1. Appear for KCET (Karnataka Common Entrance Test) or COMEDK exam
2. Register on KEA portal (kea.kar.nic.in) for KCET counselling
3. Choose KLEIT and preferred branch during seat allotment
4. Report to college with required documents

For MCA (Postgraduate):
1. Appear for KMAT or PGCET exam
2. Register on KEA portal for counselling
3. Choose KLEIT MCA during seat allotment

📌 Tip: Always check the official KEA website for exact dates every year!
    """,

    "eligibility": """
Eligibility Criteria at KLEIT:

For B.E. (Undergraduate):
✅ Must have passed 12th / PUC with Physics, Mathematics as compulsory subjects
✅ Minimum 45% marks in PCM (40% for SC/ST candidates)
✅ Must have valid KCET or COMEDK score

For MCA (Postgraduate):
✅ Bachelor's degree in any discipline with Mathematics at 10+2 or graduation level
✅ Minimum 50% marks in graduation
✅ Valid KMAT / PGCET score
    """,

    "fee": """
Fee Structure at KLEIT (Approximate):

B.E. Programmes (per year):
- Government Quota (CET): ~₹55,000 - ₹75,000 per year
- Management Quota: ~₹1,00,000 - ₹1,50,000 per year
- NRI Quota: Higher fees apply

MCA Programme:
- Fees vary based on quota — check official site

💳 Online Payment: Available via SBI Collect
🔗 Official Fee Page: https://kleit.ac.in/fee-structure/

⚠️ Note: Exact fees change every year. Always verify at kleit.ac.in
    """,

    "departments": """
KLEIT has the following departments:

Engineering Departments:
- Computer Science & Engineering (CSE)
- Electronics & Communication Engineering (ECE)
- Mechanical Engineering (ME)
- Electrical & Electronics Engineering (EEE)
- Civil Engineering (CE)

Basic Science Departments:
- Chemistry, Mathematics, Physics, Humanities

Postgraduate:
- Master of Computer Applications (MCA)
    """,

    "contact": """
📞 Contact KLEIT:

Phone: 0836 223 2681
Website: https://kleit.ac.in
Contact Page: https://kleit.ac.in/contact-us/
Online Payment: https://kleit.ac.in (SBI Collect)

🕐 Office Hours: Monday to Saturday, 9:00 AM – 5:00 PM
    """,

    "placements": """
🏢 Placements at KLEIT:

KLEIT has an active Training & Placement Cell that connects students with top companies.
- Regular placement drives are conducted on campus
- Companies from IT, Core Engineering, and Management sectors visit
- Students are trained in aptitude, soft skills, and technical interviews

🔗 More info: https://kleit.ac.in/placements/
    """,

    "facilities": """
🏫 Campus Facilities at KLEIT:

- 📚 Library & Information Center with digital resources
- 🌐 High-speed Internet & WiFi across campus
- 🔬 Well-equipped laboratories for all departments
- 🏋️ Physical Education & Sports facilities
- 🎭 Cultural activities via Sangeetha Vrinda committee
- 🩺 Youth Red Cross Wing
- 📖 E-Resources portal: https://e-resources.kleit.ac.in
- 🎥 NPTEL & IMPARTUS video lectures
    """,

    "kcet": """
KCET (Karnataka Common Entrance Test) Guide for KLEIT:

1. 📝 Exam conducted by KEA (Karnataka Examinations Authority)
2. 📚 Subjects: Physics, Chemistry, Mathematics (Biology optional)
3. ✅ Eligibility: PUC/12th with PCM, Karnataka domicile
4. 🏫 After results: Register on kea.kar.nic.in for counselling
5. 🎯 Choose KLEIT + your preferred branch during option entry
6. 📄 Documents needed:
   • KCET scorecard
   • PUC marks card
   • SSLC marks card
   • Caste certificate (if applicable)
   • Income certificate (if applicable)
   • Transfer certificate
   • Migration certificate

🔗 KEA Website: https://kea.kar.nic.in
    """,

    "comedk": """
COMEDK Guide for KLEIT:

1. COMEDK UGET is for private engineering colleges in Karnataka
2. Register at comedk.org and appear for the online exam
3. After results, participate in COMEDK counselling
4. Select KLEIT and preferred branch
5. Management quota seats are filled through COMEDK

🔗 COMEDK Website: https://www.comedk.org
    """,
}


def get_response(message):
    msg = message.lower().strip()

    # Greetings
    if any(w in msg for w in ["hello", "hi", "hey", "start", "help"]):
        return (
            "👋 Welcome to the KLEIT Admission Guidance Chatbot!\n\n"
            "I can help you with:\n"
            "🎓 Courses & Programmes\n"
            "📋 Admission Process\n"
            "✅ Eligibility Criteria\n"
            "💰 Fee Structure\n"
            "🏫 Campus Facilities\n"
            "🏢 Placements\n"
            "📞 Contact Info\n"
            "📝 KCET / COMEDK Guidance\n\n"
            "Just ask me anything about KLEIT! 😊"
        )

    # About KLEIT
    elif any(w in msg for w in ["about", "what is kleit", "kleit info", "college info", "overview"]):
        return KLEIT_INFO["about"]

    # Courses
    elif any(w in msg for w in ["mca", "postgraduate", "pg course", "master"]):
        return KLEIT_INFO["courses_pg"]

    elif any(w in msg for w in ["course", "programme", "branch", "department", "be ", "b.e", "undergraduate", "ug"]):
        return KLEIT_INFO["courses_ug"]

    # Admission
    elif any(w in msg for w in ["admission", "how to apply", "apply", "join", "enroll", "get admission"]):
        return KLEIT_INFO["admission_process"]

    # Eligibility
    elif any(w in msg for w in ["eligib", "criteria", "qualify", "requirement", "marks needed", "percentage"]):
        return KLEIT_INFO["eligibility"]

    # Fees
    elif any(w in msg for w in ["fee", "cost", "fees", "payment", "how much", "tuition", "charges"]):
        return KLEIT_INFO["fee"]

    # KCET
    elif any(w in msg for w in ["kcet", "kea", "cet", "karnataka entrance"]):
        return KLEIT_INFO["kcet"]

    # COMEDK
    elif any(w in msg for w in ["comedk", "management quota", "uget"]):
        return KLEIT_INFO["comedk"]

    # Placements
    elif any(w in msg for w in ["placement", "job", "recruit", "company", "package", "salary", "career"]):
        return KLEIT_INFO["placements"]

    # Facilities
    elif any(w in msg for w in ["facilit", "campus", "library", "wifi", "hostel", "lab", "infrastructure"]):
        return KLEIT_INFO["facilities"]

    # Contact
    elif any(w in msg for w in ["contact", "phone", "address", "location", "reach", "email", "office"]):
        return KLEIT_INFO["contact"]

    # Departments
    elif any(w in msg for w in ["cse", "ece", "mechanical", "civil", "electrical", "eee", "me dept"]):
        return KLEIT_INFO["departments"]

    # Goodbye
    elif any(w in msg for w in ["bye", "thank", "thanks", "exit", "done"]):
        return "Thank you for using the KLEIT Chatbot! 🎓 Best of luck with your admission. Feel free to visit kleit.ac.in for more details! 😊"

    # Fallback
    else:
        return (
            "🤔 I'm not sure about that. Here's what I can help with:\n\n"
            "Type any of these:\n"
            "• 'courses' — available programmes\n"
            "• 'admission' — how to apply\n"
            "• 'eligibility' — who can apply\n"
            "• 'fees' — fee structure\n"
            "• 'kcet' — KCET guidance\n"
            "• 'placements' — placement info\n"
            "• 'contact' — reach KLEIT\n"
            "• 'facilities' — campus facilities"
        )


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_reply = get_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)