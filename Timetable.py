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

    def log(event):
        win4=Toplevel()#создаём второе(дочернее) окно
        win4.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win4.geometry("275x300")
        logw=Label(win4, text="Logistikateenused ja varude juhtimine.\nÕpetaja nimi: Inessa Klimanskaja.\nKabinet: B 002", width=40,height=20)
        logw.grid(row=0, column=0)
        win4.mainloop()

    def mat(event):
        win5=Toplevel()#создаём второе(дочернее) окно
        win5.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win5.geometry("275x300")
        matw=Label(win5, text="Tunni nimetus: Matemaatika.\nÕpetaja nimi: Nadežda Voronova.\nKabinet: B 133", width=40,height=20)
        matw.grid(row=0, column=0)
        win5.mainloop()

    def est(event):
        win20=Toplevel()#создаём второе(дочернее) окно
        win20.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win20.geometry("275x300")
        estw=Label(win20, text="Tunni nimetus: Eesti keel II grupp.\nÕpetaja nimi: Olesja Ojamäe.\nKabinet: B 234", width=40,height=20)
        estw.grid(row=0, column=0)
        win20.mainloop()

    def rus(event):
        win21=Toplevel()#создаём второе(дочернее) окно
        win21.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win21.geometry("275x300")
        estw=Label(win21, text="Tunni nimetus: Keel ja kirjandus.\nÕpetaja nimi: Ljudmilla Mihhailova.\nKabinet: B 221", width=40,height=20)
        estw.grid(row=0, column=0)
        win21.mainloop()

    def matt(event):
        win22=Toplevel()#создаём второе(дочернее) окно
        win22.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win22.geometry("275x300")
        matw=Label(win22, text="Tunni nimetus: Matemaatika(Tugiõpe).\nÕpetaja nimi: Nadežda Voronova.\nKabinet: B 133", width=40,height=20)
        matw.grid(row=0, column=0)
        win22.mainloop()    
        
    def estdv(event):
        win23=Toplevel()#создаём второе(дочернее) окно
        win23.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win23.geometry("275x300")
        estdv=Label(win23, text="Tunni nimetus: Eesti keel I grupp.\nÕpetaja nimi: Alina Laaneväli.\nKabinet: B 236", width=40,height=20)
        estdv.grid(row=0, column=0)
        win23.mainloop()    

    def kem(event):
        win24=Toplevel()#создаём второе(дочернее) окно
        win24.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win24.geometry("275x300")
        kem=Label(win24, text="Tunni nimetus: Keemia(Tugiõpe).\nÕpetaja nimi: Svetlana Pesetskaja.\nKabinet: B 144", width=40,height=20)
        kem.grid(row=0, column=0)
        win24.mainloop()  
        
    def prog(event):
        win25=Toplevel()#создаём второе(дочернее) окно
        win25.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win25.geometry("275x300")
        prog=Label(win25, text="Tunni nimetus: Programmeerimise alused.\nÕpetaja nimi: Marina Oleinik.\nKabinet: E 07", width=40,height=20)
        prog.grid(row=0, column=0)
        win25.mainloop()  

    def fus(event):
        win26=Toplevel()#создаём второе(дочернее) окно
        win26.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win26.geometry("275x300")
        fus=Label(win26, text="Tunni nimetus: Füüsika.\nÕpetaja nimi: Nadežda Voronova.\nKabinet: B 133", width=40,height=20)
        fus.grid(row=0, column=0)
        win26.mainloop()    

    def estu(event):
        win27=Toplevel()#создаём второе(дочернее) окно
        win27.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win27.geometry("275x300")
        estu=Label(win27, text="Tunni nimetus: Eesti keel(Tugiõpe).\nÕpetaja nimi: Alina Laaneväli.\nKabinet: B 236", width=40,height=20)
        estu.grid(row=0, column=0)
        win27.mainloop() 

    def kun(event):
        win28=Toplevel()#создаём второе(дочернее) окно
        win28.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win28.geometry("275x300")
        kun=Label(win28, text="Tunni nimetus: Kuntsiained.\nÕpetaja nimi: Aleksandra Norkevitš.\nKabinet: B 232", width=40,height=20)
        kun.grid(row=0, column=0)
        win28.mainloop() 

    def keh(event):
        win29=Toplevel()#создаём второе(дочернее) окно
        win29.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win29.geometry("275x300")
        keh=Label(win29, text="Tunni nimetus: Kehaline kasvatus.\nÕpetaja nimi: Maksim Maksõmiv.\nKabinet: Võimla A", width=40,height=20)
        keh.grid(row=0, column=0)
        win29.mainloop() 

    def ing(event):
        win30=Toplevel()#создаём второе(дочернее) окно
        win30.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win30.geometry("275x300")
        ing=Label(win30, text="Tunni nimetus: Inglise keel I grupp.\nÕpetaja nimi: Olga Poskotinova.\nKabinet: B 138", width=40,height=20)
        ing.grid(row=0, column=0)
        win30.mainloop() 

    def ingg(event):
        win31=Toplevel()#создаём второе(дочернее) окно
        win31.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win31.geometry("275x300")
        ingg=Label(win31, text="Tunni nimetus: Inglise keel II grupp.\nÕpetaja nimi: Olga.\nKabinet: B 227", width=40,height=20)
        ingg.grid(row=0, column=0)
        win31.mainloop() 

    def ruhm(event):
        win32=Toplevel()#создаём второе(дочернее) окно
        win32.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win32.geometry("275x300")
        ruhm=Label(win32, text="Tunni nimetus: Rühmajunhatajantund.\nÕpetaja nimi: Alina Laaneväli.\nKabinet: B 236", width=40,height=20)
        ruhm.grid(row=0, column=0)
        win32.mainloop() 

    def rah(event):
        win33=Toplevel()#создаём второе(дочернее) окно
        win33.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win33.geometry("275x300")
        rah=Label(win33, text="Tunni nimetus: Rahendustrakvara.\nÕpetaja nimi: Irina Merkulova.\nKabinet: E 10", width=40,height=20)
        rah.grid(row=0, column=0)
        win33.mainloop() 

    win2=Toplevel()#создаём второе(дочернее) окно
    win2.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    win2.geometry("955x710")

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

    est1=Label(win2, borderwidth=1, bg="#cab4c7", relief="solid",text="Eesti keel", width=10,height=4)
    est1.grid(row=1, column=2,sticky=S)
    #Label(win2, relief="solid",borderwidth=0, bg="#cab4c7" ,text="B234", width=5,height=1).grid(row=1, column=2,sticky=SW)
    log1=Label(win2, borderwidth=1, bg="#80e092", relief="solid",text="Logistikateenused\nja varude juhtimine", width=10,height=8)
    log1.grid(row=1, column=3, sticky=N+S+W+E, columnspan=2)
    mat1=Label(win2, borderwidth=1, bg="#fcb9d0", relief="solid",text="Matemaatika", width=10,height=8)
    mat1.grid(row=1, column=5, sticky=N+S+W+E, columnspan=2)
    rus1=Label(win2, borderwidth=1, bg="#94ed80", relief="solid",text="Keel ja kirjandus", width=10,height=8)
    rus1.grid(row=1, column=8, sticky=N+S+W+E, columnspan=2)
    tmat1=Label(win2, borderwidth=1, bg="#fcb9d0", relief="solid",text="Tugiõpe\n(matema\natika)", width=10,height=8)
    tmat1.grid(row=1, column=10, sticky=N+S+W+E)

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

    kem1=Label(win2, borderwidth=1, bg="#e080e0", relief="solid",text="Tugiõpe\n(keemia)", width=10,height=4)
    kem1.grid(row=2, column=2,sticky=N+S+W+E)
    pr1=Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8)
    pr1.grid(row=2, column=3, sticky=N+S+W+E, columnspan=3)
    fus1=Label(win2, borderwidth=1, bg="#fcb9d0", relief="solid",text="Füüsika", width=10,height=8)
    fus1.grid(row=2, column=7, sticky=N+S+W+E, columnspan=2)

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

    test1=Label(win2, borderwidth=1, bg="#ff80ff", relief="solid",text="Tugiõpe\n(eesti keel)", width=10,height=4)
    test1.grid(row=3, column=2,sticky=N)
    kun1=Label(win2, borderwidth=1, bg="#e080ce", relief="solid",text="Kuntsiained\n(eesti keeles)", width=10,height=8)
    kun1.grid(row=3, column=3, sticky=N+S+W+E, columnspan=2)
    keh1=Label(win2, borderwidth=1, bg="#e080c0", relief="solid",text="Kehaline kasvatus", width=10,height=8)
    keh1.grid(row=3, column=6, sticky=N+S+W+E, columnspan=2)

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

    log2=Label(win2, borderwidth=1, bg="#80e092", relief="solid",text="Logistikateenused\nja varude juhtimine", width=10,height=8)
    log2.grid(row=4, column=2, sticky=N+S+W+E, columnspan=2)
    pr2=Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8)
    pr2.grid(row=4, column=5, sticky=N+S+W+E, columnspan=2)
    ing1=Label(win2, bg="#fffff0",text="Inglise keel", width=20,height=4)
    ing1.grid(row=4, column=7, sticky=N, columnspan=2)
    rah1=Label(win2, bg="#ff80a2",text="Rahendustrakvara", width=20,height=4)
    rah1.grid(row=4, column=7, sticky=S, columnspan=2)

    rah2=Label(win2, bg="#ff80a2",text="Rahendustrakvara", width=20,height=4)
    rah2.grid(row=4, column=9, sticky=N, columnspan=2)
    est2=Label(win2, bg="#cab4c7",text="Eesti keel", width=20,height=4)
    est2.grid(row=4, column=9,sticky=S, columnspan=2)
    ruhm1=Label(win2, borderwidth=1, bg="#ff80ff", relief="solid",text="Rühmaju\nhataja\ntund", width=10,height=4)
    ruhm1.grid(row=4, column=11,sticky=N+S+W+E)

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

    
    est3=Label(win2, bg="#ff80ff",text="Eesti keel", width=20,height=4)
    est3.grid(row=5, column=2, sticky=N, columnspan=2)
    rah3=Label(win2, bg="#ff80a2",text="Rahendustrakvara", width=20,height=4)
    rah3.grid(row=5, column=2, sticky=S, columnspan=2)
    pr3=Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8)
    pr3.grid(row=5, column=4, sticky=N+S+W+E, columnspan=5)
    rah4=Label(win2, bg="#ff80a2",text="Rahendustrakvara", width=20,height=4)
    rah4.grid(row=5, column=9, sticky=N, columnspan=2)
    ing2=Label(win2, bg="#80ff80",text="Inglise keel", width=20,height=4)
    ing2.grid(row=5, column=9,sticky=S, columnspan=2)

    #Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=1, column=1, sticky=N+S+W+E, columnspan=11)
    #Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=2, column=1, sticky=N+S+W+E, columnspan=11)
    #Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=3, column=1, sticky=N+S+W+E, columnspan=11)
    #Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=4, column=1, sticky=N+S+W+E, columnspan=11) 
    #Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=5, column=1, sticky=N+S+W+E, columnspan=11)

    est1.bind("<Button-1>",
       lambda e="Description": est(e))#
    est2.bind("<Button-1>",
       lambda e="Description": est(e))#
    est3.bind("<Button-1>",
       lambda e="Description": estdv(e))#
    log1.bind("<Button-1>",
       lambda e="Description": log(e))#
    log2.bind("<Button-1>",
       lambda e="Description": log(e))#
    mat1.bind("<Button-1>",
       lambda e="Description": mat(e))#
    rus1.bind("<Button-1>",
       lambda e="Description": rus(e))#
    tmat1.bind("<Button-1>",
       lambda e="Description": matt(e))#
    kem1.bind("<Button-1>",
       lambda e="Description": kem(e))#
    pr1.bind("<Button-1>",
       lambda e="Description": prog(e))#
    pr2.bind("<Button-1>",
       lambda e="Description": prog(e))#
    pr3.bind("<Button-1>",
       lambda e="Description": prog(e))#
    fus1.bind("<Button-1>",
       lambda e="Description": fus(e))#
    test1.bind("<Button-1>",
       lambda e="Description": estu(e))#
    kun1.bind("<Button-1>",
       lambda e="Description": kun(e))#
    keh1.bind("<Button-1>",
       lambda e="Description": keh(e))#
    ing1.bind("<Button-1>",
       lambda e="Description": ing(e))#
    ing2.bind("<Button-1>",
       lambda e="Description": ingg(e))#
    ruhm1.bind("<Button-1>",
       lambda e="Description": ruhm(e))#
    rah1.bind("<Button-1>",
       lambda e="Description": rah(e))
    rah2.bind("<Button-1>",
       lambda e="Description": rah(e))
    rah3.bind("<Button-1>",
       lambda e="Description": rah(e))
    rah4.bind("<Button-1>",
       lambda e="Description": rah(e))

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
