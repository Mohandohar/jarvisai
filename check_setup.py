#!/usr/bin/env python3
"""
Jarvis AI - Setup Verification Script
Tests if all dependencies and configurations are correct
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 8:
        return True
    else:
        print("  ERROR: Python 3.8+ required")
        return False

def check_dependencies():
    """Check all required dependencies"""
    deps = [
        'pyttsx3',
        'sounddevice',
        'numpy',
        'scipy',
        'speech_recognition',
        'requests',
        'flask',
        'python-dotenv',
    ]
    
    missing = []
    for dep in deps:
        try:
            __import__(dep.replace('-', '_'))
            print(f"✓ {dep}")
        except ImportError:
            print(f"✗ {dep} - NOT INSTALLED")
            missing.append(dep)
    
    return len(missing) == 0, missing

def check_env_file():
    """Check if .env file exists"""
    if os.path.exists('.env'):
        print("✓ .env file found")
        
        # Check for API keys
        with open('.env', 'r') as f:
            content = f.read()
            keys = ['GEMINI_API_KEY', 'WEATHER_API_KEY', 'NEWS_API_KEY']
            
            for key in keys:
                if key in content and 'your_' not in content:
                    print(f"  ✓ {key} configured")
                else:
                    print(f"  ⚠ {key} not configured")
        
        return True
    else:
        print("✗ .env file NOT found")
        print("  Run: cp .env.example .env")
        return False

def check_audio_devices():
    """Check audio devices availability"""
    try:
        import sounddevice as sd
        devices = sd.query_devices()
        print(f"✓ {len(devices)} audio devices found")
        return True
    except Exception as e:
        print(f"⚠ Audio devices check failed: {e}")
        return False

def check_internet():
    """Check internet connection"""
    try:
        import requests
        response = requests.get('https://api.github.com', timeout=3)
        if response.status_code == 200:
            print("✓ Internet connection OK")
            return True
    except Exception as e:
        print(f"⚠ Internet check failed: {e}")
        return False

def test_imports():
    """Test if all modules can be imported"""
    try:
        import jarvis_ai
        print("✓ jarvis_ai module loads successfully")
    except Exception as e:
        print(f"✗ jarvis_ai import failed: {e}")
        return False
    
    try:
        import api_server
        print("✓ api_server module loads successfully")
    except Exception as e:
        print(f"⚠ api_server import warning: {e}")
    
    return True

def main():
    """Run all checks"""
    print("\n" + "="*60)
    print("  JARVIS AI - SETUP VERIFICATION")
    print("="*60 + "\n")
    
    print("📋 Checking System Requirements:\n")
    py_ok = check_python_version()
    print()
    
    print("📦 Checking Dependencies:\n")
    deps_ok, missing = check_dependencies()
    print()
    
    if missing:
        print(f"⚠ {len(missing)} missing dependencies. Install with:")
        print(f"  pip install {' '.join(missing)}\n")
    
    print("⚙️  Checking Configuration:\n")
    env_ok = check_env_file()
    print()
    
    print("🔊 Checking Audio:\n")
    audio_ok = check_audio_devices()
    print()
    
    print("🌐 Checking Network:\n")
    net_ok = check_internet()
    print()
    
    print("🔧 Checking Modules:\n")
    imports_ok = test_imports()
    print()
    
    print("="*60)
    print("  VERIFICATION SUMMARY")
    print("="*60 + "\n")
    
    checks = {
        "Python Version": py_ok,
        "Dependencies": deps_ok,
        "Configuration": env_ok,
        "Audio Devices": audio_ok,
        "Internet": net_ok,
        "Modules": imports_ok,
    }
    
    for check, result in checks.items():
        status = "✓" if result else "✗"
        print(f"  {status} {check}")
    
    print("\n" + "="*60)
    
    if all(checks.values()):
        print("  ✓ ALL CHECKS PASSED - READY TO USE!")
        print("="*60 + "\n")
        print("Next steps:")
        print("  1. python jarvis_ai.py          (desktop version)")
        print("  2. python api_server.py         (API server)")
        print("  3. python mobile_app.py         (mobile preview)")
        return 0
    else:
        print("  ⚠ SOME CHECKS FAILED - READ ERRORS ABOVE")
        print("="*60 + "\n")
        print("Fix issues and run again:")
        print("  python check_setup.py")
        return 1

if __name__ == '__main__':
    sys.exit(main())
