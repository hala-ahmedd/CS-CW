""""
This code will be divided into 3 sections: generating the key, encryption and decryption. 
"""
def is_prime():
        global prime
        prime=int(input("enter prime number: "))
        if prime <= 1:
            return False
        else: 
            for i in range(2, int(prime**0.5) + 1):
                if prime % i == 0:
                    return False
            return True

def generating_keys (prime):
    global x 
    x= int(input ("Enter number: private key= "))
    global g 
    g=2 #as g should be greater than 1 and smaller than p
    while g>=2:
        check=[] #results
        for i in range(1,prime):
            result= pow(g,i,prime)
            check.append (result)
        if len(check) != len(set(check)): #if repiteted condition
            g+=1
        else:
            print(g)
            break
    global y 
    y=pow(g, x,prime)
    shared=(prime, g,y)
    return shared

def encryption(m,prime,g,y):
    b= int(input ("Enter number:  "))
    global c1
    c1=pow(g,b,prime)
    global c2
    c2=m*(pow(y,b,prime))
    return({c1,c2})

def decryption(c1,c2,prime,x): 
    z=pow(c1,x,prime)
    original_message=(c2*(pow(z,(prime-2),prime))) % prime
    return (original_message)

def message_to_number(message):
    global lst
    lst=[]
    if type(message)==str:
        for i in message:
            conversion= ord(i)
            lst.append(conversion)
        return lst
    else:
        print("The input is not a string")
    return []
#user's code:
message_type=input("Please specify your message's type(1/2):\n 1= string\n 2= integer\n")

while message_type!="1" and message_type!="2":
    message_type=input("Please specify your message's type(1/2):\n 1= string\n 2= integer\n")

if message_type=="2":
    check=is_prime()
    while check==False:
            check=is_prime() 
    print(generating_keys(prime))
    message=int(input("Enter the message: "))
    print(encryption(message,prime,g,y))
    print(decryption(c1,c2,prime,x))
    print("Process is done.")

elif message_type=="1":
    check=is_prime()
    while check==False:
            check=is_prime() 
    print(generating_keys(prime))
    message=(input("Enter the message: "))
    lst=(message_to_number(message))
    encryptionlst=[]
    decryptionlst=[]
    for add in lst:
        c1,c2 = encryption(add, prime, g, y)  # Encrypt each character
        encryptionlst.append((c1, c2))  # Append encrypted pair to the list
        
        decrypted_ascii = decryption(c1, c2, prime, x)  # Decrypt the encrypted pair
        decrypted_char = chr(decrypted_ascii)  # Convert decrypted ASCII to character
        decryptionlst.append(decrypted_char)  # Append decrypted character to the list
    
    print(f"Encrypted message (c1, c2 pairs): {encryptionlst}")
    print(f"Decrypted message: {''.join(decryptionlst)}")
    print("process is done.")
    
else:
    print("invalid choice ")






