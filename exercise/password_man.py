

pwd_try = 0      
while True:
    master_pwd = input("Enter master password?: ")
    key = "hej"
    
    if master_pwd != key:
        print("Wrong password. Try again")
        pwd_try +=1
        print("Try" , pwd_try , "/ 3")
        
        if pwd_try == 3:
            quit()
    else:
        print("Acces granted")
        break

def view():
    with open("password.txt", "r") as f:
        index_01 = 1
        for line in f.readlines():
            data = line.rstrip()
            service ,user, passw = data.split("|")
            print("Service: ", service , "| Account Name: " , user , "| Password: " , passw)
            index_01 += 1
def add():
    acc_name = input("Account: ").capitalize()
    acc_user_name = input("Login name: ").capitalize()
    acc_pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(acc_name + "|" + acc_user_name + "|" + acc_pwd + "\n")




while True:
    mode = input("Add or view passwords? (Add/View/Remove/Q): ").lower()
    if mode == "q":
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()
     


    else:
        print("Error 01; Invalid. Try again")
        continue
