# JARVIS AI - MOBILE APP SETUP

## Option 1: Desktop Preview (Recommended First)

Easy way to test the mobile app on your computer first!

### Step 1: Start the Backend API Server
```bash
cd c:\Users\06261\jarvisAi
python api_server.py
```

**You should see:**
```
 * Serving Jarvis AI API
 * Running on http://0.0.0.0:5000
```

### Step 2: Open New Terminal & Start Mobile App
```bash
cd c:\Users\06261\jarvisAi
python mobile_app.py
```

**You will see:**
- A window that looks like a phone
- Jarvis AI on the screen
- Input box to type commands
- Quick action buttons (Weather, News, Time)

### Step 3: Test It!

Type commands in the mobile app:
- "What's the weather?"
- "Tell me the news"
- "What time is it?"
- "What is Python?"

---

## Option 2: Using Batch File (Easiest)

Simply double-click:
```
run_mobile.bat
```

Then choose:
1. Run API Server only
2. Run Mobile App only
3. Run Both (recommended)

---

## Option 3: Deploy to Real Android Phone

### Requirements:
- Android phone
- USB cable
- Android SDK installed
- Buildozer installed

### Steps:

```bash
# 1. Install buildozer
pip install buildozer cython

# 2. Build APK
cd c:\Users\06261\jarvisAi
buildozer android debug

# 3. Install on phone
adb install bin/jarvisai-debug.apk

# 4. Or use buildozer to deploy
buildozer android debug deploy run
```

**Takes 10-20 minutes first time**

---

## Troubleshooting

### "Connection refused" on mobile app?

**Problem:** Mobile app can't connect to API server

**Solution 1 - Local Network:**
1. Open `mobile_app.py`
2. Find this line: `self.server_url = "http://localhost:5000"`
3. Change to your PC's IP: `self.server_url = "http://192.168.1.100:5000"`
4. Find your PC IP: `ipconfig` in PowerShell

**Solution 2 - Same PC:**
- Make sure API server is running
- Make sure mobile app is pointing to `localhost:5000`

### "Port 5000 already in use"?

```bash
# Kill the process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Mobile app window won't open?

```bash
# Run with verbose output
python mobile_app.py -h
```

### API responses are empty?

- Make sure `.env` file has API keys
- Check server terminal for errors
- Try `python api_server.py` manually

---

## API Endpoints (Testing)

Once API server is running, test these URLs:

```bash
# Health check
curl http://localhost:5000/health

# Send command
curl -X POST http://localhost:5000/command -H "Content-Type: application/json" -d "{\"command\": \"time\"}"

# Get weather
curl http://localhost:5000/weather?city=Mumbai

# Get news
curl http://localhost:5000/news

# Get conversation history
curl http://localhost:5000/history
```

---

## File Structure

```
jarvisAi/
├── api_server.py          <- Backend (run this first)
├── mobile_app.py          <- Mobile UI (run this second)
├── jarvis_ai.py           <- Core AI logic
├── run_mobile.bat         <- Quick launcher
├── MOBILE_SETUP.md        <- This file
└── .env                   <- Configuration
```

---

## Quick Commands

```bash
# Test API
python api_server.py

# Test Mobile
python mobile_app.py

# Test Desktop AI
python jarvis_ai.py

# Check Setup
python check_setup.py

# Use batch launcher
run_mobile.bat
```

---

## Next Steps

1. ✓ Run API server: `python api_server.py`
2. ✓ Run mobile preview: `python mobile_app.py`
3. ✓ Test all features
4. ✓ Deploy to Android (optional)

---

**Ready to go!** Start with `run_mobile.bat` or manually run the commands above.
