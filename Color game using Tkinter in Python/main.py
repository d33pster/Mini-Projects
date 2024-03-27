#!/usr/bin/env python3

# import the modules 

import random
import tkinter

# list of possibles colour.
colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score = 0

# the game time left, initially 30 seconds.
timeleft = 30

# function that will start the game
def startGame(event):
    if timeleft == 30:

        # start the countdown timer
        countdown()
    
    # run the function to choose the next colour
    nextColour()

# Function to choose and display the next colour
def nextColour():
    
    # use the globally declared 'score'
    # and 'play' variables above
    global score
    global timeleft

    # if a game is currently in play
    if timeleft > 0:

        # make the next entry in play
        e.focus_set()

        # if the colour typed is equal
        # to the colour of text
        if e.get().lower() == colours[1].lower():
            score += 1

        # clear the text entry box.
        e.delete(0, tkinter.END)

        random.shuffle(colours)

        # change the colour to type, by changing the
        # text and the colour to a random colour value
        label.config(fg = str(colours[1]), text = str(colours[0]))

        #updating the score
        scoreLabel.config(text = "Score: " + str(score))

# countdown timer function
def countdown():
    global timeleft

    # if a game is in play
    if timeleft > 0:

        # decerment the timer
        timeleft -= 1

        # update the time left label
        timeLabel.config(text = "Time Left: " + str(timeleft))

        # run the function again after 1 sec
        timeLabel.after(1000, countdown)

# Driver Code

# create a GUI window
root = tkinter.Tk()

# set the title
root.title("COLORGAME")

# set size 
root.geometry("375x200")

# add an instruction lable
instructions = tkinter.Label(root, text = "Type in the colour" 
                       "of the words, and not the words text!", 
                                    font = ('Helvetica', 12))
instructions.pack()

# add a score lable
scoreLabel = tkinter.Label(root, text="Press to start", font = ('Helvetica', 12))

scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font = ('Helvetica,12'))

timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()

# add a text entry box for typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()