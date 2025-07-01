from flask import Flask, render_template, request
import os

app = Flask(__name__)

symptom_disease_map = {
    "fever": "Fever",
    "cold": "Cold",
    "headache": "Headache",
    "sugar": "Diabetes",
    "diabetes": "Diabetes",
    "bp": "Hypertension",
    "high pressure": "Hypertension",
    "asthma": "Asthma",
    "cough": "Cold",
    "body pain": "Fever",
    "vomiting": "Typhoid",
    "loose motion": "Diarrhea",
    "allergy": "Allergy",
    "malaria": "Malaria",
    "chills": "Malaria"
}

disease_medicine_map = {
    "Fever": {
        "medicine": "Paracetamol", "dosage": "500mg", "timing": "Twice a day after food"
    },
    "Cold": {
        "medicine": "Cetrizine", "dosage": "10mg", "timing": "Once a day at night"
    },
    "Headache": {
        "medicine": "Aspirin", "dosage": "300mg", "timing": "Once after food"
    },
    "Diabetes": {
        "medicine": "Metformin", "dosage": "500mg", "timing": "Twice daily with meals"
    },
    "Hypertension": {
        "medicine": "Amlodipine", "dosage": "5mg", "timing": "Once in the morning"
    },
    "Asthma": {
        "medicine": "Salbutamol Inhaler", "dosage": "100mcg", "timing": "2 puffs every 6 hrs"
    },
    "Malaria": {
        "medicine": "Chloroquine", "dosage": "600mg + 300mg", "timing": "As per protocol"
    },
    "Typhoid": {
        "medicine": "Ciprofloxacin", "dosage": "500mg", "timing": "Twice a day for 7 days"
    },
    "Allergy": {
        "medicine": "Loratadine", "dosage": "10mg", "timing": "Once daily"
    },
    "Diarrhea": {
        "medicine": "ORS + Loperamide", "dosage": "ORS + 2mg", "timing": "After each loose motion"
    }
}

@app.route("/", methods=["GET", "POST"])
def chat():
    response = None
    user_input = ""

    if request.method == "POST":
        user_input = request.form["symptom"].lower()
        detected_disease = None

        for keyword, disease in symptom_disease_map.items():
            if keyword in user_input:
                detected_disease = disease
                break

        if detected_disease:
            data = disease_medicine_map.get(detected_disease)
            response = f"""
                I think you might have <b>{detected_disease}</b>.<br>
                💊 <b>Medicine:</b> {data['medicine']}<br>
                📏 <b>Dosage:</b> {data['dosage']}<br>
                🕒 <b>Timing:</b> {data['timing']}
            """
        else:
            response = "🤔 I'm not sure. Please describe your symptoms more clearly."

    return render_template("chat.html", user_input=user_input, response=response)

# ✅ Fix for Render deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
