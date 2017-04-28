[![Build Status](https://travis-ci.org/andela-gacheruevans/cp1-amity.svg?branch=develop)](https://travis-ci.org/andela-gacheruevans/cp1-amity)
[![Code Health](https://landscape.io/github/andela-gacheruevans/cp1-amity/develop/landscape.svg?style=flat)](https://landscape.io/github/andela-gacheruevans/cp1-amity/develop)

# AMITY

##Installation

1. Create a working directory.

    	mkdir Projects
    
2. Clone this repository.

    * via HTTPS

    	- https://github.com/andela-gacheruevans/cp1-amity.git

    * via SSH

    	- git@github.com:andela-gacheruevans/cp1-amity.git

3. Navigate to project directory.

		cd cp1-amity  
    
4. Create a virtual environment.
    
    	mkvirtualenv env workon env

when selecting the virtual environment, you can pick any name that suits you for now you will be using **env**
    
5. Set up the environment requirements.
    
    	pip install -r requirements.txt


6. Initialize, migrate and update the database.
	
		python run.py -i

## A room allocation system for one of Andela’s facilities. The following are the tasks needed to be accomplished;
    
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
    
    
    
