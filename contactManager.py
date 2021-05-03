#contact list that will hold the name and number
contacts =[[],[]]

#function that will ask user to enter the name and number of contact
def add():
    flag = True
    while flag: 
        f_name = input('Enter the first name of contact: ') #asks the first name
        l_name = input('Enter the last name of contact: ') #asks the last name
        fullName = f_name + ' ' + l_name #first name and last name make full name
        num = input('Enter the number of contact: ') #asks the number
        if num.isdigit() and len(num) == 10:
            contacts[0].append(fullName) #adds it to the list, row 0
            contacts[1].append(num) #adds it to the list, row 1
            save(contacts) #function called
            flag = False
        else:
            print('Enter the name in letters and number with 10 digits')

#function that will take user input and write it to a text file.       
def save(contacts):
    with open('ContactList.txt', 'w') as profile:
        for index in range(len(contacts[0])): #for every index in the range of the length of the list with names
            fullName = contacts[0][index] #the name plus the index 
            num = contacts[1][index] #the number plus the index
            space = '~' #a line between the name and number
            profile.write(fullName.center(20) + '\n') #write to the file the name in center
            profile.write((space * len(fullName)).center(20) + '\n') #make the line in center the same length as the name
            profile.write(num.center(20) + '\n' + '\n') #write the number to the file and center it

#function that will display the text file             
def display():
    with open('ContactList.txt', 'r') as profile:
        print(profile.read())
        
#function that will delete any contact user wants to delete
def delete(contacts):
    remove = input('Enter the name you want to delete: ') #asks user to enter the name
    if remove not in contacts[0]: #if the name is not in the list row 0
        print('Contact not found') #tells user, contact was not found
    else: #otherwise
        position = contacts[0].index(remove) #gets the position of the name in the list
        print('Successfully deleted ' + contacts[0][position] + '\n') #tells user it has been deleted
        contacts[0].pop(position) #removes the name from list
        contacts[1].pop(position) #removes the number from the list
        save(contacts) #save it to the text file

#function that will allow user to change any name they want to change         
def change(contacts):
    findIndex = input('Enter the name you want to change: ') #asks user the name
    if findIndex == findIndex: 
        position = contacts[0].index(findIndex) #finds the position of the name
        contacts[0].pop(position) 
        contacts[1].pop(position) 
        insertName = contacts[0].insert(position,input('Enter the new name: ')) #in that position asks user to enter the name
        insertNum = contacts[1].insert(position,input('Enter the new number: ')) # asks user to enter the number to fill in that position
        save(contacts)
    else:
        print('Contact not Found!') #otherwise tells user the contact is not found

#function that will sort the name in order with their numbers       
def sort(contacts):
    sorted_names = sorted(contacts[0]) #sorts the names in list row 0

    for loop in range(len(contacts)): #for loop that will run the length of contacts
        new_pos = sorted_names.index(contacts[0][loop - 1]) #find the index of the sorted name 
        
        for element in contacts: #for every element in the contacts
            temp_val = element[new_pos] #takes the new position of element and stores it ina variable 
            element[new_pos] = element[loop -1] #new position of the element is index - 1 
            element[loop - 1] = temp_val  # and now you store the new position into the temp value
    save(contacts)
    display() #prints out the sorted list 


#function that will search for the contact user asks and tell them if its there or not
def linearSearch(contacts):
    find = input('Enter the name of contact, you want to find: ') #asks user the name they want to find
    for element in contacts[0]: #for the amount of elements in the list
        if element == find: #if the element is what user asked for
            print('Contact found') #tell user, contact found
            return True
        else: #otherwise
            print('Contact not found') #tell user, contact not found
            return False 
             
#function that asks user what they want to do with the contact manager     
def ask():
    #will ask user over and over again what they want to do, until they quite
    flag = True
    while flag:
        #what the program does and what user should enter
        print('I am a contact manager, welcome. I will store your contacts, sort and search them.' + '\n') 
        print('Enter A to add contact')
        print('Enter P to print contacts')
        print('Enter D to delete contacts ')
        print('Enter C to change contacts')
        print('Enter S to sort contacts')
        print('Enter L to search contacts')
        print('Enter Q to quit the program')
        info = input('').upper() #makes all user input upper case
        if info == 'A':
            add()
        elif info == 'P':
            display()
        elif info == 'D':
            delete(contacts) 
        elif info == 'C':
            change(contacts)
        elif info == 'S':
            sort(contacts)
        elif info == 'L':
            linearSearch(contacts)
        elif info == 'Q':
            print('You have exited the program.')
            flag = False
        else:
            print('Please enter what you want using the letters given in the instruction.')          

#function is called            
ask()