""""
This code will be divided into 3 sections: generating the key, encryption and decryption. 
"""
import random
def is_prime(prime):
        if prime <= 1: #negatives or 1 aren't a prime number
            return False
        else: 
            for i in range(2, int(prime**0.5) + 1): #iterates from 2 to the square root+1 of the prime number, the prime number itself is not there
                if prime % i == 0: #if divisible by any:
                    return False
            return True #prime number

def generating_keys (prime):
    global x 
    x= int(input ("Enter private key= "))
    global g 
    g=2 #as g should be greater than 1 and smaller than p
    while g<prime:
        check=[] #results
        for i in range(1,prime):
            result= pow(g,i,prime)
            check.append (result)
        if len(check) != len(set(check)): #if repiteted condition
            g+=1
        else:
            print(f"G is equal to {g}")
            break
    global y 
    y=pow(g, x,prime)
    return (f"public key and private key: {prime, g, y , x}") 

def encryption(m, prime, g, y):
    b = random.randint(2, prime - 2)  # Generate random numbers key b with a range from 2 to prime-2
    global c1
    c1 = pow(g, b, prime)  # c1 = g^b mod p
    global c2
    c2 = (m * pow(y, b, prime)) % prime  # c2 = m * y^b mod p
    return (f"The encrypted message is equal to {c1, c2}") 

# Function to decrypt a message using ElGamal
def decryption(c1, c2, prime, x):
    z = pow(c1, x, prime)  # z = c1^x mod p
    s = pow(z, prime - 2, prime)  # Modular inverse of z using Fermat's Little Theorem
    original_message = (c2 * s) % prime  # Decrypted message = c2 * s mod p
    return (f"The decrypted message is equal to {original_message}")

#user's code:
#user's input:
message = None #intializing it with nothing just so i could use the variable in a condition
prime=int(input("enter prime number: "))
while not is_prime(prime):  # Looping until a valid prime is entered
    prime = int(input("The number entered is not prime. Please enter a prime number: "))
while True: #while message has a value of nothing
    try:
        message = int(input("Please enter your integer message: "))
        if message>=prime:
            print("Invalid input, message should be 0<=m<prime number")
        else:
            print(f"You entered: {message}")
            break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input, please enter a number.")
#main function: the start of every function
def main(message):
    check=is_prime(prime)
    while check==False:
            check= is_prime(prime)
    print(generating_keys(prime))
    print(encryption(message,prime,g,y))
    print(decryption(c1,c2,prime,x))
    print("Process is done.")
#provoking/calling the function
main(message)


