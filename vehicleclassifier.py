gvm = int(input("What is the gross vehicle mass (in kg)?\n"))
trailer = (input("Does the vehicle have a trailer?\n"))

if gvm <= 3500:
    base_class = "B"
    if trailer == "y" :
        gvm_trailer = int(input("What is the gross vehicle mass of the trailer (in kg)?\n"))
        if gvm_trailer> 750:
            print("This vehicle is class E" + base_class + ".")
        else:
            print("This vehicle is class " + base_class + ".")
    elif trailer == "n":
        articulate = input("Is the vehicle articulated?\n")
        if articulate == "y":
            print("This vehicle is class E" + base_class + ".")
        elif articulate == "n":
            print("This vehicle is class " + base_class + ".")
            
elif 3500 < gvm <= 16000:
    base_class = "C1"
    if trailer == "y" :
        gvm_trailer = int(input("What is the gross vehicle mass of the trailer (in kg)?\n"))
        if gvm_trailer> 750:
            print("This vehicle is class E" + base_class + ".")
        else:
            print("This vehicle is class " + base_class + ".")
    elif trailer == "n":
        articulate = input("Is the vehicle articulated?\n")
        if articulate == "y":
            print("This vehicle is class E" + base_class + ".")
        elif articulate == "n":
            print("This vehicle is class " + base_class + ".")
            
elif gvm >16000 :
    base_class = "C"
    if trailer == "y" :
        gvm_trailer = int(input("What is the gross vehicle mass of the trailer (in kg)?\n"))
        if gvm_trailer> 750:
            print("This vehicle is class E" + base_class + ".")
        else:
            print("This vehicle is class " + base_class + ".")
    elif trailer == "n":
        articulate = input("Is the vehicle articulated?\n")
        if articulate == "y":
            print("This vehicle is class E" + base_class + ".")
        elif articulate == "n":
            print("This vehicle is class " + base_class + ".")    
            
        
    
    
