
""""
El Gamal Encryption and Decryption algorithm
This application will be divided into 3 main sections: generating the key, encryption and decryption. 
It outputs encrypted and decrypted text messages using El Gamal algorithm.
Prime number: any number divided by 1 or itself ONLY
"""
import random #a module used in generating a random number (b and x here)
def is_prime(): #function to check if a number is prime or not
        global prime 
        prime=random.randint(200,1000)
        if prime <= 1: #negatives or 1 aren't prime numbers
            return False
        else: 
            for i in range(2, int(prime**0.5) + 1):  #iterates from 2 to the square root+1 of the prime number, 1 and the prime number itself are not in range
                if prime % i == 0: #if divisible by any number(i):
                    return False
            return True #Prime number

def generating_keys (prime): #function to generate all the keys needed
    global x 
    x= random.randint(2, prime - 2) #generates the private key randomly
    global g 
    g=2 #initialization: as g should be greater than 1 and smaller than p
    while g<prime: #as long as the g is smaller than prime, conditions under the loop will occur
        check_occurance=[] #results in each iteration
        for i in range(1,prime): #i=power, range: 1<g<p
            result= pow(g,i,prime) #g^i mod p 
            check_occurance.append (result) #adds the result of the calculation in the list
        if len(check_occurance) != len(set(check_occurance)): #checks if there's a repeated result, if yes:
            g+=1 #increments the g by 1 and loops again
        else: #if not
            print(g)
            break #stops the loop
    global y 
    y=pow(g, x,prime) #g^x mod p
    shared=(prime, g,y) 
    return shared

def encryption(m,prime,g,y,b): # Function to encrypt a message using ElGamal 
    c1=pow(g,b,prime) # c1 = g^b mod p
    c2=(m*pow(y,b,prime))% prime # c2 = (m * (y^b mod p)) mod p
    return c1,c2 #returns encrypted message

def decryption(c1,c2,prime,x): # Function to decrypt a message using ElGamal 
    z=pow(c1,x,prime) # z = c1^x mod p
    z_inverse = pow(z,prime-2,prime) # s=z^(prime -2) mod p
    original_message=(c2* z_inverse) % prime # decrypted message = c2 * s mod p
    return (original_message) # returns decrypted message

def message_to_number(message): #function to convert the letters into their ASCI code
    global lst
    lst=[] #empty list
    if type(message)==str:
        for letter in message: #loops through the message
            conversion= ord(letter) #covert each letter into their ASCI code
            lst.append(conversion) #adds the ASCI code to lst
        return lst #character's ASCI code
    else:
        print("The input is not a string")
    return []
#user's code:
message=input("Please enter your text message: ")
def main(message): #main function: the start of implementation of every function
    check=is_prime()
    while check==False:
            check=is_prime() 
    print(generating_keys(prime))
    lst1=(message_to_number(message))
    encryptionlst=[]
    decryptionlst=[]
    for let_num in lst1: #let_num= letter_number
        b = random.randint(2, prime-1)
        c1,c2 = encryption(let_num, prime, g, y,b)  # encrypt each character
        encryptionlst.append((c1, c2))  # append encrypted pair to the list
        
        decrypted_ascii = decryption(c1, c2, prime, x)  # Decrypt the encrypted pair
        decrypted_char = chr(decrypted_ascii)  # Convert decrypted ASCII to character
        decryptionlst.append(decrypted_char)  # Append decrypted character to the list
    
    print(f"Encrypted message (c1, c2 pairs): {encryptionlst}")
    print(f"Decrypted message: {''.join(decryptionlst)}")
    print("Process is done.")
main(message)


