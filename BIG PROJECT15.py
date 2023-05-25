#import semua
import pickle
import tkinter.messagebox
from tkinter import *
from tkinter.font import Font

root = Tk() #buat main window
root.title("ATUR AJA") #bikin judul program #agar ukuran window tidak bisa diubah ubah
root.resizable(0,0)
root.geometry("530x550") #ukuran window (ukuran pixel)
root.config(bg="#fbd043") #warna background window jadi warna abu abu

icon = PhotoImage(file="icon1.png")
root.iconphoto(False, icon)

my_font = Font(family="Arial", size=14, weight="bold") #my_font sebagai Font dengan font arial ukuran 14 dan di bold
#labelImage
labelImage = PhotoImage(file="brownbar.png")
Label(root, image=labelImage, bg="#fbd043").pack()
#iconImage
iconImage = PhotoImage(file="icon2.png")
Label(root, image=iconImage, bg="#b84104").place(x=190, y=14)
#labelTitle
Label(root, text=" Atur Aja ", font=("Goudy Stout", 15), bg="#b84104", fg="#fbd043").place(x=230,y=20) #buat label judul nama program

#fungsi-fungsi
def addTask(): #buat fungsi tambah untuk text yang ingin dimasukin ke list
    list = entryTask.get() #
    if list != "": #
        listTask.insert(END, list) #
    else: #selain itu, maka
        tkinter.messagebox.showinfo(title="Info", message="Masukkan List Anda") #
    entryTask.delete(0, "end") #

def delTask(): #buat fungsi hapus untuk text yang dipilih di list
    try: #
        taskIndex = listTask.curselection()[0] #
        listTask.delete(taskIndex) #
    except: #
        tkinter.messagebox.showinfo(title="Warning", message="Pilih List Anda") #

def saveTask():
    allItem = []
    for i in range(0, listTask.size()):
        allItem.append(listTask.get(i))
    with open("ToDoList.pickle", "wb") as f:
        pickle.dump(allItem, f)
        tkinter.messagebox.showinfo(title="Info", message="Berhasil Disimpan")

def loadTask():
    with open("ToDoList.pickle", "rb") as f:
        ls = pickle.load(f)
    listTask.delete(0, END)
    for line in ls:
        listTask.insert(END, line)

def ClearTask():
    listTask.delete(0, END)

#make a frame
frameTask = Frame(root)
frameTask.pack(pady=5)

#create a GUI
listTask = Listbox(frameTask,
                   font=my_font,
                   width=40,
                   height=12,
                   bd=5,
                   bg="#b84104",
                   fg="#fbd043",
                   highlightthickness=0,
                   selectbackground="#a6a6a6",
                   activestyle="none")
listTask.pack(side=LEFT)

#Make a scrollbar
scrollbarTask = Scrollbar(frameTask, bg="#b84104")
scrollbarTask.pack(side=RIGHT, fill=Y)
#config frame
listTask.config(yscrollcommand=scrollbarTask.set)
scrollbarTask.config(command=listTask.yview)
#ADD TASK
entryTask = Entry(root, width=51, borderwidth=5, bg="#b84104", fg="#fbd043", font="Futura-Bold")
entryTask.place(x=30, y=380)
#BUTTON ADD
buttonAdd = Button(root, text="Insert task", width=20, borderwidth=3, bg="#b84104", fg="#fbd043", command=addTask)
buttonAdd.place(x=30, y=420)
#BUTTON DELETE
buttonDel = Button(root, text="Delete task", width=20, borderwidth=3,bg="#b84104", fg="#fbd043", command=delTask)
buttonDel.place(x=30, y=460)
#BUTTON SAVE
buttonSv = Button(root, text="Save", width=10, borderwidth=3, bg="#b84104", fg="#fbd043", command=saveTask)
buttonSv.place(x=330, y=500)
#BUTTON LOAD
buttonLo = Button(root, text="Load", width=10, borderwidth=3, bg="#b84104", fg="#fbd043", command=loadTask)
buttonLo.place(x=415, y=500)
#BUTTON CLEAR
buttonClr = Button(root, text="Clear all", width=20, borderwidth=3, bg="#b84104", fg="#fbd043", command=ClearTask)
buttonClr.place(x=30, y=500)

root.mainloop()