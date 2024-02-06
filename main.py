from tkinter import *
from tkinter import messagebox
import random
import pyperclip

default_email = ""

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for x in range(nr_letters)]
    password_symbols = [random.choice(symbols) for x in range(nr_symbols)] #creates 3 lists of random characters
    password_numbers = [random.choice(numbers) for x in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password) #instantly copies password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():

    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Error", message="Don't leave any fields blank")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} \nPassword:{password} \nIs this ok?")
        #the above line asks the user if the info is ok when they hit add confirming it

        if is_ok:
            with open("data.txt", "a") as data_file: #gets the entries and writes them into the data.txt file
                data_file.write(f"{website} | {email} | {password}\n")

                web_entry.delete(0, END) #when deleting from entry line you must go from start index to end index
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=35, pady=35)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#labels

web_label = Label(text="website:", font=("Courier", 12, "normal"))
web_label.grid(column=0, row=1)
#web_label.config(padx=5, pady=5)

email_user_label = Label(text="Email/Username:", font=("Courier", 12, "normal"))
email_user_label.grid(column=0, row=2)
#email_user_label.config(padx=5, pady=5)

password_label = Label(text="Password:", font=("Courier", 12, "normal"))
password_label.grid(column=0, row=3)
#password_label.config(padx=5, pady=5)

#Entries

web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, f"{default_email}" ) #autofill email if wanted

pass_entry = Entry(width=18)
pass_entry.grid(row=3, column=1)

#Buttons

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)

add_pass = Button(text="Add", width=36, command=add_data)
add_pass.grid(row=5, column =1, columnspan=2)










window.mainloop()