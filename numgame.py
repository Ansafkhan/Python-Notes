import random
rand = random.randint(1,100)
print(rand)
for i in range(1000):
    user = int(input("plese gusss number : "))
    print (user)

    if user< rand :
        print ("guess number is smaller than system number")

    if user > rand :
        print ("guess number is grater than system number")

    if user == rand :
        print ("congrulation you won the game")
        break
