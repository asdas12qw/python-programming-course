# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        if choice =='1':
            print ("balance:",balance)
        elif choice == '2':
            print ("balance:",balance)
            amount =float(input("what do yo want to Withdraw:" ))
            if amount <= balance :
             balance -= amount
             print ("Witdraw success")
             print ("balance:",balance)
            else:
               print ("eror")
        elif choice =='3':
           print ("balance:",balance)
           deposit =float(input("what do yo want to Deposit :" ))   
           balance += deposit
           print ("Deposit success")
           print ("balance:",balance) 
        elif choice =='4':
           print ("Exit")
           break
        else:
           print ("plese do it again")   
else:
   print ("Plese Enter PIN again")           