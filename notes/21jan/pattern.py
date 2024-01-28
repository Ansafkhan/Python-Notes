# https://i.pinimg.com/736x/07/0d/e6/070de6bea184aa69c8c6b093c4e1ae5e.jpg

# for i in range (6):
#     for j in range (i):
#      print ( "*" , end ="")
#     print ("")

# for i in range (5):
#     for j in range (i):
#      print ( "*" , end ="")
#     print ("")

# row = 5
# for  i in range (1 , row +1):
#     # for space
#     for j in range (row-i):
#        print (" " , end =" ")
#        #for star
#     for k in range (i):
#             print ("*",end= " ")
#     print (" ")

# user = int(input ("please enter the row number: "))
# row = user
# for  i in range (1 , row +1):
#     # for space
#     for j in range (row-i):
#        print (" " , end =" ")
#        #for star
#     for k in range (i):
#             print ("*",end= " ")
#     print (" ")

# row = 5
# for i in range (1,row +1):
#     # for space
#     for j in range (row -i):
#         print (" ",end = "")
#         # for star
#     for k in range (i):
#         print ("*",end= " ")
#         #for next line
#     print(" ")

# row = 5
# for i in range (1, row +1):
#     for j in range (1, row +1):
#         if i == 1 or i == 5 or j ==1 or j == 5 :
#             print("*", end= " ")
#         else :
#             print (" ", end =" ")
#     print (" ")


# row = 5
# for i in range (1, row +1):
#     for j in range (1, row +1):
#             print("*", end= " ")
#     print (" ")

# for i in range (6):
#     for j in range (i):
#      print ( "*" , end =" ")
#     print ("*") 
# for k in range (6):
#     for l in range (i-k):
#      print ( "$" , end =" ")
#     print ("$") 


# row = 5
# for  i in range (1 , row +1):
#     # for space
#     for j in range (row-i):
#        print (" " , end =" ")
#        #for star
#     for k in range (i):
#             print ("*",end= " ")
#     print ("*")
# for  l in range (1 , row +1):
#     # for space
#     for m in range (l):
#        print (" " , end =" ")
#        #for star
#     for o in range (i-l):
#             print ("$",end= " ")
#     print ("$")

# row = 5
# for i in range (1,row +1):
#     # for space
#     for j in range (row -i):
#         print (" ",end = "")
#         # for star
#     for k in range (i):
#         print ("*",end= " ")
#         #for next line
#     print("*")
# for l in range (1,row +1):
#     # for space
#     for m in range (l):
#         print (" ",end = "")
#         # for star
#     for n in range (i-l):
#         print ("$",end= " ")
#         #for next line
#     print("$")
# row =5
# for l in range (row ):
#     # for space
#     for m in range (l):
#         print (" ",end = "")
#         # for star
#     for n in range (row -l):
#         print ("$",end= " ")
#         #for next line
#     print("$")
# for i in range (row +1):
#     # for space
#     for j in range (row -i):
#         print (" ",end = "")
#         # for star
#     for k in range (i):
#         print ("$",end= " ")
#         #for next line
#     print("$")
row = 7
for i in range (row, -1, -1):
    for j in range (i):
     print ( "*" , end ="")
    print ("")
for k in range (row, -1, -1):
    for l in range (k):
     print ( "*" , end ="")
    print ("")

