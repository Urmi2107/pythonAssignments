import re
def passwordCheck(passwordRegex):
    inputPass = input("Enter password:")
    flag = passwordRegex.search(inputPass)
    if flag:
        print("Strong Password")
           
    else:
        print("Not Strong Password")
        
passwordRegex=re.compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}')
passwordCheck(passwordRegex)