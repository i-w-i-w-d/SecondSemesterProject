import tkinter as tk
from PIL import Image, ImageTk

class BaseWindow:
    def __init__(self, master, text_resources, theme_manager, language):
        self.master = master
        self.text_resources = text_resources
        self.theme_manager = theme_manager
        self.language = language
        self.bg_image = None
        self.bg_photo = None
        self.bg_label = None

    def clear_window(self):
        for widget in self.master.winfo_children():
            if widget != self.bg_label:
                widget.destroy()

    def get_text(self, key):
        return self.text_resources.get_text(self.language, key)

    def apply_theme(self):
        colors = self.theme_manager.get_theme_colors()

        self.master.configure(bg=colors["bg"])

        try:
            img = Image.open(colors["bg_image"])
            img = img.resize((self.master.winfo_width(), self.master.winfo_height()), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(img)

            if self.bg_label is None:
                self.bg_label = tk.Label(self.master, image=self.bg_photo)
                self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            else:
                self.bg_label.configure(image=self.bg_photo)

            self.bg_label.lower()
        except Exception as e:
            print(f"Помилка завантаження зображення фону: {e}")
            if self.bg_label:
                self.bg_label.destroy()
                self.bg_label = None

        for widget in self.master.winfo_children():
            try:
                if widget != self.bg_label:
                    widget.configure(bg=colors["bg"], fg=colors["fg"])
                    if isinstance(widget, tk.Button):
                        widget.configure(bg=colors["btn_bg"])
                    elif isinstance(widget, tk.Radiobutton):
                        widget.configure(selectcolor=colors["selectcolor"])
            except:
                pass