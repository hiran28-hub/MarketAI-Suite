from flask import Flask, render_template, request
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Groq
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Reusable AI function
def generate_response(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to Groq API: {str(e)}"

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Campaign Generator
@app.route("/campaign", methods=["GET", "POST"])
def campaign():
    output = None
    if request.method == "POST":
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
@app.route("/pitch", methods=["GET", "POST"])
def pitch():
    output = None
    if request.method == "POST":
        product = request.form["product"]
        persona = request.form["persona"]
        industry = request.form.get("industry", "Not specified")
        size = request.form.get("size", "Not specified")
        budget = request.form.get("budget", "Not specified")
        
        prompt = f"""
        You are a B2B sales expert.
        
        Create a sales pitch for:
        Product: {product}
        Customer Persona: {persona}
        Industry: {industry}
        Company Size: {size}
        Budget Range: {budget}
        
        Respond strictly in this format:
        
        1. 30-Second Elevator Pitch:
        2. Core Value Proposition:
        3. Key Differentiators:
        4. Business Impact:
        5. Call-To-Action:
        """
        output = generate_response(prompt)
    return render_template("pitch.html", output=output)

import re

# Lead Scoring
@app.route("/lead", methods=["GET", "POST"])
def lead():
    output = None
    score = 0
    probability = 0
    if request.method == "POST":
        name = request.form["name"]
        budget = request.form["budget"]
        need = request.form["need"]
        urgency = request.form["urgency"]
        notes = request.form.get("notes", "None")

        prompt = f"""
        You are a sales qualification expert.
        
        Analyze the following lead:
        Name: {name}
        Budget: {budget}
        Need: {need}
        Urgency: {urgency}
        Additional Notes: {notes}
        
        Score using:
        Budget (25)
        Need (30)
        Urgency (20)
        Authority/Fit (25)
        
        Respond strictly in this format:
        
        1. Final Score (0-100): [Score]
        2. Score Breakdown:
        3. Category:
        4. Conversion Probability (%):
        5. Recommended Action:
        """
        output = generate_response(prompt)
        
        # Extract score and probability
        try:
            score_match = re.search(r"Final Score.*?:.*?(\d+)", output)
            if score_match:
                score = int(score_match.group(1))
        except:
            score = 0

        try:
            prob_match = re.search(r"Conversion Probability.*?:.*?(\d+)%", output)
            if prob_match:
                probability = int(prob_match.group(1))
            else:
                probability = 0
        except:
            probability = 0
            
    return render_template("lead.html", output=output, score=score, probability=probability)

if __name__ == "__main__":
    app.run(debug=True)
