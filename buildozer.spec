[app]
title = Jarvis AI
package.name = jarvisai
package.domain = org.jarvis
version = 1.0

# Source files
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy,requests,pyjnius

# Permissions
android.permissions = INTERNET,RECORD_AUDIO,ACCESS_NETWORK_STATE

# API Level
android.api = 31
android.minapi = 21
android.ndk = 25b

# Hardware features
android.features = android.hardware.microphone

# Meta data
android.meta_data = com.google.android.gms.version=@integer/google_play_services_version

[buildozer]
log_level = 2
warn_on_root = 1
