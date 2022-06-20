from  tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
new=Tk()
new.iconbitmap('calculator.ico')
new.title("ALERT")
# new.my_files=filedialog.askopenfilename(initialdir="E:\python course\python docs",title="select a file",filetypes=(("png files","*.png"),("all files","*.*")))
# my_image1=ImageTk.PhotoImage(Image.open(new.my_files))
# my_label1=Label(new,image=my_image1).pack()


# frames
# frame=LabelFrame(top,text="this is my frame",padx=5,pady=5)
# frame.pack(padx=100,pady=100)
# b=Button(frame,text="dont touch me",padx=5,pady=5)
# b.pack(padx=5,pady=5)

# radio buttons
# choices=[("car","car"),("truck","truck"),("bmw","bmw"),("bike","bike")]
# vehicle=StringVar()
# vehicle.set("car")
# for text,choice in choices:

# Radiobutton(top,text="I agree",variable=r,value=1).pack()
    # Radiobutton(top,text=text,variable=vehicle,value=choice).pack(anchor=W)

# mylabel=Label(top,text=vehicle.get()).pack()

# def click(done):
#     mylabel=Label(top,text=vehicle.get()).pack()


# choice=Button(top,text="save",command=lambda:click(vehicle.get()))

# MESSAGE BOX
# showerror,showinfo,showwarning,QUESTION
def warning():
    ads=messagebox.askquestion("you have issue a new account on basis of your information\nyour new account number is xxx-xxxxxx-xxxx-x\nyour default password is xxx-xxxxxx-xxxx-x")
    l=Label(new,text=ads).pack()

Button(new,text="Run",command=warning).pack()



# create new window

# def new_window():
#     top=Toplevel()
#     global lab
#     lab=Label(top,text="this is your new window",padx=20,pady=20).pack(padx=100,pady=20)


     

# Button(new,text="click here to get a new window",command=new_window).pack(padx=50,pady=50)




#  dialog box
# def open():
#     global my_image1
    

#     new.my_files=filedialog.askopenfilename(initialdir="E:\python course\python docs",title="select a file",filetypes=(("png files","*.png"),("all files","*.*")))
#     my_image1=ImageTk.PhotoImage(Image.open(new.my_files))
    
#     my_label1=Label(new,image=my_image1).pack()

    
#     bar1=Scale(new,from_=0, to=my_image1.height())
#     bar1.pack(anchor=W)
#     bar2=Scale(new,from_=0, to=my_image1.width(),orient=HORIZONTAL)
#     bar2.pack(anchor=W)
#     new.geometry(str(my_image1.height())+"*"+str(my_image1.width()))

# btn=Button(new,text="open a file",command=open).pack()


# check boxes

# var=IntVar()
# c=Checkbutton(new,text="check it out",variable=var)
# c.pack()

    
# lab=Label(new,text=var.get()).pack()

# btn=Button(new,text="get the value",command=check)
# btn.pack()

mainloop()