import supremoKrCrypt as skc
if __name__ == "__main__":
    password = input("EnterYourPassword: ")
    encRes = skc.encrypt(password)
    print(encRes)
    decOrNot = input("Decrypt password: ")
    if(decOrNot == "yes"):
        skc.decrypt(encRes)
