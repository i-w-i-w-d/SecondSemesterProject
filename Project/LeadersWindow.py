import tkinter as tk
from tkinter import ttk
from BaseWindow import BaseWindow
from LeaderboardManager import LeaderboardManager


class LeadersWindow(BaseWindow):
    def __init__(self, master, text_resources, theme_manager, language, on_back):
        super().__init__(master, text_resources, theme_manager, language)
        self.on_back = on_back
        self.leaderboard_manager = LeaderboardManager()
        self.create_widgets()
        self.apply_theme()

    def create_widgets(self):
        self.clear_window()
        self.master.title(self.get_text("leaders_title"))
        colors = self.theme_manager.get_theme_colors()

        self.main_frame = tk.Frame(self.master, bg=colors["bg"])
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill='both', expand=True)

        self.tabs = {}
        for level in ["easy", "medium", "hard"]:
            tab = tk.Frame(self.notebook, bg=colors["bg"])
            self.tabs[level] = tab
            self.notebook.add(tab, text=self.get_text(level))
            self.update_tab_content(level)

        self.back_btn = tk.Button(
            self.main_frame,
            text=self.get_text("back"),
            command=self.on_back,
            bg=colors["btn_bg"]
        )
        self.back_btn.pack(pady=10)

    def update_tab_content(self, level):
        tab = self.tabs[level]
        for widget in tab.winfo_children():
            widget.destroy()

        colors = self.theme_manager.get_theme_colors()
        top_results = self.leaderboard_manager.get_top_results(level, limit=10)

        if not top_results:
            tk.Label(
                tab,
                text=self.get_text("no_results"),
                bg=colors["bg"],
                fg=colors["fg"]
            ).pack(pady=20)
            return

        for i, result in enumerate(top_results, 1):
            text = f"{i}. {result['name']} - {result['moves']} {self.get_text('moves_unit')}, {result['time']} {self.get_text('time_unit')}"
            tk.Label(
                tab,
                text=text,
                bg=colors["bg"],
                fg=colors["fg"],
                font=("Arial", 12 if i <= 3 else 10)
            ).pack(pady=2, anchor='w')

    def apply_theme(self):
        super().apply_theme()
        colors = self.theme_manager.get_theme_colors()
        if hasattr(self, 'main_frame'):
            self.main_frame.configure(bg=colors["bg"])
        if hasattr(self, 'back_btn'):
            self.back_btn.configure(bg=colors["btn_bg"])