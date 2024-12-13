Problem: 
Rising threats result in significant losses, particularly in sensitive industries such as business, banking, and healthcare. 
To mitigate these risks, data must be encrypted or concealed, ensuring its security even in the event of a breach.
Consequently, traditional cryptographic methods evolved to meet the growing demands of modern cyber threats.

El Gamal Encryption and Decryption Algorithm Program
Overview:
This program implements  El Gamal algorithm, a cryptosystem that uses modular arithmetic to secure messages.
The application is divided into three main sections:
1. Key Generation: generates the private & public keys required for the encryption and decryption proccesses 
2. Encryption: converts plain text messages into encrypted messages
3. Decryption: decryptes the encrypted message to its original form: plain text

 Algorithm: 
1.	Receiver and sender generate their keys.
2.	Receiver sends his/her public key to the sender.
3.	The sender encrypts the message using the receiver’s public key.
4.	The sender sends the encrypted message.
5.	The receiver decrypts the encrypted message using his/her private key.

1.	Key generation: done by receiver  
The public key consists of 3 variables: (P, G, Y), private key= x 
P= a large prime number (at least 2048 bits long) 
G= primitive root: a number that can create all the numbers coprime to n by raising it to different powers a number using this rule: G^n mod P.
•	G represents the “generator” number, n represents the power value and P represents prime number.
•	The result of the root can’t be repeated. 
•	G should be (1<g<p).
•	N should be (1≤n<p−1).
Y=G^x mod P
private key: a random integer that’s used secretly for decryption; (1<g<p-2).

2.	Encryption: done by sender
1.	Sender receives the receiver’s public key: (P, G, Y)
2.	Name the unencrypted text “M” which stands for message; it should be smaller than P
3.	Choose a random number B: the sender picks a new random number B (should be larger than 1 and smaller than p-1) each time they send a message, making it more random.
4.	Calculate C1=G^B mod P
5.	Calculate C2= (M * Y^B mod P) mod P: Here, M= message 
6.	Ciphertext/encryption: (C1, C2) is sent to the receiver
   
3.	Decryption: done by receiver
1.	Receiver receives the encrypted message: (C1, C2)
2.	Calculates Z=(C1) ^x mod P: the receiver uses his/her private key x to compute this value. 
3.	Recovers the plaintext message: the original message is recovered by computing: M=(C2*(Z^(P-2) mod P)) mod P. 
4.	Plaintext: the result is the decrypted message M.

How to Use:
1.  Run the program in the terminal
2. Enter a text/int message when asked
The program will:
1. generate the required keys
2. (if text, the message will be converted to its ASCI codes)
3. encrypt the message
4. decrypt the message
5. the encrypted message (as (c1, c2) pairs) and the decrypted message will be displayed.
