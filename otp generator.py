#otp generator
import random

#list of integers
L1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

#list of lowercase alphabets                                                                                                 
L2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#list of uppercase alphabets
L3=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

 #list of special characters                                                                                    
L4=["!","@","#","$","%","^","&","*"]  

pwd={1:L1,2:L2,3:L3,4:L4}                                                                                               
L=[]                                                                                                                #megalist            
while True:
    try:
        n=int(raw_input("How many digit password do you want to generate?:"))                                       #Asking the user for required length
        if n==0:
            print"No null value passwords allowed"
        elif n!=0:
            break
    except ValueError:
            print "please enter a proper integer indicating the number of digits"                                 #Handling the error where an user enters a string value for the length of the otp (purposefully or otherwise)



print "MENU\n1.Numbers\n2.Lowercase Alphabets\n3.Uppercase Alphabets\n4.Special characters\n"                      #handling desired choices
ch=raw_input("Enter your choice(s);multiple choices can be added for eg.124:")

for i in ch:
    L.extend(pwd[int(i)])


otp=""
while len(otp)<n:
        i=random.randint(0,len(L)-1)
        if type(L[i])!=str:                                                                                       #Handling the case of addition of integers to a string or vice versa
            otp+=str(L[i])
        else:
            otp+=L[i]
print "Your one time password is-",otp        
        
        
    
            


    

            

        
    
    

    
