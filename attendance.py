from argparse import FileType
from dataclasses import field
from importlib.resources import contents
from re import L
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from turtle import left
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import exp
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x798+0+0")
        self.root.title("face recognition system")

       # =====================variables====================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

         #FIRST IMAGE
        img=Image.open(r"D:\photos\attend.jfif")     #PATH DALNA HAI YAHA SMJHA
        img=img.resize((800,200),Image.ANTIALIAS)                            
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #SECOND IMAGE
        img1=Image.open(r"D:\photos\attend2.jfif")     
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        #BG IMAGE
        img3=Image.open(r"D:\photos\landscape.jfif")     
        img3=img3.resize((1600,630),Image.ANTIALIAS)                            
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=200,width=1600,height=630)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("arial black",35,"bold"),bg="green",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)
        #LEFT LABEL FRAME
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT ATTENDANCE DETAILS")
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"D:\photos\landscape.jfif")     
        
        img_left=img_left.resize((720,130),Image.ANTIALIAS)                            
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=710,height=330)

        #Labelland Entry
        #attendance id
        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("arial black",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,font=("arial black",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        rollLabel=Label(left_inside_frame,text="Roll",bg="white",font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)

        #name
        nameLabel=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8)

        #department
        depLabel=Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)

        atten_name=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=3,pady=8)

        #time
        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

        #date

        dateLabel=Label(left_inside_frame,text="Date:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_roll=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_roll.grid(row=2,column=3,pady=8)
        

        #attendance 
        attendanceLabel=Label(left_inside_frame,text="Attendance:",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("status","present","absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=280,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



 

        #RIGHT LABEL FRAME
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDANCE DETAILS")
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=445)

        #============SCROLL BAR TABLE===============

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("id",text="Attendance Id")
        self.attendanceReportTable.heading("roll",text="Roll")
        self.attendanceReportTable.heading("name",text="Name" )
        self.attendanceReportTable.heading("department",text="Department ")
        self.attendanceReportTable.heading("time",text="Time ")
        self.attendanceReportTable.heading("date",text="Date ")
        self.attendanceReportTable.heading("attendance",text="Attendance" )

        self.attendanceReportTable["show"]="headings"

        self.attendanceReportTable.column("id",width=100)
        self.attendanceReportTable.column("roll",width=100)
        self.attendanceReportTable.column("name",width=100)
        self.attendanceReportTable.column("department",width=100)
        self.attendanceReportTable.column("time",width=100)
        self.attendanceReportTable.column("date",width=100)
        self.attendanceReportTable.column("attendance",width=100)

        self.attendanceReportTable.pack(fill=BOTH,expand=1)    

       # self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

 #========================FETCH  DATA===================

    def fetchData(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("",END,values=i)

    #import data
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",FileType=(("csv File","*.csv"),("All file"," *.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export data 14:28 8/9-
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("no data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",FileType=(("csv File","*.csv"),("All file"," *.*")),parent=self.root)  
            with open(fln,mod="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimeter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("data export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("error",f"due to:{str(es)}",parent=self.root) 

    def get_cursor(self,event=""):
        Cursor_row=self.attendanceReportTable.focus()
        content=self.attendanceReportTable.item(Cursor_row)
        row=content['values']  
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])
    
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
                         






if __name__=="__main__":
    root=Tk() 
    obj=Attendance(root)
    root.mainloop()

