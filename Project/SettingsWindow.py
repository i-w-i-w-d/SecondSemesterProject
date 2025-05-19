import tkinter as tk
from BaseWindow import BaseWindow

class SettingsWindow(BaseWindow):
    def __init__(self, master, text_resources, theme_manager, language, on_back, on_theme_change, on_language_change):
        super().__init__(master, text_resources, theme_manager, language)
        self.on_back = on_back
        self.on_theme_change = on_theme_change
        self.on_language_change = on_language_change
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()
        self.master.title(self.get_text("settings_title"))

        colors = self.theme_manager.get_theme_colors()

        tk.Label(
            self.master,
            text=self.get_text("choose_theme"),
            bg=colors["bg"],
            fg=colors["fg"]
        ).pack(pady=10)

        self.theme_var = tk.StringVar(value=self.theme_manager.current_theme)

        tk.Radiobutton(
            self.master,
            text=self.get_text("light_theme"),
            variable=self.theme_var,
            value="light",
            command=self.change_theme,
            bg=colors["bg"],
            fg=colors["fg"],
            selectcolor=colors["selectcolor"]
        ).pack()

        tk.Radiobutton(
            self.master,
            text=self.get_text("gray_theme"),
            variable=self.theme_var,
            value="gray",
            command=self.change_theme,
            bg=colors["bg"],
            fg=colors["fg"],
            selectcolor=colors["selectcolor"]
        ).pack(pady=5)

        tk.Label(
            self.master,
            text=self.get_text("choose_lang"),
            bg=colors["bg"],
            fg=colors["fg"]
        ).pack(pady=10)

        self.lang_var = tk.StringVar(value=self.language)

        tk.Radiobutton(
            self.master,
            text=self.get_text("uk_lang"),
            variable=self.lang_var,
            value="uk",
            command=self.change_language,
            bg=colors["bg"],
            fg=colors["fg"],
            selectcolor=colors["selectcolor"]
        ).pack()

        tk.Radiobutton(
            self.master,
            text=self.get_text("en_lang"),
            variable=self.lang_var,
            value="en",
            command=self.change_language,
            bg=colors["bg"],
            fg=colors["fg"],
            selectcolor=colors["selectcolor"]
        ).pack(pady=5)

        tk.Button(
            self.master,
            text=self.get_text("back"),
            command=self.on_back,
            bg=colors["btn_bg"]
        ).pack(pady=20)

    def change_theme(self):
        self.theme_manager.current_theme = self.theme_var.get()
        self.on_theme_change()

    def change_language(self):
        self.on_language_change()