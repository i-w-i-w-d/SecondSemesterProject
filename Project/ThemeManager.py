class ThemeManager:
    def __init__(self):
        self.current_theme = "light"

    def get_theme_colors(self):
        if self.current_theme == "light":
            return {
                "bg": "white",
                "fg": "black",
                "btn_bg": "lightgray",
                "selectcolor": "lightgray"
            }
        else:
            return {
                "bg": "black",
                "fg": "white",
                "btn_bg": "gray",
                "selectcolor": "gray"
            }