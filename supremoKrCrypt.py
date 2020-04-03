def encrypt(password):
    encPassword = ""
    for char in password:
        num = str(ord(char) ** 4 + 200) + "#"
        encPassword += num
    return(encPassword)


def decrypt(res):
    decPassword = ""
    resArray = res.split("#")[:-1]
    for num in resArray:
        char = int((int(num)-200)**(0.25))
        char = chr(char)
        decPassword += char
    print("decrypted")
    print(decPassword)
