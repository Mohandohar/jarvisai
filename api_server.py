from flask import Flask, request, jsonify
from jarvis_ai import JarvisAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)
jarvis = JarvisAI()

# Store conversation history
conversation_history = []

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "Jarvis AI is running ✓"})

@app.route('/command', methods=['POST'])
def process_command():
    """Process command from mobile app"""
    try:
        data = request.json
        command = data.get('command', '').lower()
        
        if not command:
            return jsonify({"error": "No command provided"}), 400
        
        # Store in history
        conversation_history.append({
            "user": command,
            "timestamp": str(__import__('datetime').datetime.now())
        })
        
        # Process command
        response = ""
        
        if "time" in command:
            response = jarvis.get_time()
        elif "date" in command:
            response = jarvis.get_date()
        elif "weather" in command:
            city = "Delhi"
            if "in " in command:
                city = command.split("in ")[-1].strip()
            response = jarvis.get_weather(city)
        elif "news" in command:
            response = jarvis.get_news()
        elif any(word in command for word in ["what", "who", "where", "how", "why", "tell"]):
            response = jarvis.ask_ai(command)
        else:
            response = "Command processed"
        
        conversation_history[-1]["assistant"] = response
        
        return jsonify({
            "success": True,
            "response": response,
            "command_id": len(conversation_history)
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/ask', methods=['POST'])
def ask_question():
    """Ask AI a question"""
    try:
        data = request.json
        question = data.get('question', '')
        
        if not question:
            return jsonify({"error": "No question provided"}), 400
        
        response = jarvis.ask_ai(question)
        
        return jsonify({
            "success": True,
            "question": question,
            "answer": response
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/weather', methods=['GET'])
def get_weather():
    """Get weather for a city"""
    try:
        city = request.args.get('city', 'Delhi')
        response = jarvis.get_weather(city)
        
        return jsonify({
            "success": True,
            "city": city,
            "weather": response
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/news', methods=['GET'])
def get_news():
    """Get latest news"""
    try:
        news = jarvis.get_news()
        
        return jsonify({
            "success": True,
            "news": news
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/history', methods=['GET'])
def get_history():
    """Get conversation history"""
    return jsonify({
        "success": True,
        "history": conversation_history[-10:]  # Last 10 messages
    })

@app.route('/clear-history', methods=['POST'])
def clear_history():
    """Clear conversation history"""
    global conversation_history
    conversation_history = []
    return jsonify({"success": True, "message": "History cleared"})

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    app.run(host=host, port=port, debug=debug)
