import json
import os

class LeaderboardManager:
    def __init__(self):
        self.file_path = "leaderboard.json"
        self.leaderboard = self.load_leaderboard()

    def load_leaderboard(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "easy": [],
            "medium": [],
            "hard": []
        }

    def save_leaderboard(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.leaderboard, f, ensure_ascii=False, indent=2)

    def add_result(self, level, player_name, moves, time_seconds):
        try:
            if level not in ["easy", "medium", "hard"]:
                raise ValueError("Неправильний рівень складності")

            if not isinstance(moves, int) or moves <= 0:
                raise ValueError("Кількість ходів має бути додатнім цілим числом")

            entry = {
                "name": str(player_name),
                "moves": int(moves),
                "time": int(time_seconds)
            }

            self.leaderboard[level].append(entry)
            self.leaderboard[level].sort(key=lambda x: (x["moves"], x["time"]))
            self.leaderboard[level] = self.leaderboard[level][:10]
            self.save_leaderboard()
        except Exception as e:
            print(f"Помилка при додаванні результату: {str(e)}")
            raise

    def get_top_results(self, level, limit=10):
        return self.leaderboard.get(level, [])[:limit]