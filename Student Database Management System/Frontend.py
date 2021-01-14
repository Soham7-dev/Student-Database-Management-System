from tkinter import *
import tkinter.messagebox
import Backend

class Student():

    def __init__(self):

        '''-------ROOT WINDOW-------'''
        self.root = Tk()
        self.root.title("Student DBMS")
        self.root.geometry("992x641")
        self.root.maxsize(width=992, height=641)
        self.root.minsize(width=992, height=641)
        self.root.config(bg = '#d5d3f0')

        '''-------DECLARE THE STRING VARIABLES-------'''
        stdID = StringVar()
        first_name = StringVar()
        sur_name = StringVar()
        date_of_birth = StringVar()
        age = StringVar()
        gender = StringVar()
        address = StringVar()
        mobile_no = StringVar()

        '''-----FRAME------'''

        MainFrame = Frame(self.root, bg = 'black')
        MainFrame.grid()

        #Title Frame
        TitleFrame = Frame(MainFrame, bd = 2, padx = 20, pady = 5, bg = '#481fa6', relief = RIDGE)
        TitleFrame.pack(side = TOP)

        #Label of Title Frame
        self.lblTitle = Label(TitleFrame, font = ('arial', 38, 'bold'), text = "Student Database Management System", bg= '#481fa6', fg='#eeedfc')
        self.lblTitle.grid()

        #Button Frame
        ButtonFrame = Frame(MainFrame, width = 993, height = 80, padx = 10, pady = 4, bg = 'black')
        ButtonFrame.pack(side = BOTTOM)

        #Frame for displaying date
        DataFrame = Frame(MainFrame, bd=1, width=993, height=500, padx=10, pady=4, bg='cadet blue', relief=RIDGE)
        DataFrame.pack(side = BOTTOM)

        #Frame for Student Information
        stdInfo = LabelFrame(DataFrame, bd = 2, relief = RIDGE, width = 600, height = 500, bg = 'Ghost White', font = ('arial', 20, 'bold'), text = "Student Info")
        stdInfo.pack(side = LEFT)

        #Frame where the details of the students will be displayed
        stdDetails = LabelFrame(DataFrame,bd = 2, relief = RIDGE, width = 393, height =  500, bg = 'Ghost White', font = ('arial', 20, 'bold'), text = "Student Display")
        stdDetails.pack(side = RIGHT)

        # self.root.grid_columnconfigure(0, weight = 1)
        '''-------METHODS-------'''

        #Method to exit the program
        def isExit():
            isExit = tkinter.messagebox.askyesno("Student Database Management System", "Do you want to exit?")
            if isExit == 1:
                self.root.destroy()
                return

        #Add New Student
        def addData():
            if (len(stdID.get()) != 0):
                Backend.addstdRec(stdID.get(), first_name.get(), sur_name.get(), date_of_birth.get(), age.get(),
                                  gender.get(), address.get(), mobile_no.get())
                student_list.delete(0, END)
                student_list.insert(END, stdID.get(), first_name.get(), sur_name.get(), date_of_birth.get(), age.get(),
                                    gender.get(), address.get(), mobile_no.get())

        #Display Data
        def displayData():
            student_list.delete(0, END)
            for row in Backend.viewData():
                student_list.insert(END, row, str(""))

        #Clear Data
        def clearData():
            self.txt_stdID.delete(0, END)
            self.txt_first_name.delete(0, END)
            self.txt_sur_name.delete(0, END)
            self.txt_date_of_birth.delete(0, END)
            self.txt_age.delete(0, END)
            self.txt_gender.delete(0, END)
            self.txt_address.delete(0, END)
            self.txt_mobile_no.delete(0, END)

        #Record of Students
        def StudentRec(event):
            global sd
            searchStd = student_list.curselection()[0]
            sd = student_list.get(searchStd)

            self.txt_stdID.delete(0, END)
            self.txt_stdID.insert(END, sd[1])
            self.txt_first_name.delete(0, END)
            self.txt_first_name.insert(END, sd[2])
            self.txt_sur_name.delete(0, END)
            self.txt_sur_name.insert(END, sd[3])
            self.txt_date_of_birth.delete(0, END)
            self.txt_date_of_birth.insert(END, sd[4])
            self.txt_age.delete(0, END)
            self.txt_age.insert(END, sd[5])
            self.txt_gender.delete(0, END)
            self.txt_gender.insert(END, sd[6])
            self.txt_address.delete(0, END)
            self.txt_address.insert(END, sd[7])
            self.txt_mobile_no.delete(0, END)
            self.txt_mobile_no.insert(END, sd[8])

        #Delete Data
        def deleteData():
            if (len(stdID.get()) != 0):
                Backend.delRec(sd[0])
                clearData()
                displayData()

        #Search Data
        def searchDatabase():
            student_list.delete(0, END)
            for row in Backend.searchData(stdID.get(), first_name.get(), sur_name.get(), date_of_birth.get(), age.get(),
                                          gender.get(), address.get(), mobile_no.get()):
                student_list.insert(END, row, str(""))

        #Update Data
        def updateDatabase():
            if (len(stdID.get()) != 0):
                Backend.delRec(sd[0])
            if (len(stdID.get()) != 0):
                Backend.addstdRec(stdID.get(), first_name.get(), sur_name.get(), date_of_birth.get(), age.get(),
                                  gender.get(), address.get(), mobile_no.get())
                student_list.delete(0, END)
                student_list.insert(END, stdID.get(), first_name.get(), sur_name.get(), date_of_birth.get(), age.get(),
                                    gender.get(), address.get(), mobile_no.get())

        '''-------STUDENT ENTRY-------'''

        self.label_stdID = Label(stdInfo, text = "Student ID", font = ('arial', 14, 'bold'), bg = 'Ghost White',padx = 2, pady = 6)
        self.label_stdID.grid(row = 0, column = 0)
        self.txt_stdID = Entry(stdInfo, textvariable = stdID, bd = 2, relief = SUNKEN, font = ('arial', 12, 'bold'), width = 30)
        self.txt_stdID.grid(row = 0, column = 1)

        self.label_first_name = Label(stdInfo, text="First Name", font=('arial', 14, 'bold'), bg='Ghost White', padx = 2, pady = 16)
        self.label_first_name.grid(row=1, column=0)
        self.txt_first_name = Entry(stdInfo, textvariable=first_name, bd = 2, relief = SUNKEN, font=('arial', 12, 'bold'), width=30)
        self.txt_first_name.grid(row=1, column=1)

        self.label_sur_name = Label(stdInfo, text="Sur Name", font=('arial', 14, 'bold'), bg='Ghost White', padx = 2,pady = 16)
        self.label_sur_name.grid(row=2, column=0)
        self.txt_sur_name = Entry(stdInfo, textvariable=sur_name, bd = 2, relief = SUNKEN, font=('arial', 12, 'bold'), width=30)
        self.txt_sur_name.grid(row=2, column=1)

        self.label_date_of_birth = Label(stdInfo, text="Date Of Birth", font=('arial', 14, 'bold'), bg='Ghost White', padx = 2, pady = 16)
        self.label_date_of_birth.grid(row=3, column=0)
        self.txt_date_of_birth = Entry(stdInfo, textvariable=date_of_birth, bd = 2, relief = SUNKEN, font=('arial', 12, 'bold'), width=30)
        self.txt_date_of_birth.grid(row=3, column=1)

        self.label_age = Label(stdInfo, text="Age", font=('arial', 14, 'bold'), bg='Ghost White', padx = 2, pady = 16)
        self.label_age.grid(row=4, column=0)
        self.txt_age = Entry(stdInfo, textvariable=age, bd = 2, relief = SUNKEN, font=('arial', 12, 'bold'), width=30)
        self.txt_age.grid(row=4, column=1)

        self.label_gender = Label(stdInfo, text="Gender", font=('arial', 14, 'bold'), bg='Ghost White', padx = 2, pady = 16)
        self.label_gender.grid(row=5, column=0)
        self.txt_gender = Entry(stdInfo, textvariable=gender, bd = 2, relief = SUNKEN, font=('arial', 12, 'bold'), width=30)
        self.txt_gender.grid(row=5, column=1)

        self.label_address = Label(stdInfo, text="Address", font=('arial', 14, 'bold'), bg='Ghost White', padx = 2, pady= 16)
        self.label_address.grid(row=6, column=0)
        self.txt_address = Entry(stdInfo, textvariable=address, bd = 2, relief = SUNKEN, font=('arial', 12, 'bold'), width=30)
        self.txt_address.grid(row=6, column=1)

        self.label_mobile_no = Label(stdInfo, text="Mobile no", font=('arial', 14, 'bold'), bg='Ghost White', padx = 2, pady= 13)
        self.label_mobile_no.grid(row=7, column=0)
        self.txt_mobile_no = Entry(stdInfo, textvariable=mobile_no, bd = 2, relief = SUNKEN, font=('arial', 12, 'bold'), width=30)
        self.txt_mobile_no.grid(row=7, column=1)


        '''------STUDENT DISPLAY AND SCROLLBAR-------'''

        #Horizontal Scrollbar
        horizontal_scrollbar = Scrollbar(stdDetails, orient = HORIZONTAL)
        horizontal_scrollbar.grid(row=1, column=0, sticky='we')

        #Vertical Scrollbar
        vertical_scrollbar = Scrollbar(stdDetails, bg = '#7002c9', orient = VERTICAL)
        vertical_scrollbar.grid(row = 0, column = 1, sticky='ns')

        #Listbox to display the student details
        student_list = Listbox(stdDetails, width=75, height=26, font=('arial', 9, 'bold'), fg = 'lime', bg = '#110038',
                               xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
        student_list.bind("<<ListboxSelect>>", StudentRec)
        student_list.grid(row=0, column=0, padx=4)
        horizontal_scrollbar.config(command=student_list.xview)
        vertical_scrollbar.config(command=student_list.yview)

        '''-------BUTTONS-------'''

        self.addData = Button(ButtonFrame, text = "Add New", font = ('arial', 14, 'bold'), width = 10, height = 2, bd =6, relief = GROOVE, command = addData)
        self.addData.grid(row = 0, column = 0)

        self.displayData = Button(ButtonFrame, text="Display", font=('arial', 14, 'bold'), width=10, height=2, bd=6,relief=GROOVE, command = displayData)
        self.displayData.grid(row=0, column=1)

        self.clearData = Button(ButtonFrame, text="Clear", font=('arial', 14, 'bold'), width=10, height=2, bd=6,relief=GROOVE, command = clearData)
        self.clearData.grid(row=0, column=2)

        self.delData = Button(ButtonFrame, text="Delete", font=('arial', 14, 'bold'), width=10, height=2, bd=6,relief=GROOVE, command = deleteData)
        self.delData.grid(row=0, column=3)

        self.searchData = Button(ButtonFrame, text="Search", font=('arial', 14, 'bold'), width=10, height=2, bd=6,relief=GROOVE, command = searchDatabase)
        self.searchData.grid(row=0, column=4)

        self.updateData = Button(ButtonFrame, text="Update", font=('arial', 14, 'bold'), width=10, height=2, bd=6,relief=GROOVE, command = updateDatabase)
        self.updateData.grid(row=0, column=5)

        self.exit = Button(ButtonFrame, text="Exit", font=('arial', 14, 'bold'), width=10, height=2, bd=6,relief=GROOVE, command = isExit)
        self.exit.grid(row=0, column=6)

        self.root.mainloop()

if __name__ == '__main__':

    s = Student()