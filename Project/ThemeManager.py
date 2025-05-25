class ThemeManager:
    def __init__(self):
        self.current_theme = "light"
        self.day_image = "assets/day_sun.jpg"
        self.night_image = "assets/night_moon.jpg"

    def get_theme_colors(self):
        if self.current_theme == "light":
            return {
                "bg": "#ffffff",
                "bg_image": self.day_image,
                "fg": "black",
                "btn_bg": "pink",
                "selectcolor": "white"
            }
        else:
            return {
                "bg": "#333333",
                "bg_image": self.night_image,
                "fg": "white",
                "btn_bg": "pink",
                "selectcolor": "gray"
            }