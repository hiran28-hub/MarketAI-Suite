from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


# Reusable AI function
def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Campaign Generator
@app.route("/campaign", methods=["POST"])
def campaign():
    product = request.form["product"]
    audience = request.form["audience"]
    platform = request.form["platform"]

    prompt = f"""
    You are a marketing strategist.

    Create a marketing campaign for:

    Product: {product}
    Target Audience: {audience}
    Platform: {platform}

    Respond strictly in this format:

    1. Campaign Objectives:
    2. Target Positioning:
    3. 5 Content Ideas:
    4. 3 Ad Copies:
    5. Call-To-Action:
    """

    output = generate_response(prompt)
    return render_template("campaign.html", output=output)


# Sales Pitch Generator
@app.route("/pitch", methods=["POST"])
def pitch():
    product = request.form["product"]
    persona = request.form["persona"]

    prompt = f"""
    You are a B2B sales expert.

    Create a sales pitch for:

    Product: {product}
    Customer Persona: {persona}

    Respond strictly in this format:

    1. 30-Second Elevator Pitch:
    2. Core Value Proposition:
    3. Key Differentiators:
    4. Business Impact:
    5. Call-To-Action:
    """

    output = generate_response(prompt)
    return render_template("pitch.html", output=output)


# Lead Scoring
@app.route("/lead", methods=["POST"])
def lead():
    budget = request.form["budget"]
    need = request.form["need"]
    urgency = request.form["urgency"]
    authority = request.form["authority"]

    prompt = f"""
    You are a sales qualification expert.

    Analyze the following lead:

    Budget: {budget}
    Need: {need}
    Urgency: {urgency}
    Authority: {authority}

    Score using:
    Budget (25)
    Need (30)
    Urgency (20)
    Authority (25)

    Respond strictly in this format:

    1. Final Score (0-100):
    2. Score Breakdown:
    3. Category:
    4. Conversion Probability (%):
    5. Recommended Action:
    """

    output = generate_response(prompt)
    return render_template("lead.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)
