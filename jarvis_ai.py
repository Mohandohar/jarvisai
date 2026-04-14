import pyttsx3
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import requests
import json
from datetime import datetime
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class JarvisAI:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.recognizer = sr.Recognizer()
        self.openai_key = os.getenv("OPENAI_API_KEY", "")
        self.weather_key = os.getenv("WEATHER_API_KEY", "")
        
    def speak(self, text: str, show_text: bool = True):
        """Convert text to speech"""
        if show_text:
            print(f"🤖 Jarvis: {text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"❌ Error speaking: {e}")
    
    def record_audio(self, duration: int = 4, fs: int = 44100) -> str:
        """Record audio from microphone"""
        print("🎤 Listening...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        wav.write("voice.wav", fs, recording)
        return "voice.wav"
    
    def listen(self) -> str:
        """Listen to user's voice command"""
        try:
            audio_file = self.record_audio()
            with sr.AudioFile(audio_file) as source:
                audio = self.recognizer.record(source)
            command = self.recognizer.recognize_google(audio)
            print(f"👤 You: {command}")
            return command.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't understand that")
            return ""
        except Exception as e:
            print(f"❌ Error: {e}")
            return ""
    
    def get_weather(self, city: str = "Delhi") -> str:
        """Fetch weather information"""
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1a2b3c4d5e6f7g8h9i0j"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                temp = data['main']['temp'] - 273.15
                description = data['weather'][0]['description']
                return f"In {city}, it's {temp:.1f}°C and {description}"
            return f"Couldn't fetch weather for {city}"
        except Exception as e:
            print(f"Weather error: {e}")
            return "Weather service unavailable"
    
    def get_news(self) -> str:
        """Fetch latest news headlines"""
        try:
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=demo"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                articles = response.json().get('articles', [])[:3]
                news = "Here are the top headlines: "
                for i, article in enumerate(articles, 1):
                    news += f"{i}. {article['title']}. "
                return news
            return "Couldn't fetch news"
        except Exception as e:
            print(f"News error: {e}")
            return "News service unavailable"
    
    def ask_ai(self, question: str) -> str:
        """Ask ChatGPT/Gemini for answer"""
        try:
            # Using Google Generative AI (Gemini) - free alternative
            import google.generativeai as genai
            
            genai.configure(api_key=os.getenv("GEMINI_API_KEY", ""))
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(question)
            return response.text[:200]  # Return first 200 chars
        except Exception as e:
            print(f"AI error: {e}")
            return "I need an API key to answer questions. Please set GEMINI_API_KEY"
    
    def get_time(self) -> str:
        """Get current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        return f"It's {current_time}"
    
    def get_date(self) -> str:
        """Get current date"""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}"
    
    def process_command(self, command: str) -> bool:
        """Process user commands"""
        
        if "hello" in command or "hi" in command:
            self.speak("Hello boss! How can I help you?")
            return True
        
        elif "time" in command:
            self.speak(self.get_time())
            return True
        
        elif "date" in command:
            self.speak(self.get_date())
            return True
        
        elif "weather" in command:
            city = "Delhi"  # Default city
            if "in " in command:
                city = command.split("in ")[-1].strip()
            weather = self.get_weather(city)
            self.speak(weather)
            return True
        
        elif "news" in command:
            news = self.get_news()
            self.speak(news)
            return True
        
        elif any(word in command for word in ["what", "who", "where", "how", "why", "tell"]):
            answer = self.ask_ai(command)
            self.speak(answer)
            return True
        
        elif "exit" in command or "quit" in command or "bye" in command:
            self.speak("Goodbye boss! See you soon")
            return False
        
        else:
            self.speak("I didn't understand that. Try asking about weather, time, news, or anything else!")
            return True
    
    def run(self):
        """Main loop"""
        self.speak("Hey boss, I'm Jarvis! Your personal AI assistant. How can I help?")
        
        while True:
            command = self.listen()
            if command:
                should_continue = self.process_command(command)
                if not should_continue:
                    break

if __name__ == "__main__":
    jarvis = JarvisAI()
    jarvis.run()
