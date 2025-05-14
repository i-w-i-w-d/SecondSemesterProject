import tkinter as tk

class BaseWindow:
    def __init__(self, master, text_resources, theme_manager, language):
        self.master = master
        self.text_resources = text_resources
        self.theme_manager = theme_manager
        self.language = language

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def get_text(self, key):
        return self.text_resources.get_text(self.language, key)

    def apply_theme(self):
        colors = self.theme_manager.get_theme_colors()
        self.master.configure(bg=colors["bg"])

        for widget in self.master.winfo_children():
            try:
                widget.configure(bg=colors["bg"], fg=colors["fg"])
                if isinstance(widget, tk.Button):
                    widget.configure(bg=colors["btn_bg"])
                elif isinstance(widget, tk.Radiobutton):
                    widget.configure(selectcolor=colors["selectcolor"])
            except:
                pass