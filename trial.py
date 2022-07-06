from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.simpledialog import askstring
import random as r

def reset():

    global p1_choice,p2_choice
    b1['text'] = 'Player 1 Roll'
    b1['state'] = NORMAL
    p1.configure(image=f_player1)
    p1_choice = None
    b2['text'] = 'Player 2 Roll'
    b2['state'] = NORMAL
    p2.configure(image=f_player2)
    p2_choice=None

def compare():

    if((b1['text'][0]=='r' and b2['text'][0]=='s') or (b1['text'][0]=='s' and b2['text'][0]=='p') or (b1['text'][0]=='p' and b2['text'][0]=='r')):
        messagebox.showinfo('You won!')

    elif(b1['text']==b2['text']):
        messagebox.showinfo('Its a tie')
        
    else:
        messagebox.showinfo('You Lost!!!')
    
    reset()

def check():

    if(b1['state']==b2['state']==DISABLED):
        compare()

def p1_roll():

    global p1_choice
    choice = tempchoice()
    if(choice == 'rock'):
        p1_choice = 'rock'
    elif(choice == 'scissors'):
        p1_choice = 'scissors'
    elif(choice == 'paper'):
        p1_choice = 'paper'
    else:
        wrongch()
        quit()
    p1.configure(image=moves[p1_choice])
    b1['text'] = p1_choice
    b1['state'] = DISABLED
    check()

def p2_roll():

    global p2_choice
    p2_choice=r.choice(['rock','scissors','paper'])
    p2.configure(image=moves[p2_choice])
    b2['text'] = p2_choice
    b2['state'] = DISABLED
    check()

def tempchoice():
    temp = Tk()
    temp.geometry("1500x250")
    choice = askstring("Choice","What is your choice? rock/paper/scissors? (Use lowercase letter only) Click on player 2 to continue....")
    return choice

def wrongch():
    wrong = Tk()
    wrong.geometry('1000x250')
    messagebox.showinfo("Wrong choice","You have entered a wrong choice or no choice the program wil quit now thank you... restart to continue")


################### Main #######################

root=Tk()
root.geometry("1000x500")
root.title("Rock/Paper/Scissors")
font=(('Times New Roman','bold'),'20')

img_player1 = Image.open("Assets/player1.png")
reimg_player1 = img_player1.resize((300,400))
f_player1 = ImageTk.PhotoImage(reimg_player1)

img_player2 = Image.open("Assets/player2.png")
reimg_player2 = img_player2.resize((300,400))
f_player2 = ImageTk.PhotoImage(reimg_player2)

img_vs = Image.open("Assets/vs.png")
reimg_vs = img_vs.resize((300,400))
f_vs = ImageTk.PhotoImage(reimg_vs)


moves={'rock':PhotoImage(file='Assets/rock.png'),'paper':PhotoImage(file='Assets/paper.png'),'scissors':PhotoImage(file='Assets/scissors.png')}

f1=Frame(root)

p1=Label(f1,image=f_player1)
p1.image = f_player1
p1.pack(side='left')

vs=Label(f1,image=f_vs)
vs.image = f_vs
vs.pack(side='left')

p2=Label(f1,image=f_player2)
p2.image = f_player2
p2.pack(side='left')

f1.pack()

f2=Frame(root)

b1=Button(f2,text='Player 1 Roll',width=20,font=font,command=p1_roll)
b1.pack(side='left')
f_space=Frame(f2,width=150)
f_space.pack(side='left')

b2=Button(f2,text='Player 2 Roll',width=20,font=font,command=p2_roll)
b2.pack(side='left')

f2.pack(pady=10)

p1_choice=None
p2_choice=None

root.mainloop()