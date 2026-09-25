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

#Questions
#This will appear on the left side of the window
question_label = ttk.Label(main, text="", wraplength=480, justify="left", font=("Segoe UI", 12, "bold"))
question_label.pack(anchor="w", pady=(8, 6))

#Options to the questions
options_frame = ttk.Frame(main)
options_frame.pack(fill="x", pady=(0, 8))
option_buttons = []

#This stores the chosen option
selected_answer = tk.StringVar(value="")

#This code gives the user feedback about their answer given to the previous question
feedback_label = ttk.Label(main, text="", foreground="#333")
feedback_label.pack(anchor="w", pady=(4, 8))

#Buttons for the user to interact /Submit answer/Next question/Quit quiz/
buttons = ttk.Frame(main)
buttons.pack(fill="x", pady=(8,0))
#Submit Button
submit_btn = ttk.Button(buttons, text="Submit Answer")
submit_btn.pack(side="left")
#Next Question Button
#State is set to 'disabled' because the next button can't be pushed before the question is answered
next_btn = ttk.Button(buttons, text="Next Question", state="disabled")
next_btn.pack(side="left", padx=(8,0))
#Quit Button
quit_btn = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_btn.pack(side="right")

#This code tells the user what question they are up to and out of how many questions
#'question_number' calls back to the code under the 'variable' label above and prints the question number that is one value above what was previously stored
#'quizquestions' calls back to the dictionaries containing the questions. They are counted and printed as a number using the 'len' code
def progress_update():
    progress_label.config(text=f"Question{question_number + 1} of {len(quizquestions)} Score: {score}")

#This code resets the option buttons to the options for the question the user is up to
def clear_options():
    for rb in option_buttons:
        rb.destroy()
    option_buttons.clear()

#This code resets the buttons to the correct state after each question so that the user can submit their answer again and can't go to the next question without answering
def load_question():
    progress_update()
    feedback_label.config(text="")
    submit_btn.config(state="normal")
    next_btn.config(state="disabled")
    selected_answer.set("")

    #This code gets the current question number
    q = quizquestions[question_number]
    question_label.config(text=f"Question{question_number + 1}: {q['text']}")

    clear_options()
    for option_text in q["options"]:
        rb = ttk.Radiobutton(
            options_frame,
            text=option_text,
            value=option_text,
            variable=selected_answer,
        )
        rb.pack(anchor="w", pady=2)
        option_buttons.append(rb)

#Code for the user to be able to submit an answer and receive feedback from their chosen answer
def submit_answer():
    global score
    choice = selected_answer.get()

#If the user tries to not select any answer to a question this code will be used
    if choice == "":
        messagebox.showinfo("Please select an answer")
        return

    correct = quizquestions[question_number]["answer"]

#This code runs when the user submits a valid answer. The 'if' is for the correct answer and the 'else' is for the incorrect answers
    if choice == correct:
        score += 1
        feedback_label.config(text="Correct!")
    else:
        feedback_label.config(text=f"Incorrect. Answer was, {correct}")

#Prevents multiple submissions
    submit_btn.config(state="disabled")
    next_btn.config(state="normal")

#This code takes the user to the next question and checks if there is another question. The 'if' statement takes the user to the next question, the 'else' statement finishes the quiz if all questions are done
def next_question():
    global question_number
    question_number += 1

    if question_number < len(quizquestions):
        load_question()
    else:
        finish_quiz()

def finish_quiz():
    percent = int((score / len(quizquestions)) * 100)
    again = messagebox.askyesno("Quiz is complete", f"You scored {score} out of {len(quizquestions)}. \n\nPlay again?")
    if again:
        restart_quiz()
    else:
        root.destroy()

#Code to restart the quiz after the user has played it
def restart_quiz():
    global question_number, score
    question_number = 0
    score = 0
    load_question()

#Links the buttons to their purpose
submit_btn.config(command=submit_answer)
next_btn.config(command=next_question)

#Required at the end of the python program for it to work
root.mainloop()