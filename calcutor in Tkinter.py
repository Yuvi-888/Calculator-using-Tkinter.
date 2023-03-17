from tkinter import *
root=Tk()
def click(event):
    global sc_value
    text=event.widget.cget('text')
    print(text)
    if text=='=':
        if sc_value.get().isdigit():
            value=int(sc_value.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                value='Error'
                print(e)
        sc_value.set(value)
        screen.update()
    elif text=='C':
        sc_value.set('')
        screen.update()
    else:
        sc_value.set(sc_value.get()+text)
root.geometry('500x700')
root.title('Calculator')
root.maxsize(width=500,height=700)
root.config(bg='black')
root.iconbitmap("C:\\Users\\Yuvraj\\Downloads\\Wineass-Ios7-Redesign-Calculator.ico")
sc_value=StringVar()
sc_value.set('')
screen=Entry(root,bg='white',borderwidth=3,textvariable=sc_value,relief=SUNKEN,font='lucida 38 bold')
screen.pack(padx=9,pady=12,fill=X)

frame=Frame(root,bg='black')
b=Button(frame,bg='orange',font='lucida 35 bold',relief=RIDGE,text='9')
b.pack(side=LEFT,padx=30,pady=3,fill=X)
b.bind('<Button-1>',click)

b=Button(frame,bg='orange',font='lucida 35 bold',relief=RIDGE,text='8')
b.pack(side=LEFT,padx=50,pady=3,fill=X)
b.bind('<Button-1>',click)

b=Button(frame,bg='orange',font='lucida 35 bold',relief=RIDGE,text='7')
b.pack(side=LEFT,padx=30,pady=3,fill=X)
b.bind('<Button-1>',click)
frame.pack()

frame=Frame(root,bg='black')
b=Button(frame,bg='orange',font='lucida 35 bold',relief=RIDGE,text='6')
b.pack(side=LEFT,padx=30,pady=3,fill=X)
b.bind('<Button-1>',click)

b=Button(frame,bg='orange',font='lucida 35 bold',relief=RIDGE,text='5')
b.pack(side=LEFT,padx=50,pady=3,fill=X)
b.bind('<Button-1>',click)

b=Button(frame,bg='orange',font='lucida 35 bold',relief=RIDGE,text='4')
b.pack(side=LEFT,padx=30,pady=3,fill=X)
b.bind('<Button-1>',click)
frame.pack()

frame=Frame(root,bg='black')
b=Button(frame,bg='orange',font='lucida 35 bold',relief=RIDGE,text='3')
b.pack(side=LEFT,padx=30,pady=3,fill=X)
b.bind('<Button-1>',click)

b=Button(frame,bg='orange',font='lucida 35 bold',relief=RIDGE,text='2')
b.pack(side=LEFT,padx=50,pady=3,fill=X)
b.bind('<Button-1>',click)

b=Button(frame,bg='orange',font='lucida 35 bold',relief=RIDGE,text='1')
b.pack(side=LEFT,padx=30,pady=3,fill=X)
b.bind('<Button-1>',click)
frame.pack()

frame=Frame(root,bg='grey')
b=Button(frame,bg='orange',font='lucida 26 bold',relief=RIDGE,text='0')
b.pack(side=LEFT,padx=70,pady=10,fill=X)
b.bind('<Button-1>',click)

b=Button(frame,bg='orange',font='lucida 26 bold',relief=RIDGE,text='=')
b.pack(side=LEFT,padx=32,pady=10,fill=X)
b.bind('<Button-1>',click)

b=Button(frame,bg='orange',font='lucida 26 bold',relief=RIDGE,text='.')
b.pack(side=LEFT,padx=72,pady=10,fill=X)
b.bind('<Button-1>',click)
frame.pack(fill=X)

frame=Frame(root,bg='grey')
b=Button(frame,bg='orange',font='lucida 26 bold',relief=RIDGE,text='+')
b.pack(side=LEFT,padx=69,pady=10,fill=X)
b.bind('<Button-1>',click)

b=Button(frame,bg='orange',font='lucida 26 bold',relief=RIDGE,text='-')
b.pack(side=LEFT,padx=37,pady=10,fill=X)
b.bind('<Button-1>',click)

b=Button(frame,bg='orange',font='lucida 26 bold',relief=RIDGE,text='*')
b.pack(side=LEFT,padx=69,pady=10,fill=X)
b.bind('<Button-1>',click)
frame.pack(fill=X)

frame=Frame(root,bg='grey')
b=Button(frame,bg='orange',font='lucida 30 bold',relief=RIDGE,text='/')
b.pack(side=LEFT,padx=71,pady=10,fill=X)
b.bind('<Button-1>',click)

b=Button(frame,bg='orange',font='lucida 30 bold',relief=RIDGE,text='%')
b.pack(side=LEFT,padx=24,pady=10,fill=X)
b.bind('<Button-1>',click)

b=Button(frame,bg='orange',font='lucida 30 bold',relief=RIDGE,text='C')
b.pack(side=LEFT,padx=60,pady=10,fill=X)
b.bind('<Button-1>',click)
frame.pack(fill=X)
root.mainloop()