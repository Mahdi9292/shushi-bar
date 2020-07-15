# shushi-bar

# Welcome to Sushi-Bar development review !!

I developed the Sushi-Bar as below:

0- Analyzed the project and seperated it to few small parts.

1- Made a static list of 0's & 1's to simulate the table with free and occupied seats

2- Made a function to circulate the list in order to simulate the Round Table

3- Made a function to created a random rounded list of 0's & 1's based on the number(quantity) of Seats (We should allocate a number)

4- Made a function to insure all the inputs are of type int(number)

5- Simulated dynamic incomming Guests in groups of Ks and finding K consecutive seats
	5-1- made a string of the list to easy-check if there are K consecutive free seats (1's)
	5-2- made a function (check_in):
		5-2-1- to get the K and show the possible seats using their indexes
		5-2-2- to use K and indexes to update the list after the user choose the first Seat for group --> (change K consecutive 0's to 1's)
	5-3- made a for loop in order to accept more K groups

6- Simulated an automatic outgoing Guests in groups of K's and emptying K consecutive seats
	6-1- made a function (check_out): to use K's and indexes to update the list (automatically) --> (change K consecutive 0's to 1's)
	6-2- made a time scheduler function to execute the check_out function every n seconds
	6-3- improved the time scheduler in order to other scripts run without being blocked

7- Tried to improve my code in order to accept Groups as soon as a Group leaves OR a Group leaves during accepting new Group


Note :
I used Python 3.7
I tried to use just Built-in libraries in order you can run the code without much effort. And to minimize the file size.


While making the time scheduler I had some difficulties. I tried to fix it, but I put the function-executor in comment mode.
You may uncomment it and rerun the whole code. :-)
