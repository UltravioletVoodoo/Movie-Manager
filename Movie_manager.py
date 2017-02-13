#Simple movie manager for my mother, because I am bored over reading break


movies_list = []


def sync_movies_list_and_database():
    file = open("Database.txt", "w")
    #empty the file
    file.write("")

    for x in movies_list:
        file.write(x + "\n")
    file.close()


#this function adds a new movie to the current movies list
def add_new_movies():
    print "add_new_movies is just a hollow shell"

    input = raw_input("Please enter the names of movies you want to add seperated by commas")

    input = input.split(",")
    
    for x in input:
        if x not in movies_list:
            movies_list.append(x)
        else:
            print "{} is already in your movie list".format(x)

    #modify the database
    sync_movies_list_and_database()


#this function removes movies from the current list
def remove_movies():
    print "remove_movies is a hollow shell"

    input = raw_input("Please enter the names of movies that you want to remove seperated by commas")
    input = input.split(",")

    for x in input:
        if x in movies_list:
            movies_list.remove(x)
        else:
            print "{} is not in your movies list, and therefore cannot be removed".format(x)

    #modify the database
    sync_movies_list_and_database


#this function prompts the user to choose to add or remove list elements
def modify_movies_list():

    input = raw_input("Do you want to add or remove list elements?\n(1.) -> Add elements\n(2.) -> Remove elements")

    if input == "1":
        add_new_movies()
    if input == "2":
        remove_movies()


#this function initializes the movies list with the current list stored in the database
def initialize_movies_list():
    global movies_list

    file = open("Database.txt", "r")
    for line in file:
        movies_list.append(line.rstrip("\n"))
    file.close()


#this function tells the user if they have any movies in their list, and if they do, how many
def print_movies_list_data():

    if len(movies_list) == 0:
        print "You do not currently have any movies registered with this system"
    
    else:
        print "Your movie list contains {} movies".format(len(movies_list))


def print_movies_list():
    print "\n"
    for x in movies_list:
        print x


#loop for user input
def input_loop():

    input = raw_input("What would you like to do?\n(1.) -> View the current movies list\n(2.) -> Modify the list\n(3.) -> Quit")
    
    if input == "1":
        print_movies_list()
    if input == "2":
        modify_movies_list()
    if input == "3":
        #ensure that the database is synchronized with the current data
        sync_movies_list_and_database()
        quit()


    #seperate loop instances
    print "\n"
    #re-loop
    input_loop()



def start():

    initialize_movies_list()

    print_movies_list_data()

    input_loop()



start()