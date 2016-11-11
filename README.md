[![Build Status](https://travis-ci.org/andela-gacheruevans/cp1-amity.svg?branch=develop)](https://travis-ci.org/andela-gacheruevans/cp1-amity)
[![Code Health](https://landscape.io/github/andela-gacheruevans/cp1-amity/develop/landscape.svg?style=flat)](https://landscape.io/github/andela-gacheruevans/cp1-amity/develop)
[![Test Coverage](https://codeclimate.com/repos/5820c59c631af60051001b3e/badges/9386e9148d3a76904344/coverage.svg)](https://codeclimate.com/repos/5820c59c631af60051001b3e/coverage)
[![Issue Count](https://codeclimate.com/repos/5820c59c631af60051001b3e/badges/9386e9148d3a76904344/issue_count.svg)](https://codeclimate.com/repos/5820c59c631af60051001b3e/feed)
#AMITY

####A room allocation system for one of Andela’s facilities. The following are the tasks needed to be accomplished;
    
    1. create_room <room_name>... 
        - Creates rooms in Amity. Using this command I should be able to create as many rooms as possible by 
        specifying multiple room names after the create_room command.
        
    2. add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
        - Adds a person to the system and allocates the person to a random room. wants_accommodation here is an 
        optional argument which can be either Y or N. The default value if it is not provided is N.
    
    3. reallocate_person <person_identifier> <new_room_name> 
        - Reallocate the person with person_identifier to new_room_name.
    
    4. load_people - Adds people to rooms from a txt file. See Appendix 1A for text input format.
    
    5. print_allocations [-o=filename]  
        - Prints a list of allocations onto the screen. Specifying the optional -o option here outputs the registered 
        allocations to a txt file. See Appendix 2A for format.
    
    6. print_unallocated [-o=filename] 
        - Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to 
        the txt file provided.
    
    7. print_room <room_name> 
        - Prints  the names of all the people in room_name on the screen.
    
    
    
