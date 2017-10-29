import webbrowser
import time
from Tkinter import *
from PIL import ImageTk, Image
def to_happen():
    b_c=0
    t_c=a1.get()
    text2=nint.get()
    text1=mint.get()
    while(b_c<t_c):
        time.sleep(float(text2))
        text1=mint.get()
        webbrowser.open(text1)
        b_c=b_c+1
    return
def quit():
    root.destroy()
root= Tk()
mint = StringVar()
nint=StringVar()
a1=IntVar()

root.geometry("420x400")
root.title("Mood Pop")
root.configure(bg = 'grey')    
root.resizable(width=FALSE, height=FALSE)
#root.iconbitmap(r'mp.ico') 
logo = ImageTk.PhotoImage(Image.open("add1.gif"))
w1 = Label(root, image=logo).pack(expand=1)   
lb11= Label(root,text="Enter the time in seconds",fg="#383a39", bg="#a1dbcd", font=("Helvetica",10)).pack(pady=5)

eBox =Entry(root,textvariable=nint).pack(pady=5)
lb12= Label(root,text="Enter the link",fg="#383a39", bg="#a1dbcd", font=("Helvetica",10)).pack(pady=10)

eBox2 =Entry(root,textvariable=mint).pack(pady=5)
lb13= Label(root,text="For how many times do you want this to happen",fg="#383a39", bg="#a1dbcd", font=("Helvetica",10)).pack(pady=10)
eBox3 =Entry(root,textvariable=a1).pack(pady=5)
#frame = Frame(root, relief=RAISED, borderwidth=1)
#frame.pack(fill=BOTH, expand=1)
#root.pack(fill=BOTH, expand=1)


btn1= Button(root,text="Okay",command=to_happen)
btn1.pack(side=LEFT,padx=30, pady=5)
btn1.config(relief=SUNKEN)
btn2= Button(root,text="Close",command=quit)
btn2.pack(side=RIGHT,padx=30, pady=5)
btn2.config(relief=SUNKEN)

mainloop()


