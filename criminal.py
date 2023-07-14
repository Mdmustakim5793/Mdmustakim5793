from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
import mysql.connector 
from tkinter import messagebox


class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANGEMENT SYSTEM (mustakim)')


        # variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_BirthMark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()


        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70)


        # logo

        img_logo=Image.open('images/logo.jpg')
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=80,y=5,width=60,heigh=60)

        # image frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)

        img1=Image.open('images/police.jpg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        # # 2nd 
        img_2=Image.open('images/police2.jpg')
        img_2=img_2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img_2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)


        #  3rd
        img_3=Image.open('images/police.jpg')
        img_3=img_3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1080,y=0,width=540,height=160)


       # Main Frame

        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=1500,height=560)

        # Upper frame

        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # lebal entry

        # case id
        caseid=Label(upper_frame,text='case ID:',font=('arial',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        # Criminal no
        lbl_criminal_no=Label (upper_frame,font=("arial",12,"bold"),text="Criminal_NO:",bg="white")
        lbl_criminal_no.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=("arial",11,"bold"))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7)

        # Criminal name
        lbl_Name=Label(upper_frame,font=("arial",12,"bold"),text="Criminal_Name:",bg="white")
        lbl_Name.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        txt_Name.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # NickName
        lbl_nickname=Label(upper_frame,font=("arial",12,"bold"),text="nickname:",bg="white")
        lbl_nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=("arial",11,"bold"))
        txt_nickname.grid(row=1,column=3,padx=2,pady=7)

        # Arrest Date
        lbl_arrestDate=Label(upper_frame,font=("arial",12,"bold"),text="Arrest Date:",bg="white")
        lbl_arrestDate.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=("arial",11,"bold"))
        txt_arrestDate.grid(row=2,column=1,padx=2,pady=7)

        # Date of crime
        lbl_dateofCrime=Label(upper_frame,font=("arial",12,"bold"),text="Date_of_Crime:",bg="white")
        lbl_dateofCrime.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_dateofCrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=("arial",11,"bold"))
        txt_dateofCrime.grid(row=2,column=3,sticky=W,padx=2,pady=7)


        # Address
        lbl_address=Label(upper_frame,font=("arial",12,"bold"),text="Address:",bg="white")
        lbl_address.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_address.grid(row=3,column=1,padx=2,pady=7)

        # Age
        lbl_age=Label(upper_frame,font=("arial",12,"bold"),text="Age:",bg="white")
        lbl_age.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=("arial",11,"bold"))
        txt_age.grid(row=3,column=3,padx=2,pady=7)

        # Occupution
        lbl_occupution=Label(upper_frame,font=("arial",12,"bold"),text="occupution:",bg="white")
        lbl_occupution.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_occupation=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=("arial",11,"bold"))
        txt_occupation.grid(row=4,column=1,padx=2,pady=7)

        # Birth mark
        lbl_birthMark=Label(upper_frame,font=("arial",12,"bold"),text="BirthMark:",bg="white")
        lbl_birthMark.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_Birthmark=ttk.Entry(upper_frame,textvariable=self.var_BirthMark,width=22,font=("arial",11,"bold"))
        txt_Birthmark.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        # Crime type
        lbl_crimeType=Label(upper_frame,font=("arial",12,"bold"),text="Crime_Type:",bg="white")
        lbl_crimeType.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_crimeType=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=("arial",11,"bold"))
        txt_crimeType.grid(row=0,column=5,padx=2,pady=7)

        # Father name
        lbl_fatherName=Label(upper_frame,font=("arial",12,"bold"),text="FatherName:",bg="white")
        lbl_fatherName.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_fatherName=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=("arial",11,"bold"))
        txt_fatherName.grid(row=1,column=5,padx=2,pady=7)

        # Gender
        lbl_gender=Label(upper_frame,font=("arial",12,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        # Wanted
        lbl_wanted=Label(upper_frame,font=("arial",12,"bold"),text="Most Wanted:",bg="white")
        lbl_wanted.grid(row=3,column=4,sticky=W,padx=2,pady=7)

        # Radio button gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=730,y=90,width=190,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='Male',font=("arial",9,"bold"),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)


        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='Female',font=("arial",9,"bold"),bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)




        # Radio button wanted
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=730,y=130,width=190,height=30)

        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=("arial",9,"bold"),bg='white')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)

        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=("arial",9,"bold"),bg='white')
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        # Buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=620,height=45)

        # add button
        btn_add=Button(button_frame,command=self.add_data,text='Record Save',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        # update button
        btn_update=Button(button_frame,command=self.update_data,text='Update',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        # delete button
        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        # clear button
        btn_Clear=Button(button_frame,command=self.clear_data,text='Clear',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_Clear.grid(row=0,column=3,padx=3,pady=5)

        # background right side image
        img_crime=Image.open('images/background2.webp')
        img_crime=img_crime.resize((470,245),Image.ANTIALIAS)
        self.photocrime=ImageTk.PhotoImage(img_crime)

        self.img_crime=Label(upper_frame,image=self.photocrime)
        self.img_crime.place(x=1000,y=0,width=470,height=245)











        # Down frame

        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=280,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)
        
        self.var_com_search=StringVar()
        bo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("arial",11,"bold"),width=18,state='readonly')
        bo_search_box['value']=('Select Option','Case_id','Criminal_no')
        bo_search_box.current(0)
        bo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        # search button
        btn_search=Button(search_frame,command=self.search_data,text='Search',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        # all button
        btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5)


        
        crimeagency=Label(search_frame,font=("arial",30,"bold"),text="NATIONAL CRIME AGENCY",bg="white",fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=50,pady=0)


        #Table frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='Case id')
        self.criminal_table.heading('2',text="Criminal no")
        self.criminal_table.heading('3',text="Criminal Name")
        self.criminal_table.heading('4',text="Nick Name")
        self.criminal_table.heading('5',text="Arrest Date")
        self.criminal_table.heading('6',text="Crime of Date")
        self.criminal_table.heading('7',text="Address")
        self.criminal_table.heading('8',text="Age")
        self.criminal_table.heading('9',text="Occupation")
        self.criminal_table.heading('10',text="Birth Mark")
        self.criminal_table.heading('11',text="Crime Type")
        self.criminal_table.heading('12',text="Father Name")
        self.criminal_table.heading('13',text="Gender")
        self.criminal_table.heading('14',text="Wanted")

        self.criminal_table['show']='headings'
        
        self.criminal_table.column("1",width=100)
        self.criminal_table.column("2",width=100)
        self.criminal_table.column("3",width=100)
        self.criminal_table.column("4",width=100)
        self.criminal_table.column("5",width=100)
        self.criminal_table.column("6",width=100)
        self.criminal_table.column("7",width=100)
        self.criminal_table.column("8",width=100)
        self.criminal_table.column("9",width=100)
        self.criminal_table.column("10",width=100)
        self.criminal_table.column("11",width=100)
        self.criminal_table.column("12",width=100)
        self.criminal_table.column("13",width=100)
        self.criminal_table.column("14",width=100)

        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
    
    
    # Add function

    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='must@0786',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                           
                                                                                                            self.var_case_id.get(),
                                                                                                            self.var_criminal_no.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_nickname.get(),
                                                                                                            self.var_arrest_date.get(),
                                                                                                            self.var_date_of_crime.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_age.get(),
                                                                                                            self.var_occupation.get(),
                                                                                                            self.var_BirthMark.get(),
                                                                                                            self.var_crime_type.get(),
                                                                                                            self.var_father_name.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_wanted.get(), 


                                                                                                          ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been added')
            except Exception as es:
                   messagebox.showerror('Error',f'Due To{str(es)}')

        
    # fetch data
    def fetch_data(self):
        conn=mysql.connector.Connect(host='localhost',username='root',password='must@0786',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()     
        conn.close()    
        
    # get cursor

    def get_cursor(self,event=""):
        cursur_row=self.criminal_table.focus() 
        content=self.criminal_table.item(cursur_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_BirthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])

    # update

    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this criminal record')           
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='must@0786',database='management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateofcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',(

                                                                                                                                                                                                                                                    self.var_criminal_no.get(), 
                                                                                                                                                                                                                                                    self.var_arrest_date.get(),
                                                                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                                                                    self.var_date_of_crime.get(),
                                                                                                                                                                                                                                                    self.var_nickname.get(),
                                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                                    self.var_age.get(),
                                                                                                                                                                                                                                                    self.var_occupation.get(),
                                                                                                                                                                                                                                                    self.var_BirthMark.get(),
                                                                                                                                                                                                                                                    self.var_crime_type.get(),
                                                                                                                                                                                                                                                    self.var_father_name.get(),
                                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                                    self.var_wanted.get(),
                                                                                                                                                                                                                                                    self.var_case_id.get(), 



                                                                                                                                                                                                                                                ))
                else:
                    if not update:
                        return
                conn.commit()    
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record successfully Updated')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')    

    # delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure Delete this criminal')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='must@0786',database='management')
                    my_cursor=conn.cursor()
                    sql='delete from criminal where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:     
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record successfully Delete')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')    

    # clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_BirthMark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    # search
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='must@0786',database='management')            
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+"LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("",END,values=i)
                conn.commit()        
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')    
        
        


         

       







if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()   