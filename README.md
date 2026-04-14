# 🤖 Jarvis AI - Personal Mobile Assistant

A Python-based AI assistant with voice recognition, natural language processing, and smart features for your phone.

## Features

✅ **Voice Commands** - Talk to Jarvis naturally  
✅ **AI Q&A** - Ask anything using ChatGPT/Gemini  
✅ **Weather Updates** - Real-time weather information  
✅ **News Headlines** - Latest news from around the world  
✅ **Time & Date** - Quick access to current time and date  
✅ **Smart Response** - Context-aware answers  
✅ **Multi-Platform** - Desktop (Python) + Android (Kivy)  

---

## Installation

### 1. **Clone/Setup the Project**
```bash
cd jarvisAi
pip install -r requirements.txt
```

### 2. **Get API Keys** (Free)

**For AI Responses:**
- **Google Gemini** (Free): https://ai.google.dev/
- OR **OpenAI ChatGPT** (Paid): https://platform.openai.com/

**For Weather:**
- **OpenWeatherMap** (Free tier): https://openweathermap.org/api

**For News:**
- **NewsAPI** (Free): https://newsapi.org/

### 3. **Configure Environment**
```bash
# Copy example config
cp .env.example .env

# Edit .env and add your API keys
GEMINI_API_KEY=your_key_here
WEATHER_API_KEY=your_key_here
NEWS_API_KEY=your_key_here
```

---

## Usage

### Option 1: Desktop (Voice + Terminal)
```bash
python jarvis_ai.py
```
- Speak your commands aloud
- Jarvis responds with voice and text
- Say "exit" to quit

**Example Commands:**
- "Hello Jarvis"
- "What's the weather in Mumbai?"
- "Tell me the latest news"
- "What time is it?"
- "What is Python?"

---

### Option 2: Desktop API Server (for Mobile App)
```bash
python api_server.py
```
Server runs at: `http://localhost:5000`

**API Endpoints:**

```bash
# Health check
GET http://localhost:5000/health

# Send command
POST http://localhost:5000/command
Body: {"command": "what's the weather"}

# Ask question
POST http://localhost:5000/ask
Body: {"question": "what is machine learning?"}

# Get weather
GET http://localhost:5000/weather?city=Mumbai

# Get news
GET http://localhost:5000/news

# Get conversation history
GET http://localhost:5000/history

# Clear history
POST http://localhost:5000/clear-history
```

---

### Option 3: Mobile App (Android)

#### A. Run on Desktop (Kivy Preview)
```bash
# Install Kivy
pip install kivy

# Run the app
python mobile_app.py
```

#### B. Deploy to Android

**Step 1: Install Buildozer**
```bash
pip install buildozer cython
```

**Step 2: Create buildozer.spec**
```bash
buildozer android debug
```

**Step 3: Configure spec file**
Edit `buildozer.spec`:
```ini
title = Jarvis AI
package.name = jarvisai
package.domain = org.jarvis
requirements = python3,kivy,requests

# Set permissions for Android
android.permissions = INTERNET,RECORD_AUDIO

# Set API level
android.api = 31
```

**Step 4: Build APK**
```bash
buildozer android debug
# Output: bin/jarvisai-debug-1.0-debug.apk
```

**Step 5: Install on Phone**
```bash
buildozer android debug deploy run
# OR
adb install bin/jarvisai-debug-1.0-debug.apk
```

---

## Project Structure

```
jarvisAi/
├── app.py                    # Original basic version
├── jarvis_ai.py             # Enhanced AI with features
├── api_server.py            # Flask API backend
├── mobile_app.py            # Kivy Android app
├── requirements.txt         # Python dependencies
├── .env.example            # Configuration template
└── README.md               # This file
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Your Phone (Android)                       │
│                   ┌──────────────────┐                       │
│                   │  Jarvis Mobile   │                       │
│                   │      (Kivy)      │                       │
│                   └──────┬───────────┘                       │
│                          │ HTTP REST API                    │
│                          ▼                                  │
│                   ┌──────────────────┐                       │
│                   │  Flask Server    │                       │
│                   │ (api_server.py)  │                       │
│                   └──────┬───────────┘                       │
│                          │                                  │
├─────────────────────────┼──────────────────────────────────┤
│              Backend Processing (jarvis_ai.py)              │
│          ┌──────────────┬──────────────┬──────────────┐     │
│          ▼              ▼              ▼              ▼     │
│    ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│    │  Voice   │  │   AI     │  │ Weather  │  │   News   │ │
│    │ Recogn.  │  │ (Gemini) │  │  (API)   │  │  (API)   │ │
│    └──────────┘  └──────────┘  └──────────┘  └──────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## Troubleshooting

**Q: Audio recording not working?**
```bash
# Install PortAudio
# Ubuntu/Debian:
sudo apt-get install portaudio19-dev

# macOS:
brew install portaudio

# Windows: Already included with sounddevice
```

**Q: Google API Key errors?**
- Make sure `.env` file exists and has correct keys
- Restart the app after updating .env

**Q: Connection refused on mobile?**
- Update server URL in `mobile_app.py`: Change to your PC's IP
- Example: `self.server_url = "http://192.168.1.100:5000"`
- PC and phone must be on same WiFi

**Q: Low audio quality?**
- Adjust recording duration in code: `duration = 5` (line in `jarvis_ai.py`)
- Check microphone permissions

---

## Features Roadmap

- [ ] Voice wake-word detection ("OK Jarvis")
- [ ] Smart home integration (lights, switches)
- [ ] Calendar & reminders
- [ ] WhatsApp/SMS automation
- [ ] Offline mode with local AI
- [ ] Music player control
- [ ] Navigation & maps
- [ ] Voice conversations storage

---

## Contributing

Feel free to:
- Add new commands
- Improve AI responses
- Add more API integrations
- Fix bugs

Submit pull requests on GitHub!

---

## License

This project is open source and available under the MIT License.

---

## Support

For issues and questions:
1. Check README troubleshooting
2. Review error messages
3. Check API keys configuration
4. Ensure all dependencies are installed

---

**Made with ❤️ by Jarvis AI**
