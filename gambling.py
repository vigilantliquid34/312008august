import random
import time
BALANCE = 150
print("gambling 🤑")
print("18+ lol")
customer = input("what's your name btw?: ").strip()
while not customer:
    print("your name can't be that!")
    customer = input("what's your name btw?: ").strip()
print("processing...")
time.sleep(1)
while True:
    try:
        age =  int(input(f"{customer} what's your age?: "))
        if age <= 0:
            print("processing...")
            time.sleep(1)  
            print("why are you doing this naw")
        else:
            print("processing...")
            time.sleep(1)
            break
    except:
        print("processing...") 
        time.sleep(1)
        print("seriously?💀")   
balls_list = ["blue","red","yellow","green"]
def lets_gamble():
    the_random_ball = random.choice(balls_list) 
    return the_random_ball
if age < 18:
    print(f"woah! i'm sorry {customer} but it's clearly for 18+")
    print("but let's say nothing happened here alright...you can play🙂")   
    print("you are gonna lose either way so i'm giving you extra $50")
    time.sleep(5) 
    BALANCE += 50
elif age >= 18:
    print("welcome.")
print("processing...")
time.sleep(1)              
print("jsyk i don't encourage gambling.")
print("there are 4 balls in the slot:blue,red,yellow and green")
print("for each round;if you get it right your cash will be tripled")
print("if not...it will be halved")
print("at the moment you have:$",BALANCE)
start = input(f"type START to begin and STOP to quit....goodluck {customer}: ")
print("processing....")
time.sleep(1)

make_bet = "start"
while make_bet.upper() != "STOP":
    while start.upper() != "START":
        time.sleep(1)
        print("🤡")
        start = input("just type start: ")
    while True:
        try:
            cash_deposited = int(input("how much do you want to deposit?: "))
            if BALANCE < cash_deposited:
                print("sorry but you don't have up to that")
            elif cash_deposited <= 0:
                print("sorry but that doesn't make sense")
            else:
                print(cash_deposited)
                break
        except:
            print("numbers?") 
    the_guessed_ball = input("now bet on the ball you think will be shot out: ") 
    while  the_guessed_ball.lower() not in balls_list:
        print("sorry but that isn't part of the collection of balls") 
        the_guessed_ball = input("now bet on the ball you think will be shot out: ")                      
    time.sleep(1)
    the_random_ball = lets_gamble()
    print(f"{customer} you have used ${cash_deposited} to bet on {the_guessed_ball}") 
    time.sleep(1)
    print("calculating results...") 
    time.sleep(2)
    if the_guessed_ball.lower() == the_random_ball:
        print(f"hurray... the choice {the_guessed_ball} was correct!")
        cash_deposited *= 3
        BALANCE += cash_deposited
        print("your balance is $",BALANCE) 
    else:
        print(f"sorry...but the choice {the_guessed_ball} ball was wrong.")
        print(f"{the_random_ball} ball was right") 
        cash_deposited /= 2
        BALANCE -= cash_deposited
        print("your balance is $",BALANCE) 
    make_bet = input("START to continue or STOP to quit: ")
    while make_bet.upper() not in ["START","STOP"]:
        print("🤡")    
        make_bet = input("START to continue or STOP to quit: ")
    if make_bet.upper() == "STOP":
        print(f"dear {customer} you have succesfully withdrawn $",BALANCE) 
    elif BALANCE < 30:
        print(f"dear {customer} you are low on cash as of now your balance is $",BALANCE)
        break       