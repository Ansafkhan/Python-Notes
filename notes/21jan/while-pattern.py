# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print("*",end=".")
#         j+=1
#     print("")
#     i+=1

# i=1
# while i<=5:
#      j=1
#      while j<=5:
#         if i == 1 or i == 5 or j ==1 or j == 5 :
#                 print("*", end= " ") 
                
#         else :
#                 print (" ", end =" ")
#         j+=1       
#      print (" ")
#      i+=1
row=5
for i in range (row +1):
    # for space
    for j in range (row -i):
        print (" ",end = "")
        # for star
    for k in range (i):
        print ("$",end= " ")
        #for next line
    print("$")

# i=1
# while i<5:
#     j=1
#     while j<5:
#         print("*",end="")
#         j+=1
#     print("")
#     i+=1