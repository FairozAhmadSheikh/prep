# factorial of number 
# inp=int(input("Enter a number : "))
# fact=1
# if inp<1:
#     print("Factorial is not defined for negatve numbers ")
# elif inp==0 or inp==1:
#     print("Factorial is : 1") 
# else:
#     for i in range(1,inp+1):
#         fact*=i 
# print("FACORIAL IS ",fact)


# positive negative check

# num=int(input("enter  nmber "))
# if num>0:
#     print("+")
# else:
#     print('-')


# prime chek
# number 

# # Input from the user
# num = int(input("Enter a number: "))
# is_prime=True
# if num>1:
#     for i in range(2,int(num**0.5)+1):
#         if num%i ==0 :
#             is_prime=False
#             break
#     if is_prime:
#         print("Number is prime")
#     else:
#         print("Not prime")
    

# comprehension

l1=['eesa',"Sameer",'abrar',"ali","feroz","ahmad","hussain"]

l2=['a','e','i','o','u']

for i in l1 :
    for v in i:
        if v in l2:
            print("yes",end="❤")
        else:
            print("no",end="🖤")
