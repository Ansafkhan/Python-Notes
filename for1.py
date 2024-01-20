# for abc in range(12):
#  if abc % 2 != 0 :
#    print (abc )

# table = int (input ("which table you want : "))
# for abc in range(11):
#     print (abc*table)
for i in range (5):
 operator1 = int (input("Put 1st number : ")) 
 operator2 = int (input("Put 2nd number : ")) 
 operand = input ("which operand you want + , - , * , / , % : ")
 if "+" == operand :
    print (operator1 + operator2)
 elif "-" == operand :
    print (operator1-operator2)
 elif "*" == operand :
    print (operator1*operator2)
 elif "/" == operand : 
    print (operator1/operator2)
 elif "%" == operand : 
    print (operator1%operator2)
 else :
    ("Invalid command")
    
 more = input ("press 1 to end : " )
 if more == "1":
    break

           


