from tkinter import ttk
import tkinter as tk
from TextResources import TextResources
from ThemeManager import ThemeManager
from MainMenuWindow import MainMenuWindow
from GameWindow import GameWindow
from LeadersWindow import LeadersWindow
from SettingsWindow import SettingsWindow

class TheGame:
    def __init__(self, title="Меню", width=550, height=500):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(f'{width}x{height}')
        self.text_resources = TextResources()
        self.theme_manager = ThemeManager()
        self.current_language = "uk"
        self.current_window = None
        self.show_main_menu()

    def show_main_menu(self):
        self.current_window = MainMenuWindow(
            self.window,
            self.text_resources,
            self.theme_manager,
            self.current_language,
            on_start=self.show_game_window,
            on_settings=self.show_settings_window,
            on_leaders=self.show_leaders_window,
            on_exit=self.window.quit
        )

    def show_game_window(self):
        self.current_window = GameWindow(
            self.window,
            self.text_resources,
            self.theme_manager,
            self.current_language,
            on_back=self.show_main_menu
        )

    def show_leaders_window(self):
        self.current_window = LeadersWindow(
            self.window,
            self.text_resources,
            self.theme_manager,
            self.current_language,
            on_back=self.show_main_menu
        )

    def show_settings_window(self):
        self.current_window = SettingsWindow(
            self.window,
            self.text_resources,
            self.theme_manager,
            self.current_language,
            on_back=self.show_main_menu,
            on_theme_change=self.apply_theme,
            on_language_change=self.update_language
        )

    def apply_theme(self):
        colors = self.theme_manager.get_theme_colors()
        self.window.configure(bg=colors["bg"])

        for widget in self.window.winfo_children():
            try:
                widget.configure(bg=colors["bg"], fg=colors["fg"])
                if isinstance(widget, tk.Button):
                    widget.configure(bg=colors["btn_bg"])
                elif isinstance(widget, tk.Radiobutton):
                    widget.configure(selectcolor=colors["selectcolor"])
            except:
                pass

    def update_language(self):
        self.current_language = self.current_window.lang_var.get()

        if isinstance(self.current_window, MainMenuWindow):
            self.show_main_menu()
        elif isinstance(self.current_window, GameWindow):
            self.show_game_window()
        elif isinstance(self.current_window, LeadersWindow):
            self.show_leaders_window()
        elif isinstance(self.current_window, SettingsWindow):
            self.show_settings_window()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TheGame()
    game.run()