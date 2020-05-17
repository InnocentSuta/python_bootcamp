# -*- coding: utf-8 -*-
import csv
from IPython.display import clear_output


#user registration

def registerUser():
    with open("users.csv", mode= "a", newline = "") as f:
        
        writer = csv.writer(f)
        
        print("To register please enter your details: ")
        
        email = input("E-mail: ")
        password = input("Password: ")
        password2 = input("Re-type password: ")
        clear_output( )
        
        if password == password2:
            
            writer.writerow( [email, password] )
            
            print("You are now registered!")
            
        else:
            
            print("Something went wrong. Try again.")
        
    


def userLogin():
    print("To register please enter your details: ")
    
    email = input("E-mail: ")
    password = input("Password: ")
    clear_output( )
   
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f)
        
        for row in reader:
            if row == [email, password]:
                print("You're logged in: ")
                
                return True
    print("Something went Wrong!")
    return False

            
#main loop

active = True

logged_in = False

while active:
    if logged_in:
        print("1. Logout\n2. Quit")
    else:
        print("1. Login\n2. Register\n3. Quit")
        
        choice = input("What would you like to do? ").lower( )
        
        clear_output()
        
    if choice == "register" and logged_in == False:
        
        registerUser( )
        
    elif choice == "login" and logged_in == False:
        
        logged_in = userLogin()
        
    elif choice == "quit":
        
        active = False
        print("Thanks for using our software!")
    
    elif choice == "logout" and logged_in == True:
        
        logged_in = False
        print("You are now logged out.")
    else:
            print("Sorry, please try again!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    