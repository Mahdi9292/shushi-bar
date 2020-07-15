from itertools import groupby, cycle, chain, repeat
from threading import Thread
from time import sleep
import random


# Make a random list of the places around the Sushi-Bar. Some would be occupied.
def Rand(occupied, free, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(occupied, free)) 
  
    return res 


# Make a circular list --> in order to simulate the Rounded Sushi-Bar
def ncycles(iterable, n):
    
    return chain.from_iterable(repeat(tuple(iterable), n))


# Incoming Guests
# First check if there is k(empty places), then show several possible Seats, if exist.
# ex: [3,9] --> Seats number 3 to number 9 are suitable for our Guests.
# Because the table is round we may get ex: [9-2]
# Ask for the first Seat Number. Then Guests sit consecutively from the Seat number chosen.
# Update the Sushi-Bar Seats
def check_in(s,k): 

    new = "1"*k  

    if new in Str: 

        groups = [(n, sum(1 for _ in g)) for n, g in groupby(new_lst)]
        cursor = 0
        result = []

        for n, l in groups:
            if cursor < ln:
                if n and l >= k and cursor+l > ln:
                    result.append([cursor+1, cursor + l-ln])

                elif n and l >= k :  
                    result.append([cursor +1 , cursor + l ]) 

                cursor += l
        print("Your guests may take Seats in range",result)

        global ind
        ind = input("Enter the first Seat Number please:") 
        ind = isdigit(ind) -1

        length = k
        element = 0
        h= ln - ind

        if ind + 1 + length > ln:
            index, length = ind ,h
            lst[index:index + length] = (element for _ in range(length))
            index, length = 0, k-h
            lst[index:index + length] = (element for _ in range(length))
        else:    
            index, length = ind, k
            lst[index:index + length] = (element for _ in range(length))
        print ("Sushi Bar Seats have been updated as -->", lst)
    else: 
        print ("There is no", k , "Consecutive empty seats for this group. Offer them something delicious to keep them waiting")


# For executing the time scheduler for Outgoing Guests, please uncomment the below Function
# Execute the timer and then run the check-out
def myTimer(seconds):
    sleep(seconds)
    check_out(Str, k, ind_checkout)


# Outgoing Guests
# When Guests in special (or random) time leave, Master must be informed and the list of the Seats must be updated
# For this function I tried to reuse the groups members ('k's) and the places they had sit ('ind's)
def check_out(s,k, ind_ch): 

    gone = "0"*k  

    if gone in Str: 

        length = k
        element = 1
        h= ln - ind_ch

        if ind_ch + 1 + length > ln:
            index, length = ind_ch ,h
            lst[index:index + length] = (element for _ in range(length))
            index, length = 0, k-h
            lst[index:index + length] = (element for _ in range(length))
        else:    
            index, length = ind_ch, k
            lst[index:index + length] = (element for _ in range(length))

          
        print ("A group of", k , " members, has left")
        print ("Sushi Bar Seats have been updated as -->", lst)

    else:
        print("all seats are free")
        

# Check if inputs are numbers(int)
def isdigit(d):
    while d.isalpha() or d == '' or d==' ':
        d = input ("Please Enter a valid Number:")

    return int(d)





# code drives here

num = input ("Please Tell me how many seats are around your Sushi Bar: ")
num = isdigit(num)

occupied = 0    # We assume occupied seats as 0's
free = 1        # We assume free seats as 1's

lst = Rand(occupied, free, num)     # Generate a random list of 0's and 1's
print ("Your guests may sit as you see ---->", lst)
ln = len(lst) 


for x in range(8):     # Choose the number of times you want to accept new incoming Groups

    new_lst= list(ncycles(lst, 2)) 
    k = input ("Enter the number of new group's members please: ")
    k= isdigit(k)

    Str = ''.join([str(elem) for elem in new_lst])

    check_in(Str, k)


    ind_checkout = ind

    #---> For executing the time scheduler for Outgoing Guests, please uncomment the below Script
    
    # guestOff = Thread(target=myTimer, args=(20,))     # You may set the time
    # guestOff.start()