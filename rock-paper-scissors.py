import random,time
rps = ["rock","paper","scissors"]
you_score = 0
bot_score = 0
for i in range(5):
    def shuffle():
        return random.choice(rps)
    you = input("rock/paper/scissors: ")
    you = you.lower()
    while you not in rps:
        print("processing....")
        time.sleep(2)
        print("i thought we were playing a game here?")
        you = input("rock/paper/scissors: ")
        you = you.lower()
    else:
        print("processing....")
        time.sleep(2)  
        bot = shuffle()
        print(f"you:{you}")
        print(f"me:{bot}")
        print("processing...")
        time.sleep(2)
        if you == bot:
            print("it's a tie!")
            you_score += 1
            bot_score += 1
        elif you == "rock" and bot == "paper":   
            print("you lost!")
            bot_score += 1
        elif you == "rock" and bot == "scissors":
            print("you won!")
            you_score += 1
        elif you == "paper" and bot == "rock":
            print("you won!")
            you_score += 1
        elif you =="paper" and bot == "scissors":
            print("you lost!")
            bot_score += 1
        elif you == "scissors" and bot == "rock":
            print("you lost!")
            bot_score += 1
        elif you == "scissors" and bot == "paper":
            print("you won!")                   
            you_score += 1
        print(f'''you:me
{you_score}:{bot_score}''')    
if you_score > bot_score:
    print("hurray you won!")
elif you_score < bot_score:
    print("well you lost lol!")
elif you_score == bot_score:
    print("it's a draw!")                