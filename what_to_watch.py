from random import choice
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *

## database lists
movies = [
    ["Spirited Away","Animation"],
    ["The Boy and The Heron","Animation"],
    ["Slumdog Millionaire","Drama"],
    ["Minari","Drama"],
    ["Clueless","Rom-Com"],
    ["Notting Hill","Rom-Com"],
    ['La La Land','Romance'],
    ['Hum Tum','Romance'],
    ['Alita: Battle Angel','Action'],
    ['Baby Driver','Action'],
    ['Parasite','Thriller'],
    ['Qala','Thriller'],
    ['Oppenheimer','Historical'],
    ['Schindler\'s List','Historical'],
    ['Gravity','Sci-Fi'],
    ['Interstellar','Sci-Fi'],
    ['The Hunger Games','Dystopian'],
    ['Maze Runner','Dystopian'],
    ["Brave","Fantasy"],
    ["Ready Player One","Fantasy"]
]

shows = [
    ["My Demon","Rom-Com"],
    ["Welcome to Samdal-ri","Rom-Com"],
    ["Peaky Blinders","Drama"],
    ["Anne With an E","Drama"],
    ["Gyeongseong Creature","Thriller"],
    ['Strangers From Hell','Thriller'],
    ["Alice in Borderland","Thriller"],
    ["New Girl","Sit-Com"],
    ["The Office","Sit-Com"],
    ['SpyxFamily','Animation'],
    ['Yuri on Ice','Animation'],
    ['Demon Slayer','Animation'],
    ['The Witcher','Fantasy'],
    ['Moving','Fantasy'],
    ['The Crown','Historical'],
    ['Kingdom','Historical'],
    ['The Silent Sea','Sci-Fi'],
    ['Lost in Space','Sci-Fi']    
]




def find_movie():

    def find():
        global x,y
        x = gen_entry.get()
        y=[]
        for i in movies:
            if i[1]==x:
                y.append(i[0])
        x = choice(y)
        label2.config(text=x)

    global x,y
    movies_window = Toplevel(root)
    movies_window.geometry("400x400")
    movies_window.config(bg="#1c5c5e")
    movies_window.title("Generate Movie")
    
    label1 = tk.Label(movies_window, text="W A T C H :", font=("helvetica",24,"bold"), fg="#fff7cc", bg="#1c5c5e")
    label1.pack(pady=10,padx=10) 

    ## pick genre
    gen_label = tk.Label(movies_window, text="Pick Genre : ", font=("helvetica",18,"bold"),fg="#fff7cc", bg="#1c5c5e")
    gen_label.pack(pady=10)
    gen_entry = ttk.Combobox(movies_window, width=10)
    gen_entry.pack(pady=10)
    gen_entry['values']=['Drama','Thriller','Animation','Romance','Rom-Com','Action','Fantasy','Historical','Sci-Fi','Dystopian']

    frame3 = tk.Frame(movies_window, bg="#1c5c5e")
    frame3.pack()
    find_btn = tk.Button(frame3,text="Find", font=("helvetica",18,"bold"),fg="#1c5c5e", bg="#fff7cc", command=find)
    find_btn.pack(side="left",padx=10)
    quit_btn = tk.Button(frame3, text="Quit",font=("helvetica",18,"bold"),fg="#1c5c5e", bg="#fff7cc", command=exit)
    quit_btn.pack(side="left",padx=10)

    label2 = tk.Label(movies_window, text='',font=("helvetica",18,"bold"), fg="#fff7cc", bg="#1c5c5e" )
    label2.pack(pady=10,padx=10)


def find_show():

    def find():
        global x,y
        x = gen_entry.get()
        y=[]
        for i in shows:
            if i[1]==x:
                y.append(i[0])
        x = choice(y)
        label2.config(text=x)

    global x,y
    shows_window = Toplevel(root)
    shows_window.geometry("400x400")
    shows_window.config(bg="#1c5c5e")
    shows_window.title("Generate Show")
    
    label1 = tk.Label(shows_window, text="W A T C H :", font=("helvetica",24,"bold"), fg="#fff7cc", bg="#1c5c5e")
    label1.pack(pady=10,padx=10) 

    ## pick genre
    gen_label = tk.Label(shows_window, text="Pick Genre : ", font=("helvetica",18,"bold"),fg="#fff7cc", bg="#1c5c5e")
    gen_label.pack(pady=10)
    gen_entry = ttk.Combobox(shows_window, width=10)
    gen_entry.pack(pady=10)
    gen_entry['values']=['Drama','Thriller','Animation','Rom-Com','Fantasy','Historical','Sci-Fi','Sit-Com']

    frame4 = tk.Frame(shows_window, bg="#1c5c5e")
    frame4.pack()
    find_btn = tk.Button(frame4,text="Find", font=("helvetica",18,"bold"),fg="#1c5c5e", bg="#fff7cc", command=find)
    find_btn.pack(side="left",padx=10)
    quit_btn = tk.Button(frame4, text="Quit",font=("helvetica",18,"bold"),fg="#1c5c5e", bg="#fff7cc", command=exit)
    quit_btn.pack(side="left",padx=10)

    label2 = tk.Label(shows_window, text='',font=("helvetica",18,"bold"), fg="#fff7cc", bg="#1c5c5e" )
    label2.pack(pady=10,padx=10)

def add():

    def submit():
        name = name_entry.get()
        typemedia = type.get()
        genre = genre_entry.get()

        if not typemedia:
            messagebox.showerror("error", "Please enter type!")
        elif not name:
            messagebox.showerror("error","enter name")
        elif not genre:
            messagebox.showerror("error","please enter genre!")
        else:
            entry = [name,genre]
            if entry[0]=="Movie":
                movies.append(entry)
                print(movies)
            else:
                shows.append(entry)
                print(shows)

    add_window = Toplevel(root)
    add_window.geometry("400x400")
    add_window.config(bg="#1c5c5e")
    add_window.title("Add New")

    label_add = tk.Label(add_window, text="A D D  N E W ",font=("helvetica",24,"bold"), fg="#fff7cc", bg="#1c5c5e")
    label_add.pack(pady=10)

    frame = tk.Frame(add_window, bg="#1c5c5e")
    frame.pack()

   

    type_label = tk.Label(frame, text="Type :",font=("helvetica",16,"bold"), fg="#fff7cc", bg="#1c5c5e")
    type_label.pack(side="left")
    type = ttk.Combobox(frame,width=10)
    type.pack(side="left",pady=10,padx=10)
    type['values'] = ["Movie", "Show"]

    frame2 = tk.Frame(add_window, bg="#1c5c5e")
    frame2.pack()

    
    name_label = tk.Label(frame2, text="Name : ",font=("helvetica",16,"bold"), fg="#fff7cc", bg="#1c5c5e")
    name_label.pack(side="left",pady=10)
    name_entry = tk.Entry(frame2)
    name_entry.pack(side="left")

    

    frame3 = tk.Frame(add_window, bg="#1c5c5e")
    frame3.pack()

    
    genre_label = tk.Label(frame3, text="Genre : ", font=("helvetica",16,"bold"), fg="#fff7cc", bg="#1c5c5e")
    genre_label.pack(side="left", pady=10)
    genre_entry = ttk.Combobox(frame3, width=10)
    genre_entry.pack(side="left", pady=10,padx=10)
    genre_entry['values']=['Drama','Thriller','Animation','Romance','Rom-Com','Action','Fantasy','Historical','Sci-Fi','Dystopian']

    frame5 = tk.Frame(add_window, bg="#1c5c5e")
    frame5.pack()

    submit_btn = tk.Button(frame5, text="Save",font=("helvetica",18,"bold"),fg="#1c5c5e", bg="#fff7cc", command =submit)
    submit_btn.pack(side="left",pady=10,padx=10)

    quit_btn = tk.Button(frame5, text="Quit",font=("helvetica",18,"bold"),fg="#1c5c5e", bg="#fff7cc", command=exit)
    quit_btn.pack(side="left",pady=10,padx=10)

## window
root = tk.Tk()
root.geometry=("400x400")
root.config(bg ="#1c5c5e")

## title 
title_label = tk.Label(root, text="~ W H A T  2  W A T C H ~",font=("helvetica",24,"bold"), fg="#fff7cc", bg="#1c5c5e")
title_label.pack(pady=20,padx=20)

frame = tk.Frame(root)
frame.pack(pady=10,padx=10)
frame.config(bg="#1c5c5e")

## btn for movies / shows
mov_btn = tk.Button(frame, text="Movies", font=("helvetica",18,"bold"),fg="#1c5c5e", bg="#fff7cc", command=find_movie)
mov_btn.pack(side="left", padx=10)

show_btn = tk.Button(frame, text="Shows",font=("helvetica",18,"bold"),fg="#1c5c5e", bg="#fff7cc", command = find_show)
show_btn.pack(side="left", padx=10)

add_btn = tk.Button(frame, text="Add To Watch",font=("helvetica",18,"bold"),fg="#1c5c5e", bg="#fff7cc", command = add )
add_btn.pack(side="left",padx=10)


root.mainloop()
