# MarketAI Suite

MarketAI Suite is an all-in-one, AI-powered marketing and sales co-pilot designed to help businesses scale their outreach and branding efforts with professional-grade tools.

## 🚀 Key Features

### 1. User Authentication System
- **Secure Access**: SQLite-backed user registration and login.
- **Persistent History**: Every action is saved to your profile and can be viewed later.
- **Dedicated Activity Page**: A complete log of your previous tasks (Campaigns, Logos, etc.), accessible from the navigation bar.

### 2. Pitch Deck Creator
- **Gemini Powered**: Generates structured, high-conversion slide content (Titles, Subtitles, Bullet Points).
- **Local PPTX Generation**: Creates and downloads real `.pptx` files instantly using `python-pptx`.

### 3. Logo Generator
- **Multi-Model Engine**: Uses high-speed Flux (via Pollinations) with OpenAI DALL-E 3 fallback for reliable result delivery.
- **Commercial Quality**: Generates clean, professional minimalist logos on white backgrounds.

### 4. Cold Email Generator
- **Strategic B2B Outreach**: Crafts personalized, high-converting emails based on product, role, and industry.
- **Instant Download**: Save your emails as `.txt` files or copy them directly to clipboard.

### 5. Marketing Campaign Generator
- **Full Strategy**: Generates objectives, positioning, content ideas, and ad copies using the Gemini model.

### 6. Lead Scoring
- **Urgency Analysis**: Data-backed qualification for sales leads based on Budget, Need, Urgency, and Authority.

## 🛠️ Tech Stack
- **Backend**: Python 3.8+, Flask, SQLite3
- **AI Inference**: 
  - **Text**: Google Gemini (model: `gemini-flash-latest`)
  - **Images**: Flux (via Pollinations), OpenAI DALL-E 3
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism), JavaScript (Fetch API, Clipboard API)
- **Primary Libraries**: 
  - `flask`: Web framework
  - `google-generativeai`: Gemini AI access
  - `openai`: DALL-E 3 AI access
  - `python-pptx`: Presentation generation
  - `requests`: API communication
  - `python-dotenv`: Environment variable management
  - `werkzeug`: Secure password hashing

## ⚙️ Setup & Installation

1. **Clone the Repository**
2. **Setup Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_key_here
   OPENAI_API_KEY=your_openai_key_here
   ```
5. **Run the Application**
   ```bash
   python app.py
   ```
   Access the suite at `http://127.0.0.1:5000`

## 📊 Database Management
The project uses `marketai.db` (SQLite). On first run, the system automatically initializes:
- `users` table: For profile and credential management.
- `activities` table: For persistent task logging.

## 📁 File Downloads
All generated assets (logos, pitch decks, cold emails) are available for instant download. Pitch decks and logos are saved locally in the `static/generated/` folder.
