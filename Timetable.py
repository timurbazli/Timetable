from tkinter import *
aken=Tk()
aken.geometry("300x500")
aken.configure(bg="#141414")
aken.title("LOGITpv21")
def anim(x,y,text,bcolor,fcolor,cmd):
    def on_enter(e):
        mybutton["background"]=bcolor
        mybutton["foreground"]=fcolor
    def on_leave(e):
        mybutton["background"]=fcolor
        mybutton["foreground"]=bcolor
    mybutton=Button(aken,width=42, height=2,text=text,
                    fg=bcolor,
                    bg=fcolor,
                    border=0,
                    activeforeground=fcolor,
                    activebackground=bcolor,
                    command=cmd,)
    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)

    mybutton.place(x=x,y=y)

def open_win2():
    win2=Toplevel()#создаём второе(дочернее) окно
    win2.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    win2.configure(bg="#141414")
    win2.geometry("955x710")
    def com1():
        pass

    Label(win2, borderwidth=1, relief="solid",text=" ", width=20,height=5).grid(row=0, column=0)
    Label(win2, borderwidth=1, relief="solid",text=" 0 ", width=10,height=5).grid(row=0, column=1)
    Label(win2, borderwidth=1, relief="solid",text=" 1 ", width=10,height=5).grid(row=0, column=2)
    Label(win2, borderwidth=1, relief="solid",text=" 2 ", width=10,height=5).grid(row=0, column=3)
    Label(win2, borderwidth=1, relief="solid",text=" 3 ", width=10,height=5).grid(row=0, column=4)
    Label(win2, borderwidth=1, relief="solid",text=" 4 ", width=10,height=5).grid(row=0, column=5)
    Label(win2, borderwidth=1, relief="solid",text=" 5 ", width=10,height=5).grid(row=0, column=6)
    Label(win2, borderwidth=1, relief="solid",text=" 6 ", width=10,height=5).grid(row=0, column=7)
    Label(win2, borderwidth=1, relief="solid",text=" 7 ", width=10,height=5).grid(row=0, column=8)
    Label(win2, borderwidth=1, relief="solid",text=" 8 ", width=10,height=5).grid(row=0, column=9)
    Label(win2, borderwidth=1, relief="solid",text=" 9 ", width=10,height=5).grid(row=0, column=10)
    Label(win2, borderwidth=1, relief="solid",text=" 10 ", width=10,height=5).grid(row=0, column=11)

    Label(win2, borderwidth=0, relief="solid", text="7.40-8.25", width=10,height=2).grid(row=0, column=1,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="8.30-9.15", width=10,height=2).grid(row=0, column=2,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="9.20-10.05", width=10,height=2).grid(row=0, column=3,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="10.10-10.55", width=10,height=2).grid(row=0, column=4,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="11.00-11.45", width=10,height=2).grid(row=0, column=5,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="11.50-12.35", width=10,height=2).grid(row=0, column=6,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="12.40-13.25", width=10,height=2).grid(row=0, column=7,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="13.30-14.15", width=10,height=2).grid(row=0, column=8,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="14.20-15.05", width=10,height=2).grid(row=0, column=9,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="15.10-15.55", width=10,height=2).grid(row=0, column=10,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="16.00-16.45", width=10,height=2).grid(row=0, column=11,sticky=S)


    Label(win2, borderwidth=1, relief="solid",text="Esmaspäev", width=20,height=8).grid(row=1, column=0)
    Label(win2, borderwidth=1, relief="solid",text="Teisipäev", width=20,height=8).grid(row=2, column=0)
    Label(win2, borderwidth=1, relief="solid",text="Kolmapäev", width=20,height=8).grid(row=3, column=0)
    Label(win2, borderwidth=1, relief="solid",text="Neljapäev", width=20,height=8).grid(row=4, column=0)
    Label(win2, borderwidth=1, relief="solid",text="Reede", width=20,height=8).grid(row=5, column=0)

    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=1)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=1)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=1)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=1)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=1)


        #1
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=2)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=3)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=4)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=5)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=6)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=7)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=8)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=9)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=10)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=11)

    est1=Label(win2, borderwidth=1, bg="#cab4c7", relief="solid",text="Eesti keel", width=10,height=4).grid(row=1, column=2,sticky=S)
    #Label(win2, relief="solid",borderwidth=0, bg="#cab4c7" ,text="B234", width=5,height=1).grid(row=1, column=2,sticky=SW)
    log1=Label(win2, borderwidth=1, bg="#80e092", relief="solid",text="Logistikateenused\nja varude juhtimine", width=10,height=8).grid(row=1, column=3, sticky=N+S+W+E, columnspan=2)
    mat1=Label(win2, borderwidth=1, bg="#fcb9d0", relief="solid",text="Matemaatika", width=10,height=8).grid(row=1, column=5, sticky=N+S+W+E, columnspan=2)
    rus1=Label(win2, borderwidth=1, bg="#94ed80", relief="solid",text="Keel ja kirjandus", width=10,height=8).grid(row=1, column=8, sticky=N+S+W+E, columnspan=2)
    tmat1=Label(win2, borderwidth=1, bg="#fcb9d0", relief="solid",text="Tugiõpe\n(matema\natika)", width=10,height=8).grid(row=1, column=10, sticky=N+S+W+E)

        #2
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=2)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=3)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=4)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=5)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=6)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=7)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=8)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=9)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=10)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=11)

    kem1=Label(win2, borderwidth=1, bg="#e080e0", relief="solid",text="Tugiõpe\n(keemia)", width=10,height=4).grid(row=2, column=2,sticky=N+S+W+E)
    pr1=Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=2, column=3, sticky=N+S+W+E, columnspan=3)
    fus1=Label(win2, borderwidth=1, bg="#fcb9d0", relief="solid",text="Füüsika", width=10,height=8).grid(row=2, column=7, sticky=N+S+W+E, columnspan=2)

        #3
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=2)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=3)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=4)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=5)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=6)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=7)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=8)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=9)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=10)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=11)

    test1=Label(win2, borderwidth=1, bg="#ff80ff", relief="solid",text="Tugiõpe\n(eesti keel)", width=10,height=4).grid(row=3, column=2,sticky=N)
    kun1=Label(win2, borderwidth=1, bg="#e080ce", relief="solid",text="Kuntsiained\n(eesti keeles)", width=10,height=8).grid(row=3, column=3, sticky=N+S+W+E, columnspan=2)
    keh1=Label(win2, borderwidth=1, bg="#e080c0", relief="solid",text="Kehaline kasvatus", width=10,height=8).grid(row=3, column=6, sticky=N+S+W+E, columnspan=2)

        #4
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=2)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=3)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=4)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=5)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=6)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=7)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=8)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=9)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=10)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=11)

    log2=Label(win2, borderwidth=1, bg="#80e092", relief="solid",text="Logistikateenused\nja varude juhtimine", width=10,height=8).grid(row=4, column=2, sticky=N+S+W+E, columnspan=2)
    pr2=Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=4, column=5, sticky=N+S+W+E, columnspan=2)
    ing1=Label(win2, bg="#fffff0",text="Inglise keel", width=20,height=4).grid(row=4, column=7, sticky=N, columnspan=2)
    rah1=Label(win2, bg="#ff80a2",text="Rahendustrakvara", width=20,height=4).grid(row=4, column=7, sticky=S, columnspan=2)

    rah2=Label(win2, bg="#ff80a2",text="Rahendustrakvara", width=20,height=4).grid(row=4, column=9, sticky=N, columnspan=2)
    est2=Label(win2, bg="#cab4c7",text="Eesti keel", width=20,height=4).grid(row=4, column=9,sticky=S, columnspan=2)
    ruhm1=Label(win2, borderwidth=1, bg="#ff80ff", relief="solid",text="Rühmaju\nhataja\ntund", width=10,height=4).grid(row=4, column=11,sticky=N+S+W+E)

        #5
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=2)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=3)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=4)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=5)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=6)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=7)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=8)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=9)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=10)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=11)

    
    est3=Label(win2, bg="#ff80ff",text="Eesti keel", width=20,height=4).grid(row=5, column=2, sticky=N, columnspan=2)
    rah3=Label(win2, bg="#ff80a2",text="Rahendustrakvara", width=20,height=4).grid(row=5, column=2, sticky=S, columnspan=2)
    pr3=Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=5, column=4, sticky=N+S+W+E, columnspan=5)
    rah4=Label(win2, bg="#ff80a2",text="Rahendustrakvara", width=20,height=4).grid(row=5, column=9, sticky=N, columnspan=2)
    ing2=Label(win2, bg="#80ff80",text="Inglise keel", width=20,height=4).grid(row=5, column=9,sticky=S, columnspan=2)

    #Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=1, column=1, sticky=N+S+W+E, columnspan=11)
    #Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=2, column=1, sticky=N+S+W+E, columnspan=11)
    #Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=3, column=1, sticky=N+S+W+E, columnspan=11)
    #Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=4, column=1, sticky=N+S+W+E, columnspan=11) 
    #Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=5, column=1, sticky=N+S+W+E, columnspan=11)

    est1.bind("<Button-1>", com1)
    est2.bind("<Button-1>", com1)
    est3.bind("<Button-1>", com1)
    log1.bind("<Button-1>", com1)
    log2.bind("<Button-1>", com1)
    mat1.bind("<Button-1>", com1)
    rus1.bind("<Button-1>", com1)
    tmat1.bind("<Button-1>", com1)
    kem1.bind("<Button-1>", com1)
    pr1.bind("<Button-1>", com1)
    pr2.bind("<Button-1>", com1)
    pr3.bind("<Button-1>", com1)
    fus1.bind("<Button-1>", com1)
    test1.bind("<Button-1>", com1)
    kun1.bind("<Button-1>", com1)
    keh1.bind("<Button-1>", com1)
    ing1.bind("<Button-1>", com1)
    ing2.bind("<Button-1>", com1)
    ruhm1.bind("<Button-1>", com1)


    win2.mainloop()

def cmd():
    print("Grid")
    aken.command=open_win2()
def cmd1():
    print("Exit . . . ")

    aken.destroy()

anim(0,0,"G R I D","#8f77bf","#141414",cmd)
anim(0,37,"E X I T","#ffcc66","#141414",cmd1)


aken.mainloop()