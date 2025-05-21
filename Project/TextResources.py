class TextResources:
    def __init__(self):
        self.texts = {
            "uk": {
                "menu": "Меню",
                "start": "Почати гру",
                "settings": "Налаштування",
                "leaders": "Лідери",
                "exit": "Вийти",
                "game_title": "Гра - Запам'ятовування",
                "choose_level": "Оберіть рівень складності:",
                "easy": "Легкий",
                "medium": "Середній",
                "hard": "Складний",
                "back": "Повернутись",
                "leaders_title": "Таблиця лідерів",
                "leaders_text": "Найкращі результати",
                "no_results": "Ще немає результатів",
                "settings_title": "Налаштування",
                "choose_theme": "Оберіть тему вікна:",
                "light_theme": "Світла тема",
                "gray_theme": "Сіра тема",
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
                "leaders_text": "Top results",
                "no_results": "No results yet",
                "settings_title": "Settings",
                "choose_theme": "Choose window theme:",
                "light_theme": "Light theme",
                "gray_theme": "Gray theme",
                "choose_lang": "Choose language:",
                "uk_lang": "Ukrainian",
                "en_lang": "English",
                "level_msg": "You selected {level} difficulty level"
            }
        }

    def get_text(self, language, key):
        return self.texts[language][key]