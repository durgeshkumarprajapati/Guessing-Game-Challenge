import random
a=random.randint(1,100)
u_guesses=[]
print('''Rules:-
    1. you have to guess a number between 1 to 100
    2. if your guess is correct then you won the game
    3. if your guessed number is 10 away from the number then you get WARM else you get COLD
    4. if your guess is closer than previous guess then you get warmer 
    5. if your guess is more away from previous guess then you get colder
    ''')
while True:
 
    u_input=int(input("guess a number:"))
    if u_input<1 or u_input>100:
        print("OUT OF BOUNDS")
        continue
    else:
        u_guesses.append(u_input)
        if u_input==a:
            print("You guess correctly:\n you guessed in:",len(u_guesses),"attempt")
            break
        elif abs(u_input-a)<=10 and abs(a-u_input)<=10 and len(u_guesses)==1:
            print("Warm")
        elif abs(u_input-a)>10 and abs(a-u_input)>10 and len(u_guesses)==1:
            print("COLD")
        elif (abs(u_input-a)>abs(u_guesses[-2]-a)):
            print("COLDER")
        elif (abs(u_input-a)<abs(u_guesses[-2]-a)):
            print("WARMER")
        else:
            pass
