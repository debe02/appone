from datetime import datetime
import random

#registration form
def register():
  print ("Fill in the following form to own your Account")
name = input("What is your name? \n")
age = input ("What is your age? \n")
address = input ("What is your address? \n")
phoneNumber = input ("Phone number?")
password = input ("Password?")

#Generate acoount number for the user
def account():
 accountNumber = random.randint(1000000000 , 1100000000)

 #instantiate current date for user
now = datetime.now()

allowedUsers=[]
allowedUsers.append(name)
allowedPassword=[]
allowedPassword.append(password)
if{name in allowedUsers}:
  password = input("Your password \n")
  userId = allowedUsers.index(name)

  if{password == allowedPassword[userId]}:
        print('Welcome ! %s' %name + " Your Account number is %d" %accountNumber)
        print('These are the available Options:')
        print('1. Withdrawal:')
        print('2. Cash Deposit:')
        print('3. Complaint:')
        print("Current date and Time = ", now)
        
        
        selectedOption = input('please select an option :')
        if selectedOption == "1":
            print('How much would you like to Withdraw %s' %selectedOption)

            cashOption = int(input(' '))
            print('Take your cash')
         
       
        elif selectedOption == "2":
            print('How much would you like to deposit? %s' %selectedOption)

            cashOption = int (input(''))
            currentBalance = 10000 + cashOption
            print (currentBalance)

        elif selectedOption == "3":
            print('What issue will you like to report? %s' %selectedOption)
            queryOption = input ('')
            print('Thank you for contacting us')
        else:
            print('wait')
  else:
     print('Password incorrect, please try again')
else:
    print('Name not found, please try again')
