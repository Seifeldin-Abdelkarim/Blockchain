from chain import Chain
from tkinter import *


chain = Chain(20)  # the 20 is the requiment we set

root = Tk()

transactions_blocks = []


def Register():  # On-click this function will work, it registers the details entered
    while True:
        try:  # validation of input fields
            name = nameinfo.get()
        except ValueError:
            displayError.config(text="something went wrong, please try again.")
            print("something went wrong, please try again.")
        if name == "":
            displayError.config(text="You have missing fields, please try again.")
            print("You have missing fields, please try again.")
            return
        else:
            break
    degree = degreeinfo.get()
    while True:
        try:  # validation of input fields
            experience = int(experienceinfo.get())
        except ValueError:
            displayError.config(
                text="please enter proper characters in the experience field, try again."
            )
            print("please enter proper characters in the experience field, try again.")
            return
        if experience < 0 or experience > 99:
            displayError.config(
                text="Don't enter a number less than zero or more than two digits, please try again."
            )
            print(
                "Don't enter a number less than zero or more than two digits, please try again."
            )
            return
        elif experience == "":
            displayError.config(text="You have missing fields, please try again.")
            print("You have missing fields, please try again.")
            return
        else:
            break

    data = [
        name,
        degree,
        str(experience) + " years",
    ]  # the data entered into the blockchain

    transactions_blocks.append(data)
    chain.add_to_current_details(data)
    slashes, Hashinfo, PreHashinfo, Nonceinfo, Details = chain.mine()
    print(transactions_blocks)
    d1.config(text=slashes)
    d2.config(text=Hashinfo)
    d3.config(text=PreHashinfo)
    d4.config(text=Nonceinfo)
    d5.config(text=Details)
    name_entry.delete(
        0, END
    )  # deletes the text in the input fields once an employee's details is registered into the blockchain
    experience_entry.delete(0, END)


root.geometry("600x600")  # the size of the application window
root.resizable(width=False, height=False)  # disables the resizing of the application
root.title("Securing employee identities")  # the title of the application
heading = Label(
    text="Employee identity entry", bg="grey", fg="black", height="3", width="600"
)
heading.pack()

name_lbl = Label(
    text="Name",
)
degree_lbl = Label(
    text="degree",
)
experience_lbl = Label(
    text="Experience (number of years)",
)
name_lbl.place(x=200, y=60)
degree_lbl.place(x=200, y=110)
experience_lbl.place(x=200, y=170)
nameinfo = StringVar()
degreeinfo = StringVar()
experienceinfo = StringVar()

degree_options = [
    "Associate Degree",
    "Bachelor's Degree",
    "Master's Degree",
    "Doctoral Degree",
    "Professional Degree",
]
degreeinfo.set(degree_options[0])

name_entry = Entry(textvariable=nameinfo, width="30")
degree_entry = OptionMenu(root, degreeinfo, *degree_options)
experience_entry = Entry(textvariable=experienceinfo, width="30")

name_entry.place(x=200, y=90)
degree_entry.place(x=200, y=130)
experience_entry.place(x=200, y=200)
# Display = Chain.mine()
displayError = Label(text="")

d1 = Label(text="")
d2 = Label(text="")
d3 = Label(text="")
d4 = Label(text="")
d5 = Label(text="")

displayError.place(x=200, y=250)
d1.place(x=100, y=350)
d2.place(x=100, y=400)
d3.place(x=100, y=450)
d4.place(x=100, y=500)
d5.place(x=100, y=550)

register = Button(
    root, text="Register", width="50", height="2", command=Register, bg="grey"
)
register.place(x=100, y=300)
root.mainloop()
