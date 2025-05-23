import tkinter as tk
import random
import time
from PIL import Image, ImageTk
from LeaderboardManager import LeaderboardManager
import os

class GameLogic:
    def __init__(self, master, size, language, mode="letters", on_back=None):
        self.master = master
        self.size = size
        self.mode = mode
        self.on_back = on_back
        self.language = language
        self.canvas_items = {}
        self.first = None
        self.second = None
        self.locked = False
        self.matches_found = 0
        self.total_pairs = (size * size) // 2
        self.symbols = self.generate_symbols()
        self.click_count = 0
        self.timer = time.time()
        self.leaderboard_manager = LeaderboardManager()
        self.window_width = 550
        self.window_height = 450
        self.cell_size = 55
        self.spacing = 5

        self.images = {}

        self.create_ui()

    def generate_symbols(self):
        if self.mode == "letters":
            if self.language == "en":
                symbols = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
            else:
                symbols = list("АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦ")
            chosen = random.sample(symbols, self.total_pairs)
            items = chosen * 2
        elif self.mode == "colors":
            available = list(range(1, 20))
            if self.total_pairs > len(available):
                raise ValueError("Недостатньо зображень!")
            chosen = random.sample(available, self.total_pairs)
            items = chosen * 2

        random.shuffle(items)
        return items

    def create_ui(self):
        self.canvas = tk.Canvas(
            self.master,
            width=self.window_width,
            height=self.window_height,
            bg="white",
            highlightthickness=0
        )
        self.canvas.pack()

        # Обчислення сітки
        grid_width = self.size * self.cell_size + (self.size - 1) * self.spacing
        grid_height = self.size * self.cell_size + (self.size - 1) * self.spacing
        offset_x = (self.window_width - grid_width) // 2
        offset_y = ((self.window_height - 60) - grid_height) // 2

        for i in range(self.size):
            for j in range(self.size):
                index = i * self.size + j
                x1 = offset_x + j * (self.cell_size + self.spacing)
                y1 = offset_y + i * (self.cell_size + self.spacing)
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray", outline="black")
                text = self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="", font=("Arial", 18))
                image_id = None
                if self.mode == "colors":
                    image_id = self.canvas.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=None)

                self.canvas.tag_bind(rect, "<Button-1>", lambda event, idx=index: self.reveal(idx))
                self.canvas.tag_bind(text, "<Button-1>", lambda event, idx=index: self.reveal(idx))
                if image_id:
                    self.canvas.tag_bind(image_id, "<Button-1>", lambda event, idx=index: self.reveal(idx))

                self.canvas_items[index] = {
                    "rect": rect,
                    "text": text,
                    "revealed": False,
                    "image_id": image_id
                }

        self.back_button = tk.Button(self.master, text="Назад", command=self.back)
        self.back_button.pack(pady=5)

    def reveal(self, index):
        if self.locked or self.canvas_items[index]["revealed"]:
            return

        self.click_count += 1
        self.canvas_items[index]["revealed"] = True

        if self.mode == "letters":
            self.canvas.itemconfigure(self.canvas_items[index]["text"], text=self.symbols[index])
        else:  # кольори
            image_index = self.symbols[index]
            image_path = os.path.join("assets", f"c{image_index}.png")
            if image_path not in self.images:
                try:
                    img = Image.open(image_path)
                    img = img.resize((self.cell_size - 10, self.cell_size - 10))
                    self.images[image_path] = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f"Помилка завантаження зображення {image_path}: {e}")
                    return
            self.canvas.itemconfigure(self.canvas_items[index]["image_id"], image=self.images[image_path])
            self.canvas.itemconfigure(self.canvas_items[index]["text"], text="")

        if self.first is None:
            self.first = index
        elif self.second is None:
            self.second = index
            self.locked = True
            self.master.after(700, self.check_match)

    def check_match(self):
        idx1 = self.first
        idx2 = self.second

        if self.symbols[idx1] == self.symbols[idx2]:
            self.canvas.itemconfigure(self.canvas_items[idx1]["rect"], fill="green")
            self.canvas.itemconfigure(self.canvas_items[idx2]["rect"], fill="green")
            self.matches_found += 1
            if self.matches_found == self.total_pairs:
                self.show_victory_screen()
        else:
            if self.mode == "letters":
                self.canvas.itemconfigure(self.canvas_items[idx1]["text"], text="")
                self.canvas.itemconfigure(self.canvas_items[idx2]["text"], text="")
            else:
                self.canvas.itemconfigure(self.canvas_items[idx1]["image_id"], image='')
                self.canvas.itemconfigure(self.canvas_items[idx2]["image_id"], image='')

            self.canvas_items[idx1]["revealed"] = False
            self.canvas_items[idx2]["revealed"] = False

        self.first = None
        self.second = None
        self.locked = False

    def show_victory_screen(self):
        self.canvas.destroy()
        self.back_button.destroy()
        elapsed = int(time.time() - self.timer)
        moves = self.click_count // 2

        self.victory_frame = tk.Frame(self.master)
        self.victory_frame.pack()

        tk.Label(self.victory_frame, text="Всі пари знайдено!", font=("Arial", 18)).pack(pady=20)
        tk.Label(self.victory_frame, text=f"Ходи: {moves}", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.victory_frame, text=f"Час: {elapsed} с", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.victory_frame, text="Введіть ваше ім'я:").pack()

        self.name_entry = tk.Entry(self.victory_frame)
        self.name_entry.pack()

        tk.Button(
            self.victory_frame,
            text="Зберегти результат",
            command=lambda: self.save_score(moves, elapsed)
        ).pack(pady=5)

        tk.Button(self.victory_frame, text="Меню", command=self.back).pack(pady=10)

    def save_score(self, moves, time_seconds):
        player_name = self.name_entry.get() or "Гравець"
        level = self.get_level_name()
        self.leaderboard_manager.add_result(level, player_name, moves, time_seconds)
        self.show_leaderboard()

    def get_level_name(self):
        if self.size == 2:
            return "easy"
        elif self.size == 4:
            return "medium"
        return "hard"

    def show_leaderboard(self):
        for widget in self.victory_frame.winfo_children():
            widget.destroy()

        level = self.get_level_name()
        top_results = self.leaderboard_manager.get_top_results(level)

        tk.Label(self.victory_frame, text="Топ гравців:", font=("Arial", 16)).pack()

        for i, result in enumerate(top_results, 1):
            text = f"{i}. {result['name']} - {result['moves']} ходів, {result['time']} с"
            tk.Label(self.victory_frame, text=text).pack()

        tk.Button(self.victory_frame, text="Меню", command=self.back).pack(pady=10)

    def back(self):
        if hasattr(self, 'canvas'):
            self.canvas.destroy()
        if hasattr(self, 'victory_frame'):
            self.victory_frame.destroy()
        if hasattr(self, 'back_button'):
            self.back_button.destroy()
        if self.on_back:
            self.on_back()
