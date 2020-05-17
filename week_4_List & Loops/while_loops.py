
health = 5

while health > 0:
    print(health)
    health -= 1 # forgetting this line will result in infinite loop


# using two or more loops together is called a nested loop
for i in range(2): # outside loop
    for j in range(3): # inside loop
        print( i, j )
        
sentinel = input("Enter quit to exit: ")

while sentinel != "quit":
    
    print(sentinel)
    
    sentinel = input("Enter quit to exit: ")