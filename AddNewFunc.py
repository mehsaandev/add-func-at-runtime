#  This Program will let You add a new Function at Runtime
def AddNewFunc():
    print("-- Add A Custom Function in your Program at Runtime, No Need to Change the code in order to Add New Functions---")
    try:
        select = "0"
        while select !=3:
            select = input(int("1) Add Custom Function\n2) List of Functions\n3) Exit"))
            if select == 3:
                break
            elif select == 1:
                print('\033c')
                print("Enter Name of Function: ")
                funcLineCheck = 0
                print("Enter code lines, Enter -1 to finish")
                while funcLineCheck !=-1:
                    funcLine = input("(-1 to Finish) Enter Line #"+funcLineCheck +": ")
                    


    except:
        print("Invalid Input, Program is Closing...")
    
    