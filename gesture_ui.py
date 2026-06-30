import tkinter as tk
from tkinter import ttk


class GestureUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gesture Controller")
        self.root.geometry("520x360")
        self.root.resizable(False, False)
        self.root.configure(bg="#111827")

        self.enabled = False

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Title.TLabel",
            background="#111827",
            foreground="white",
            font=("Segoe UI", 22, "bold")
        )

        self.style.configure(
            "Subtitle.TLabel",
            background="#111827",
            foreground="#9CA3AF",
            font=("Segoe UI", 11)
        )

        self.style.configure(
            "Status.TLabel",
            background="#1F2937",
            foreground="#F9FAFB",
            font=("Segoe UI", 16, "bold"),
            padding=14
        )

        self.style.configure(
            "Gesture.TLabel",
            background="#1F2937",
            foreground="#38BDF8",
            font=("Segoe UI", 15, "bold"),
            padding=14
        )

        self.container = tk.Frame(self.root, bg="#111827")
        self.container.pack(fill="both", expand=True, padx=32, pady=28)

        self.title_label = ttk.Label(
            self.container,
            text="Gesture Controller",
            style="Title.TLabel"
        )
        self.title_label.pack(anchor="w")

        self.subtitle_label = ttk.Label(
            self.container,
            text="Control your system using hand gestures",
            style="Subtitle.TLabel"
        )
        self.subtitle_label.pack(anchor="w", pady=(4, 24))

        self.status_label = ttk.Label(
            self.container,
            text="Status: OFF",
            style="Status.TLabel",
            anchor="center"
        )
        self.status_label.pack(fill="x", pady=(0, 16))

        self.toggle_button = tk.Button(
            self.container,
            text="TURN ON",
            command=self.toggle,
            bg="#22C55E",
            fg="white",
            activebackground="#16A34A",
            activeforeground="white",
            font=("Segoe UI", 15, "bold"),
            relief="flat",
            cursor="hand2",
            height=2
        )
        self.toggle_button.pack(fill="x", pady=(0, 18))

        self.gesture_label = ttk.Label(
            self.container,
            text="Current Gesture: None",
            style="Gesture.TLabel",
            anchor="center"
        )
        self.gesture_label.pack(fill="x")

        self.footer_label = ttk.Label(
            self.container,
            text="Press Q or close this window to exit",
            style="Subtitle.TLabel"
        )
        self.footer_label.pack(side="bottom", pady=(22, 0))

    def toggle(self):
        self.enabled = not self.enabled

        if self.enabled:
            self.status_label.config(text="Status: ON")
            self.toggle_button.config(
                text="TURN OFF",
                bg="#EF4444",
                activebackground="#DC2626"
            )
        else:
            self.status_label.config(text="Status: OFF")
            self.toggle_button.config(
                text="TURN ON",
                bg="#22C55E",
                activebackground="#16A34A"
            )

    def set_gesture(self, gesture):
        self.gesture_label.config(text=f"Current Gesture: {gesture}")