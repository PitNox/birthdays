## Project title: birthdays 

## Welcome to our project! 
We are group “DSLNR” and in our project, called “birthdays”, we provide the birthdays of several people to the user.
You can find a file called main.py that will authenticate the user and return the birthday of the person searched for. 

    In this repository you can find:
    - the folder “script” that contains the file """dbmanager.py"""; it needs to run first in order to create the database structure for usernames and passwords
    - The folder “test”, which contains a python module (a test suit) for testing the code in the ‘birthday.py’ file.
    - The file “Data_file.csv”, in which are stored the names and the respective birthdays.
    - The file “LICENSE”, in which there is a description of the terms and conditions for use, reproduction and distribution of the program (Apache Version 2.0).
    - The file ```birthdays.py```, the starting code for the project.
    - The file “main.py”, the code to run.

## Installing
First step is to open the dbmanager.py file in the "script" folder.
Running the file with a python interpreter will create the SQLite database that will be containing passwords and usernames.
Run it with a python interpreter, adding arguments
- -a <username>         Save <username> as a new user for the system
- -p <password>         Save <password> as password for the user -a

This will create a new user for the system.

## Usage
Now main.py is ready to function.
Running it with a python interpreter will identicte the user and return the birthday of the person searched for.
Possible arguments are:
- -c <username>         Autheniticates the user <username>
- -p <password>         Stores <password> as password for the user <username>
- -n <name>             The name of the person searhed for (eg. "Albert Einstein"). Only birthdays of people present in the file Data_file.csv will be returned.
- -v                    Increase verbosity (show additional info)

## Credits
Everyone in the group contributed to the making of this project. We are: https://github.com/barbaradanzo, https://github.com/xuelanli, https://github.com/PitNox, https://github.com/teorad, https://github.com/klaus108
The project  is inspired by some code taken from: https://github.com/swdevel-lab-h-farm-2019/birthdays

## License
Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/
The Apache License is a non-copyleft free software license written by the Apache Software Foundation (ASF) that obliges users to preserve the copyright notice and disclaimer in modified versions.


