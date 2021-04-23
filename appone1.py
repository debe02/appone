from datetime import datetime
import random

def login():
      print ("You need to register to be able to login")



print("Welcome, what would you like to do?")
print("1. Login")
print("2. Register")

actionSelect = int(input("Select an option \n"))

if(actionSelect == 1):
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        isLoginSuccessful = login()

    #bankOperations()
            
else:
    print('Login failed, please register')


#registration form
def register():
  print ("My form")
name = input("What is your name? \n")
age = input ("What is your age? \n")
address = input ("What is your address? \n")
phoneNumber = input ("Phone number?")
password = input ("Password?")

#Generate acoount number for the user

accountNumber = random.randint(1000000000 , 1100000000)

 #instantiate current date for user
now = datetime.now()

#login with the appended name and password
allowedUsers=[]
allowedUsers.append(name)
allowedPassword=[]
allowedPassword.append(password)
if{name in allowedUsers}:
  password = input("Your password \n")
  userId = allowedUsers.index(name)
  userId = allowedPassword.index(password)

  if{password == allowedPassword[userId]}:
        print('Welcome ! %s' %name + ' Your Account number is %d' %accountNumber)
        print('These are the available Options:')
        print('1. Withdrawal:')
        print('2. Cash Deposit:')
        print('3. Complaint:')
        print('4. Logout:')
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

        elif selectedOption == "4":
             exit()
             
        else:
            print('wait')
  else:
     print('Password incorrect, please try again')
else:
    print('Name not found, please try again')

    
