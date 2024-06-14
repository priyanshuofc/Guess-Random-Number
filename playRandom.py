import random

def randomNumber():
    return random.randint(1, 101)

point = 0

print("""Welcome to Trivitz.com!
      
      In this game you have to enter a number between 1 to 100.
      
      And guess your number is greater than, equal to or less than system
      generated number.
      
      If your guess is right you will be awarded +10 Points and on worng guess
      -8 Points
      
      To exit the game write quit, leave or end
      
      """)

playGame = input("are you want to play game: [y] or [n]: ").lower()

if playGame == "y":
    while(True):
        
        user = input("Your guess: ").lower().strip() 
        
        if user in ["quit", "leave", "end"]:
            print(f"Your total point is {point}")
            break
        
        try:
            yourGuess = input("Guess number is greater than, equal to or less than system generated number - [g for greater], [e for equal] [l for less]: ").lower()
            userN = int(user)
            randomNum = randomNumber()
            
            if yourGuess == "g" and userN > randomNum:
                print("You Win")
                print(f"your number is {userN} and computer generated number is {randomNum}")
                point = point + 10             
            elif yourGuess == "l" and userN < randomNum:
                print("You Win")
                print(f"your number is {userN} and computer generated number is {randomNum}")
                point = point + 10
            elif yourGuess == "e" and userN == randomNum:
                print("You Win")
                print(f"your number is {userN} and computer generated number is {randomNum}")
                point = point + 10
            else:
                print("You Lose")
                print(f"your number is {userN} and computer generated number is {randomNum}")
                point = point - 8
                
        except ValueError:
            print("Enter the correct input")                
