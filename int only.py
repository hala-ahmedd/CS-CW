""""
El Gamal Encryption and Decryption algorithm
This application will be divided into 3 main sections: generating the key, encryption and decryption. 
It outputs encrypted and decrypted messages using El Gamal algorithm.
prime number: any number divided by 1 or itself ONLY
"""
import random #a module used in generating a random number during the encryption process
def is_prime(prime):
        if prime <= 1: #negatives or 1 aren't prime numbers
            return False
        else: 
            for i in range(2, int(prime**0.5) + 1): #iterates from 2 to the square root+1 of the prime number, 1 and the prime number itself are not in range
                if prime % i == 0: #if divisible by any:
                    return False
            return True #prime number

def generating_keys (prime):
    global x 
    x= int(input ("Enter private key= ")) #takes the private key as an input
    global g 
    g=2 #initialization: as g should be greater than 1 and smaller than p
    while g<prime: #as long as the g is smaller than prime, conditions under the loop will occur
        check=[] #results
        for i in range(1,prime): #i=power, range: 1<g<p-2
            result= pow(g,i,prime) #g^i % p 
            check.append (result) #adds the result of the calculation in the "check" list
        if len(check) != len(set(check)): #checks if there's a repeated result
            g+=1 #increments the g by 1 and loops again
        else:
            print(f"G is equal to {g}")
            break #stops the loop
    global y 
    y=pow(g, x,prime) #g^x mod p
    return (f"Public key and Private key: {prime, g, y , x}") 

def encryption(m, prime, g, y):
    b = random.randint(2, prime - 2)  # generates random number(b) with a range from 2 to prime-2
    global c1
    c1 = pow(g, b, prime)  # c1 = g^b mod p
    global c2
    c2 = (m * pow(y, b, prime)) % prime  # c2 = (m * (y^b mod p)) mod p
    return (f"The encrypted message is equal to {c1, c2}") #returns encrypted message

# Function to decrypt a message using ElGamal
def decryption(c1, c2, prime, x):
    z = pow(c1, x, prime)  # z = c1^x mod p
    s = pow(z, prime - 2, prime)  # s=z^(prime -2) mod p
    original_message = (c2 * s) % prime  # decrypted message = c2 * s mod p
    return (f"The decrypted message is equal to {original_message}") # returns decrypted message

#user's code:
#user's input:
message = None #intializing it with nothing just so i could use the variable in a condition
prime=int(input("Enter prime number: "))
#checking process:
while not is_prime(prime):  # Looping until a valid prime is entered
    prime = int(input("The number entered is not prime. Please enter a prime number: "))
while True: #an infinite loop,(will continue until 'broken')
    try:
        message = int(input("Please enter your integer message: "))
        if message>=prime: #if the message int value is greater than or equal to prime:
            print("Invalid input, message should be 0<=m<prime number")
        else:
            print(f"You entered: {message}")
            break  # exit the loop when the input is valid
    except ValueError: #exception handeling: handeling wrong inputs
        print("Invalid input, please enter a number.")

#main function: the start of implementation of every function
def main(message):
    check=is_prime(prime) # checks if the value 'prime' is a prime number by calling the is_prime function
    while check==False: # loop until 'prime' is confirmed to be prime
            check= is_prime(prime)
    #provoking/calling and printing the functions
    print(generating_keys(prime))  
    print(encryption(message,prime,g,y))
    print(decryption(c1,c2,prime,x))
    print("Process is done.") #print a message indicating the process is done

main(message) #provoking/calling the function


