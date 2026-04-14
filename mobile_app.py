"""
Jarvis AI - Android Mobile App using Kivy Framework
This can be packaged for Android using buildozer
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import requests
import threading
from datetime import datetime

# Set window size for mobile
Window.size = (400, 800)

class JarvisApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.server_url = "http://localhost:5000"  # Change to your server IP
        self.conversation = []
    
    def build(self):
        """Build the mobile UI"""
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(
            text='[b]JARVISH AI[/b]\n[size=14sp]Personal Assistant[/size]',
            size_hint_y=0.12,
            font_size='32sp',
            color=(0.1, 0.7, 1, 1),
            markup=True,
            bold=True
        )
        main_layout.add_widget(header)
        
        # Chat display area
        chat_scroll = ScrollView(size_hint_y=0.7)
        self.chat_display = Label(
            text='Hello! I\'m Jarvis, your personal AI. How can I help?',
            size_hint_y=None,
            markup=True,
            color=(1, 1, 1, 1)
        )
        self.chat_display.bind(texture_size=self.chat_display.setter('size'))
        chat_scroll.add_widget(self.chat_display)
        main_layout.add_widget(chat_scroll)
        
        # Input area
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=0.15, spacing=5)
        
        self.text_input = TextInput(
            hint_text='Type your command...',
            multiline=False,
            size_hint_x=0.7
        )
        input_layout.add_widget(self.text_input)
        
        send_btn = Button(
            text='Send',
            size_hint_x=0.3,
            background_color=(0.2, 0.6, 1, 1)
        )
        send_btn.bind(on_press=self.send_command)
        input_layout.add_widget(send_btn)
        
        main_layout.add_widget(input_layout)
        
        # Quick action buttons
        buttons_layout = GridLayout(cols=3, size_hint_y=0.1, spacing=5)
        
        weather_btn = Button(text='🌤️ Weather', background_color=(0.1, 0.5, 0.9, 1))
        weather_btn.bind(on_press=self.get_weather)
        buttons_layout.add_widget(weather_btn)
        
        news_btn = Button(text='📰 News', background_color=(0.1, 0.5, 0.9, 1))
        news_btn.bind(on_press=self.get_news)
        buttons_layout.add_widget(news_btn)
        
        time_btn = Button(text='⏰ Time', background_color=(0.1, 0.5, 0.9, 1))
        time_btn.bind(on_press=self.get_time)
        buttons_layout.add_widget(time_btn)
        
        main_layout.add_widget(buttons_layout)
        
        return main_layout
    
    def send_command(self, instance):
        """Send command to Jarvis"""
        command = self.text_input.text.strip()
        if not command:
            return
        
        self.text_input.text = ''
        self.add_message(f"You: {command}", is_user=True)
        
        # Send to server in background
        thread = threading.Thread(target=self.process_command, args=(command,))
        thread.daemon = True
        thread.start()
    
    def process_command(self, command):
        """Process command with server"""
        try:
            response = requests.post(
                f'{self.server_url}/command',
                json={'command': command},
                timeout=10
            )
            data = response.json()
            if data.get('success'):
                self.add_message(f"Jarvis: {data.get('response', 'Command processed')}", is_user=False)
            else:
                self.add_message(f"Error: {data.get('error', 'Unknown error')}", is_user=False)
        except Exception as e:
            self.add_message(f"Connection Error: {str(e)}", is_user=False)
    
    def get_weather(self, instance):
        """Get weather info"""
        self.add_message("You: What's the weather?", is_user=True)
        thread = threading.Thread(target=self.process_command, args=("weather",))
        thread.daemon = True
        thread.start()
    
    def get_news(self, instance):
        """Get news"""
        self.add_message("You: Show me the news", is_user=True)
        thread = threading.Thread(target=self.process_command, args=("news",))
        thread.daemon = True
        thread.start()
    
    def get_time(self, instance):
        """Get time"""
        self.add_message("You: What time is it?", is_user=True)
        thread = threading.Thread(target=self.process_command, args=("time",))
        thread.daemon = True
        thread.start()
    
    def add_message(self, message, is_user=False):
        """Add message to chat display"""
        self.conversation.append({
            'message': message,
            'is_user': is_user,
            'time': datetime.now().strftime('%H:%M')
        })
        
        # Update display
        chat_text = ""
        for msg in self.conversation:
            if msg['is_user']:
                chat_text += f"[color=87ceeb]{msg['message']}[/color]\n"
            else:
                chat_text += f"[color=90ee90]{msg['message']}[/color]\n"
        
        self.chat_display.text = chat_text

if __name__ == '__main__':
    JarvisApp().run()
