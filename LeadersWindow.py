import tkinter as tk
from BaseWindow import BaseWindow
from LeaderboardManager import LeaderboardManager

class LeadersWindow(BaseWindow):
    def __init__(self, master, text_resources, theme_manager, language, on_back):
        super().__init__(master, text_resources, theme_manager, language)
        self.on_back = on_back
        self.leaderboard_manager = LeaderboardManager()
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()
        self.master.title(self.get_text("leaders_title"))
        colors = self.theme_manager.get_theme_colors()

        self.notebook = tk.ttk.Notebook(self.master)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        for level in ["easy", "medium", "hard"]:
            frame = tk.Frame(self.notebook, bg=colors["bg"])
            self.notebook.add(frame, text=self.get_text(level))
            self.create_level_tab(frame, level)

        tk.Button(
            self.master,
            text=self.get_text("back"),
            command=self.on_back,
            bg=colors["btn_bg"]
        ).pack(pady=10)

    def create_level_tab(self, parent, level):
        top_results = self.leaderboard_manager.get_top_results(level)
        colors = self.theme_manager.get_theme_colors()

        if not top_results:
            tk.Label(
                parent,
                text="Ще немає результатів",
                bg=colors["bg"],
                fg=colors["fg"]
            ).pack(pady=20)
            return

        for i, result in enumerate(top_results, 1):
            text = f"{i}. {result['name']} - {result['moves']} ходів, {result['time']} с"
            tk.Label(
                parent,
                text=text,
                bg=colors["bg"],
                fg=colors["fg"],
                font=("Arial", 12 if i <= 3 else None)
            ).pack(pady=2)