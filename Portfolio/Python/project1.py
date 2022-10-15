import random


def madlib():
    #String concantenation aka how to put strings together
    # suppose we  want that says "subscribe to _____"

    #different ways to do this

    youtuber = "KingKonceptz"
    print("subscribe to " + youtuber)
    print("subscribe to {}".format(youtuber))

    #cleanest way to do print concantenation
    print(f"subscribe to {youtuber}")

    #creating a madlib
    adj = input("Adjective: ")
    verb = input("Input verb: ")
    verb2 = input("Input verb: ")
    famous_person = ("input famous Person: ")
    madlib = f"Computer programming is so {adj}! It makes me so excited all the time because\
     I love to {verb}. Stay hydrated and {verb2} like you are {famous_person}!"

    print(madlib)





def band_name_generator():
    #this was a basic coding program that reintialized my journey in coding
    print(" Welcome to the band name generator\n")
    print("What city you grew up in?\n")
    code = input("Your answer: ")

    ans1 = code
    print("\nWhat's your pets name?\n")
    code = input("Your answer: ")
    ans2 = code

    print("\nYour band name is: ",ans1,"-",ans2)


#making 'x' a parameter to pass into the function
def guessing_game_pvc(x):

    #generating a random number using rand int the '1' is an absoulute number making x the only random variable
    random_number = random.randint(1,x)

    #iniatilizing the variable guess
    guess = 0

    #if you don't have a predefined restrictions for a loop to iterate use a while loop
    while guess != random_number:

        #cast the input as an integer while also using f string
        guess= int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number :
            print (" You guessed too low guess again")
        elif guess > random_number:
            print("You guessed too high guess again")
        else:
            print(f"You have guessed the number {random_number} correctly! ")
            print("Returning to the main menu:\n")

            programs()

def guessing_game_cvp(x):
    # creating some bounds a low bound is the first one
    low = 1
    # the high bound is a variable passed to the function
    high = x
    # initializing a feedback variable
    feedback = ''
    # displaying instructions
    print("Enter 'l', too high 'h' or if its correct 'c'")
    #While feedback is not Correct
    while feedback != 'c':
        # if low and high is not the same
        if low != high:
            # Guess takes two variables in this case 1,30
            guess= random.randint(low, high)
        else:
            guess = low # could be equal to high
        feedback = input(f"Is {guess} correct? ").lower
        # if the feedback is h then its too high try again
        if feedback == "h":
        # if its too high it will subtract 1 and ask again
            high = guess -1
        # setting the low bound
        elif feedback == "l" :
        # If its too low it will add one and ask again
            low = guess +1
        else:
            # Congratulate the computer
            print(f"The computer has guessed your answer {guess} correctly")
            # Quit the program
            quit()





def programs():
    #List of programs available
    options = ["MadLib","Band_Name_Generator","guessing_game_pvc"," guessing_game_cvp"]

    #intializing variables one for the list items and one to count with
    list_items = 0
    counter = 0

    #For loop to iterate through the list
    for list_items in options:
        #increasing the value of counter every iteration of the loop
        counter += 1


        #printing the list with a number
        print(f"{counter}:{list_items}")


   # casting the user input as an integer
    choice = int(input("Select which program you would like to use: "))

    #try catch statement to verify input
    try:

        #if else statements to set boundaries
        if choice > len(options):
            print("Invalid selection please enter a number or enter 10 to quit\n")
            programs()
        if choice < 0:
            print("Invalid selection please enter a number or enter 20 to quit\n")
            programs()
    except:
        print("Invalid selection please enter a number or enter 30 to quit\n")
        programs()


    #creating if statements to correspond to the items in the list
    if choice == 0:
        #terminating the script
        exit()
    elif choice == 1:
        madlib()
    elif choice == 2:
        band_name_generator()
    elif choice == 3:
        # calling the function and making the x parameter 20
        guessing_game_pvc(20)
    elif choice == 4:
        guessing_game_cvp(30)

programs()
