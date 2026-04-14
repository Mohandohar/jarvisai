# 🚀 Quick Start Guide - Jarvis AI

## Step 1: Setup (5 minutes)

```bash
cd c:\Users\06261\jarvisAi

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment
cp .env.example .env
# Edit .env and add your API keys
```

## Step 2: Get Free API Keys (2 minutes)

### Option A: Google Gemini (RECOMMENDED - FREE)
1. Go to: https://ai.google.dev/
2. Click "Get API Key"
3. Create new API key
4. Copy and paste in `.env` as `GEMINI_API_KEY`

### Option B: ChatGPT (Paid)
1. Go to: https://platform.openai.com/account/api-keys
2. Create new key
3. Paste in `.env` as `OPENAI_API_KEY`

### Weather API (FREE)
1. Go to: https://openweathermap.org/api
2. Sign up for free tier
3. Get API key from account settings
4. Paste in `.env` as `WEATHER_API_KEY`

### News API (FREE)
1. Go to: https://newsapi.org/
2. Sign up
3. Copy API key
4. Paste in `.env` as `NEWS_API_KEY`

---

## Step 3: Test Desktop Version

### Test 1: Basic Commands (Terminal Only)
```bash
python jarvis_ai.py
# Type: hello
# Type: time
# Type: exit
```

### Test 2: API Server + Mobile App Preview
```bash
# Terminal 1 - Start API server
python api_server.py
# Output: Running on http://0.0.0.0:5000

# Terminal 2 - Start mobile app (Kivy preview)
python mobile_app.py
```

Then in the app window:
- Type "What's the weather?"
- Click "Weather" button
- Type "Tell me about AI"

---

## Step 4: Deploy to Android

### Prerequisites
```bash
# Install buildozer and dependencies
pip install buildozer cython

# Install Java (required for buildozer)
# Windows: Download from oracle.com

# Install Android SDK
# Download Android Studio from developer.android.com
```

### Build APK
```bash
# Navigate to project folder
cd c:\Users\06261\jarvisAi

# Build for Android
buildozer android debug

# This will take 10-20 minutes first time
# APK will be saved in: bin/jarvisai-debug.apk
```

### Install on Phone
```bash
# Enable Developer Mode on phone:
# Settings > About > Build Number (tap 7 times)
# Settings > Developer options > USB Debugging (ON)

# Connect phone to PC via USB

# Install app
adb install bin/jarvisai-debug.apk

# Or use buildozer deploy
buildozer android debug deploy run
```

---

## Common Issues & Fixes

### ❌ "No API key found" error
**Fix:** Make sure `.env` file exists and has your API keys
```bash
cat .env  # Verify file exists
```

### ❌ Audio recording failed
**Fix:** Install PortAudio
```bash
# Windows already has it, but try:
pip install --upgrade sounddevice
```

### ❌ Kivy not found
**Fix:**
```bash
pip install --upgrade kivy
```

### ❌ Connection refused on mobile
**Fix:** Update server IP in `mobile_app.py`
```python
# Find this line:
self.server_url = "http://localhost:5000"

# Change to your PC's IP (e.g., 192.168.x.x):
self.server_url = "http://192.168.1.100:5000"

# Find your PC IP:
# Windows: ipconfig | findstr "IPv4"
```

### ❌ Buildozer fails on Windows
**Easy Alternative: Use GitHub Codespaces**
- Push code to GitHub
- Use Codespaces (free Ubuntu environment)
- Build APK there (Linux is better for Android builds)

---

## Command Examples

After setup, try these commands:

```
"Hello Jarvis"
→ Jarvis: Hello boss! How can I help you?

"What's the weather?"
→ Current temperature and conditions

"Tell me about space"
→ AI-generated answer about space

"What time is it?"
→ Current time

"Show me news"
→ Latest headlines

"What is Python?"
→ Explanation of Python

"Bye"
→ Jarvis: Goodbye boss!
```

---

## Deployment Options

### Option 1: Phone (Native Android)
- Pros: Works offline, fast, no WiFi needed
- Cons: Need to build & sign APK
- Time: 30 mins

### Option 2: Local Network
- Pros: Easy to test, no build needed
- Cons: Requires WiFi
- Time: 5 mins

### Option 3: Cloud Deployment
- Pros: Works from anywhere
- Cons: Need server (AWS, Heroku, etc.)
- Time: 1 hour

---

## Next Steps

1. ✅ Complete setup
2. ✅ Test desktop version
3. ✅ Try all commands
4. ✅ Deploy to Android (Optional)
5. ✅ Customize with your own features!

---

## Support

**Questions?** Check the full README.md or the code comments!

Good luck! 🚀
