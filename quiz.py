from questionsAndAnswers import answer_key, questionsAndOptions
import random

highestscore = 0

def entername():
    name = input("Please press enter your name to begin: ")
    if name.strip() == "":
        entername()
    return name

def askQuestion(numofq):
    score = 0
    for i in range(numofq):
        question = random.randrange(1,len(answer_key))
        key, value = list(questionsAndOptions.items())[question]
        rightanswer = list(answer_key.values())[question]
        
        print(i  + 1,'.',key)
        for i in value:
            print(i)
            
        answer = input("Answer: ")
        if answer == rightanswer:
            score = score + 1
            print("correct")
        else:
            print("incorrect")
    return score


print("Welcome to the quiz!")
name = entername()
print("Hello", name, "let's get started!")

score = askQuestion(2)

if highestscore < score:
    highestscore = score
    
print("Mr.", name, "your score is", score)
print("Mr.", name, "your Highestscore is", highestscore)



    
    

