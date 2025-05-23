class TextResources:
    def __init__(self):
        self.texts = self.load_texts()

    def load_texts(self):
        return {
            "uk": {
                "menu": "Меню",
                "start": "Старт",
                "settings": "Налаштування",
                "leaders": "Таблиця лідерів",
                "exit": "Вихід",
                "game_title": "Гра",
                "easy": "Легко",
                "medium": "Середньо",
                "hard": "Важко",
                "back": "Назад",
                "settings_title": "Налаштування",
                "choose_theme": "Оберіть тему",
                "light_theme": "Світла",
                "gray_theme": "Сіра",
                "choose_lang": "Оберіть мову",
                "uk_lang": "Українська",
                "en_lang": "Англійська",
                "choose_mode": "Оберіть режим",
                "letters_mode": "Букви",
                "colors_mode": "Кольори",
                "choose_level": "Оберіть рівень"
            },
            "en": {
                "menu": "Menu",
                "start": "Start",
                "settings": "Settings",
                "leaders": "Leaderboard",
                "exit": "Exit",
                "game_title": "Game",
                "easy": "Easy",
                "medium": "Medium",
                "hard": "Hard",
                "back": "Back",
                "settings_title": "Settings",
                "choose_theme": "Choose theme",
                "light_theme": "Light",
                "gray_theme": "Gray",
                "choose_lang": "Choose language",
                "uk_lang": "Ukrainian",
                "en_lang": "English",
                "choose_mode": "Choose mode",
                "letters_mode": "Letters",
                "colors_mode": "Colors",
                "choose_level": "Choose level"
            }
        }

    def get_text(self, language, key):
        return self.texts[language].get(key, f"[{key}]")
