
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
print("TEMPLATE FOLDER:", app.template_folder)
print("APP ROOT:", app.root_path)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/simulate-scan", methods=["POST"])
def simulate_scan():
    # Safe, predefined demo scenarios only
    scenarios = {
        "normal": {
            "files_monitored": 5,
            "suspicious_events": 0,
            "threat_level": "Low",
            "message": "Normal simulated activity detected."
        },
        "medium": {
            "files_monitored": 10,
            "suspicious_events": 3,
            "threat_level": "Medium",
            "message": "Several suspicious demo events detected."
        },
        "high": {
            "files_monitored": 15,
            "suspicious_events": 8,
            "threat_level": "High",
            "message": "Multiple suspicious demo events detected."
        }
    }

    scenario_name = request.args.get("scenario", "normal").lower()
    result = scenarios.get(scenario_name)

    if result is None:
        return jsonify({
            "status": "error",
            "message": "Unknown demo scenario. Choose normal, medium, or high."
        }), 400

    return jsonify({
        "status": "success",
        "mode": "SIMULATION ONLY",
        **result
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False, use_reloader=False)
