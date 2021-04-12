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
hp_charachter_list = {
                    'harry potter': 'The Boy Who lived. Defeated Lord Voldemort. Sorted into Gryffindor at Hogwarts.',
                    'hermionie granger': 'Cleverest girl in her year at Hogwarts. Harry Potter\'s friend. Sorted into Gryffindor.',
                    'ron weasley': 'Harry Potter\'s best friend. One of 7 Weasley children. Sorted into Gryffindor at Hogwarts'
                    }    

search_name = input('Which Harry Potter Charachter would you like to know more about?: ')

if search_name.lower() in hp_charachter_list:
    print('Ok I will tell you more about ', search_name) # <-- try to return capatalized version
    print(hp_charachter_list.get(search_name))
else:
    print('Sorry that charachter is not in the database')


