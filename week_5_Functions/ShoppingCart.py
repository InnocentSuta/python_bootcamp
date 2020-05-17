# -*- coding: utf-8 -*-

from IPython.display import clear_output

#glogal variable

cart = []

#adding items to cart

def addItem(item):
    clear_output()
    cart.append(item)
    print(f"{item} has been added in the cart")


#removing item from the cart 

def removeItem(item):
    clear_output()
    
    try:
        cart.remove(item)
        print(f"{item} has been removed from the cart")
        
    except:
        print("Sorry we couldn't remove an item")
        
#showing items in the cart

def showCart():
    clear_output()
    if cart:
        print("Here is your Cart Items")
        
        for item in cart:
            print(f"- {item}")
    else:
        print("CART EMPTY")

#clearing the cart
        
def clearCart():
    clear_output()
    cart.clear()
    print("Cart is empty now")
    
    
    
    
#main Function
    
def main():
    done = False
    
    while not done:
        
        ans = input("quit/add/remove/show/clear: ").lower()
        
        if ans == "quit":
            
            print("Thank you for using our program")
            
            showCart()
            done = True
            
        elif ans == "add":
            
            item = input("What would you like to add: ").title()
            addItem(item)
            
        elif ans == "remove":
            
            showCart()
            item = input("What would you like to reomove: ").title()
            removeItem(item)
            
        elif ans == "show":
            
            showCart()
        
        elif ans == "clear":
            
            clearCart()
            
        else:
            
            print("sorry try agin")        
        
main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            
            
            
            
            