import json

class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        #This game will begin in an inactiive state
        self.game_active = False
        self.high_score = 0

        #JSON file for high score
        self.my_scores = "Highscores.json"

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def create_high_score_json(self):
        scores_dict = {}
        for i in range (1,11):
            scores_dict[str(i)] = 0
        with open(self.my_scores, "w") as f:
            json.dump(scores_dict, f)

    def update_high_scores(self):
        try:
            with open(self.my_scores,"r") as f:
                high_scores = json.load(f)
        except FileNotFoundError:
            print("File not found! That's weird ...")

        scores_list = []

        for value in high_scores.values():
            scores_list.append(value)

        scores_list.append(round(self.score, -1))

        scores_list.sort(reverse=True)

        for i in range (10):
            high_scores[str(i+1)] = scores_list[i]

        with open(self.my_scores,"w") as f:
            json.dump(high_scores,f)
