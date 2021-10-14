#  This Program will let You add a new Function at Runtime
def AddNewFunc():
    print("-- Add A Custom Function in your Program at Runtime, No Need to Change the code in order to Add New Functions---")
    try:
        select = 0
        while select !=3:
            select = int(input("1) Add Custom Function\n2) List of Functions\n3) Exit\nSelect: "))
            if select == 3:
                print("Program is Closing...")
                break
            elif select == 1:
                print('\033c')
                f_old = open("AddNewFunc.py",'r')
                read_old_func = f_old.readlines()
                f_new = open("AddNewFunc.py",'w')
                f_funcName = open("FunctionsList.txt",'a')
                func_Name = input("Enter Name of Function: ")
                func_Name = func_Name.lstrip()
                f_new.write("def "+func_Name+"():\n")
                f_funcName.write(func_Name+"\n")
                funcLineCheck = 0
                print("Enter code lines, Enter -1 to finish")
                while funcLineCheck !=-1:
                    func_Line = input("(-1 to Finish) Enter Line #"+str(funcLineCheck+1)+": ")
                    if func_Line == "-1":
                        break
                    else:
                        func_Line = func_Line.lstrip()
                        f_new.write("    "+func_Line+"\n")
                        for i in read_old_func:
                            f_new.write(i)
                        funcLineCheck +=1
            elif select == 2:
                print('\033c')
                fname_List = open("FunctionsList.txt",'r')
                NameList = fname_List.readlines()
                print("List of Added Functions:")
                for i in NameList:
                    print(i)
                print()

    except:
        print("Invalid Input, Program is Closing...")
    
AddNewFunc()