from Project import In, Get_Summary_Data,CheckFile


def main():
    test_In()
    test_Get_Summary_Data()
    test_CheckFile()

    
def test_In():
    assert In("YES") == True
    assert In("NO")  == False
    
def test_Get_Summary_Data():
    assert Get_Summary_Data("title/tt0111161") == "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
    assert Get_Summary_Data("title/tt7144666") == "After being abducted by a child killer and locked in a soundproof basement, a 13-year-old boy starts receiving calls on a disconnected phone from the killer's previous victims."
    
def test_CheckFile():
    assert CheckFile("yes") == "FILE SUCCESFULY CREATED"
    assert CheckFile("NO") == "ENJOY WATCHING :)" #Not necessarly NO 
    
    
    
    
if "__name__"=="__main__":
    main()
