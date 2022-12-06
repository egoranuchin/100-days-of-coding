from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # messagebox.showinfo(title="Заткнись, сука блять", message="А не то я тебя убью нахуй")

        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {username}\nPassword: {password}\nIs it ok to save?")

        if is_ok == True:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, END)
            # username_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:", bg="white")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

# Inputs

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
username_entry = Entry(width=50)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "angela@email.com")
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons

generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()