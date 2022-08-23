
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from random import randint


# main window
root = tkinter.Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

# picture
rock_img = ImageTk.PhotoImage(Image.open("humRock.png"))
paper_img = ImageTk.PhotoImage(Image.open("humPaper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("humanSci.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("compRock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("CompPaper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("compSci.png"))
youWin_img_comp = ImageTk.PhotoImage(Image.open("youwin.png"))
youLose_img_comp = ImageTk.PhotoImage(Image.open("youlose.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="#9b59b6")
user_label.grid(row=1, column=4)
comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)


# scores
playerScore = Label(root, font=50, text=0, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicators
user_indicator =  Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font = 50, text="COMPUTER",  bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

# update message
def updateMessage(x):
    msg ['text'] = x

#final result

def finalResult(winner):
    if winner == "human":
        destroyLabels()
        user_label = Label(root, image=youWin_img_comp, bg="#9b59b6")
        user_label.grid(row=0, column=0)

    elif winner == "computer":
        destroyLabels()
        user_label = Label(root, image=youLose_img_comp, bg="#9b59b6")
        user_label.grid(row=0, column=0)

# destroy labels

def destroyLabels():
    user_label.destroy() 
    comp_label.destroy() 
    computerScore.destroy()
    playerScore.destroy()
    user_indicator.destroy()
    comp_indicator.destroy()
    msg.destroy()
    rock.grid_forget()
    paper.grid_forget()
    scissor.grid_forget()




# update human score
def UpdateHumanScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
    if score == 5:
        finalResult("human")

# update computer score
def UpdateComputerScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)
    if score == 5:
        finalResult("computer")

#winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("it is a tie")
        pass
    elif player == "rock":
        if computer == "paper":
         updateMessage ("You have lost")
         UpdateComputerScore()
         pass
        else:
           updateMessage ("You have won")
           UpdateHumanScore()
           pass
    elif player == "paper":
        if computer == "scissor":
         updateMessage ("You have lost")
         UpdateComputerScore()
         pass
        else:
           updateMessage ("You have won")
           UpdateHumanScore()
           pass
    elif player == "scissor":
        if computer == "rock":
         updateMessage ("You have lost")
         UpdateComputerScore()
         pass
        else:
           updateMessage ("You have won")
           UpdateHumanScore()
           pass

choices = ["rock", "paper", "scissor"]

def updateChoice(X):
     # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    if X == rock:
           user_label.configure(image=rock_img)
    elif X == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkWin(X, compChoice)
    


#buttons
#lamda is an anonymous function that allows you to add another fucntion
rock = tkinter.Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock"))
rock.grid(row=2, column=1)
paper = tkinter.Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white", command=lambda: updateChoice("paper"))
paper.grid(row=2, column=2)
scissor = tkinter.Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor"))
scissor.grid(row=2, column=3)

root.mainloop()