from cProfile import label
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from attendance import Attendance
from face_recognition import Face_Recognition


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

#first image
        img=Image.open("D:\\photos\\code.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

#second image
        img1=Image.open("D:\\photos\\code.jpg")
        img1=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

#third image
        img2=Image.open("D:\\photos\\code.jpg")
        img2=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

#background image
        img3=Image.open("D:\\photos\\backgroundimg.jpg")
        img3=img3.resize((1500,720),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

#student details button
        img4=Image.open("D:\\photos\\code.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details ,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details ,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

#train data button
        img8=Image.open("D:\\photos\\code.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b6=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.train_data)
        b6.place(x=500,y=100,width=220,height=220)

        b6_6=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=500,y=300,width=220,height=40)


#Face Detector button
        img9=Image.open("D:\\photos\\code.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b7=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.face_data)
        b7.place(x=800,y=100,width=220,height=220)

        b7_7=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=800,y=300,width=220,height=40)

#attendance button
        img7=Image.open("D:\\photos\\code.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.attendance_data)
        b4.place(x=1100,y=100,width=220,height=220)

        b4_4=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=1100,y=300,width=220,height=40)


#Photos button
        img5=Image.open("D:\\photos\\code.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.open_img)
        b2.place(x=500,y=380,width=220,height=220)

        b2_2=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=500,y=580,width=220,height=40)


#Exit button
        img6=Image.open("D:\\photos\\code.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b3.place(x=800,y=380,width=220,height=220)

        b3_3=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=800,y=580,width=220,height=40)


#============photos utton backend=============

    def open_img(self):
        os.startfile("data")
        

        #========================function buttons=============================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
                

if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()