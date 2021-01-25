from tkinter import *
import mysql.connector
from tkinter import messagebox as mb


mydb = mysql.connector.connect(
    host='localhost',
    user ='lifechoices',
    password='@Lifechoices1234',
    database='Lifechoicesonline'
)
cur =mydb.cursor()
cur.execute("CREATE database if not exists lifechoicesonline")
cur.execute("CREATE TABLE if not exists ADMIN( id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)")
cur.execute("use lifechoicesonline")
mydb.commit()
cur.execute("CREATE TABLE if not exists ADMIN( id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)")
cur.execute("CREATE TABLE if not exists users( id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)")

cur.execute("INSERT INTO ADMIN(id, username, password) \
   SELECT * FROM (SELECT '01', 'lifechoices', '@Lifechoices1234') as temp \
   WHERE NOT EXISTS \
   (SELECT 'lifechoices' FROM ADMIN WHERE username = 'lifechoices') LIMIT 1")

#

# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    register_screen.configure(bg="black")

    global username
    global password
    global username_entry
    global password_entry
    global mobile
    global mobile_entry
    mobile =StringVar()
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="grey").pack()

    username_lable = Label(register_screen, text="Mobile Number  ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    mobileL = Label(register_screen, text="Username  ")
    mobileL.pack()
    mobileEn = Entry(register_screen, textvariable=mobile)
    mobileEn.pack()

    password_lable = Label(register_screen, text="Password  ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password)
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="green", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()


    global username_verify
    global password_verify
    global mobile_verify

    username_verify = StringVar()
    password_verify = StringVar()
    mobile_verify = IntVar()

    global username_login_entry
    global password_login_entry



    Label(login_screen, text="Usernname * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1,bg=' green', command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()
    mobile_info = mobile.get()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    cur = mydb.cursor("CREATE database if not exists lifechoicesonline")

    s = "INSERT INTO users(id , username, password) Values (%s,%s,%s)"

    cur.execute(s, [(username_info),( password_info),( mobile_info)])
    mydb.commit()

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)


    # if password1:
    #     db = mysql.connector.connect(host="localhost",
    #                                  user='lifechoices',
    #                                  password='@Lifechoices1234',
    #                                  db="Lifechoicesonline")
    #     cursor = db.cursor()
    #
    #     # If no password is enetered by the
    #     # user
    # else:
    #     db = mysql.connector.connect(host="localhost",
    #                                  user='lifechoices',
    #                                  db="Lifechoicesonline",
    #                                  password="@Lifechoices1234")
    #     cursor = db.cursor()
    cursor = mydb.cursor()
    # A Table in the database
    savequery =  "SELECT * FROM ADMIN WHERE username = %s and password = %s"
    cursor.execute(savequery,([username1,password1]))


    try:
        myresult = cursor.fetchall()

        for x in myresult:
         print(x)
         mb.showinfo("Query"," Executed successfully")
        login_screen.destroy()
        import admin


    except Exception as e:
        mb.showinfo("showinfo", "Error , Please try again")


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Successful").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window
login_screen = 0
def Adminlogin():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Admin Login")
    login_screen.geometry("300x250")
    login_screen.configure(bg="black")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify
    global mobile_verify

    username_verify = StringVar()
    password_verify = StringVar()
    mobile_verify = IntVar()

    global username_login_entry
    global password_login_entry



    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
    main_screen.withdraw()




def main_account_screen():
    global main_screen



    main_screen = Tk()
    main_screen.geometry("400x350")
    main_screen.title("Account Login")
    main_screen.configure(bg="black")
    main_screen.bind("<a>", lambda z: Adminlogin())
    Label(text="WELCOME TO LIFECHOICES ONLINE ACCOUNT", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    loginB= Button(text="Login", height="2", width="30", bg="green", command=login)
    loginB.place(x=50 , y=80)
    Label(text="").pack()
    RegistB = Button(text="Register", height="2", width="30",bg= "orange", command=register)
    RegistB.place(x=50 , y=150)

    admin =Button(text="Login as Admin", height="2", width="30", bg="red", command=Adminlogin)
    admin.place( x=50 ,y = 210)

    exit_button = Button(main_screen, text="Exit", command=main_screen.destroy , bg= 'blue')
    exit_button.place(x=160, y=290)


main_account_screen()



main_screen.mainloop()


