
from tkinter import *

import mysql.connector
from tkinter import messagebox as mb






mydb = mysql.connector.connect(
    host='localhost',
    user ='lifechoices',
    password='@Lifechoices1234',
    database='Lifechoicesonline'
)




def admin():
    global main
    main = Tk()
    main.geometry("620x400")
    main.title("ADMINISTRATION")
    main.configure(bg ="black")
    Label(main,text="ADMINISTRATION", bg="grey", width="100", height="2", font=("Calibri", 13)).pack()

    loginB= Button(main,text="Add user", height="2", width="20", bg="green" , command = adduser)
    loginB.place(x=50 , y=80)

    exit_button = Button(main, text="Exit", command=main.destroy)
    exit_button.place(x=160 , y=290)

    def de():
        userna = username_Entry.get()
        passi = PASS_Entry.get()
        cur = mydb.cursor()
        dela = "DELETE FROM ADMIN WHERE username = %s and password = %s"
        cur.execute(dela, ([userna, passi]))
        mydb.commit()


        mb.showinfo("Delete status", "Successfully deleted user")

    Delete = Button(main,text="Delete user", height="2", width="20",bg= "red",command =de )
    Delete.place(x=50 , y=150)

    admin =Button(main,text="Time management", height="2", width="20", bg="orange")
    admin.place( x=50 ,y = 210)



    username_labe = Label(main, text='username', width = 10, height=1)
    username_labe.place(x= 270, y = 90)

    username_Entry = Entry(main)
    username_Entry.place(x= 360 , y = 90)

    PASS_labe = Label(main, text='Password', width=10, height=1)
    PASS_labe.place(x=270, y=160)

    PASS_Entry = Entry(main)
    PASS_Entry.place(x=360, y=160)

    def display():
        listbox = Listbox(main, height=5,
                          width=35,
                          bg="grey",

                          font="Helvetica",
                          fg="yellow")
        listbox.place(x =300 , y = 220)

        cursor = mydb.cursor()
        # A Table in the database
        savequery = "SELECT * FROM ADMIN"
        cursor.execute(savequery)
        result = cursor.fetchall()


        mydb.commit()

        for i in result:
            listbox.insert(END,(i) )

    button = Button(main,text='Display ', command=display)
    button.place(x = 60, y = 290)
    main.mainloop()



def adduser():


    main = Tk()
    main.geometry("400x350")
    main.title("Add user")
    main.configure(bg="black")




    username_labe = Label(main, text='username', width=10, height=1)
    username_labe.place(x=70, y=90)

    username_Entry = Entry(main)
    username_Entry.place(x=160, y=90)

    PASS_labe = Label(main, text='Password', width=10, height=1)
    PASS_labe.place(x=70, y=160)

    PASS_Entry = Entry(main)
    PASS_Entry.place(x=160, y=160)

    Fullname= Label(main, text= 'Fullname' , width = 10 , height=1)
    Fullname.place(x=70 , y =230)

    FullnamEntry = Entry(main)
    FullnamEntry.place(x=160, y = 230)

    def add():
        # username_labe = Label(main_screen, text='username', width=10, height=1)
        # username_labe.place(x=270, y=90)
        #
        # username_Entry = Entry(main_screen)
        # username_Entry.place(x=360, y=90)
        #
        # PASS_labe = Label(main_screen, text='Password', width=10, height=1)
        # PASS_labe.place(x=270, y=160)
        #
        # PASS_Entry = Entry(main_screen)
        # PASS_Entry.place(x=360, y=160)
        #
        # username = username_Entry.get()
        # password = PASS_Entry.get()

        cur = mydb.cursor()
        s = "INSERT INTO ADMIN(username , password) Values (%s,%s)"
        username = username_Entry.get()
        password = PASS_Entry.get()
        cur.execute(s, (username, password))
        mydb.commit()

    ApplyButt = Button( main,text = 'Apply', bg= 'green', command =add )
    ApplyButt.place(x=70, y=300)

    ExitButton = Button(main, text='Exit', bg='red', command = main.destroy)
    ExitButton.place(x=170, y=300)





admin()
adduser()