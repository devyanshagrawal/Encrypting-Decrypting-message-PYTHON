print()
print(" "*20+"!!!! Welcom to Encryption & Decryption Environment !!!!")
print()


def encryption(text, key):
    encrypted_text = ''
    key1 = key
    for i in range(len(text)):
        ascii_l = ord(text[i])
        if key+ascii_l > 122:
            key1 = key+ascii_l - 122
            encrypted_text = encrypted_text + chr(97+key1-1)
        else:
            encrypted_text = encrypted_text + chr(ascii_l+key)    
    return encrypted_text       

def decryption(text, key):
    decryptied_text = ''
    key1 = key
    for i in range(len(text)):
        ascii_l = ord(text[i])
        if ascii_l-key < 97:
            key1 = ascii_l-key-97+122
            decryptied_text = decryptied_text + chr(key1+1)
        else:
            decryptied_text = decryptied_text + chr(ascii_l-key)    
    return decryptied_text


if __name__=="__main__":
    while(True):
        n = int(input("If you want to encrypt type 1, else if you to decrypt type 2: "))

        if n == 1:
            text = list(input("Please enter the text and a key as (example:abcd 4): ").split(" "))
            text, key = text
            text = text.lower()
            print(f'Encryted text: {encryption(text, int(key))}')

        elif n ==2:
            text = list(input("Please enter the text and a key as (example:abcd 4): ").split(" "))
            text, key = text
            text = text.lower()
            print(f'Decrypted text: {decryption(text, int(key))}')   
        else:
            raise Exception("Invalid Choice!")
