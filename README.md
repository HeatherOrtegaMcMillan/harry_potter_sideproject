# Harry Potter Sideproject

The overall purpose of this project is to create a program that a user can enter the name 
(or partial name) of a HP charachter, and will see returned info about that charachter. 
I am doing this sideproject to learn more about python, maybe learn about web scraping. I chose Harry Potter because I am a huge fan. 
###  I will need to:
1. get list of charachters
    - prompt user for input, check see if it's valid
    - be able to provide list (maybe by alphabet letter) for user to select from
    - maybe have random option
2. get information about the charachters (scrape the wiki page for data maybe)
3. compile all info into one spot, use that file to pull from during program
4. Use info to analyize and answer other questions later on
    - i.e. Breakdown of alliterative names, like Godric Gryffendor 
    - i.e. People who lived and died by house or some other parameter
5. Turn into downloadable package using pip, for use in the terminal.
    

### Cleaning the Data
This process actually took quite a while. I initially found a JSON of data from TheDavidBarton's github (HP Project)[https://github.com/theDavidBarton/the-harry-potter-database/blob/master/resources/characters.json]. And I used **Beautiful Soup** to scrap info from [this website](http://magical-menagerie.com/wizardry/full-character-listing/). I also used **FuzzyWuzzy** to compare the slightly different names in order to add the info that was scraped, to the JSON. 