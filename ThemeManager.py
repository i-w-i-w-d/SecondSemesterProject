class ThemeManager:
    def __init__(self):
        self.current_theme = "light"

    def get_theme_colors(self):
        if self.current_theme == "light":
            return {
                "bg": "white",
                "fg": "black",
                "btn_bg": "pink",
                "selectcolor": "white"
            }
        else:
            return {
                "bg": "gray",
                "fg": "black",
                "btn_bg": "pink",
                "selectcolor": "gray"
            }