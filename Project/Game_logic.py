import tkinter as tk
import random
import time

class GameLogic:
    def __init__(self, master, size, on_back=None):
        self.master = master
        self.size = size
        self.on_back = on_back
        self.buttons = []
        self.first = None
        self.second = None
        self.locked = False
        self.matches_found = 0
        self.total_pairs = (size * size) // 2
        self.symbols = self.generate_symbols()
        self.click_count = 0
        self.timer = time.time()
        self.create_ui()

    def generate_symbols(self):
        symbols = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")  # Поки просто символи
        needed = self.total_pairs
        chosen = random.sample(symbols, needed)
        grid_symbols = chosen * 2
        random.shuffle(grid_symbols)
        return grid_symbols

    def create_ui(self):
        bg_color = self.master.cget("bg")
        fg_color = "black"
        self.frame = tk.Frame(self.master, bg=bg_color)
        self.frame.pack()

        for i in range(self.size):
            row = []
            for j in range(self.size):
                index = i * self.size + j
                btn = tk.Button(
                    self.frame,
                    text="",
                    width=6,
                    height=3,
                    command=lambda idx=index: self.reveal(idx),
                    fg=fg_color,
                    activebackground=bg_color)
                btn.grid(row=i, column=j, padx=2, pady=2)
                row.append(btn)
            self.buttons.append(row)

        self.back_button = tk.Button(
            self.master,
            text="Назад",
            command=self.back
        )
        self.back_button.pack(pady=10)

    def reveal(self, index):
        if self.locked:
            return

        row, col = divmod(index, self.size)
        btn = self.buttons[row][col]

        if btn["text"] != "":
            return  # кнопка вже відкрита

        self.click_count += 1
        symbol = self.symbols[index]
        btn.config(text=symbol)

        if self.first is None:
            self.first = (index, btn)
        elif self.second is None:
            self.second = (index, btn)
            self.locked = True
            self.master.after(500, self.check_match)  # Через 0.5 сек перевірити

    def show_victory_screen(self):
        self.frame.destroy()
        if hasattr(self, 'back_button'):  # Знищує кнопку Назад, якщо вона існує
            self.back_button.destroy()
        self.victory_frame = tk.Frame(self.master)
        self.victory_frame.pack()
        current_time = int(time.time() - self.timer)
        tk.Label(self.victory_frame, text="Всі пари знайдено!", font=("Arial", 18)).pack(pady=20)
        tk.Label(self.victory_frame, text=f"Загальна кількість ходів: {int(self.click_count/2)}", font=("Arial", 14)).pack(pady=5) # Можна змінити на к-сть натискань
        tk.Label(self.victory_frame, text=f"Час проходження: {current_time} с", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.victory_frame, text="Меню", command=self.back).pack(pady=10)

    def check_match(self):
        idx1, btn1 = self.first
        idx2, btn2 = self.second

        if self.symbols[idx1] == self.symbols[idx2]:
            btn1.config(state="disabled")
            btn2.config(state="disabled")
            self.matches_found += 1
            if self.matches_found == self.total_pairs:
                self.show_victory_screen()
        else:
            btn1.config(text="")
            btn2.config(text="")

        self.first = None
        self.second = None
        self.locked = False  # Дозволити натискання після перевірки

    def back(self):
        if hasattr(self, 'frame'):
            self.frame.destroy()
        if hasattr(self, 'victory_frame'):
            self.victory_frame.destroy()
        if hasattr(self, 'back_button'):
            self.back_button.destroy()

        if self.on_back:
            self.on_back()
