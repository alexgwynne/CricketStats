#Cricket Rules Quiz with graphical interface
#By Alex Gwynne
#Comments are above what they comment on

#This 'tkinter' code is what allows the python program to appear in a graphical interface rather than the terminal
import tkinter as tk
from tkinter import ttk, messagebox

#Questions are stored within dictionaries *curly brackets* to be called upon during the quiz
quizquestions = [
    {"question": "Which of the following situations constitutes a ‘wide ball’ signal from the umpire?", "options": ["The ball passes the batter too wide to hit with a normal cricket shot", "The bowler delivers a full toss above waist height", "The bowler oversteps the front crease during delivery"], "answer": "The ball passes the batter too wide to hit with a normal cricket shot"},
    {"question": "Which of the following situations constitutes a ‘no ball’ signal from the umpire?", "options": ["The bowler runs in to deliver the ball but pulls out", "The bowler delivers a full toss above waist height", "The batter hits his own stumps"], "answer": "The bowler delivers a full toss above waist height"},
    {"question": "If the batsman hits the ball over the boundary on the full, how many runs are awarded?", "options": ["4", "6", "7"], "answer": "6"},
    {"question": "If the batsman hits the ball to the boundary along the ground, how many runs are awarded?", "options": ["3", "6", "4"], "answer": "4"},
    {"question": "What does LBW stand for?", "options": ["Leg Before Wicket", "Lunch Before Wides", "Leg Behind Waist"], "answer": "Leg Before Wicket"},
    {"question": "How many players from the fielding team can be on the field at once?", "options": ["11", "10", "9"], "answer": "11"},
    {"question": "Apart from boundaries, how else can the batsman score runs?", "options": ["Hitting the ball to certain zones", "Running between the wickets", "Dodging the fielders that are throwing the ball at them"], "answer": "Running between the wickets"},
    {"question": "How many deliveries are in an over?", "options": ["4", "8", "6"], "answer": "6"},
    {"question": "What is the maximum number of fielders the fielding team can have behind the 90-degree angle on the leg side of the pitch?", "options": ["1", "2", "As many as they like"], "answer": "2"},
]

#Variables
#The question number that the user is up to
question_number = 0
#The score that the user is on
score = 0
#The answer the user has selected
selected_answer = None

#'root' code is for the main window that the graphical interface appears in
root = tk.Tk()
root.title("Cricket Rules Quiz")
root.geometry("500x400")

#mainframe
main = ttk.Frame(root, padding=16)
main.pack(fill="both", expand=True)

#Progress Bar
#This will appear on the right of the window
progress_label = ttk.Label(main, text="")
progress_label.pack(anchor="e")

#Required at the end of the python program for it to work
root.mainloop()