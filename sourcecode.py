#Cricket Rules Quiz
#By Alex Gwynne
#All comments are written above what they are commenting on
#I did use Chatgpt for different parts during the creation of this quiz. Mainly to explain to me what some of the more complicated code meant that was required for me to build this program and to find out what parts of my code were stopping the program from running
import tkinter as tk
from tkinter import ttk, messagebox


#Variables
#Chatgpt was used to understand the functions of the lists and dictionaries in this code
quiz_options = {
    #Each question and it's possible answers (for all four quizzes) are stored in dictionaries to keep the information together and related
    #The possible answers are stored within lists inside the dictionaries so that they display in the right order
    #First Rules Quiz
    "Easy Cricket Rules Quiz": [
        #Dictionaries for the questions
        {"question": "Which of the following situations constitutes a ‘wide ball’ signal from the umpire?", "options": ["The ball passes the batter too wide to hit with a normal cricket shot", "The bowler delivers a full toss above waist height", "The bowler oversteps the front crease during delivery"], "answer": "The ball passes the batter too wide to hit with a normal cricket shot"},
        {"question": "Which of the following situations constitutes a ‘no ball’ signal from the umpire?", "options": ["The bowler runs in to deliver the ball but pulls out", "The bowler delivers a full toss above waist height", "The batter hits his own stumps"], "answer": "The bowler delivers a full toss above waist height"},
        {"question": "If the batsman hits the ball over the boundary on the full, how many runs are awarded?", "options": ["4", "6", "7"], "answer": "6"},
        {"question": "If the batsman hits the ball to the boundary along the ground, how many runs are awarded?", "options": ["3", "6", "4"], "answer": "4"},
        {"question": "What does LBW stand for?", "options": ["Leg Before Wicket", "Lunch Before Wides", "Leg Behind Waist"], "answer": "Leg Before Wicket"},
        {"question": "How many players from the fielding team can be on the field at once?", "options": ["11", "10", "9"], "answer": "11"},
        {"question": "Apart from boundaries, how else can the batsman score runs?", "options": ["Hitting the ball to certain zones", "Running between the wickets", "Dodging the fielders that are throwing the ball at them"], "answer": "Running between the wickets"},
        {"question": "How many deliveries are in an over?", "options": ["4", "8", "6"], "answer": "6"},
        {"question": "What is the maximum number of fielders the fielding team can have behind the 90-degree angle on the leg side of the pitch?", "options": ["1", "2", "As many as they like"], "answer": "2"},
        {"question": "How many umpires are there for a cricket match?", "options": ["2", "3", "0"], "answer": "2"},
    ],

    #Second Rules Quiz
    "Hard Cricket Rules Quiz": [
        #Dictionaries for the questions
        {"question": "What is the weight range that a new cricket ball must be within at the beginning of play?", "options": ["140 to 150 grams", "155.9 to 163 grams", "164.3 to 167 grams"], "answer": "155.9 to 163 grams"},
        {"question": "When does the first powerplay end in a traditional length T20 and One Day match?", "options": ["5 and 15 overs", "6 and 10 overs", "8 and 12 overs"], "answer": "6 and 10 overs"},
        {"question": "How long does the batsman have to be present at the crease after the last batter was dismissed?", "options": ["60 seconds", "120 seconds", "180 seconds"], "answer": "180 seconds"},
        {"question": "When should a fielder repair the boundary if they were to damage it when fielding the ball?", "options": ["Immediately", "The next time the ball is dead", "They don't need to repair the boundary"], "answer": "The next time the ball is dead"},
        {"question": "When can the pitch be watered during a match?", "options": ["When the groundsman deem it necessary", "At the request of either captain", "The pitch may not be watered during a match"], "answer": "The pitch may not be watered during a match"},
        {"question": "Which of the following is not a legal method of fielding the ball?", "options": ["Using your foot", "Using your head", "Using your clothing"], "answer": "Using your clothing"},
        {"question": "What happens if the bowler hits the wickets with their delivery, but the bails are not broken?", "options": ["The umpire signals dead ball", "The batter is out", "Play continues"], "answer": "Play continues"},
        {"question": "What happens when a batter is dismissed by the bowler’s delivery, but there is no appeal from the fielders?", "options": ["The player is given Out by the umpire", "The player is Not Out", "The square-leg umpire can give the batter out"], "answer": "The player is Not Out"},
        {"question": "After a delivery is completed, when does the ball next become ‘in-play’?", "options": ["When the bowler begins their run-up", "When the ball has been returned to the bowler", "When the batter takes guard"], "answer": "When the bowler begins their run-up"},
        {"question": "What will the umpire do if they deem a fielder to have unfairly distracted the batter during a delivery?", "options": ["Call a No-Ball", "Give the fielder a warning only", "Award 5 penalty runs"], "answer": "Award 5 penalty runs"},
    ],

    #Trivia Quiz
    "Trivia Quiz": [
        #Dictionaries for the questions
        {"question": "Which player has scored the most test match runs of all time?", "options": ["Sachin Tendulkar", "Rahul Dravid", "Joe Root"], "answer": "Sachin Tendulkar"},
        {"question": "Which player has taken the most test match wickets of all time?", "options": ["Shane Warne", "Jimmy Anderson", "Muttiah Muralitharan"], "answer": "Muttiah Muralitharan"},
        {"question": "Which player has the best individual bowling figures of all time?", "options": ["Jim Laker", "Anil Kumble", "Ajaz Patel"], "answer": "Jim Laker"},
        {"question": "Which player has scored the most runs in one inning?", "options": ["Brian Lara", "Matthew Hayden", "Garry Sobers"], "answer": "Brian Lara"},
        {"question": "Which of these countries has never won a Cricket World Cup?", "options": ["England", "Pakistan", "New Zealand"], "answer": "New Zealand"},
        {"question": "What year was the first Test match played?", "options": ["1776", "1877", "1905"], "answer": "1877"},
        {"question": "What country did Don Bradman play for?", "options": ["England", "Australia", "South Africa"], "answer": "Australia"},
        {"question": "Who has taken the most catches in test cricket as an outfielder?", "options": ["Joe Root", "Steve Waugh", "Mike Gatting"], "answer": "Joe Root"},
        {"question": "Which player has the highest batting average in test cricket?", "options": ["Graeme Pollock", "Don Bradman", "Virat Kohli"], "answer": "Don Bradman"},
        {"question": "Which of these players never captained their country?", "options": ["Brian Lara", "Rahul Dravid", "Muttiah Muralitharan"], "answer": "Muttiah Muralitharan"},
    ],

    #LingoQuiz
    "Lingo Quiz": [
        #Dictionaries for the questions
        {"question": "What does ‘getting a duck’ mean in cricket?", "options": ["Scoring exactly 100 runs in an innings", "Getting out without scoring any runs", "Taking 5 wickets in a match"], "answer": "Getting out without scoring any runs"},
        {"question": "The piece of cricket equipment known as a ‘bail’ is used for what?", "options": ["To place on top of the stumps", "To mark the boundary line", "To measure the pitch length"], "answer": "To place on top of the stumps"},
        {"question": "The term ‘dolly’ is used to describe what in cricket?", "options": ["A batsman who scores very slowly", "A soft, easily caught ball", "A slow, underarm delivery"], "answer": "A soft, easily caught ball"},
        {"question": "What does ‘square-leg’ mean?", "options": ["A fielding position on the leg side", "A type of bowling action", "An area outside the boundary"], "answer": "A fielding position on the leg side"},
        {"question": "If the batsman has played an ‘agricultural shot’. What has he done?", "options": ["Played a technically perfect textbook shot", "Missed the ball completely and been bowled", "Played a wild, unsophisticated slog across the line"], "answer": "Played a wild, unsophisticated slog across the line"},
        {"question": "If the bowler has bowled a dangerous delivery, what would that delivery be called?", "options": ["Beamer", "Boomer", "Beeker"], "answer": "Beamer"},
        {"question": "Which country is known for the ‘baggy green’ cricket cap?", "options": ["Australia", "South Africa", "Pakistan"], "answer": "Australia"},
        {"question": "If the cricket pitch is described as a ‘road’. Does it favour the bowler or the batter?", "options": ["Bowler", "Batter", "Neither"], "answer": "Batter"},
        {"question": "What happens if the captain was to ‘declare’?", "options": ["The team forfeits the match", "The captain challenges an umpire's decision", "The batting team voluntarily ends their innings"], "answer": "The batting team voluntarily ends their innings"},
        {"question": "If the batsman has scored a ‘century’, how many runs has he scored?", "options": ["100", "50", "0"], "answer": "100"},
    ]
}


root = tk.Tk()
root.title("My Quiz")
root.geometry("520x420")  # width x height

main = ttk.Frame(root, padding=16)
main.pack(fill="both", expand=True)

#Welcome message
print("Welcome to the best quiz for learning the rules of cricket!")
print("This quiz is suitable for people of varying experience playing cricket.")
print("Hopefully you will find this quiz helpful whether you are a player, coach or umpire!")
#While loop that runs until the user enters a valid name
while True:
    name = input("What is your name? ").strip()
    #if the user does not type anything before pressing enter, this message displays and they are instructed to enter their name again
    if name == "":
        print("Please enter your name!")
    #else the name is accepted and the user can move on (loop is broken)
    else:
        print(f"Welcome {name}. Let's play a quiz!")
        break

#Code that runs the quiz for the user to play
#I used Chatgpt to learn what things like enumerate do. This helped me to write the code
def run_quiz(name_quiz):
    #This line of code retrieves the questions from the dictionaries above for the quiz the user picked
    questions = quiz_options [name_quiz]
    #This code defines the score variable that will increase when the user gets a question right
    score = 0
    #I used Chatgpt to write the code that enumerates the questions
    print(f"\nThe '{name_quiz}' is about to begin!\n")
    #In this code 'i' is the question number and 'q' is the actual question from the dictionary above. The question number starts at 1 because of the 'questions, start=1' code
    for i, q in enumerate (questions, start=1):
        print(f"{i}: {q['question']}")
        for idx, option in enumerate(q["options"], start=1):
            print(f" {idx}.{option}")
    #This code is for the user to input the answer they want to put to the question. I added the 'try' function so that if the user does not put a valid answer to the question, the code doesn't break
        try:
            choice = int(input("Select your answer: "))
            #Prints if the option number the user selected was right
            if q["options"][choice - 1] == q["answer"]:
                print("\nThat is correct! ✅\n")
                score += 1
            #Prints if the user puts a valid answer but its wrong
            else:
                print("\nThat was not the correct answer ❌\n")
                print(f"The correct answer was {q['answer']}\n")
        #except only runs if the user doesn't put a valid answer to the question (1,2 or 3) so if they put 6 this code would run
        except (IndexError,ValueError):
            print("\nThat was not an option!")
            print("Entering invalid answers will forfeit your attempt at this question\n")
    #Ending message
    print("Nice Job!")
    print(f"You completed the {name_quiz}")
    #This code prints the users score out of the number of questions in the quiz. Each quiz has 10 questions so it will always be out of 10 but if the quizzes had different amounts of questions this message would change depending on the number of total questions
    #len counts the length (number of questions) in the above quiz lists
    print(f"Your score on the quiz was {score}/{len(questions)}")

#Code that lets the user decide which of the four quizzes they want to play
def main ():
    #while true makes this code run again when the user is finished the quiz. This makes it so the user can play another quiz
    while True:
        print("\nThese are the four cricket related quizzes you can play!")
        quiz_names = list(quiz_options.keys())

        for idx, name_quiz in enumerate(quiz_options, start=1):
            print(f"{idx}.{name_quiz}")
        #prints an exit option for the user as well as the quiz options
        print(f"{len(quiz_names)+1}.Exit")

        quiz = int(input("Choose a quiz to play by typing it's number "))
        #Code that makes the selcted quiz run
        if 1 <= quiz <= len(quiz_names):
            selected_quiz = quiz_names[quiz - 1]
            run_quiz(selected_quiz)
        #prints if the user selects number 5 which is the exit option
        elif quiz == len(quiz_names) + 1:
            print("Thanks for playing the Cricket Rules Quiz! Goodbye")
            break
        #prints if the user didn't type the number for a quiz
        else:
            print("That's not a quiz number!")

#Chatgpt suggested this code when I asked it why the program was stopping at the name input
if __name__ == "__main__":
    main()