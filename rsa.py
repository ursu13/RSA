
import random
import gmpy2
import sys
import os
from Crypto.Util.number import long_to_bytes

#FIRST STEP: CREATE 2 PRIME NUMBERS 

from Crypto.Util import number

prime_one = number.getPrime(1024)
prime_two = number.getPrime(1024)

#SECOND STEP: CALCULATE prime_one*prime_two

N=prime_one*prime_two

#STEP 3 : CALCULATE TOTIENT T=(P-1)*(Q-1)

T=(prime_one-1)*(prime_two-1)





#STEP 4: SELECT A PUBLIC KEY
#IT MUST BE PRIME
#IT MUST BE < TOTIENT
#IT MUST NOT BE A FACTOR OF TOTIENT

ok = 0

public_key = 0




while ok == 0 : 
    public_key = number.getPrime(1024)
    if public_key < T and T % public_key != 0 :
        ok = 1
print('\n\n')

print('>>>PUBLIC KEY GENERATED<<< : {} \n\n'.format(public_key))


#STEP 5 : SELECT A PRIVATE_KEY

def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 


# function to find extended gcd
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)
def gcd(p, q): 
      
    if q == 0: 
        return p 
          
    return gcd(q, p % q) 



#mod invers
def modinv(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		return None
	else:
		return x%m


private_key = modinv(public_key,T)

print('<<<PRIVATE KEY COMPUTED>>>: {} \n'.format(private_key))





def get_ascii():
    ascii_string = ""
    for elem in list(map(ord, raw_input(">>INSERT MESSAGE :  "))):
        ascii_string += str(elem)
    return ascii_string



ascii_string = get_ascii()
print('>>>>MESAJ_ASCII {}\n'.format(ascii_string))


cipher = pow (int(ascii_string),public_key,N)
print('\n\n\n')
print('>>>>CRIPTED : {}\n'.format(cipher))



decipher = pow (cipher,private_key,N)
print('\n\n\n')

print('>>>>DECRIPTED : {}\n'.format(decipher))

"""
def get_string(ascii):
    i = 0
    string = ""
    while i < len(ascii):
        ascii_len = int(ascii[i])
        ascii_elem = ""
        for j in range (1, ascii_len + 1):
            ascii_elem += ascii[i+j]
        string += chr(int(ascii_elem))
        i += ascii_len + 1
    return string

print( get_string(ascii_string))
"""

"""
def lcm(p, q): 
    return p * q / gcd(p, q) 
"""

dp = gmpy2.invert(public_key, (prime_one-1)) 

dq = gmpy2.invert(public_key, (prime_two-1)) 

qinv = gmpy2.invert(prime_two, prime_one) 



# CHINESE REMAINDER THEOREM

def decrypt(c):
  m1 = pow(c, dp, prime_one)
  m2 = pow(c, dq, prime_two)
  h = (qinv * (m1 - m2)) % prime_one 
  
  m = m2 + h * prime_two
  return m


m=decrypt(int(cipher))

print('>>>>DECRIPTED USING CRT : {}\n'.format(m))