import time
import sys

started = False

def type(string):
  for i in string:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.03)

def quiz():
    score = 0
    
    type("\nThe quiz has now started.")
    time.sleep(1)
    q1correct = False
    type("\n\nQUESTION 1: What is the capital of France?")

    while q1correct == False:
        q1 = input("\n>")
        
        if q1.lower() == "paris":
            type("\nCorrect! The capital of France is Paris.")
            score = score + 1
            q1correct = True
        else:
            type("\nThat was incorrect. Please try again.")

    type("\n\nQUESTION 2: What is 200,000 + 300,000?")
    try:
        q2 = input("\n>")

        if q2 == "500,000":
            type("\nCorrect! 200,000 + 300,000 is 500,000.")
            score = score + 1
        elif int(q2) == 200000+300000:
            type("\nCorrect! 200,000 + 300,000 is 500,000.")
            score = score + 1
        else:
            type("\nIncorrect. The answer was 500,000.")
    except ValueError:
        type("\nIncorrect. The answer was 500,000.")

    type("\n\nQUESTION 3: Who is the current prime minister of the United Kingdom (January 2023)? You get 3 tries at this question.")
    q3correct = False
    tries = 3

    while q3correct == False:
        while tries != 0:
            q3 = input("\n>")
            if q3.lower() == "rishi sunak":
                type("Correct! The prime minister of the United Kingdom is Rishi Sunak (in January 2023)")
                score = score + 1
                q3correct = True
                break
            else:
                tries = tries - 1
                if tries == 1:
                    type(("Incorrect. You have ", str(tries), " more try."))
                elif tries != 0:
                    type(("Incorrect. You have ", str(tries), " more tries."))
        if q3correct != True:
            type("\nYou have run out of tries. The answer was Rishi Sunak.")
        break

    type("\n\nWould you like to try a Bonus question? This will be added onto your score if you get it correct. (Y/N)")
    bonus = input("\n>")

    if bonus.lower() == "y":
        type("\nBONUS QUESTION: What is the brains of a computer called? You have 3 tries at this question.")
        bonuscorrect = False
        bonustries = 3

        while bonuscorrect == False:
            while bonustries != 0:
                bonusq = input("\n>")
                if bonusq.lower() == "cpu":
                    type("Correct! The brains of a computer is called the CPU")
                    score = score + 1
                    bonuscorrect = True
                    break
                else:
                    bonustries = bonustries - 1
                    if bonustries == 1:
                        type(("Incorrect. You have ", str(bonustries), " more try."))
                    elif bonustries != 0:
                        type(("Incorrect. You have ", str(bonustries), " more tries."))
            if bonuscorrect != True:
                type("\nYou have run out of tries. The answer was CPU.")
            break

    type("\n\nWell done for completing Jamie's mega hard quiz! Here is your score: ")
    if bonus.lower() == "y":
        type((str(score), "/4"))
    else:
        type((str(score), "/3"))

type("Welcome to Jamie's mega hard quiz!\n\n")
time.sleep(2)
type("In this quiz you will be asked a series of questions. ")
time.sleep(0.5)
type("To which you will have to answer, ")
time.sleep(0.2)
type("of course. ")
time.sleep(0.5)
type("You will get 1 point for every quesion you get correct, ")
time.sleep(0.2)
type("and some questions you can't move on until your answer is correct. \n\n")
time.sleep(2)
print("Good luck! \n")

while started == False:
    print("When you are ready to start the quiz, please enter Y, if you would like to close the quiz, please type N.")
    start = input("\n>")

    if start.lower() == "y":
        started = True
        quiz()
    elif start.lower() == "n":
        print("Thank you for trying out Jamie's mega hard quiz, I hope to see you again. Goodbye!")
        sys.exit(0)
    else:
        print("\nThat was not an option. Please try again.")
