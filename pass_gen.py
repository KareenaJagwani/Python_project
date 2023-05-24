from tkinter import*
import string
import random

root = Tk()
root.geometry("480x350")
root.title("Password Generator")

def gen():
    num = int(e1.get())
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    password = s[0:num]

    L4 = Label(root,text="Password: ",font= "time 15 bold")
    L4.place(x = 30, y = 250 )

    L5 = Label(root,text=password,font= "time 15 bold",width=24 , bg="white" )
    L5.place(x = 150, y = 250 )

    

L1 = Label(root,text="Password Generator",font= "time 15 bold")
L1.place(x = 30, y = 30 )

L2 = Label(root,text="Enter Password Length :",font= "time 15 bold")
L2.place(x = 30, y = 90)

e1 = Entry(root, width= 46, bd=2 ,font="time 13 bold")
e1.place(x = 30,y=133)

button = Button(root,text= "Generate Password",fg ="black", bg= "gold",font="time 15 bold",width= 34,command= gen)

button.place(x = 30, y=180)



root.mainloop()