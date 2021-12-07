from tkinter import *
import tkinter.font as font 
import random 

quotes = ["Today is a good day", "Take it easy", "Have fun"]
timer = 60
score = 0 
starting_word= ''

#function for start button

def startGame():
    global starting_word
    if(timer==60):
        startCountdown()
        starting_word = random.choice(quotes).lower()
        display_words.config(Text = random.choice(quotes), fg = starting_word)
        quote_entry.bind('<Return>', displayNextWord)

#function to reset the game

def resetGame():
    global timer, score, starting_word
    timer = 60
    score = 0 
    starting_word= ''
    game_score.config(text = "Your score: " + (str(score)))
    display_words.config(text = '')
    time_left.config(text = "Game ending in:  -")
    quote_entry.delete(0, END)

def startCountdown():
    global timer
    if (timer>=0):
        time_left.config(text = "Game ends in:" + str(timer) + "sec")
        timer -= 1
        time_left.after(1000, startCountdown)
        if (timer == -1):
            time_left.config(text = "Game over")

#function for displaying random words

def displayNextWord(Event):
    global starting_word, score
    if(timer > 0):
        if(starting_word == quote_entry.get()().lower()):
            score +=1
            game_score.config(Text = "Your score:" + str(score))
        quote_entry.delete(0, END)
        starting_word = random.choice(quotes).lower()
        display_words.config(text = random.choice(quotes),fg = starting_word)

#displaying window
my_window = Tk()
my_window.title("Quote Guessing Game")
my_window.geometry("600x200")
app_font = font.Font(family= "Helvetica", size = 16)
game_desc = "Guess the phrase"
game_description = Label(my_window, text= game_desc, font = app_font, fg = "grey")
game_description.pack()
game_Score = "Your Score is:" + str(score)
game_score = Label(my_window, text= game_Score, font = font.Font(size = 13), fg = "green")
game_score.pack()
display_words = Label(my_window, font = font.Font(size = 25), pady = 10)
display_words.pack()
quote_entry = Entry(my_window, width = 30)
quote_entry.pack(pady = 10)
time_lefttext = "Game ends in: " 
time_left = Label(my_window, text = time_lefttext, font = font.Font(size = 13), fg = "red")
time_left.pack()
btn_frame = Frame(my_window, width = 80, height = 40, bg = "red")
btn_frame.pack(side = BOTTOM)
start_button = Button(btn_frame, text = "Play", width = 20, fg = "black", bg = "brown", bd = 0, pady = 10, command= startGame)
start_button.grid(row = 0, column = 0)
reset_button = Button(btn_frame, text = "Restart", width = 20, fg = "black", bg = "light blue", padx = 20, pady = 10, command = resetGame)
reset_button.grid(row = 0, column = 1)
my_window.geometry("600x300")
my_window.mainloop()

