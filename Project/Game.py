import tkinter as tk
from tkinter import messagebox

class TheGame:
    def __init__(self, title="Меню", width=300, height=200):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(f'{width}x{height}')
        self.current_theme = "light"
        self.current_language = "uk"
        self.texts = { #Напевно, дарма я зара зробив зміну мови, потім доведеться додавати, чи може норм...
            "uk": {
                "menu": "Меню",
                "start": "Почати гру",
                "settings": "Налаштування",
                "leaders": "Лідери",
                "exit": "Вийти",
                "game_title": "Гра - Запам'ятовування",
                "choose_level": "Оберіть рівень складності:",
                "easy": "Легко",
                "medium": "Середньо",
                "hard": "Важко",
                "back": "Повернутись",
                "leaders_title": "Таблиця лідерів",
                "leaders_text": "Тут буде таблиця лідерів",
                "settings_title": "Налаштування",
                "choose_theme": "Оберіть тему вікна:",
                "light_theme": "Світла тема",
                "dark_theme": "Темна тема",
                "choose_lang": "Оберіть мову:",
                "uk_lang": "Українська",
                "en_lang": "Англійська",
                "level_msg": "Ви обрали {level} рівень складності"
            },
            "en": {
                "menu": "Menu",
                "start": "Start Game",
                "settings": "Settings",
                "leaders": "Leaders",
                "exit": "Exit",
                "game_title": "Game - Memorization",
                "choose_level": "Choose difficulty level:",
                "easy": "Easy",
                "medium": "Medium",
                "hard": "Hard",
                "back": "Back",
                "leaders_title": "Leaderboard",
                "leaders_text": "Leaderboard will be here",
                "settings_title": "Settings",
                "choose_theme": "Choose window theme:",
                "light_theme": "Light theme",
                "dark_theme": "Dark theme",
                "choose_lang": "Choose language:",
                "uk_lang": "Ukrainian",
                "en_lang": "English",
                "level_msg": "You selected {level} difficulty level"
            }
        }
        self.apply_theme()
        self.show_main_menu()

    def apply_theme(self):
        if self.current_theme == "light":
            bg_color = "white"
            fg_color = "black"
            btn_bg = "lightgray"
        else:
            bg_color = "black"
            fg_color = "white"
            btn_bg = "gray"

        self.window.configure(bg=bg_color)

        for widget in self.window.winfo_children():
            try:
                widget.configure(bg=bg_color, fg=fg_color)
                if isinstance(widget, tk.Button):
                    widget.configure(bg=btn_bg)
                elif isinstance(widget, tk.Radiobutton):
                    widget.configure(selectcolor=btn_bg)
            except:
                pass

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def get_text(self, key):
        return self.texts[self.current_language][key]

    def show_main_menu(self):
        self.clear_window()
        self.window.title(self.get_text("menu"))
        self.create_main_menu_buttons()

    def create_main_menu_buttons(self):
        tk.Button(
            self.window,
            text=self.get_text("start"),
            command=self.show_game_window,
            bg="lightgray" if self.current_theme == "light" else "gray"
        ).pack(pady=10)

        tk.Button(
            self.window,
            text=self.get_text("settings"),
            command=self.show_settings_window,
            bg="lightgray" if self.current_theme == "light" else "gray"
        ).pack(pady=10)

        tk.Button(
            self.window,
            text=self.get_text("leaders"),
            command=self.show_leaders_window,
            bg="lightgray" if self.current_theme == "light" else "gray"
        ).pack(pady=10)

        tk.Button(
            self.window,
            text=self.get_text("exit"),
            command=self.window.quit,
            bg="lightgray" if self.current_theme == "light" else "gray"
        ).pack(pady=10)

    def show_game_window(self):
        self.clear_window()
        self.window.title(self.get_text("game_title"))

        tk.Label(
            self.window,
            text=self.get_text("choose_level"),
            bg="white" if self.current_theme == "light" else "black",
            fg="black" if self.current_theme == "light" else "white"
        ).pack(pady=10)

        frame = tk.Frame(self.window, bg="white" if self.current_theme == "light" else "black")
        frame.pack(pady=10)

        tk.Button(
            frame,
            text=self.get_text("easy"),
            command=self.start_easy_level,
            width=10,
            bg="lightgray" if self.current_theme == "light" else "gray"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame,
            text=self.get_text("medium"),
            command=self.start_medium_level,
            width=10,
            bg="lightgray" if self.current_theme == "light" else "gray"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame,
            text=self.get_text("hard"),
            command=self.start_hard_level,
            width=10,
            bg="lightgray" if self.current_theme == "light" else "gray"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            self.window,
            text=self.get_text("back"),
            command=self.show_main_menu,
            bg="lightgray" if self.current_theme == "light" else "gray"
        ).pack(pady=20)

    def start_easy_level(self):
        self.show_empty_game_window(self.get_text("easy"))

    def start_medium_level(self):
        self.show_empty_game_window(self.get_text("medium"))

    def start_hard_level(self):
        self.show_empty_game_window(self.get_text("hard"))

    def show_empty_game_window(self, level):
        self.clear_window()
        self.window.title(f"{self.get_text('game_title')} - {level}")

        tk.Button(
            self.window,
            text=self.get_text("back"),
            command=self.show_game_window,
            bg="lightgray" if self.current_theme == "light" else "gray"
        ).pack(pady=10)

    def show_leaders_window(self):
        self.clear_window()
        self.window.title(self.get_text("leaders_title"))

        tk.Label(
            self.window,
            text=self.get_text("leaders_text"),
            bg="white" if self.current_theme == "light" else "black",
            fg="black" if self.current_theme == "light" else "white"
        ).pack(pady=20)

        tk.Button(
            self.window,
            text=self.get_text("back"),
            command=self.show_main_menu,
            bg="lightgray" if self.current_theme == "light" else "gray"
        ).pack(pady=10)

    def show_settings_window(self):
        self.clear_window()
        self.window.title(self.get_text("settings_title"))

        tk.Label(
            self.window,
            text=self.get_text("choose_theme"),
            bg="white" if self.current_theme == "light" else "black",
            fg="black" if self.current_theme == "light" else "white"
        ).pack(pady=10)

        self.theme_var = tk.StringVar(value=self.current_theme)

        tk.Radiobutton(
            self.window,
            text=self.get_text("light_theme"),
            variable=self.theme_var,
            value="light",
            command=self.change_theme,
            bg="white" if self.current_theme == "light" else "black",
            fg="black" if self.current_theme == "light" else "white",
            selectcolor="lightgray"
        ).pack()

        tk.Radiobutton(
            self.window,
            text=self.get_text("dark_theme"),
            variable=self.theme_var,
            value="dark",
            command=self.change_theme,
            bg="white" if self.current_theme == "light" else "black",
            fg="black" if self.current_theme == "light" else "white",
            selectcolor="gray"
        ).pack(pady=5)

        tk.Label(
            self.window,
            text=self.get_text("choose_lang"),
            bg="white" if self.current_theme == "light" else "black",
            fg="black" if self.current_theme == "light" else "white"
        ).pack(pady=10)

        self.lang_var = tk.StringVar(value=self.current_language)

        tk.Radiobutton(
            self.window,
            text=self.get_text("uk_lang"),
            variable=self.lang_var,
            value="uk",
            command=self.change_language,
            bg="white" if self.current_theme == "light" else "black",
            fg="black" if self.current_theme == "light" else "white",
            selectcolor="lightgray" if self.current_theme == "light" else "gray"
        ).pack()

        tk.Radiobutton(
            self.window,
            text=self.get_text("en_lang"),
            variable=self.lang_var,
            value="en",
            command=self.change_language,
            bg="white" if self.current_theme == "light" else "black",
            fg="black" if self.current_theme == "light" else "white",
            selectcolor="lightgray" if self.current_theme == "light" else "gray"
        ).pack(pady=5)

        tk.Button(
            self.window,
            text=self.get_text("back"),
            command=self.show_main_menu,
            bg="lightgray" if self.current_theme == "light" else "gray"
        ).pack(pady=20)

    def change_theme(self):
        self.current_theme = self.theme_var.get()
        self.apply_theme()

    def change_language(self):
        self.current_language = self.lang_var.get()
        if self.window.title() == self.get_text("settings_title"):
            self.show_settings_window()
        elif self.window.title() == self.get_text("leaders_title"):
            self.show_leaders_window()
        elif self.get_text("game_title") in self.window.title():
            self.show_game_window()
        else:
            self.show_main_menu()

    def run(self):
        self.window.mainloop()

"""
Хммм... ну напевно можеш почати вже робити саму гру, її вікно знаходиться в def StartGameWindow(self)... я подивився і там можна
додати бібліотеку із зображеннями, можемо використати для клітинок, коли вони обертаються, але тоді вони мають бути на комп'ютері,
тож можна просто додати кольори або цифри

Окрім тих ідей, які ми обговорили, пропоную ще реалізувати складності гри:
Easy: створюється вікно 2x2
Medium: 4x4
Hard: 6x6

Старі ідеї:
1) Час проходження
2) Кількість спроб
3) Почати знову
4) ...
"""