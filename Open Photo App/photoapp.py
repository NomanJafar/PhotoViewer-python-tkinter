from  tkinter import *
from PIL import ImageTk,Image
top =Tk()
top.iconbitmap('calculator.ico')
top.title("Photos")


my_image1=ImageTk.PhotoImage(Image.open("player1.png"))
my_image2=ImageTk.PhotoImage(Image.open("car.png"))
my_image3=ImageTk.PhotoImage(Image.open("cow.png"))
my_image4=ImageTk.PhotoImage(Image.open("enemy.png"))
my_image5=ImageTk.PhotoImage(Image.open("turtle.png"))

image_list=[my_image1,my_image2,my_image3,my_image4,my_image5]
my_label=Label(image=my_image1)
my_label.grid(row=0,column=0,columnspan=3)

status=Label(top,text="Image 1 of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=W)

    
def forward(img_number):
    global my_label
    global for_pic
    global for_back
    my_label.grid_forget()
    my_label=Label(image=image_list[img_number])
    forward_button=Button(top,text=">>",command=lambda:forward(img_number+1))
    back_button=Button(top,text="<<",command=lambda:back(img_number-1))
    status=Label(top,text="Image " +str(img_number+1)+" of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=W)
    
    if img_number==4:
       forward_button=Button(top,text=">>",state=DISABLED)
    my_label.grid(row=0,column=0,columnspan=3)
    back_button.grid(row=1,column=0)
    forward_button.grid(row=1,column=2)
    status.grid(row=2,column=2,columnspan=3,sticky=E+W)
        

  
def back(img_number):
    global my_label
    global for_pic
    global for_back
    my_label.grid_forget()
    my_label=Label(image=image_list[img_number])
    forward_button=Button(top,text=">>",command=lambda:forward(img_number+1))
    back_button=Button(top,text="<<",command=lambda:back(img_number-1))
    status=Label(top,text="Image " +str(img_number+1)+" of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=W)
    if img_number==0:
        back_button=Button(top,text="<<",state=DISABLED)

   
    my_label.grid(row=0,column=0,columnspan=3)
    back_button.grid(row=1,column=0)
    forward_button.grid(row=1,column=2)
    status.grid(row=2,column=2,columnspan=3,sticky=E+W)

    
qiut=Button(top,text="quit window",bg="black",fg="white",padx=10,pady=10,command=top.quit)
back_button=Button(top,text="<<",command=back,state=DISABLED)
forward_button=Button(top,text=">>",command=lambda:forward(1))


qiut.grid(row=1,column=1)
back_button.grid(row=1,column=0)
forward_button.grid(row=1,column=2)
status.grid(row=2,column=2,columnspan=3,sticky=E+W)

mainloop()



