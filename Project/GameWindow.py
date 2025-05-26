import tkinter as tk
from BaseWindow import BaseWindow
from Game_logic import GameLogic

class GameWindow(BaseWindow):
    def __init__(self, master, text_resources, theme_manager, language, on_back):
        super().__init__(master, text_resources, theme_manager, language)
        self.on_back = on_back
        self.mode_var = tk.StringVar(value="letters")
        self.create_widgets()

    def create_widgets(self):
        self.clear_window()
        self.master.title(self.get_text("game_title"))

        colors = self.theme_manager.get_theme_colors()

        tk.Label(
            self.master,
            text=self.get_text("choose_mode"),
            bg=colors["bg"],
            fg=colors["fg"]
        ).pack(pady=10)

        mode_frame = tk.Frame(self.master, bg=colors["bg"])
        mode_frame.pack()

        tk.Radiobutton(
            mode_frame,
            text=self.get_text("letters_mode"),
            variable=self.mode_var,
            value="letters",
            bg=colors["bg"],
            fg=colors["fg"],
            selectcolor=colors["selectcolor"]
        ).pack(side=tk.LEFT, padx=10)

        tk.Radiobutton(
            mode_frame,
            text=self.get_text("colors_mode"),
            variable=self.mode_var,
            value="colors",
            bg=colors["bg"],
            fg=colors["fg"],
            selectcolor=colors["selectcolor"]
        ).pack(side=tk.LEFT, padx=10)

        tk.Label(
            self.master,
            text=self.get_text("choose_level"),
            bg=colors["bg"],
            fg=colors["fg"]
        ).pack(pady=10)

        level_frame = tk.Frame(self.master, bg=colors["bg"])
        level_frame.pack(pady=10)

        tk.Button(
            level_frame,
            text=self.get_text("easy"),
            command=self.start_easy_level,
            width=10,
            bg=colors["btn_bg"]
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            level_frame,
            text=self.get_text("medium"),
            command=self.start_medium_level,
            width=10,
            bg=colors["btn_bg"]
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            level_frame,
            text=self.get_text("hard"),
            command=self.start_hard_level,
            width=10,
            bg=colors["btn_bg"],
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            self.master,
            text=self.get_text("back"),
            command=self.on_back,
            bg=colors["btn_bg"],
            fg=colors.get("back_btn_fg", "black")
        ).pack(pady=20)

    def start_easy_level(self):
        self.clear_window()
        title = f"{self.get_text('game_title')} - {self.get_text('easy')}"
        self.master.title(title)
        GameLogic(
            self.master,
            size=2,
            mode=self.mode_var.get(),
            on_back=self.on_back,
            language=self.language,
            text_resources=self.text_resources,
            theme_manager=self.theme_manager
        )

    def start_medium_level(self):
        self.clear_window()
        title = f"{self.get_text('game_title')} - {self.get_text('medium')}"
        self.master.title(title)
        GameLogic(
            self.master,
            size=4,
            mode=self.mode_var.get(),
            on_back=self.on_back,
            language=self.language,
            text_resources=self.text_resources,
            theme_manager=self.theme_manager
        )

    def start_hard_level(self):
        self.clear_window()
        title = f"{self.get_text('game_title')} - {self.get_text('hard')}"
        self.master.title(title)
        GameLogic(
            self.master,
            size=6,
            mode=self.mode_var.get(),
            on_back=self.on_back,
            language=self.language,
            text_resources=self.text_resources,
            theme_manager=self.theme_manager
        )