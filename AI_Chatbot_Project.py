#AI Chatbot, Built by Jayden, Matthew and Anmol
#import
from tkinter import *
import time
import random

#variables
name = ""
low_choice = ""
chances = int(0)
greg_think = ""

#------WINDOWS-------
#Defines screen1
def Screen1():
    frame1
    
def Screen2():
    Begin()




#------FUNCTIONS------
#Chat function
#Hobby code
def hobby2():
    print("do you think I could do something like that?")
    print("1. Yes")
    print("2. No")
    GM = input("> ")
    if GM == "1":
        print("Nice!")
        time.sleep(1)
        print("That was a nice chat, lets talk agian sometime")
        loop()
    elif GM == "2":
        print("oh")
        print("Is it because I'm a robot?")
        GM = input("> ")
        print("sure it is...")
        time.sleep(1)
        print("Thanks for the chat")
        loop()
    else:
        print("that isn't one of the options...")
        time.sleep(1)
        print("")
        hobby2()

def hobby():
    print("Do you have any hobbies?")
    print("1. Yes")
    print("2. No")
    GM = input("> ")
    if GM == "1":
        print("What is your hobby?")
        usertext = input("> ")
        print("{} sounds like a lot of fun!".format(usertext))
        time.sleep(1)
        hobby2()
    elif GM == "2":
        print("No hobbies? Okay... maybe give coding a try!")
        time.sleep(1)
    else:
        print("that isn't one of the options...")
        time.sleep(1)
        print("")
        hobby()

#If User is Good
def chatgood():
    print("Thats good to hear! What made your day good?")
    GM = input("> ")
    print("That's great!")
    time.sleep(1)
    hobby()

#If user is Bad
def chatbad():
    print("Sorry to hear that {}".format(name))
    GM = input("> ")
    print("I hope your day gets better soon")
    time.sleep(1)
    hobby()

#If user is Sad
def chatsad():
    print("I'm sorry to hear that you are sad today! What has made you sad?")
    GM = input("> ")
    print("I hope you feel better soon")
    time.sleep(1)
    hobby()

def chat():
    print("-----CONVERSATION: BEGIN-----")
    print("How are you doing today?")
    print("1 - Good")
    print("2 - Bad")
    print("3 - Sad")
    try:
        GM = int(input("> "))
    except ValueError:
        print("Pick one of the numbers")
        chat()
    if GM >= 4:
        print("That isn't one of my functions")
        chat()
    elif GM <= 0:
        print("That isn't one of my functions")
        chat()
    
    if GM == 1:
        chatgood()
    elif GM == 2:
        chatbad()
    elif GM == 3:
        chatsad()
    
    
    
#PSR player chooses if they want to play agian
def PSRChoice():
    print("Wanna play agian?")
    psrchoice = input("> ")
    if psrchoice.lower() == "y":
        psr()
    elif psrchoice.lower() == "n":
        print("Okay, maybe another time")
        loop()
    else:
        print("Input Y for yes or N for no")
        PSRChoice()
    
#Paper Scissors Rock (PSR) function
def psr():
    psr_list = ["Paper", "Scissors", "Rock"]
    print("-----PAPER SCISSORS ROCK-----")
    print("Okay! Pick an option from below (don't worry, I won't look!)")
    print("1. Scissors")
    print("2. Paper")
    print("3. Rock")
    try:
        psr_choice = int(input("> "))
    except ValueError:
        print("That isn't an option")
        print("These will be translated into buttons later so dont feel bad for being a super big dumb dumb")
        psr()
    if psr_choice >= 4:
        print("That isn't an option")
        psr()
    elif psr_choice <= 0:
        print("what are you even doing...")
        psr()
    greg_choice = random.choice(psr_list)
    print("Gregory chose: {}".format(greg_choice))
    
    #User picks scissors
    if psr_choice == 1:
        if greg_choice == "Rock":
            print("Gergory wins!")
        elif greg_choice == "Scissors":
            print("Draw!")
        elif greg_choice == "Paper":
            print("You win!")
        PSRChoice()
    
    #User picks paper
    if psr_choice == 2:
        if greg_choice == "Rock":
            print("You win!")
        elif greg_choice == "Scissors":
            print("Gregory wins!")
        elif greg_choice == "Paper":
            print("Draw!")
        PSRChoice()
    
    #User picks rock
    if psr_choice == 3:
        if greg_choice == "Rock":
            print("Draw!")
        elif greg_choice == "Scissors":
            print("You win!")
        elif greg_choice == "Paper":
            print("Gregory wins!")
        PSRChoice()    
    

#GTN player chooses if they want to play again        
def GTNChoice():
    print("Wanna play agian?")
    gtnchoice = input("> ")
    if gtnchoice.lower() == "y":
        gtn()
    elif gtnchoice.lower() == "n":
        print("Okay, maybe another time")
        loop()
    else:
        print("Input Y for yes or N for no")
        GTNChoice()

#Easy function
def easy():
    for chances in range(0, 3):
        user_choice = int(input("> "))
        if user_choice == greg_think:
            print("You got it!")
            GTNChoice()
        elif user_choice != greg_think:
            print("Thats not it")
            print("You have {} chance/s".format(chances))
        
        if chances == 0:
            print("-----You've run out of chances!-----")
            time.sleep(1)
            GTNChoice()            
            
            

#Med function

#Hard function
        
#Guess the number (GTN) function
def gtn():
    global chances
    global greg_think
    
    print("-----GUESS THE NUMBER-----")
    print("Okay! Pick a difficulty from below!")
    print("1. Easy (1 - 10)")
    print("2. Medium (1 - 50)")
    print("3. Hard (1 - 100)")
    try:
        gtn_diff = int(input("> "))
    except ValueError:
        print("Not an option")
        gtn()

    if gtn_diff >= 4:
        print("That isn't an option")
        psr()
    elif gtn_diff <= 0:
        print("what are you even doing...")
        psr()
    
    #Easy
    if gtn_diff == 1:
        chances = int(3)
        greg_think = random.randint(1, 10)
        print("I am thinking of a number between 1 and 10...")
        easy()
    
    #Medium
    
    #Hard


#Game Hub function
def Game():
    print("----GAME HUB---")
    print("This is the Game Hub!")
    print("Here you can choose from two simple games for us to play!")
    print("Just enter the corrosponding number to what you would like to do:")
    print("1 - Paper Scissors Rock!")
    print("2 - Guess the number!")
    print("3 - Exit back to the menu")
    game_choice = input("> ")
    if game_choice == "1":
        psr()
    elif game_choice == "2":
        gtn()
    elif game_choice == "3":
        loop()
    else:
        print("Thats, not an option... pick from between 1-3")
        Game()


#Help list
def help():
    print("----Help----")
    print("Don't fret! Here is a list of my functions and some tips!:")
    print("Chat: This lets me know you want to have a conversation with me!")
    print("Game: This lets us play paper sissors rock! And possibly other games, but we will have to wait and see...")
    print("Exit: This lets you close this application")
    print("------------")
    loop()


#End function
def End():
    print("Goodbye")




#Loop
def loop():
    global choice
    
    print("")
    print("--------MAIN MENU--------")
    print("what would you like to do now?")
    choice = input("> ")
    choicelow = choice.lower()
    if choicelow == "exit":
        End()
    elif choicelow == "game":
        Game()
    elif choicelow == "help":
        help()
    elif choicelow == "chat":
        chat()
    else:
        print("Sorry, that isn't one of my functions...")
        print("If you are having trouble figuring this out, type help.")
        loop()
    
#Beginning routine
def Begin():
    print("Hello there, my name is Gregory, I am a digital assistant. What is your name?")
    name = input("> ")
    print("hello {}, if you are unsure of what to do, type help.".format(name))
    time.sleep(2)
    loop() 
    


#Main routine

root = Tk()
root.title("Gregory The Chatbot")
root.geometry("300x145+800+0")

#Create frame1
frame1 = LabelFrame(root, height = "300", width = "600", bg = "white")
frame1.grid(row=0, column=0)

#widgets
TitleLabel = Label(frame1, bg = "black", fg = "white", width = 20, padx = 30,
                   pady = 10, text = "Gregory The Chatbot", font =("comic sans ms", "14", "bold"))
TitleLabel.grid(columnspan = 2)

AboutLabel = Label(frame1, text = "Built by Jayden, Matthew and Anmol", width = 20, height = 3,
                   padx = 80, pady = 10, bg = "white", fg = "black", font =("comic sans ms", "7"))
AboutLabel.grid(row = 4, column = 0)



button1 = Button(frame1, text = "Start", anchor = W, command = Screen2)
button1.grid(row = 9, column = 0)


#begin
Screen1()
root.mainloop()