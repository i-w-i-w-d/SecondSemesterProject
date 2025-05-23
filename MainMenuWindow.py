import tkinter as tk
from BaseWindow import BaseWindow

class MainMenuWindow(BaseWindow):
    def __init__(self, master, text_resources, theme_manager, language, on_start, on_settings, on_leaders, on_exit):
        super().__init__(master, text_resources, theme_manager, language)
        self.on_start = on_start
        self.on_settings = on_settings
        self.on_leaders = on_leaders
        self.on_exit = on_exit
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()
        self.master.title(self.get_text("menu"))

        colors = self.theme_manager.get_theme_colors()

        tk.Button(
            self.master,
            text=self.get_text("start"),
            command=self.on_start,
            bg=colors["btn_bg"]
        ).pack(pady=10)

        tk.Button(
            self.master,
            text=self.get_text("settings"),
            command=self.on_settings,
            bg=colors["btn_bg"]
        ).pack(pady=10)

        tk.Button(
            self.master,
            text=self.get_text("leaders"),
            command=self.on_leaders,
            bg=colors["btn_bg"]
        ).pack(pady=10)

        tk.Button(
            self.master,
            text=self.get_text("exit"),
            command=self.on_exit,
            bg=colors["btn_bg"]
        ).pack(pady=10)