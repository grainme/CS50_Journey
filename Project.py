
#Modules
import bs4
import requests
import csv
import random
import sys
import pyfiglet 
import termcolor




def main():
    #Creating a csv file
    with open('ListOfMovies.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["TITLES","DATE OF RELEASE","SUMMARY"])


        #Introducing a dict of Options
        Option = {"1/ Top Box Office (US)":"https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht",
              "2/ IMDb Top 250 Movies":"https://www.imdb.com/chart/top/?ref_=nv_mv_250",
              "3/ Most Popular Movies":"https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"}
        
        #Aesthetic Stuff
        print(pyfiglet.figlet_format("LIST OF OPTIONS", font = "doom", width = 70 ))
        
        #Printing the options to the user
        for i in Option:print(i)
        
        #Blank Line
        print("\n")
        try:
            choice = int(input("Choose one option(1,2 or 3): "))
            number = int(input("How many movies your are looking for? "))
            LastQuestion = input("Do you want to get a CSV file of the Movies names (yes/no)? ")
            print("\n")
            if choice in {1, 2, 3}:
                Myfunc(Option, choice, csv_writer,number,LastQuestion)
                
                print(termcolor.colored(CheckFile(LastQuestion),'green'))
                print()
            else:
                print("NOT EXISTED YET !")
                sys.exit()
        except ValueError:
            print("OOPS SOMETHING GOES WRONG WITH YOUR INPUT !")



def Myfunc(Option, choice, csv_writer,number,LastQuestion):
    source = requests.get(Option[list(Option)[choice-1]]).text
    Mv = GetData(source)
    ListOfMovies = random.sample(Mv,number)
    for movie in ListOfMovies:
        href_Var = movie.a['href']
        Summary = Get_Summary_Data(href_Var)
        Titre = movie.a.text.lstrip().replace("\n"," ")
        try:
            Date = movie.span.text
        except Exception:
            Date = "2022"
        if In(LastQuestion):
            csv_writer.writerow([Titre,Date,Summary])
        print(f"{termcolor.colored(Titre,'red')},{Date}\n---------------\n{Summary}")
        print()
        

    
def Get_Summary_Data(x):
    new_source = f"https://www.imdb.com/{x}"
    source01 = requests.get(new_source).text
    soup01 = bs4.BeautifulSoup(source01,"lxml")
    article01 = soup01.find("span",class_="sc-16ede01-2 gXUyNh")
    return article01.text
    
def GetData(source):
    soup = bs4.BeautifulSoup(source,"lxml")
    article = soup.find("div",class_="article")
    return article.find_all("td",class_="titleColumn")


def In(x):
    return x in ["yes","YES","Yes"]


def CheckFile(LastQuestion):
    return "FILE SUCCESFULY CREATED" if In(LastQuestion) else "ENJOY WATCHING :)"


if __name__=="__main__":
    main()
