#------- Harry Potter Charachter info database lookup (a side project) ------- # 

# the overall purpose of this project is to create a program that a user can enter the name 
# (or partial name) of a HP charachter, and will see returned info about that charachter.
# I will need to:
    # 1. get list of charachters
        # prompt user for input, check see if it's valid
        # be able to provide list (maybe by alphabet letter) for user to select from
        # maybe have random option
    # 2. get information about the charachters (scrape the wiki page for data maybe)
    # 3. compile all info into one spot, use that file to pull from during program
    # 4. Use info to analyize and answer other questions later on
        # i.e. Breakdown of alliterative names, like Godric Gryffendor 
        # i.e. People who lived and died by house or some other parameter


# ------------- Beginning of inital code --------------------     
import time
import pandas as pd
def capitalize_name (string):
    """
    This function splits a string and capitalizes every element. input is string, output is string.
    """
    return ' '.join([word.capitalize() for word in string.split()])

# fun startup graphics! 
print('~~~ Welcome to the Harry Potter Lookup Program! ~~~')
print(""" 
                                         _ __
         ___                             | '  \\
    ___  \ /  ___         ,'\_           | .-. \        /|
    \ /  | |,'__ \  ,'\_  |   \          | | | |      ,' |_   /|
  _ | |  | |\/  \ \ |   \ | |\_|    _    | |_| |   _ '-. .-',' |_   _
 // | |  | |____| | | |\_|| |__    //    |     | ,'_`. | | '-. .-',' `. ,'\_
 \\\\_| |_,' .-, _  | | |   | |\ \  //    .| |\_/ | / \ || |   | | / |\  \|    \\
  `-. .-'| |/ / | | | |   | | \ \//     |  |    | | | || |   | | | |_\ || |\_|
    | |  | || \_| | | |   /_\  \ /      | |`    | | | || |   | | | .---'| |
    | |  | |\___,_\ /_\ _      //       | |     | \_/ || |   | | | |  /\| |
    /_\  | |           //_____//       .||`      `._,' | |   | | \ `-' /| |
         /_\           `------'        \ |   AND        `.\  | |  `._,' /_ \\
                                        \|       THE          `. \\
                                            
                                            CHARACTER LOOKUP PROGRAM!

                                            by: Heather Ortega McMillan 

""")
# use pandas to read in csv file of charachter list
df = pd.read_csv('charachter_list.csv')
# use pandas to_dict function with the arguement records, to turn into dictionary
# effectively re creating the dictionary from previous versions
hp_charachter_list = df.to_dict('records')
# this value stays true unless the user wants to quit the program (see continue_var)
program_open = True
while program_open == True:
    # user should type in name here. capitalized names don't matter but name all in one. 'first last'. 
    search_name = input('Which Harry Potter Charachter would you like to know more about?\n(Type a single letter to see list of names beginning with that letter) : ')
    
    # add printing a list of charachters who's first name begins with the letter entered
    while len(search_name) == 1:
        letter = search_name.lower()
        # print out capitalized names of all people who's first name with the letter inputted
        names = [capitalize_name(person['name']) for person in hp_charachter_list if person['name'].startswith(letter)]
        if len(names) == 0:
            print('There are no charachters in the database that start with that letter')
        for name in names:
            print(name) 
        search_name = (input('Please enter a charachter: '))
    while search_name.lower() not in [name['name'] for name in hp_charachter_list]:
        #if a valid name is not entered, user prompted to enter another name
        search_name = input('Sorry that charachter is not in the database\nEnter another name: ')

    if search_name.lower() in [name['name'] for name in hp_charachter_list]:   # <-- eventually need to figure out how to search for partial names (i.e. 'harry')
        print('Ok I will tell you more about ', capitalize_name(search_name))
        # print out the 'info' key related to that charachter name
        # eventually figure out how to specify type of info <----
        for person in hp_charachter_list:
            if person['name'] == search_name.lower():
                time.sleep(2.0)
                print("{name} : {info}".format(name = capitalize_name(person['name']), info = person['info']))
    
    #ask about the same charachter's house (eventually add more inputs here (i.e. House, birthday, etc))
    time.sleep(2.0)
    more_info_var = input('Would you like to know their Hogwarts House?: ')

    #check for valid input (will have to update if dict key search is added)
    while more_info_var.lower() not in ('y', 'yes', 'n', 'no'):
        more_info_var = input('Please type y or n: ')

    #if they say yes print the house the charachter was in
    if more_info_var.lower() in ('y', 'yes'):
        for person in hp_charachter_list:
            if person['name'] == search_name.lower():
                print("They were in {hogwarts_house} house".format(**person)) #some cool dictionary formatting I found
    #if they say no continue on
    else:
        pass
        
    # ask if the user wants to coninue
    time.sleep(2.0)
    continue_var = input('Would you like to know about a different charachter?: ')
    
    #ensure user gives yes or no input
    while continue_var.lower() not in ('y', 'yes', 'n', 'no'):
        continue_var = input('Please type y or n: ')
    
    
    # if they do not, close the program
    if continue_var.lower() in ('n', 'no'):
        print('Ok goodbye!')
        print("""
          ___                      ___  
         (o o)                    (o o) 
        (  V  ) Mischief Managed (  V  )
        --m-m----------------------m-m--
        """)
        program_open = False


