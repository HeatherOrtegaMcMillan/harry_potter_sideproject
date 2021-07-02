#~~~~~~~~~~~ Harry Potter Lookup program Helper Functions ~~~~~~~~~~~~~~ 

# This module needs to be imported into the main program for it to run. 

import time
import pandas as pd

#### 
def capitalize_name (string):
    """
    This function splits a string and capitalizes every element. input is string, output is string.
    """
    return ' '.join([word.capitalize() for word in string.split()])