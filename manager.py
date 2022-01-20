master_pwd = input("What is the master password. ")


def view():
    pass


def add():
    name = input("Account name: ")
    pws = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd)


while True:
    mode = input("Would you like to add to add a new password or view current ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
