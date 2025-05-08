#!/bin/bash

# 🔧 CONFIG
ENGINE_DIR="$HOME/EE198_EESeniorDesignProject_SJSU/midi_sound_engine"
LAUNCH_AGENT_DIR="$HOME/Library/LaunchAgents"
SCRIPT_PATH="$ENGINE_DIR/pico_autorun.sh"
PLIST_NAME="com.sharkisha.pico.synth.plist"
PLIST_PATH="$LAUNCH_AGENT_DIR/$PLIST_NAME"

# ✅ Step 1: Install required Python packages (user-level)
echo "🐍 Installing required Python packages..."
pip3 install --user sounddevice mido keyboard python-rtmidi

# ✅ Step 2: Ensure the LaunchAgents dir exists
mkdir -p "$LAUNCH_AGENT_DIR"

# ✅ Step 3: Create pico_autorun.sh if missing
if [ ! -f "$SCRIPT_PATH" ]; then
  echo "📄 Creating $SCRIPT_PATH..."
  cat <<EOF > "$SCRIPT_PATH"
#!/bin/bash
if system_profiler SPUSBDataType | grep -q "RP2040"; then
  echo "🎹 Pico detected — launching synth!"
  cd "$ENGINE_DIR"
  /usr/bin/python3 unified_listener.py
else
  echo "❌ Pico not found."
fi
EOF
  chmod +x "$SCRIPT_PATH"
else
  echo "✅ $SCRIPT_PATH already exists"
fi

# ✅ Step 4: Create LaunchAgent plist
echo "📄 Writing LaunchAgent: $PLIST_PATH"
cat <<EOF > "$PLIST_PATH"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.sharkisha.pico.synth</string>

    <key>ProgramArguments</key>
    <array>
        <string>$SCRIPT_PATH</string>
    </array>

    <key>StartInterval</key>
    <integer>10</integer>

    <key>RunAtLoad</key>
    <true/>

    <key>StandardOutPath</key>
    <string>/tmp/pico_autorun.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/pico_autorun_error.log</string>
</dict>
</plist>
EOF

# ✅ Step 5: Load the LaunchAgent
echo "🔁 Loading LaunchAgent..."
launchctl unload "$PLIST_PATH" 2>/dev/null
launchctl load "$PLIST_PATH"

echo "🎉 Done! Your synth engine will auto-launch every time you plug in your Pico."
echo "💡 Make sure your Python files are in: $ENGINE_DIR"