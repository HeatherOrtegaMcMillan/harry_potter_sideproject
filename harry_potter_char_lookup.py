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

# this is just for now, eventually will put into csv list in some way
    # can you store the dictionary keys uppercased? or can I just return that later? 
hp_charachter_dict = {
                    'harry potter': 'The Boy Who lived. Defeated Lord Voldemort. Sorted into Gryffindor at Hogwarts.',
                    'hermionie granger': 'Cleverest girl in her year at Hogwarts. Harry Potter\'s friend. Sorted into Gryffindor.',
                    'ron weasley': 'Harry Potter\'s best friend. One of 7 Weasley children. Sorted into Gryffindor at Hogwarts'
                    } 
hp_charachter_list = [
                        {
                            'name': 'harry potter',
                            'hogwarts_house': 'Gryffindor',
                            'info': 'The Boy Who lived. Defeated Lord Voldemort.'

                        },  
                        {
                            'name': 'hermione granger',
                            'hogwarts_house': 'Gryffindor',
                            'info': 'Cleverest girl in her year at Hogwarts.'
                        },
                        {
                            'name': 'ron weasley',
                            'hogwarts_house': 'Gryffindor',
                            'info': 'Harry Potter\'s best friend. One of 7 Weasley children.'
                        },
                        {
                            'name': 'draco malfoy',
                            'hogwarts_house': 'slytherin',
                            'info': 'Pure-blood snob and only son of Lucius and Narcissa. Harry Potter\'s nemesis'
                        }
                     ]       

def capitalize_name (string):
    """
    This function splits a string and capitalizes every element. input is string, output is string.
    """
    return ' '.join([word.capitalize() for word in string.split()])

# fun startup graphics! 
print('~~~ Welcome to the Harry Potter Lookup Program! ~~~')
print(""" 
                                         _ __
         ___                             | '   \\
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
                                            
                                            CHARACHTER LOOKUP PROGRAM!

                                            by: Heather Ortega McMillan 

""")
# this value stays true unless the user wants to quit the program (see continue_var)
program_open = True
while program_open == True:
    # user should type in name here. capitalized names don't matter but name all in one. 'first last'. 
    search_name = input('Which Harry Potter Charachter would you like to know more about?: ')
        
    while search_name.lower() not in [name['name'] for name in hp_charachter_list]:
        #if a valid name is not entered, user prompted to enter another name
        ## add printing a list of available charachters
        search_name = input('Sorry that charachter is not in the database\nEnter another name: ')

    if search_name.lower() in [name['name'] for name in hp_charachter_list]:   # < -- eventually need to figure out how to search for partial names (i.e. 'harry')
        print('Ok I will tell you more about ', capitalize_name(search_name))
        # print out the 'info' key related to that charachter name
        # eventually figure out how to specify type of info 
        for person in hp_charachter_list:
            if person['name'] == search_name.lower():
                print("{name} : {info}".format(name = capitalize_name(person['name']), info = person['info']))
    
    #ask about the same charachter's house (eventually add more inputs here (i.e. House, birthday, etc))
    more_info_var = input('Would you like to know their Hogwarts House?: ')

    #check for valid input (will have to update if dict key search is added)
    while more_info_var.lower() not in ('y', 'yes', 'n', 'no'):
        more_info_var = input('Please type y or n: ')

    #if they say yes print the house the charachter was in
    if more_info_var.lower() in ('y', 'yes'):
        for person in hp_charachter_list:
            if person['name'] == search_name.lower():
                print("They were in {hogwarts_house} house".format(**person))
    #if they say no continue on
    else:
        pass
        
    # ask if the user wants to coninue
    continue_var = input('Would you like to know about a different charachter?: ')
    
    #ensure user gives yes or no input
    while continue_var.lower() not in ('y', 'yes', 'n', 'no'):
        continue_var = input('Please type y or n: ')
    
    
    # if they do not close the program
    if continue_var.lower() in ('n', 'no'):
        print('Ok goodbye!')
        program_open = False


