import tkinter as tk
from tkinter import messagebox #Потім для таблички рекордів

class TheGame:
    def __init__(self, title = "Меню", width = 300, height = 150):
        #Створює вікно
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(f'{width}x{height}')
        self.CreateButtons()

    def CreateButtons(self):
        #Кнопка, яка відкриває нове вікно, де буде основна гра
        self.StartButton = tk.Button(
            self.window,
            text = 'Почати гру',
            command = self.StartGameWindow
        )
        self.StartButton.pack(pady = 10)

        #Кнопка, яка відкриває нове вікно, де будуть відображатись лідери та їхній час проходження гри
        self.LeadersButton = tk.Button(
            self.window,
            text = 'Лідери',
            command = self.LeadersWindow
        )
        self.LeadersButton.pack(pady = 10)

        #Кнопка, яка дає змогу закрити вікно
        self.ExitButton = tk.Button(
            self.window,
            text = 'Вийти',
            command = self.window.quit
        )
        self.ExitButton.pack(pady = 10)

    #Вікно, де буде реалізована гра
    def StartGameWindow(self):
        GameWindow = tk.Toplevel(self.window)
        GameWindow.title("Гра - Запам'ятовуввання")
        GameWindow.geometry('300x150')

        CloseButton = tk.Button(
            GameWindow,
            text = 'Вийти',
            command = GameWindow.destroy
        )
        CloseButton.pack(pady = 50)

    # Вікно, де буде реалізована табличка лідерів
    def LeadersWindow(self):
        Leaders = tk.Toplevel(self.window)
        Leaders.title("Легенди, які увійшли в історію")
        Leaders.geometry('300x150')

        CloseButton = tk.Button(
            Leaders,
            text = 'Вийти',
            command = Leaders.destroy
        )
        CloseButton.pack(pady = 50)

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
