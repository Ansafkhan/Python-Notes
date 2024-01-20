# i=1
# while i <= 10:
#     print (i)
#     i+=1
while True:
 op = int(input("press 1 to continue and 0 to end : "))
 if op ==1 :
    oper1 = int(input ("please enter 1st number : "))
    oper2 = int(input ("please enter 2nd number : "))
    aa = input("select operator + , - , / , * : ")
    if aa == "+" :
        print (oper1 + oper2)
    elif aa == "-":
        print (oper1 - oper2)
    elif aa == "*":
        print(oper1 * oper2)
    elif aa == "/":
        print (oper1 / oper2)
    else : 
        ("invalid command")
 else :
   print ("command ended succesfully")
   break  


