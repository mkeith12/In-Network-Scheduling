#Import calendar & datetime to implement in code
import calendar
import datetime

#Display 2022 Calendar
print(calendar.calendar(2022))

#List to hold concatenated string of date and name of appointments
app_created=[]

#List to hold date and time of scheduled apppointment
appointments =[]

#List of names that concatenate with date and time list
names = []

#function to check date is taken or not
def check_date(date1):
    if date1 in appointments:
        print('Error date already taken\n')
    else:
        appointments.append(date1)
        print('Date entered!!\n')


#Function to check name entered with appointment concatenating with date and time
def search(f_name):
    if f_name in names:
        print(f_name)
        n = names.index(f_name)
        print('Appointment on '+ str(appointments[n])+('\n'))
    else:
        print('No Appointment for given date\n')

#Checks if name containing only letters
def name():
    name = input('Enter First name:')
    if name.isalpha():
        print('Name entered is Valid\n')
        names.append(name)
        search(name)
    else:
        print('Invalid name\n')

#prints full appointment scheduled
def print_app():
    for i in names:
        for j in appointments:
            print(i + ' Appointment on '+ str(j))

#Concatenates both list and adds to app_created list
def add_app():
    for i in names:
        for j in appointments:
            newapp =(str(i) + ' Appointment on '+ str(j))
            app_created.append(newapp)

#main function displays menu
def main():
    #list of available times for the shop
    times = ['1pm','2pm','3pm','4pm']

    #Prints out menu asks for user input
    print('Welcome to X Insurance')
    print('Would you like to make an Apppointment or look up Appoinment?\n')
    print('1. Create Appointment')
    print('2. Look up Appointment')
    print('3. Speak to a Representative')
    print('4. Quit\n')

    #User input for their choice
    choice = int(input('Choose 1, 2, or 3,4\n'))
    while choice <=4 and choice>=1:
        if choice ==1:
            print('\nEnter date for appointment using only numbers\n')
            #Assigns year to only 2022
            year = 2022

            #while loop to allow input and check for date validation
            while True:
                try:
                    month = int(input('Enter a month: '))
                    day = int(input('Enter a day: '))
                    dt=datetime.datetime(year,month,day)
                except ValueError:
                    print('Invalid Date')
                    continue
                else:
                    break
            #loops through times list
            for i in times:
                print('\n'+i)

            #validates through the valid input for time
            while True:
                try:
                    time =int(input('\nEnter time in range 1-4: '))
                except ValueError:
                    print('Not a number')
                    continue
                else:
                    if 1 <= time <5:
                        break
                    else:
                        print('Out of range. try Again')
            #converts time int into str
            convt_num = str(time)
            tm=datetime.time(time)
            
            #conbimes date and time
            combined = dt.combine(dt,tm)

            #checks date through function
            check_date(combined)

            #calls functions
            name()
            add_app()

            
            choice = int(input('\nChoose 1, 2, or 3,4\n'))

        elif choice == 2 :
            f_name = input('\nEnter your first name: ')
            #calls function and prints appointment if name match
            search(f_name)
            choice = int(input('Choose 1, 2, or 3,4\n'))
            
        elif choice == 3 :
            print('Connecting..')
            
        else:
            for i in app_created:
                print(i)
            print('Quitting...')
            break

        
#calls main function
main()

#Opens file 
file = open('Sche_appointments.txt','w')

#While file opens app_created list is written in file
with open('Sche_appointments.txt','w')as out_file:
    for i in range(len(app_created)):
        print(str(app_created[i]))
#closes file
file.close()
