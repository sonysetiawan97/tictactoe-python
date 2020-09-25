from tkinter import *
import tkinter.messagebox

titleGame = "Tic Tac Toe"

tk = Tk()
tk.title(titleGame)

playerOne = StringVar()
playerTwo = StringVar()
buttons = StringVar()

# True = player one turn, False = player two turn
playerTurn = True
# turn for count every player turn and if no one winner, while turn=9 it will stop then game is tie
turn = 0

# input every player name
playerOneNameInput = Entry(tk, textvariable = playerOne, bd=3, width=40)
playerOneNameInput.grid(row=1, column=1, columnspan=2)
playerTwoNameInput = Entry(tk, textvariable = playerTwo, bd=3, width=40)
playerTwoNameInput.grid(row=2, column=1, columnspan=2)

# create title game for player name
labelPlayerX = Label( tk, text="Player X:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
labelPlayerX.grid(row=1, column=0)

labelplayerY = Label( tk, text="Player O:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
labelplayerY.grid(row=2, column=0)

labelTitleTurn = Label( tk, text="Turn:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
labelTitleTurn.grid(row=3, column=0)

labelTurn = Label( tk, text="X", font='Times 20 bold', bg='white', fg='black', height=1, width=16)
labelTurn.grid(row=3, column=1, columnspan=2)

# create column game
button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=4, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=4, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=4, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=5, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=5, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=5, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=6, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=6, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=6, column=2)

# disable if player win / tie
def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)

    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

    playerOneNameInput.configure(state=DISABLED)
    playerTwoNameInput.configure(state=DISABLED)

# enable for new game
def enableButton():
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)

    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)

# set button to normal
def recreatePanel():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "

    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "

    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    labelTurn["text"] = "X"

# restart game if choose yes on askquestion messagebox
def restartGame():
    global turn, playerTurn
    restartGameDialogBox = tkinter.messagebox.askquestion(titleGame, "restart Game?")
    if restartGameDialogBox == "yes":
        recreatePanel()
        turn = 0
        playerTurn = True
        enableButton()
    else :
        disableButton()

# function when button clicked
def btnClick(buttons):
    global playerOne, playerTwo, playerTurn, turn
    if buttons["text"] == " " and playerTurn == True:
        turn += 1
        buttons["text"] = "X"
        labelTurn["text"] = "O"
        playerTurn = False
        checkWinner()
    elif buttons["text"] == " " and playerTurn == False:
        turn += 1
        buttons["text"] = "O"
        labelTurn["text"] = "X"
        playerTurn = True
        checkWinner()
    else:
        tkinter.messagebox.showinfo(titleGame, "Button already clicked")

# check winner player if have 1 condition
def checkWinner():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo(titleGame, playerOne.get() + " Wins!")
        restartGame()
    elif turn == 9:
        tkinter.messagebox.showinfo(titleGame, "Game tie!")
        restartGame()
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
          tkinter.messagebox.showinfo(titleGame, playerTwo.get() + " Wins!")
          restartGame()

# start the tkinter
tk.mainloop()