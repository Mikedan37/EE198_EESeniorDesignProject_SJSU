import rumps
from engine import play_note, stop_note, shutdown, get_last_note_info

class SynthMenuBarApp(rumps.App):
    def __init__(self):
        super().__init__(
            "🎵 Synth",
            icon=None,
            quit_button=None,
            menu=[
                "Stop Synth",
                rumps.MenuItem("Now Playing: —", callback=None),
                "Exit"
            ]
        )
        self.now_playing_item = self.menu["Now Playing: —"]
        self.timer = rumps.Timer(self.update_menu, 0.1)  # 100ms refresh rate
        self.timer.start()

    @rumps.clicked("Stop Synth")
    def stop_synth(self, _):
        shutdown()
        rumps.quit_application()

    @rumps.clicked("Exit")
    def quit_app(self, _):
        shutdown()
        rumps.quit_application()

    def update_menu(self, _):
        note, freq = get_last_note_info()
        if note is not None:
            self.now_playing_item.title = f"Now Playing: {note} ({freq:.2f} Hz)"
            self.title = f"🎵 {note} ({freq:.0f}Hz)"
        else:
            self.now_playing_item.title = "Now Playing: —"
            self.title = "🎵 Synth"

if __name__ == "__main__":
    SynthMenuBarApp().run()