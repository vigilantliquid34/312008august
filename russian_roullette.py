print("russian roulette")
# once your bar reaches zero it’s game over.
import random, time

def ran_bullet():
    return random.randint(2, 6)

def live_bullets():
    return random.randint(1, 3)

def abilities():
    return random.choice(["incognito", "useless fuck"] * 6)

round = 0
user_health = 3
bots_health = 3

username = input("what's your name?: ").strip()
print("....")
time.sleep(1)
while username == "":
    username = input("what's your name?: ").strip()
    print("....")
    time.sleep(1)

needs_help = input("do you know the basics of the game btw?\n:") 
print("....")
time.sleep(1)
while needs_help.lower() not in ["yes", "no"]:
    print("a yes or no will do")
    needs_help = input("do you know the basics of the game btw?\n:")  
    print("....")
    time.sleep(1)

if needs_help.lower() == "no":
    print("ok sooo basically you are playing with a madman")
    time.sleep(1)    
    print("you and the 'madman' are playing a death game")
    time.sleep(1)    
    print("you each take turns pointing the gun at one another")
    time.sleep(1)    
    print("some shots are live...some are blank")
    time.sleep(1)    
    print("it's up to you to guess the right from the wrongs")
    time.sleep(1)    
    print("with the incognito ability you can know the next shot.......(and yh you have 3 hearts)")
elif needs_help.lower() == "yes":
    print(f"{username}? that's your name right? lol you sabi")

print("alright then goodluck!")     

for i in range(3):
    round += 1
    print(f"\nROUND: {round}")
    number_of_shells = ran_bullet()
    live_shells = live_bullets()

    if live_shells == number_of_shells:
        live_shells -= 1
    elif live_shells == 3 and number_of_shells == 2:
        live_shells, number_of_shells = number_of_shells, live_shells

    the_shell = ["a", "b", "c", "d", "e", "f"]
    the_shell = the_shell[0:number_of_shells]   
    the_liveshell = random.sample(the_shell, live_shells)

    users_ability = abilities()

    print(f"rn there are {number_of_shells} bullets.")
    print(f"and also there are/is {len(the_liveshell)} live shots!")
    time.sleep(1)
    if users_ability == "incognito":
        print("yayyy you got the incognito buff!")
        users_ability = 1
    else:
        print(f"lol you got the {users_ability} buff")   

    while len(the_shell) != 0 and user_health > 0 and bots_health > 0:
        user_shot = input(f"choose which shell you would like to use to shoot {the_shell}: ")
        while user_shot.lower() not in the_shell:
            print("sorry but that's not an option!")
            user_shot = input(f"{the_shell}: ")

        if user_shot in the_liveshell:
            user_shot_result = 1
            user_live_blank = "live"
            the_shell.remove(user_shot)
            the_liveshell.remove(user_shot)   
        else:
            user_shot_result = 0      
            user_live_blank = "blank" 
            the_shell.remove(user_shot) 

        if len(the_shell) > 0:
            bot_shot = random.choice(the_shell)
            if bot_shot in the_liveshell:
                bot_shot_result = 1
                bot_live_blank = "live"
                the_shell.remove(bot_shot)
                the_liveshell.remove(bot_shot)   
            else:
                bot_shot_result = 0    
                bot_live_blank = "blank"
                the_shell.remove(bot_shot) 
                if bot_shot in the_liveshell:
                    the_liveshell.remove(bot_shot)
        else:
            print("no bullets left for the madman to shoot.")
            bot_shot = "none"
            bot_shot_result = 0
            bot_live_blank = "blank"

        def at_you(user_health, shot):
            return user_health - shot

        def at_madman(bots_health, shot):
            return bots_health - shot    

        bots_health = at_madman(bots_health, user_shot_result)
        user_health = at_you(user_health, bot_shot_result)

        print("processing...")
        time.sleep(2)
        print(f"apparently {username} shot the madman... and it was a {user_live_blank} shot! ({user_shot})") 
        time.sleep(1)
        if bot_shot != "none":
            print("now it's his turn...")
            time.sleep(1)
            print(f"well the madman shot at {username}... and it was a {bot_live_blank} shot! ({bot_shot})")
        
        print(f'''scores:
        you ---- madman
        {user_health} hearts ---- {bots_health} hearts
        ''')

        if len(the_shell) == 0:
            print(f"well that's the end of round {round}, out of bullets")
        else:
            print("looks like we still have some bullets left!... let's continue then")    

        if user_health == 0:
            print("you died!")    
        if bots_health == 0:
            print("the madman died!") 
