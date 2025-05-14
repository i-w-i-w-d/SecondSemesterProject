import tkinter as tk
from BaseWindow import BaseWindow

class LeadersWindow(BaseWindow):
    def __init__(self, master, text_resources, theme_manager, language, on_back):
        super().__init__(master, text_resources, theme_manager, language)
        self.on_back = on_back
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()
        self.master.title(self.get_text("leaders_title"))

        colors = self.theme_manager.get_theme_colors()

        tk.Label(
            self.master,
            text=self.get_text("leaders_text"),
            bg=colors["bg"],
            fg=colors["fg"]
        ).pack(pady=20)

        tk.Button(
            self.master,
            text=self.get_text("back"),
            command=self.on_back,
            bg=colors["btn_bg"]
        ).pack(pady=10)