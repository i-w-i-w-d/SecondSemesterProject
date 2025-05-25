import json
import os
from collections import OrderedDict

class LeaderboardManager:
    def __init__(self):
        self.file_path = "leaderboard.json"
        self.leaderboard = self._load_leaderboard()

    def _load_leaderboard(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for level in ["easy", "medium", "hard"]:
                        if level not in data:
                            data[level] = []
                    return data
            except:
                pass
        return OrderedDict([
            ("easy", []),
            ("medium", []),
            ("hard", [])
        ])

    def _save_leaderboard(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.leaderboard, f, ensure_ascii=False, indent=2)

    def add_result(self, level, player_name, moves, time_seconds):
        if level not in self.leaderboard:
            self.leaderboard[level] = []

        entry = {
            "name": player_name[:20],
            "moves": int(moves),
            "time": int(time_seconds)
        }

        self.leaderboard[level].append(entry)
        self.leaderboard[level].sort(key=lambda x: (x["moves"], x["time"]))
        self.leaderboard[level] = self.leaderboard[level][:10]
        self._save_leaderboard()

    def get_top_results(self, level, limit=10):
        return self.leaderboard.get(level, [])[:limit]