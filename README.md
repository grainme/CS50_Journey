

# Movie Recommendation System // WebScarping
#### Demo Video : www.youtube.com/watch?v=rZFYF-xwQkg

<details>
  <summary>Index</summary>
  <ol>
    <li><a href="#description">Description</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#Project steps">Project steps</a></li>
    <li><a href="#Personal Words">Personal Words</a></li>
  </ol>
</details>

![movie](https://user-images.githubusercontent.com/104838272/209021838-11283e0c-9ee1-458a-a8fa-af323df21054.jpg)
#### Description

We often find ourselves looking for an interseting movie to watch but ended up with no choice that's probably
because the way we search is not effective enough, so I made  this project so that we can get randomly a bunch of good movies, that are highly recommended at least based on IMDB's rating.

At the end of the search, the user is asked wether he want/not want to save the list of the recommended movies as CSV file, with the aim of sharing it with a friend or just saving it on his laptop!


#### CONTENT 

##### Prerequisites

The following items below are necessary to have the application working.

- [Python 3.10 or higher](https://www.python.org/)
- [Pip 22.1.2 or higher](https://pypi.org/project/pip/)
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [pyfiglet](https://pypi.org/project/pyfiglet/0.7/)
- [termcolor](https://pypi.org/project/termcolor/)

#### File structure

**Repository files**

```
README.md - _This file_
logo.png - CS50 logo image
project.py - Main project code
test_project.py - Tests
requirements.txt - Requirement modules
```

**After execution**

```
ListOfMovies.csv - CSV file in which the user will find the selected movies.
```

##### Execution
```
Once the program get executed, a list of Options will shows up as so:

      1/ Top Box Office (US)
      2/ IMDb Top 250 Movies
      3/ Most Popular Movies

Then the user will need to choose one Option, otherwise, the program will exit (sys.exit),
while printing out the following message "OOPS SOMETHING GOES WRONG WITH YOUR INPUT !" 
or "NOT EXISTED YET !" depending on the situation.

After choosing an available option, the user will then be asked the number of movies
he would like to get, and based on that digit(or double/triple digits) a specific 
number of loops will occur.

Elabortating line of code:
LastQuestion = input("Do you want to get a CSV file of the Movies names (yes/no)? ")
if Answer is "yes" or even ["YES","Yes"] , a CSV file called "ListOfMovies" is going 
to be created with the aim of storing DATA later on!

I created 2 principal functions:

    1 - First Function : GetData, that grabs data from the source ("IMDB" in this case)
    using request.get (method from request module), at this stage I needed to pull out
    specific data from the source code so I used the beautiful library "bs4" aka beautiful
    soup, and basically It creates a parse tree from page source code which extract 
    data in a hierarchical and more readable manner.
    
    2 - Second Function : Get_Summary_Data, This is one is kind of the same as the last one but
    with different type of information.

I created the Csv file using the following syntax: with open.....as...: , to save data 
automatically, also I use try and except to prevent and handle different shenanigans 
that can be generated during the execution. 
        
```




#### Project steps:

- [x] Create the project idea and design
- [x] Read bs4 and requests documentation
- [x] Code the project
- [x] Write Tests
- [x] Write Readme.md (This one!)
- [x] Record the Demo

#### Personal Words

- I want to thank the CS50 Team for this unique experience.
- Huge Thanks to Professor [David C. Malan](https://github.com/dmalan), your energy is unmatched!

#### Usefull links

- [CS50P EDX](https://www.edx.org/course/cs50s-introduction-to-programming-with-python)
- [CS50P Harvard](https://cs50.harvard.edu/python/2022/)
- [CS50 Youtube Channel](https://www.youtube.com/c/cs50)

