from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search_data():
    mywebsite = website_entry.get()

    try:
        with open("saved_password.json", "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="The File has not been created yet")

    else:
        try:
            data_item = data[mywebsite]
        except KeyError:
            messagebox.showinfo(title="Error", message="Given entry not found")
        else:
            messagebox.showinfo(title=mywebsite,
                                message=f"Email: {data_item['email']}\n Password: {data_item['password']}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_entry.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for x in range(nr_letters)]

    password_list += [random.choice(symbols) for y in range(nr_symbols)]

    password_list += [random.choice(numbers) for z in range(nr_numbers)]
    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_values():
    mypassword = password_entry.get()
    myemail = email_entry.get()
    mywebsite = website_entry.get()
    new_entry = {
        mywebsite: {
            "email": myemail,
            "password": mypassword

        }

    }
    if len(mywebsite) == 0 or len(mypassword) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any of the fields empty: ")
    else:
        is_ok = messagebox.askokcancel(title=mywebsite,
                                       message=f"These are the details entered:\nEmail: {myemail}\nPassword: {mypassword}\nDo you wish to save?")
        if is_ok:
            try:
                with open("saved_password.json", 'r') as f:

                    data = json.load(f)
                    data.update(new_entry)
            except FileNotFoundError:
                with open("saved_password.json", "w") as f:
                    json.dump(new_entry, f, indent=4)
            else:
                with open("saved_password.json", 'w') as f:

                    json.dump(data, f, indent=4)
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
                with open("saved_password.txt", "a") as file:
                    file.write(f"{mywebsite} | {myemail} | {mypassword}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=190)
myimg = PhotoImage(file="./logo.png")

canvas.create_image(100, 95, image=myimg)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()

search = Button(text="Search", command=search_data, width=15)
search.grid(row=1, column=2)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abhinav@email.com")

password = Label(text="Password:")
password.grid(row=3, column=0)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate = Button(text="Generate Password", command=generate_password)
generate.grid(row=3, column=2)

add = Button(text="Add", width=44, command=get_values)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
