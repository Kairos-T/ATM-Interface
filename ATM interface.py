import time

print("Welcome to ABC Bank")
restart=("Y")
tries=3
balance=float(5309.43)
format(balance, '.2f')

while tries >= 0:
  pin=int(input("Enter your 4 Digit PIN"))
  if pin==(1703):
    print("You have entered your PIN correctly.\r\n")
    while restart not in ('n','NO','no','N'):
      print("Selection your transaction:\r\n")
      time.sleep(0.5)
      print("1 - Cash Withdrawal\r\n")
      time.sleep(0.5)
      print("2 - Deposit\r\n")
      time.sleep(0.5)
      option = int(input("3 - Balance Enquiry"))

      if option == 1:
        option1 = ('y')
        print("Your current balance is $",balance,".")
        withdrawal= int(input("Select an amount to withdraw:$ \r\n($10/$50/$80/$100/$150/$200/$300/$500/$1000)"))
        if withdrawal in [10,50,80,100,150,200,300,500,1000]:
          balance=balance-withdrawal
          print("Please wait...")
          time.sleep(1)
          print("Transaction complete! Your current balance now is $", balance, ".")
          restart = input("Is there anything else you would like to do?")
          if restart in ("n", "no","NO", "N"):
            print("Thank you for banking with ABC Bank! Have a nice day.")
            time.sleep(1)
            break

        elif withdrawal != [10,50,80,100,150,200,300,500,1000]:
          print("You have entered an invalid amount. Please try again.\r\n")
          time.sleep(1)
          restart = ('y')
    
      elif option == 2:
        print("Your current balance is $", balance, ".")
        deposit=float(input("How much would you like to deposit?"))
        print("Please wait...")
        time.sleep(1)
        balance=balance+deposit
        print("Transaction complete! Your current balance now is $", balance,".")
        restart=input("Is there anything else you would like to do?")
        if restart in ("n", "no","NO", "N"):
          print("Thank you for banking with ABC Bank! Have a nice day.")
          time.sleep(1)
          break
      
      elif option == 3:
        print("Your current balance is now $", balance, ".\r\n")
        time.sleep(1)
        restart=input("Is there anything else you would like to do?")
        if restart in ("n", "no","NO", "N"):
          print("Thank you for banking with ABC Bank! Have a nice day.")
          time.sleep(1)
          break

  elif pin != (1703):
    print("You have entered an incorrect password. You have", tries, "left before your account is locked.")
    tries=tries-1
    if tries ==0:
      print("Your account is now locked due to too many invalid attempts. Please contact customer service for assisstance.")
      time.sleep(2)
      break
