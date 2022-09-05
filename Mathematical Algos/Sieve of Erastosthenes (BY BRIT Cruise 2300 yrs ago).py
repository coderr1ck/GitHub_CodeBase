#Sieve of Erasthothenes is an algo developed by Brit Cruise that
#allows us to find prime numbers upto any given number 
#and to check if given no. is prime or not

def SieveOfErasthothenes(num):          #MAIN ALGORYTHM
    from math import sqrt
    prime_ls = [True]*(num+1)
    prime_ls[0] = False
    prime_ls[1] = False
    
    for i in range(2,int(sqrt(num)+1)):   #Outer LOOP
        if prime_ls[i] == True:
            for j in range(i*i,num+1,i): #Inner LOOP
                prime_ls[j] = False
#___________________________________________________________                
    temp_ls = []    
    for val in range(len(prime_ls)):
        if prime_ls[val] == True :
            temp_ls.append(val)
    if prime_ls[num] == True:
        print("[",num,"is a Prime Number ]")
    else:
        print("[",num,"is Not a Prime Number ]")
    return print(temp_ls,"\nList of all prime Numbers upto",num)    
SieveOfErasthothenes(36)

            
                
                
            
        
