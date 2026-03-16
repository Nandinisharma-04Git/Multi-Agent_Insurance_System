from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POLICIES_PATH = os.path.join(BASE_DIR, "policies.json")


def load_policies():
    with open(POLICIES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_input(data):
    errors = []

    try:
        age = int(data.get("age", 0))
        if age <= 0 or age > 120:
            errors.append("Age must be between 1 and 120.")
    except ValueError:
        errors.append("Age must be a valid number.")

    try:
        income = float(data.get("income", 0))
        if income <= 0:
            errors.append("Income must be a positive number.")
    except ValueError:
        errors.append("Income must be a valid number.")

    try:
        family_members = int(data.get("family_members", 1))
        if family_members <= 0:
            errors.append("Family members must be at least 1.")
    except ValueError:
        errors.append("Family members must be a valid number.")

    insurance_type = data.get("insurance_type")
    if insurance_type not in ["Health", "Life", "Vehicle"]:
        errors.append("Insurance type must be Health, Life, or Vehicle.")

    try:
        coverage_amount = float(data.get("coverage_amount", 0))
        if coverage_amount <= 0:
            errors.append("Coverage amount must be positive.")
    except ValueError:
        errors.append("Coverage amount must be a valid number.")

    risk_preference = data.get("risk_preference")
    if risk_preference not in ["Low", "Medium", "High"]:
        errors.append("Risk preference must be Low, Medium, or High.")

    return errors


def score_policy(policy, user_profile):
    # Simple heuristic scoring based on type, coverage, premium and risk
    score = 0

    # Match insurance type
    if policy.get("type") == user_profile["insurance_type"]:
        score += 30

    # Coverage closeness
    desired = user_profile["coverage_amount"]
    coverage = policy.get("coverage", 0)
    coverage_ratio = min(coverage / desired, desired / coverage) if coverage and desired else 0
    score += coverage_ratio * 30

    # Premium vs income and risk preference
    income = user_profile["income"]
    premium = policy.get("premium", 0)
    premium_ratio = premium / max(income, 1)
    if user_profile["risk_preference"] == "Low":
        score += max(0, 20 - premium_ratio * 100)
    elif user_profile["risk_preference"] == "Medium":
        score += max(0, 25 - premium_ratio * 80)
    else:  # High risk
        score += max(0, 30 - premium_ratio * 60)

    # Feature alignment (very simple)
    if user_profile["insurance_type"] == "Health" and "hospitalization" in policy.get("benefits_text", "").lower():
        score += 10
    if user_profile["insurance_type"] == "Vehicle" and "accident" in policy.get("benefits_text", "").lower():
        score += 10

    return score


def recommend_policies(user_profile):
    policies = load_policies()
    scored = []
    for p in policies:
        p_score = score_policy(p, user_profile)
        scored.append({**p, "score": round(p_score, 2)})
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:3]


def compare_policies(policy_ids):
    policies = load_policies()
    id_map = {str(p["id"]): p for p in policies}
    return [id_map[str(pid)] for pid in policy_ids if str(pid) in id_map]


def query_agent(question, policies=None):
    q = (question or "").lower()

    rules = [
        ("hospital", "hospitalization", "Most of our health policies include comprehensive hospitalization coverage, including room rent and basic procedures."),
        ("accident", "accident coverage", "Accident coverage is included in our vehicle policies and selected life insurance plans."),
        ("pre-existing", "pre existing", "Pre-existing conditions may come with a waiting period. Please review the policy terms for exact details."),
        ("cashless", "network hospital", "Our partner health policies support cashless treatment at a wide network of hospitals."),
        ("claim", "reimbursement", "Claims can be filed online with supporting documents; reimbursement is typically processed within 7–14 working days."),
    ]

    for keywords in rules:
        *keys, answer = keywords
        if any(k in q for k in keys):
            return answer

    if "premium" in q:
        return "Premium depends on coverage amount, age, and risk profile. Higher coverage and higher risk generally increase the premium."
    if "coverage" in q:
        return "Coverage refers to the maximum amount the insurer will pay for a covered claim during the policy period."
    if "deductible" in q:
        return "A deductible is the amount you must pay out of pocket before the insurance coverage starts paying."

    return "This is a simple rule-based assistant. Please ask about hospitalization, accident coverage, claims, or coverage details."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/result")
def result_page():
    # This route is only for direct navigation safety; real data flows via /recommend
    return render_template("result.html", policies=[], comparison=[])


@app.post("/recommend")
def recommend():
    data = request.get_json() or request.form

    errors = validate_input(data)
    if errors:
        return jsonify({"success": False, "errors": errors}), 400

    user_profile = {
        "age": int(data.get("age")),
        "income": float(data.get("income")),
        "family_members": int(data.get("family_members")),
        "insurance_type": data.get("insurance_type"),
        "coverage_amount": float(data.get("coverage_amount")),
        "risk_preference": data.get("risk_preference"),
    }

    policies = recommend_policies(user_profile)
    return jsonify({"success": True, "policies": policies})


@app.get("/compare")
def compare():
    ids = request.args.getlist("id")
    if not ids:
        return jsonify({"success": False, "error": "No policy IDs provided."}), 400
    policies = compare_policies(ids)
    return jsonify({"success": True, "policies": policies})


@app.post("/chat")
def chat():
    data = request.get_json() or {}
    question = data.get("question", "")
    answer = query_agent(question)
    return jsonify({"success": True, "answer": answer})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

