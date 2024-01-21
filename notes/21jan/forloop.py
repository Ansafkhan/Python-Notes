value  = range (6)
for i in value: 
 if i !=5 :
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
