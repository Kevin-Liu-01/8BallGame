import random
#List containing all possible responses
rollResult = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes-definitely.", "You may rely on it.",
              "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
              "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Better not tell you now.",
              "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
              "My sources say no.", "Outlook not so good.", "Very doubtful."]
#ValidationFunction
def validateUserInput(s, valid_inputs):
    u = s.upper()
    for v in valid_inputs:
        if u == "YES":
            return True
    if(u != "NO"):
        print("Invalid Input: " + s + ". Only YES and NO are accepted.")
        return False
    return False
#Credits
print("---------------------------------------------")
print("Made by Kevin Liu for ROCO. Use responsibly.")
print("---------------------------------------------")
print("Hey User! You will be able to find answers to")
print("your life's most pressing problems through the")
print("analytical wizardry of a UTF-8 encoded 8Ball!")
print("Another thing - this 8ball suffers from no such")
print("qualms as capitalization. YEs or nO away!")
print("---------------------------------------------")

#Infinite while loop
while True:
    begin = input("Welcome to the 8ball. Input YES or NO to activate me. ")
    #NO will simply end the program
    if validateUserInput(begin, ["YES", "NO"]):
        filler=["red herring ;)"]
    elif begin.upper() == "NO":
        break
    elif begin.upper() != "NO":
        continue
    escape = False
    while begin.upper() == "YES" and not escape:
        while not escape:
            questioning=input("What kind of pressing issue do you want me to answer? Write NOTHING to access settings. ")
            #Accessing settings
            if questioning.upper() == "NOTHING":
                print("Opening settings editor.")
                escape = True;
                break
            #8Ball responds
            print("Your response: " + questioning)
            Add = input("Are you sure you want to ask me this? YES/NO ")
            if not validateUserInput(Add, ["yes", "no"]):
                print("Don't waste my time. Even a ball has priorities.")
                continue
            if Add.upper() == "YES":
                rolled = rollResult[random.randint(1, 20)]
                print(rolled)
                file=False
            #Saving the results
                while file==False:
                    confirmation=input("Would you like to save your question and response? YES/NO ")
                    if confirmation.upper()=="YES":
                        saveFile=open("SavedResponse", "w")
                        saveFile.write("USER-QUESTION: " + str(questioning))
                        saveFile.write("\n 8BALL RESPONSE: " + str(rolled))
                        saveFile.close()
                        file=True
                    elif confirmation.upper()=="NO":
                        break
                    else:
                        print("Invalid Input: " + confirmation)
            else:
                print("Invalid Input. Try again, please.")


    #Settings
    settingsOpener = input("Welcome to the 8ball Settings Editor. Are you sure you want to begin the settings prompts? YES/NO ")
    if validateUserInput(settingsOpener, ["YES", "NO"]):
        all_grades = {}
    elif settingsOpener.upper() == "NO":
        break
    elif settingsOpener.upper() != "NO":
        continue
    escape = False

    while not escape:
        #Adding responses
        while True:
            newAnswer = input("Would you like to add additional responses to the 8ball? YES/NO ")
            if newAnswer.upper() == "YES":
                ballResponses=input("Give me a potential response. ")
                rollResult.append(ballResponses)
                print("Response - " + ballResponses + " - has been added.")
            elif newAnswer.upper() == "NO":
                break
            else:
                print("Invalid Input: " + newAnswer.upper() + ". Please try again.")
        #Viewing responses
        while True:
            allAnswers = input("Would you like to view all responses? YES/NO ")
            if allAnswers.upper() == "YES":
                for everyResponse in rollResult:
                    print(everyResponse)
            elif allAnswers.upper() == "NO":
                break
            else:
                print("Invalid Input: " + allAnswers.upper() + ". Please try again.")
        #Viewing specific responses
        while True:
            specAnswers = input("Would you like to view a specific response? YES/NO ")
            if specAnswers.upper() == "YES":
                specAnswerInRoll=input("There are " + str(len(rollResult)) + " responses. Which response do you want to view? Etc. 18 would print response 18. ")
                print("Response " + specAnswerInRoll + ": " + str(rollResult[int(specAnswerInRoll)-1]))
            elif specAnswers.upper() == "NO":
                break
            else:
                print("Invalid Input: " + specAnswers.upper() + ". Please try again.")
        #Removing responses
        while True:
            Remove = input("Would you like to remove a response? YES/NO ")
            if Remove.upper() == "YES":
                remove_answer = input("Which response would you like to remove? Etc. 18 would remove response 18. ")
                rollResult.pop(int(remove_answer))
                print("Response " + remove_answer + " - " + rollResult[int(remove_answer)-1] + " - has been removed. ")
                print("New Response List: " + str(rollResult))
            elif Remove.upper() == "NO":
                break
            else:
                print("Invalid Input: " + Remove.upper() + ". Please try again.")
    print("Settings mode deactivated.")
    #Back to the beginning
