import random

def play_innings(player_no):
    print("\nPlayer", player_no, "Batting Started")

    score = 0
    legal_balls = 0
    overs = 0
    scorecard = []

    previous_ball = None   

    while True:
        ball = random.randint(0, 9)

        print(f"Over {overs}.{legal_balls} | Run Value: {ball}")

        # OUT
        if ball == 0:
            if previous_ball in {5,7,8,9}:
                print("Free Hit! Cannot be OUT.")
                continue  # Free hit, cannot be out
            else:
                scorecard.append("OUT")
                print("OUT! Innings Ended")
                break

        # NO BALL / WIDE + BOUNDARY
        if ball in {5, 7, 8, 9}:
            score += ball
            scorecard.append(f"{ball} runs (NB/WD + Boundary)")
            print(f"{ball} runs (NB/WD), Free Hit next ball")
            previous_ball = ball
            continue   # not a legal ball

        # CHECK FREE HIT CONDITION
        if previous_ball in {5, 7, 8, 9}:
            score += ball
            legal_balls += 1
            scorecard.append(f"{ball} run(s) [Free Hit]")
            previous_ball = ball

        # NORMAL BALL
        else:
            score += ball
            legal_balls += 1
            scorecard.append(f"{ball} run(s)")
            previous_ball = ball

        # OVER COMPLETE
        if legal_balls == 6:
            overs += 1
            legal_balls = 0
            print("Over", overs, "completed")

    # SAVE TO FILE
    with open(f"{player_no}.txt", "w") as f:
        f.write(f"Player {player_no} Final Score: {score}\n")
        f.write(f"Overs Played: {overs}.{legal_balls}\n")
        f.write("Scorecard:\n")
        for i, entry in enumerate(scorecard, 1):
            f.write(f"Ball {i}: {entry}\n")

    return score, scorecard

# MATCH START

print("RANDOM 2 PLAYER CRICKET GAME")
p1_score, p1_card = play_innings(1)
p2_score, p2_card = play_innings(2)

# FINAL SCORECARD
print("\nFINAL SCORECARD")
print("\nPlayer 1:")
for i, ball in enumerate(p1_card, 1):
    print(f"Ball {i}: {ball}")
print("Total Score:", p1_score)
print("\nPlayer 2:")
for i, ball in enumerate(p2_card, 1):
    print(f"Ball {i}: {ball}")
print("Total Score:", p2_score)

# MATCH RESULT
print("\nMATCH RESULT")
if p1_score > p2_score:
    print("Player 1 Wins")

elif p2_score > p1_score:
    print("Player 2 Wins")
else:
    print("Match Draw")
