user=[]

for i in range(5):
    reg = int(input("Do you to register press 1 and for list press 2 and 3 for exit : "))
    if reg == 1:
        A= input("please provide your name : ")
        
        B = int(input ("please provide your age : "))
       
        C = input("please provide your contact number : ")
       
        D = input("Please provide your email : ")
    
    print("Thank you your data saved succesfully")
    Data = [A,B,C,D]
    user.append(Data)
    # print(user)
    # break
    if reg ==2:
     print(user)
     if reg == 3:
        break
    




