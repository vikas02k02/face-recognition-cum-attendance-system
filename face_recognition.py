from tkinter import*
from tkinter import ttk
from turtle import bgcolor
from PIL import Image,ImageTk
from tkinter import messagebox

import numpy
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import requests
import imutils





class Face_Recognition:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face_recognition system")
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("arial black",35,"bold"),bg="yellow",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #FIRST IMAGE
        img_top=Image.open("D:\\photos\\facescan3.jfif")     
        img_top=img_top.resize((800,700),Image.ANTIALIAS)                            
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=800,height=700)

        #SECOND IMAGE
        img_bottom=Image.open("D:\\photos\\facescan.jfif")     #PATH DALNA HAI YAHA SMJHA
        img_bottom=img_bottom.resize((750,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=800,y=55,width=750,height=700)

          
        #BUTTON
        b1_1=Button(f_lbl,text="FACE RECOGNITION",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="green",fg="white")
        b1_1.place(x=280,y=600,width=300,height=40)    
#==============attendance===============
    def mark_attendance(self,r,n,d):
        with open("attend.csv","r+",newline="\n") as f:   #name of the file
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            
            if((r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime('%H:%M:%S')
                f.writelines(f"\n{r},{n},{d},{dtString},{d1},Present")


 #=============FACE RECOGNITION==============   

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="vik@s",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                

                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                        
                    self.mark_attendance(r,n,d)              
                else:

                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,y]

            return coord 

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)           #make it work
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")      
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")    

        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face recognisation",img)


            
            if cv2.waitKey(1)==ord('q'):
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()  


