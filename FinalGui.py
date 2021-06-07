from tkinter import *
from tkinter import messagebox
import fetch
import singleres
def confirm():
    res = messagebox.askquestion("askquestion", """This will take 10 - 15 min and Your App will be unresponsive 
                                 Are you sure?""")
    if res == 'yes':
        GetCompleteResult()
    
def GetCompleteResult():
    lb = Listbox(
    frame,
    width=int(width/2),
    height=300,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
    )
    result=[]
    rollno = my_entry.get()
    rollno = int(rollno)//100
    roll=rollno*100+1
    lb.insert(END, ("Rank   Roll No.    SGPA               Name"))
    lb.pack(side=LEFT, fill=BOTH)
    for rol in range(75):
        res = fetch.getres(roll)
        if res !=0 :
            result.append(res)
        roll+=1
        
    result.sort(reverse=True ,key=lambda t: t[0])  
    rank=1
    for res in result:
        if rank < 10 :
            lb.insert(END, ("    "+str(rank) +"      " + str(res[1])+"        " + str(res[0]) +"      "+ str(res[2])))
        else :
            lb.insert(END, ("   "+str(rank) +"     " + str(res[1])+"        " + str(res[0]) +"      "+ str(res[2])))
        rank+=1
        
    sb = Scrollbar(frame)
    sb.pack(fill=BOTH,expand=TRUE)
    
    lb.config(yscrollcommand=sb.set)
    sb.config(command=lb.yview)


    
def GetResult():
    rollno = my_entry.get()  
    singleres.getSingleRes(rollno)

root = Tk()
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("Knit Result Analyser")
root.config(bg='white')

frame = Frame(root)
frame.pack(pady=10)

canvas1 = Canvas(root, width = width, height = height,bg='white',  relief = 'raised')
canvas1.pack()

label1 = Label(root, text='KNIT Result Analyser')
label1.config(font=('helvetica', 28))
canvas1.create_window(width/2, 40, window=label1)

label2 = Label(root, text='Enter Roll Number')
label2.config(font=('helvetica', 24))
canvas1.create_window(width/2, 150, window=label2)

my_entry = Entry(
    root,
    #width=int(width/10) ,
    font=('times', 24)
    
    )
canvas1.create_window(width/2, 200, window=my_entry)

#button_frame = Frame(root)

button1 = Button(
    #button_frame,
    text='Get Single Result',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=GetResult
)
canvas1.create_window(3*width/7, 250, window=button1)

button2 = Button(
    #button_frame,
    text='Get Complete Result',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=confirm
)
canvas1.create_window(4*width/7, 250, window=button2)

root.mainloop()
