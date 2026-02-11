 MarketAI-Suite
# MarketAI Suite - Requirements

## Project Description
MarketAI Suite is an intelligent sales and marketing platform that leverages Groq's LLaMA 3.3 70B AI model to provide comprehensive marketing and sales support.

## Core Technologies
- **Python 3.8+**
- **Flask**: Web framework
- **Groq API**: AI inference using LLaMA 3.3 70B model
- **Python Requests**: HTTP client
- **HTML/CSS/JavaScript**: Frontend

## Features

### 1. Marketing Campaign Generator
- **Inputs**: Product, Target Audience, Platform
- **Outputs**:
  - Campaign Objectives
  - Target Positioning
  - 5 Content Ideas
  - 3 Ad Copies
  - Call-To-Action

### 2. Intelligent Sales Pitch Generator
- **Inputs**: Product, Customer Persona
- **Outputs**:
  - 30-Second Elevator Pitch
  - Core Value Proposition
  - Key Differentiators
  - Business Impact
  - Call-To-Action

### 3. Lead Scoring
- **Inputs**: Budget, Need, Urgency, Authority
- **Outputs**:
  - Final Score (0-100)
  - Score Breakdown
  - Category
  - Conversion Probability (%)
  - Recommended Action

## Setup
1. Create virtual environment.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up `.env` with `GROQ_API_KEY`.
