from tkinter import *
from jeopardy import *
from similar_text import similar_text

gPlayer = Player('default')  # global variable
pName = StringVar()

# intialize main window
root = Tk()

root.configure(bg='blue')
root.title('Jeopardy')


def buttonClick():
    current = nameEntry.get()
    print(current)
    pName.set(gPlayer.name)


def disableButton(button, entry):
    button.config(state='disabled')  # disable the button
    entry.config(state='disabled')
    print(nameEntry.get())
    gPlayer.name = nameEntry.get()
    buttonClick()


def newWindow(question, cat, answer, button):
    def close_window():
        newWindow.destroy()

    def checkAnswer():
        if answer[0:3] == '<i>':
            ans = answer[3:-4]

        # if answer[0:3] == '<i>': # edge case, sometimes answer contains <i> </i>
        #   ans = answer[3:-4]

        if e.get() == answer:
            print('correct!')
            gPlayer.score += 1

        else:
            print(text)
            print('incorrect!')
            gPlayer.score -= 1

        close_window()

    button.config(state='disabled')  # disable the button

    newWindow = Toplevel(root)
    newWindow.title(cat)
    Label(newWindow,
          text=question, padx=50, pady=10, bg='blue', fg='#ebd534').grid(column=0, row=0)
    # Developer cheat##################
    # Developer cheat##################
    Label(newWindow,
          text=answer, padx=50, pady=10, bg='blue', fg='#ebd534').grid(column=0, row=3)
    ###########
    text = str()
    e = Entry(newWindow, textvariable=text)
    e.grid(column=0, row=1)
    button = Button(newWindow, text='Submit', padx=50, pady=10, bg='blue', fg='black', border=5, command=checkAnswer)
    button.grid(row=2, column=0)


def newWindowEndGame():  # Ends the game
    alt = Tk()
    newWindowEnd = Toplevel(alt)
    Label(newWindowEnd, text='Game Over!', padx=50, pady=50).pack()
    Label(newWindowEnd, text=gPlayer.score).pack()
    root.destroy()


# Name question label
nameEntry = Entry(root)
nameEntry.grid(column=1, row=10, sticky="nsew")
label_name = Label(root, text='Welcome what is your name?!', bg='blue', fg='#ebd534')

# Name Entry Button
button_submit = Button(root, text='submit', padx=50, pady=10,
                       border=5, highlightbackground='red', command=lambda: disableButton(button_submit, nameEntry))
button_submit.grid(column=2, row=10, sticky="nsew")

# Name Label
label_score0 = Label(root, textvariable=pName)
label_score0.grid(column=0, row=11, sticky="nsew")

# Score Label
label_score = Label(root, text=gPlayer.score)
label_score.grid(column=1, row=11, sticky="nsew")

# End game button
button_end = Button(root, text="End Game", command=lambda: newWindowEndGame())
button_end.grid(column=1, row=11)

# category labels
label_1 = Label(root, text=cat1.name, padx=10, pady=10, bg='blue', fg='#ebd534')
label_2 = Label(root, text=cat2.name, padx=10, pady=10, bg='blue', fg='#ebd534')
label_3 = Label(root, text=cat3.name, padx=10, pady=10, bg='blue', fg='#ebd534')
label_4 = Label(root, text=cat4.name, padx=10, pady=10, bg='blue', fg='#ebd534')
label_5 = Label(root, text=cat5.name, padx=10, pady=10, bg='blue', fg='#ebd534')

label_1.grid(row=0, column=0, sticky="nsew")
label_2.grid(row=0, column=1, sticky="nsew")
label_3.grid(row=0, column=2, sticky="nsew")
label_4.grid(row=0, column=3, sticky="nsew")
label_5.grid(row=0, column=4, sticky="nsew")
label_name.grid(row=10, column=0, sticky="nsew")

# initializing question buttons
# NOTE: bug on mac that does not allow bg to work on buttons with fg
button_1 = Button(root, text='100', padx=50, pady=10, bg='blue', fg='black',
                  border=5, highlightbackground='blue',
                  command=lambda: newWindow(cat1.questions[0], cat1.name, cat1.answers[0], button_1))
button_2 = Button(root, text='200', padx=50, pady=10, bg='blue', fg='black',
                  border=5, highlightbackground='blue',
                  command=lambda: newWindow(cat1.questions[1], cat1.name, cat1.answers[1], button_2))
button_3 = Button(root, text='400', padx=50, pady=10, bg='blue', fg='black',
                  border=5, highlightbackground='blue',
                  command=lambda: newWindow(cat1.questions[2], cat1.name, cat1.answers[2], button_3))
button_4 = Button(root, text='600', padx=50, pady=10, bg='blue', fg='black',
                  border=5, highlightbackground='blue',
                  command=lambda: newWindow(cat1.questions[3], cat1.name, cat1.answers[3], button_4))
button_5 = Button(root, text='800', padx=50, pady=10, bg='blue', fg='black',
                  border=5, highlightbackground='blue',
                  command=lambda: newWindow(cat1.questions[4], cat1.name, cat1.answers[4], button_5))
button_1a = Button(root, text='100', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat2.questions[0], cat2.name, cat2.answers[0], button_1a))
button_2a = Button(root, text='200', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat2.questions[1], cat2.name, cat2.answers[1], button_2a))
button_3a = Button(root, text='400', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat2.questions[2], cat2.name, cat2.answers[2], button_3a))
button_4a = Button(root, text='600', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat2.questions[3], cat2.name, cat2.answers[3], button_4a))
button_5a = Button(root, text='800', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat2.questions[4], cat2.name, cat2.answers[4], button_5a))
button_1b = Button(root, text='100', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat3.questions[0], cat3.name, cat3.answers[0], button_1b))
button_2b = Button(root, text='200', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat3.questions[1], cat3.name, cat3.answers[1], button_2b))
button_3b = Button(root, text='400', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat3.questions[2], cat3.name, cat3.answers[2], button_3b))
button_4b = Button(root, text='600', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat3.questions[3], cat3.name, cat3.answers[3], button_4b))
button_5b = Button(root, text='800', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat3.questions[4], cat3.name, cat3.answers[4], button_5b))
button_1c = Button(root, text='100', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat4.questions[0], cat4.name, cat4.answers[0], button_1c))
button_2c = Button(root, text='200', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat4.questions[1], cat4.name, cat4.answers[1], button_2c))
button_3c = Button(root, text='400', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat4.questions[2], cat4.name, cat4.answers[2], button_3c))
button_4c = Button(root, text='600', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat4.questions[3], cat4.name, cat4.answers[3], button_4c))
button_5c = Button(root, text='800', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat4.questions[4], cat4.name, cat4.answers[4], button_5c))
button_1d = Button(root, text='100', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat5.questions[0], cat5.name, cat5.answers[0], button_1d))
button_2d = Button(root, text='200', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat5.questions[1], cat5.name, cat5.answers[1], button_2d))
button_3d = Button(root, text='400', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat5.questions[2], cat5.name, cat5.answers[2], button_3d))
button_4d = Button(root, text='600', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat5.questions[3], cat5.name, cat5.answers[3], button_4d))
button_5d = Button(root, text='800', padx=50, pady=10, bg='blue', fg='black',
                   border=5, highlightbackground='blue',
                   command=lambda: newWindow(cat5.questions[4], cat5.name, cat5.answers[4], button_5d))
### end initialization of buttons

## positioning of buttons
button_1.grid(row=1, column=0, sticky="nsew")
button_2.grid(row=2, column=0, sticky="nsew")
button_3.grid(row=3, column=0, sticky="nsew")
button_4.grid(row=4, column=0, sticky="nsew")
button_5.grid(row=5, column=0, sticky="nsew")

button_1a.grid(row=1, column=1, sticky="nsew")
button_2a.grid(row=2, column=1, sticky="nsew")
button_3a.grid(row=3, column=1, sticky="nsew")
button_4a.grid(row=4, column=1, sticky="nsew")
button_5a.grid(row=5, column=1, sticky="nsew")

button_1b.grid(row=1, column=2, sticky="nsew")
button_2b.grid(row=2, column=2, sticky="nsew")
button_3b.grid(row=3, column=2, sticky="nsew")
button_4b.grid(row=4, column=2, sticky="nsew")
button_5b.grid(row=5, column=2, sticky="nsew")

button_1c.grid(row=1, column=3, sticky="nsew")
button_2c.grid(row=2, column=3, sticky="nsew")
button_3c.grid(row=3, column=3, sticky="nsew")
button_4c.grid(row=4, column=3, sticky="nsew")
button_5c.grid(row=5, column=3, sticky="nsew")

button_1d.grid(row=1, column=4, sticky="nsew")
button_2d.grid(row=2, column=4, sticky="nsew")
button_3d.grid(row=3, column=4, sticky="nsew")
button_4d.grid(row=4, column=4, sticky="nsew")
button_5d.grid(row=5, column=4, sticky="nsew")

##### end positioning

root.mainloop()
